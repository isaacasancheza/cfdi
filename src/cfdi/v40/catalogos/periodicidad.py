from enum import StrEnum


class Periodicidad(StrEnum):
    P_SEMANAL = '02'
    """Semanal"""
    P_QUINCENAL = '03'
    """Quincenal"""
    P_MENSUAL = '04'
    """Mensual"""
    P_BIMESTRAL = '05'
    """Bimestral"""
