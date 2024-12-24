from enum import StrEnum


class ObjetoImp(StrEnum):
    OI_01 = '01'
    """No objeto de impuesto."""
    OI_02 = '02'
    """Sí objeto de impuesto."""
    OI_03 = '03'
    """Sí objeto del impuesto y no obligado al desglose."""
    OI_04 = '04'
    """Sí objeto del impuesto y no causa impuesto."""
    OI_05 = '05'
    """Sí objeto del impuesto, IVA crédito PODEBI."""
    OI_06 = '06'
    """Sí objeto del IVA, No traslado IVA."""
    OI_07 = '07'
    """No traslado del IVA, Sí desglose IEPS."""
    OI_08 = '08'
    """No traslado del IVA, No desglose IEPS."""
