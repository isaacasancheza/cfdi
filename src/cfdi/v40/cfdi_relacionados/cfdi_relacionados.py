from pydantic_xml import attr

from cfdi.v40 import catalogos
from cfdi.v40.base import BaseModel
from cfdi.v40.cfdi_relacionados.cfdi_relacionado import CFDIRelacionado


class CFDIRelacionados(
    BaseModel,
    tag='CfdiRelacionados',
):
    """
    Schema of a "Cfdi Relacionados" of a CFDI v4.0.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    """

    tipo_relacion: catalogos.TipoRelacion = attr('TipoRelacion')
    """
    Atributo requerido para indicar la clave de la relación que existe entre éste que se esta generando y el o
    los CFDI previos.
    """

    cfdi_relacionados: list[CFDIRelacionado]
    """
    CFDIs relacionados.
    """
