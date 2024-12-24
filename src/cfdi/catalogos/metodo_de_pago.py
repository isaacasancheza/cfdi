from enum import StrEnum


class MetodoDePago(StrEnum):
    """
    Catálogo de "Metodo De Pago".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    PUE = 'PUE'
    """
    Pago en una sola exhibición.
    """

    PPD = 'PPD'
    """
    Pago en parcialidades o diferido.
    """
