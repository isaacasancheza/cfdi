from pydantic_xml import wrapped

from cfdi.v33.base import BaseModel
from cfdi.v33.concepto.impuestos.retencion import Retencion
from cfdi.v33.concepto.impuestos.traslado import Traslado


class Impuestos(
    BaseModel,
    tag='Impuestos',
):
    """
    Schema of a "Concepto / Impuestos" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    traslados: list[Traslado] = wrapped('Traslados', default=[])
    """
    Nodo opcional para asentar los impuestos trasladados aplicables al presente concepto.
    """

    retenciones: list[Retencion] = wrapped('Retenciones', default=[])
    """
    Nodo opcional para asentar los impuestos retenidos aplicables al presente concepto.
    """
