from enum import StrEnum


class TipoDeComprobante(StrEnum):
    """
    Catálogo de "Tipo De Comprobante".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    INGRESO = 'I'
    """
    Ingreso.
    """

    EGRESO = 'E'
    """
    Egreso.
    """

    TRASLADO = 'T'
    """
    Traslado.
    """

    NOMINA = 'N'
    """
    Nomina.
    """

    PAGO = 'P'
    """
    Pago.
    """
