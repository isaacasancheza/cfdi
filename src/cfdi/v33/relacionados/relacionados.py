from pydantic_xml import attr

from cfdi import catalogos
from cfdi.v33.base import BaseModel
from cfdi.v33.relacionados.relacionado import Relacionado


class Relacionados(BaseModel):
    """
    Schema of a "Cfdi Relacionados" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    tipo_relacion: catalogos.TipoRelacion = attr('TipoRelacion')
    """
    Atributo requerido para indicar la clave de la relación que existe entre éste que se esta generando y el o
    los CFDI previos.
    """

    cfdi_relacionado: list[Relacionado]
    """
    CFDI Relacionados.
    """
