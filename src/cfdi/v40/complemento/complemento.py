from cfdi.v40.base import BaseModel
from cfdi.v40.complemento.timbre_fiscal_digital import TimbreFiscalDigital


class Complemento(
    BaseModel,
    tag='Complemento',
):
    timbre_fiscal_digital: TimbreFiscalDigital | None = None
