from typing import Annotated

from pydantic import Field
from pydantic_xml import attr

from cfdi import catalogos, fields
from cfdi.v33.base import BaseModel


class Receptor(
    BaseModel,
    tag='Receptor',
):
    """
    Schema of a "Receptor" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    rfc: fields.RFC = attr('Rfc')
    """
    Atributo requerido para precisar la Clave del Registro Federal de Contribuyentes correspondiente al
    contribuyente receptor del comprobante.
    """

    nombre: str | None = attr('Nombre', default=None)
    """
    Atributo opcional para precisar el nombre, denominación o razón social del contribuyente receptor del
    comprobante.
    """

    residencia_fiscal: catalogos.Pais | None = attr('ResidenciaFiscal', default=None)
    """
    Atributo condicional para registrar la clave del país de residencia para efectos fiscales del receptor del
    comprobante, cuando se trate de un extranjero, y que es conforme con la especificación ISO 3166-1 alpha-3.
    Es requerido cuando se incluya el complemento de comercio exterior o se registre el atributo NumRegIdTrib.
    """

    num_reg_id_trib: Annotated[
        str | None,
        Field(
            min_length=1,
            max_length=40,
        ),
    ] = attr('NumRegIdTrib', default=None)
    """
    Atributo condicional para expresar el número de registro de identidad fiscal del receptor cuando sea residente
    en el extranjero. Es requerido cuando se incluya el complemento de comercio exterior.
    """

    uso_cfdi: catalogos.UsoCFDI = attr('UsoCFDI')
    """
    Atributo requerido para expresar la clave del uso que dará a esta factura el receptor del CFDI.
    """
