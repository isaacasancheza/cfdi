from pydantic_xml import attr

from cfdi import fields
from cfdi.v40 import catalogos
from cfdi.v40.base import BaseModel


class Retencion(
    BaseModel,
    tag='Retencion',
):
    """
    Schema of a "Comprobante / Retencion" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    impuesto: catalogos.Impuesto = attr('Impuesto')
    """
    Atributo requerido para señalar la clave del tipo de impuesto retenido
    """

    importe: fields.NonNegativeSixDecimals = attr('Importe')
    """
    Atributo requerido para señalar el monto del impuesto retenido. No se permiten valores negativos.
    """
