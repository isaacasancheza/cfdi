from enum import StrEnum


class TipoRelacion(StrEnum):
    TR_01 = '01'
    """Nota de crédito de los documentos relacionados"""
    TR_02 = '02'
    """Nota de débito de los documentos relacionados"""
    TR_03 = '03'
    """Devolución de mercancía sobre facturas o traslados previos"""
    TR_04 = '04'
    """Sustitución de los CFDI previos"""
    TR_05 = '05'
    """Traslados de mercancías facturados previamente"""
    TR_06 = '06'
    """Factura generada por los traslados previos"""
    TR_07 = '07'
    """CFDI por aplicación de anticipo"""
