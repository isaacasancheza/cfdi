from typing import Annotated

from pydantic import StringConstraints
from pydantic_xml import attr

from cfdi import fields
from cfdi.v40 import catalogos
from cfdi.v40.base import BaseModel


class Emisor(
    BaseModel,
    tag='Emisor',
):
    """
    Schema of a "Emisor" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    rfc: fields.RFC = attr('Rfc')
    """
    Atributo requerido para registrar la Clave del Registro Federal de Contribuyentes correspondiente al
    contribuyente emisor del comprobante.
    """

    nombre: Annotated[
        str,
        StringConstraints(
            min_length=1,
            max_length=300,
            pattern=r'[^|]{1,300}',
        ),
    ] = attr('Nombre')
    """
    Atributo requerido para registrar el nombre, denominación o razón social del contribuyente inscrito en el RFC,
    del emisor del comprobante.
    """

    regimen_fiscal: catalogos.RegimenFiscal = attr('RegimenFiscal')
    """
    Atributo requerido para incorporar la clave del régimen del contribuyente emisor al que aplicará el efecto
    fiscal de este comprobante.
    """

    fac_atr_adquirente: Annotated[
        str | None,
        StringConstraints(
            min_length=10,
            max_length=10,
            pattern=r'[0-9]{10}',
        ),
    ] = attr('FacAtrAdquirente', default=None)
    """
    Atributo condicional para expresar el número de operación proporcionado por el SAT cuando se trate de un
    comprobante a través de un PCECFDI o un PCGCFDISP.
    """
