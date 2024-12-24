from enum import StrEnum


class FormaPago(StrEnum):
    FP_01 = '01'
    """Efectivo"""
    FP_02 = '02'
    """Cheque nominativo"""
    FP_03 = '03'
    """Transferencia electrónica de fondos"""
    FP_04 = '04'
    """Tarjeta de crédito"""
    FP_05 = '05'
    """Monedero electrónico"""
    FP_06 = '06'
    """Dinero electrónico"""
    FP_08 = '08'
    """Vales de despensa"""
    FP_12 = '12'
    """Dación en pago"""
    FP_13 = '13'
    """Pago por subrogación"""
    FP_14 = '14'
    """Pago por consignación"""
    FP_15 = '15'
    """Condonación"""
    FP_17 = '17'
    """Compensación"""
    FP_23 = '23'
    """Novación"""
    FP_24 = '24'
    """Confusión"""
    FP_25 = '25'
    """Remisión de deuda"""
    FP_26 = '26'
    """Prescripción o caducidad"""
    FP_27 = '27'
    """A satisfacción del acreedor"""
    FP_28 = '28'
    """Tarjeta de débito"""
    FP_29 = '29'
    """Tarjeta de servicios"""
    FP_30 = '30'
    """Aplicación de anticipos"""
    FP_31 = '31'
    """Intermediario pagos"""
    FP_99 = '99'
    """Por definir"""
