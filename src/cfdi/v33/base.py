from abc import ABC

from pydantic_xml import BaseXmlModel


class BaseModel(
    BaseXmlModel,
    ABC,
    ns='cfdi',
    nsmap={
        'cfdi': 'http://www.sat.gob.mx/cfd/3',
    },
):
    pass
