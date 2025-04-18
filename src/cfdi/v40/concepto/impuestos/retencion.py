from pydantic_xml import attr

from cfdi import fields
from cfdi.v40 import catalogos
from cfdi.v40.base import BaseModel


class Retencion(
    BaseModel,
    tag='Retencion',
):
    """
    Schema of a "Concepto / Impuestos / Retencion" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    base: fields.PositiveSixDecimals = attr('Base')
    """
    Atributo requerido para señalar la base para el cálculo del impuesto, la determinación de la base se realiza de
    acuerdo con las disposiciones fiscales vigentes. No se permiten valores negativos.
    """

    impuesto: catalogos.Impuesto = attr('Impuesto')
    """
    Atributo requerido para señalar la clave del tipo de impuesto retenido aplicable al concepto.
    """

    tipo_factor: catalogos.TipoFactor = attr('TipoFactor')
    """
    Atributo requerido para señalar la clave del tipo de factor que se aplica a la base del impuesto.
    """

    tasa_o_cuota: fields.NonNegativeSixDecimals = attr('TasaOCuota')
    """
    Atributo condicional para señalar el valor de la tasa o cuota del impuesto que se retiene para el presente
    concepto. Es requerido cuando el atributo TipoFactor tenga una clave que corresponda a Tasa o Cuota.
    """

    importe: fields.NonNegativeSixDecimals = attr('Importe')
    """
    Atributo requerido para señalar el importe del impuesto retenido que aplica al concepto.
    No se permiten valores negativos.
    """
