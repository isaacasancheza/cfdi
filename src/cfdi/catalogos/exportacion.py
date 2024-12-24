from enum import StrEnum


class Exportacion(StrEnum):
    """
    Catálogo de "Exportacion".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    E01 = '01'
    """
    No aplica.
    """

    E02 = '02'
    """
    Definitiva.
    """

    E03 = '03'
    """
    Temporal.
    """

    E04 = '04'
    """
    Definitiva con clave distinta a A1 o cuando no existe enajenación en términos del CFF.
    """
