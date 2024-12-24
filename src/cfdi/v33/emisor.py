from pydantic_xml import attr

from cfdi import catalogos, fields
from cfdi.v33.base import BaseModel


class Emisor(
    BaseModel,
    tag='Emisor',
):
    rfc: fields.RFC = attr('Rfc')
    """
    Atributo requerido para registrar la Clave del Registro Federal de Contribuyentes 
    correspondiente al contribuyente emisor del comprobante.
    """

    nombre: str = attr('Nombre')
    """
    Atributo opcional para registrar el nombre, denominación o razón social del contribuyente emisor del comprobante.
    """

    regimen_fiscal: catalogos.RegimenFiscal = attr('RegimenFiscal')
    """
    Atributo requerido para incorporar la clave del régimen del contribuyente emisor al que 
    aplicará el efecto fiscal de este comprobante.
    """
