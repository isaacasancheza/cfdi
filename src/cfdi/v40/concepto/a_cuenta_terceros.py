from typing import Annotated

from pydantic import StringConstraints
from pydantic_xml import attr

from cfdi import fields
from cfdi.v40 import catalogos
from cfdi.v40.base import BaseModel


class ACuentaTerceros(
    BaseModel,
    tag='ACuentaTerceros',
):
    """
    Schema of a "Comprobante / Concepto / ACuentaTerceros" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    rfc_a_cuenta_terceros: fields.RFC = attr('RfcACuentaTerceros')
    """
    Atributo requerido para registrar la Clave del Registro Federal de Contribuyentes del contribuyente Tercero,
    a cuenta del que se realiza la operación.
    """

    nombre_a_cuenta_terceros: Annotated[
        str,
        StringConstraints(
            min_length=1,
            max_length=300,
            pattern=r'[^|]{1,300}',
        ),
    ] = attr('NombreACuentaTerceros')
    """
    Atributo requerido para registrar el nombre, denominación o razón social del contribuyente Tercero
    correspondiente con el Rfc, a cuenta del que se realiza la operación.
    """

    regimen_fiscal_a_cuenta_terceros: catalogos.RegimenFiscal = attr(
        'RegimenFiscalACuentaTerceros'
    )
    """
    Atributo requerido para incorporar la clave del régimen del contribuyente Tercero, a cuenta del que se realiza
    la operación.
    """

    domicilio_fiscal_a_cuenta_terceros: Annotated[
        str,
        StringConstraints(
            min_length=5,
            max_length=5,
            pattern=r'[0-9]{5}',
        ),
    ] = attr('DomicilioFiscalACuentaTerceros')
    """
    Atributo requerido para incorporar el código postal del domicilio fiscal del Tercero, a cuenta del que se
    realiza la operación.
    """
