from enum import StrEnum


class Exportacion(StrEnum):
    E_01 = '01'
    """No aplica"""
    E_02 = '02'
    """Definitiva con clave A1"""
    E_03 = '03'
    """Temporal"""
    E_04 = '04'
    """Definitiva con clave distinta a A1 o cuando no existe enajenación en términos del CFF"""
