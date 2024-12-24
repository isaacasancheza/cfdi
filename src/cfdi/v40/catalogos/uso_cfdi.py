from enum import StrEnum


class UsoCFDI(StrEnum):
    UC_G01 = 'G01'
    """Adquisición de mercancías."""
    UC_G02 = 'G02'
    """Devoluciones, descuentos o bonificaciones."""
    UC_G03 = 'G03'
    """Gastos en general."""
    UC_I01 = 'I01'
    """Construcciones."""
    UC_I02 = 'I02'
    """Mobiliario y equipo de oficina por inversiones."""
    UC_I03 = 'I03'
    """Equipo de transporte."""
    UC_I04 = 'I04'
    """Equipo de computo y accesorios."""
    UC_I05 = 'I05'
    """Dados, troqueles, moldes, matrices y herramental."""
    UC_I06 = 'I06'
    """Comunicaciones telefónicas."""
    UC_I07 = 'I07'
    """Comunicaciones satelitales."""
    UC_I08 = 'I08'
    """Otra maquinaria y equipo."""
    UC_D01 = 'D01'
    """Honorarios médicos, dentales y gastos hospitalarios."""
    UC_D02 = 'D02'
    """Gastos médicos por incapacidad o discapacidad."""
    UC_D03 = 'D03'
    """Gastos funerales."""
    UC_D04 = 'D04'
    """Donativos."""
    UC_D05 = 'D05'
    """Intereses reales efectivamente pagados por créditos hipotecarios (casa habitación)."""
    UC_D06 = 'D06'
    """Aportaciones voluntarias al SAR."""
    UC_D07 = 'D07'
    """Primas por seguros de gastos médicos."""
    UC_D08 = 'D08'
    """Gastos de transportación escolar obligatoria."""
    UC_D09 = 'D09'
    """Depósitos en cuentas para el ahorro, primas que tengan como base planes de pensiones."""
    UC_D10 = 'D10'
    """Pagos por servicios educativos (colegiaturas)."""
    UC_S01 = 'S01'
    """Sin efectos fiscales."""
    UC_CP01 = 'CP01'
    """Pagos"""
    UC_CN01 = 'CN01'
    """Nómina"""
