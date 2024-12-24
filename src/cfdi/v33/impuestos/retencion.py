from pydantic_xml import attr

from cfdi import catalogos, fields
from cfdi.v33.base import BaseModel


class Retencion(
    BaseModel,
    tag='Retencion',
):
    """
    Schema of a "Comprobante / Retencion" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    impuesto: catalogos.Impuesto = attr('Impuesto')
    """
    Atributo requerido para señalar la clave del tipo de impuesto retenido
    """

    importe: fields.NonNegativeSixDecimals = attr('Importe')
    """
    Atributo requerido para señalar el monto del impuesto retenido. No se permiten valores negativos.
    """
