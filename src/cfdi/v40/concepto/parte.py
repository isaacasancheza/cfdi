from typing import Annotated

from pydantic import NonNegativeFloat, StringConstraints
from pydantic_xml import attr

from cfdi import fields
from cfdi.v40.base import BaseModel
from cfdi.v40.concepto.informacion_aduanera import InformacionAduanera


class Parte(
    BaseModel,
    tag='Parte',
):
    """
    Schema of a "Parte" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    informacion_aduanera: list[InformacionAduanera] = []
    """
    Nodo opcional para introducir la información aduanera aplicable cuando se trate de ventas de primera mano de
    mercancías importadas o se trate de operaciones de comercio exterior con bienes o servicios.
    """

    clave_prod_serv: str = attr('ClaveProdServ')
    """
    Atributo requerido para expresar la clave del producto o del servicio amparado por la presente parte.
    Es requerido y deben utilizar las claves del catálogo de productos y servicios, cuando los conceptos que
    registren por sus actividades correspondan con dichos conceptos.
    """

    no_identificacion: Annotated[
        str | None,
        StringConstraints(
            min_length=1,
            max_length=100,
            pattern=r'[^|]{1,100}',
        ),
    ] = attr('NoIdentificacion', default=None)
    """
    Atributo opcional para expresar el número de serie, número de parte del bien o identificador del producto o del
    servicio amparado por la presente parte. Opcionalmente se puede utilizar claves del estándar GTIN
    """

    cantidad: fields.PositiveSixDecimals = attr('Cantidad')
    """
    Atributo requerido para precisar la cantidad de bienes o servicios del tipo particular definido por la presente
    parte.
    """

    unidad: Annotated[
        str | None,
        StringConstraints(
            min_length=1,
            max_length=20,
            pattern=r'[^|]{1,20}',
        ),
    ] = attr('Unidad', default=None)
    """
    Atributo opcional para precisar la unidad de medida propia de la operación del emisor, aplicable para la
    cantidad expresada en la parte. La unidad debe corresponder con la descripción de la parte.
    """

    descripcion: Annotated[
        str,
        StringConstraints(
            min_length=1,
            max_length=1000,
            pattern=r'[^|]{1,1000}',
        ),
    ] = attr('Descripcion')
    """
    Atributo requerido para precisar la descripción del bien o servicio cubierto por la presente parte.
    """

    valor_unitario: NonNegativeFloat | None = attr('ValorUnitario', default=None)
    """
    Atributo opcional para precisar el valor o precio unitario del bien o servicio cubierto por la presente parte.
    No se permiten valores negativos
    """

    importe: fields.NonNegativeSixDecimals | None = attr('Importe', default=None)
    """
    Atributo opcional para precisar el importe total de los bienes o servicios de la presente parte. Debe ser
    equivalente al resultado de multiplicar la cantidad por el valor unitario expresado en la parte.
    No se permiten valores negativos.
    """
