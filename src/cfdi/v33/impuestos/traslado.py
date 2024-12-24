from pydantic_xml import attr

from cfdi import catalogos, fields
from cfdi.v33.base import BaseModel


class Traslado(
    BaseModel,
    tag='Traslado',
):
    """
    Schema of a "Comprobante / Traslado" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    base: fields.PositiveSixDecimals | None = attr('Base', default=None)
    """
    Atributo opcional para señalar la base para el cálculo del impuesto, la determinación de la base se realiza de
    acuerdo con las disposiciones fiscales vigentes. No se permiten valores negativos.
    """

    impuesto: catalogos.Impuesto = attr('Impuesto')
    """
    Atributo requerido para señalar la clave del tipo de impuesto trasladado.
    """

    tipo_factor: catalogos.TipoFactor = attr('TipoFactor')
    """
    Atributo requerido para señalar la clave del tipo de factor que se aplica a la base del impuesto.
    """

    tasa_o_cuota: fields.NonNegativeSixDecimals = attr('TasaOCuota')
    """
    Atributo requerido para señalar el valor de la tasa o cuota del impuesto que se traslada por los conceptos
    amparados en el comprobante.
    """

    importe: fields.NonNegativeSixDecimals = attr('Importe')
    """
    Atributo requerido para señalar la suma del importe del impuesto trasladado, agrupado por impuesto, TipoFactor
    y TasaOCuota. No se permiten valores negativos.
    """
