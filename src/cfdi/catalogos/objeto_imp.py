from enum import StrEnum


class ObjetoImp(StrEnum):
    """
    Catálogo de "Objecto Imp".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    O01 = '01'
    """
    No objeto de impuesto.
    """

    O02 = '02'
    """
    Sí objeto de impuesto.
    """

    O03 = '03'
    """
    Sí objeto del impuesto y no obligado al desglose.
    """

    O04 = '04'
    """
    Sí objeto del impuesto y no causa impuesto.
    """

    O05 = '05'
    """
    Sí objeto del impuesto, IVA crédito PODEBI.
    """

    O06 = '06'
    """
    Sí objeto del IVA, No traslado IVA.
    """

    O07 = '07'
    """
    No traslado del IVA, Sí desglose IEPS.
    """

    O08 = '08'
    """
    No traslado del IVA, No desglose IEPS.
    """
