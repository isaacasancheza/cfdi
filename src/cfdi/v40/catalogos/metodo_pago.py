from enum import StrEnum


class MetodoPago(StrEnum):
    MP_PUE = 'PUE'
    """Pago en una sola exhibición"""
    MP_PPD = 'PPD'
    """Pago en parcialidades o diferido"""
