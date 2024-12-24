from decimal import Decimal

from pydantic_xml import attr

from cfdi import fields
from cfdi.v40 import catalogos
from cfdi.v40.base import BaseModel


class Traslado(
    BaseModel,
    tag='Traslado',
):
    """
    Schema of a "Comprobante / Traslado" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    impuesto: catalogos.Impuesto = attr('Impuesto')
    """
    Atributo requerido para señalar la clave del tipo de impuesto trasladado.
    """

    tipo_factor: catalogos.TipoFactor = attr('TipoFactor')
    """
    Atributo requerido para señalar la clave del tipo de factor que se aplica a la base del impuesto.
    """

    base: fields.NonNegativeSixDecimals = attr('Base')
    """
    Atributo requerido para señalar la suma de los atributos Base de los conceptos del impuesto trasladado.
    No se permiten valores negativos.
    """

    tasa_o_cuota: fields.NonNegativeSixDecimals = attr('TasaOCuota', default=Decimal(0))
    """
    Atributo condicional para señalar el valor de la tasa o cuota del impuesto que se traslada por los conceptos
    amparados en el comprobante.
    """

    importe: fields.NonNegativeSixDecimals = attr('Importe', default=Decimal(0))
    """
    Atributo condicional para señalar la suma del importe del impuesto trasladado, agrupado por impuesto, TipoFactor
    y TasaOCuota. No se permiten valores negativos.
    """
