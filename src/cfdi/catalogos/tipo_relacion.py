from enum import StrEnum


class TipoRelacion(StrEnum):
    """
    Catálogo de "Tipo Relacion".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    NOTA_CREDITO = '01'
    """
    Nota de crédito de los documentos relacionados.
    """

    NOTA_DEBITO = '02'
    """
    Nota de débito de los documentos relacionados.
    """

    DEVOLUCION = '03'
    """
    Devolución de mercancía sobre facturas o traslados previos.
    """

    SUSTITUCION = '04'
    """
    Sustitución de los CFDI previos.
    """

    TRASLADOS = '05'
    """
    Traslados de mercancias facturados previamente.
    """

    FACTURA_TRASLADOS = '06'
    """
    Factura generada por los traslados previos.
    """

    APLICACION_DE_ANTICIPO = '07'
    """
    CFDI por aplicación de anticipo.
    """

    PAGOS_EN_PARCIALIDADES = '08'
    """
    Facturas Generadas por Pagos en Parcialidades.
    """

    PAGOS_DIFERIDOS = '09'
    """
    Factura Generada por Pagos Diferidos.
    """
