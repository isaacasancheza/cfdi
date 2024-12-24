from enum import StrEnum


class TipoDeComprobante(StrEnum):
    TC_INGRESO = 'I'
    """Ingreso"""
    TC_EGRESO = 'E'
    """Egreso"""
    TC_TRASLADO = 'T'
    """Traslado"""
    TC_NÓMINA = 'N'
    """Nómina"""
    TC_PAGO = 'P'
    """Pago"""
