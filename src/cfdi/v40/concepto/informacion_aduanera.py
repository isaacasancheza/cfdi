from typing import Annotated

from pydantic import StringConstraints
from pydantic_xml import attr

from cfdi.v40.base import BaseModel


class InformacionAduanera(
    BaseModel,
    tag='InformacionAduanera',
):
    """
    Schema of a "Informacion Aduanera" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    numero_pedimento: Annotated[
        str,
        StringConstraints(
            min_length=21,
            max_length=21,
            pattern=r'[0-9]{2}  [0-9]{2}  [0-9]{4}  [0-9]{7}',
        ),
    ] = attr('NumeroPedimento')
    """
    Atributo requerido para expresar el número del pedimento que ampara la importación del bien que se expresa en el
    siguiente formato: últimos 2 dígitos del año de validación seguidos por dos espacios, 2 dígitos de la aduana de
    despacho seguidos por dos espacios, 4 dígitos del número de la patente seguidos por dos espacios, 1 dígito que
    corresponde al último dígito del año en curso, salvo que se trate de un pedimento consolidado iniciado en el año
    inmediato anterior o del pedimento original de una rectificación, seguido de 6 dígitos de la numeración
    progresiva por aduana.
    """
