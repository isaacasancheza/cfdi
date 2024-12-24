from decimal import Decimal

from pydantic_xml import attr, wrapped

from cfdi import fields
from cfdi.v40.base import BaseModel
from cfdi.v40.impuestos.retencion import Retencion
from cfdi.v40.impuestos.traslado import Traslado


class Impuestos(
    BaseModel,
    tag='Impuestos',
):
    """
    Schema of a "Comprobante / Impuestos" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    retenciones: list[Retencion] = wrapped('Retenciones', default=[])
    """
    Nodo condicional para capturar los impuestos retenidos aplicables. Es requerido cuando en los conceptos se
    registre algún impuesto retenido
    """

    traslados: list[Traslado] = wrapped('Traslados', default=[])
    """
    Nodo condicional para capturar los impuestos trasladados aplicables. Es requerido cuando en los conceptos se
    registre un impuesto trasladado.
    """

    total_impuestos_retenidos: fields.NonNegativeSixDecimals = attr(
        'TotalImpuestosRetenidos', default=Decimal(0)
    )
    """
    Atributo condicional para expresar el total de los impuestos retenidos que se desprenden de los conceptos
    expresados en el comprobante fiscal digital por Internet. No se permiten valores negativos. Es requerido cuando
    en los conceptos se registren impuestos retenidos
    """

    total_impuestos_trasladados: fields.NonNegativeSixDecimals = attr(
        'TotalImpuestosTrasladados', default=Decimal(0)
    )
    """
    Atributo condicional para expresar el total de los impuestos trasladados que se desprenden de los conceptos
    expresados en el comprobante fiscal digital por Internet. No se permiten valores negativos. Es requerido cuando
    en los conceptos se registren impuestos trasladados.
    """
