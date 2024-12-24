from pydantic_xml import attr

from cfdi.v40 import catalogos
from cfdi.v40.base import BaseModel


class InformacionGlobal(
    BaseModel,
    tag='InformacionGlobal',
):
    """
    Schema of a "Comprobante / InformacionGlobal" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    periodicidad: catalogos.Periodicidad = attr('Periodicidad')
    """
    Atributo requerido para expresar el período al que corresponde la información del comprobante global.
    """

    meses: catalogos.Meses = attr('Meses')
    """
    Atributo requerido para expresar el mes o los meses al que corresponde la información del comprobante global
    """

    año: int = attr('Año', ge=2021)
    """
    Atributo requerido para expresar el año al que corresponde la información del comprobante global.
    """
