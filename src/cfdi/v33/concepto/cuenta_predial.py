from typing import Annotated

from pydantic import StringConstraints
from pydantic_xml import attr

from cfdi.v33.base import BaseModel


class CuentaPredial(
    BaseModel,
    tag='CuentaPredial',
):
    """
    Schema of a "Cuenta Predial" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    numero: Annotated[
        str,
        StringConstraints(
            min_length=1,
            max_length=150,
            pattern=r'[0-9]{1,150}',
        ),
    ] = attr('Numero')
    """
    Atributo requerido para precisar el número de la cuenta predial del inmueble cubierto por el presente concepto,
    o bien para incorporar los datos de identificación del certificado de participación inmobiliaria no amortizable,
    tratándose de arrendamiento.
    """
