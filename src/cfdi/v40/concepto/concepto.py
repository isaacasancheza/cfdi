from decimal import Decimal
from typing import Annotated

from pydantic import StringConstraints
from pydantic_xml import attr, element

from cfdi import fields
from cfdi.v40 import catalogos
from cfdi.v40.base import BaseModel
from cfdi.v40.concepto.a_cuenta_terceros import ACuentaTerceros
from cfdi.v40.concepto.cuenta_predial import CuentaPredial
from cfdi.v40.concepto.impuestos import Impuestos
from cfdi.v40.concepto.informacion_aduanera import InformacionAduanera
from cfdi.v40.concepto.parte import Parte


class Concepto(
    BaseModel,
    tag='Concepto',
):
    """
    Schema of a "Concepto" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    impuestos: Impuestos | None = None
    """
    Nodo opcional para capturar los impuestos aplicables al presente concepto. Cuando un concepto no registra un
    impuesto, implica que no es objeto del mismo.
    """

    informacion_aduanera: list[InformacionAduanera] = []
    """
    Nodo opcional para introducir la información aduanera aplicable cuando se trate de ventas de primera mano de
    mercancías importadas o se trate de operaciones de comercio exterior con bienes o servicios.
    """

    cuenta_predial: list[CuentaPredial] = []
    """
    Nodo opcional para asentar el número de cuenta predial con el que fue registrado el inmueble, en el sistema
    catastral de la entidad federativa de que trate, o bien para incorporar los datos de identificación del
    certificado de participación inmobiliaria no amortizable.
    """

    complemento_concepto: list[dict[str, str]] = element(
        'ComplementoConcepto', default=[]
    )  # TODO agrega timbre fiscal digital
    """
    Nodo opcional donde se incluyen los nodos complementarios de extensión al concepto definidos por el SAT,
    de acuerdo con las disposiciones particulares para un sector o actividad específica.
    """

    parte: list[Parte] = []
    """
    Nodo opcional para expresar las partes o componentes que integran la totalidad del concepto expresado en el
    comprobante fiscal digital por Internet.
    """

    clave_prod_serv: str = attr('ClaveProdServ')
    """
    Atributo requerido para expresar la clave del producto o del servicio amparado por el presente concepto.
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
    Atributo opcional para expresar el número de parte, identificador del producto o del servicio, la clave de
    producto o servicio, SKU o equivalente, propia de la operación del emisor, amparado por el presente concepto.
    Opcionalmente se puede utilizar claves del estándar GTIN.
    """

    cantidad: fields.PositiveSixDecimals = attr('Cantidad')
    """
    Atributo requerido para precisar la cantidad de bienes o servicios del tipo particular definido por el presente
    concepto.
    """

    clave_unidad: str = attr('ClaveUnidad')
    """
    Atributo requerido para precisar la clave de unidad de medida estandarizada aplicable para la cantidad expresada
    en el concepto. La unidad debe corresponder con la descripción del concepto.
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
    cantidad expresada en el concepto. La unidad debe corresponder con la descripción del concepto.
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
    Atributo requerido para precisar la descripción del bien o servicio cubierto por el presente concepto.
    """

    valor_unitario: fields.NonNegativeSixDecimals = attr('ValorUnitario')
    """
    Atributo requerido para precisar el valor o precio unitario del bien o servicio cubierto por el presente concepto.
    """

    importe: fields.NonNegativeSixDecimals = attr('Importe')
    """
    Atributo requerido para precisar el importe total de los bienes o servicios del presente concepto. Debe ser
    equivalente al resultado de multiplicar la cantidad por el valor unitario expresado en el concepto.
    No se permiten valores negativos.
    """

    descuento: fields.NonNegativeSixDecimals = attr('Descuento', default=Decimal(0))
    """
    Atributo opcional para representar el importe de los descuentos aplicables al concepto. No se permiten valores
    negativos.
    """

    objeto_imp: catalogos.ObjetoImp = attr('ObjetoImp')
    """
    Atributo requerido para expresar si la operación comercial es objeto o no de impuesto.
    """

    a_cuenta_terceros: list[ACuentaTerceros] = []
    """
    Nodo opcional para registrar información del contribuyente Tercero, a cuenta del que se realiza la operación.
    """
