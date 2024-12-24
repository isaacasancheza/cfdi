from enum import StrEnum


class TipoFactor(StrEnum):
    """
    Catálogo de "Tipo Factor".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    TASA = 'Tasa'
    """
    Tasa.
    """

    CUOTA = 'Cuota'
    """
    Cuota.
    """

    EXENTO = 'Exento'
    """
    Exento.
    """
