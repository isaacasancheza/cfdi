from enum import StrEnum


class Impuesto(StrEnum):
    """
    Catálogo de "Impuesto".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    ISR = '001'
    """
    Impuesto Sobre la Renta (ISR).
    """

    IVA = '002'
    """
    Impuesto al Valor Agregado (IVA).
    """

    IEPS = '003'
    """
    Impuesto Especial Sobre Producción y Servicios (IEPS).
    """
