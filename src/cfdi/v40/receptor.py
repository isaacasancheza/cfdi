from typing import Annotated

from pydantic import StringConstraints
from pydantic_xml import attr

from cfdi import fields
from cfdi.v40 import catalogos
from cfdi.v40.base import BaseModel


class Receptor(
    BaseModel,
    tag='Receptor',
):
    """
    Schema of a "Receptor" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    rfc: fields.RFC = attr('Rfc')
    """
    Atributo requerido para precisar la Clave del Registro Federal de Contribuyentes correspondiente al
    contribuyente receptor del comprobante.
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
    Atributo requerido para registrar el nombre(s), primer apellido, segundo apellido, según corresponda,
    denominación o razón social del contribuyente, inscrito en el RFC, del receptor del comprobante.
    """

    domicilio_fiscal_receptor: Annotated[
        str,
        StringConstraints(
            min_length=5,
            max_length=5,
            pattern=r'[0-9]{5}',
        ),
    ] = attr('DomicilioFiscalReceptor')
    """
    Atributo requerido para registrar el código postal del domicilio fiscal del receptor del comprobante.
    """

    residencia_fiscal: catalogos.Pais | None = attr('ResidenciaFiscal', default=None)
    """
    Atributo condicional para registrar la clave del país de residencia para efectos fiscales del receptor del
    comprobante, cuando se trate de un extranjero, y que es conforme con la especificación ISO 3166-1 alpha-3.
    Es requerido cuando se incluya el complemento de comercio exterior o se registre el atributo NumRegIdTrib.
    """

    num_reg_id_trib: Annotated[
        str | None,
        StringConstraints(
            min_length=1,
            max_length=40,
        ),
    ] = attr('NumRegIdTrib', default=None)
    """
    Atributo condicional para expresar el número de registro de identidad fiscal del receptor cuando sea residente
    en el extranjero. Es requerido cuando se incluya el complemento de comercio exterior.
    """

    regimen_fiscal_receptor: catalogos.RegimenFiscal = attr('RegimenFiscalReceptor')
    """
    Atributo requerido para incorporar la clave del régimen del contribuyente receptor al que aplicará el efecto
    fiscal de este comprobante.
    """

    uso_cfdi: catalogos.UsoCFDI = attr('UsoCFDI')
    """ 
    Atributo requerido para expresar la clave del uso que dará a esta factura el receptor del CFDI.
    """
