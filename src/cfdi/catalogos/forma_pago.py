from enum import StrEnum


class FormaPago(StrEnum):
    """
    Catálogo de "Forma Pago".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    EFECTIVO = '01'
    """
    Efectivo.
    """

    CHEQUE_NOMINATIVO = '02'
    """
    Cheque nominativo.
    """

    TRANSFERENCIA = '03'
    """
    Transferencia electrónica de fondos.
    """

    TARJETA_DE_CREDITO = '04'
    """
    Tarjeta de crédito.
    """

    MONEDERO_ELECTRONICO = '05'
    """
    Monedero electrónico.
    """

    DINERO_ELECTRONICO = '06'
    """
    Dinero electrónico.
    """

    VALES_DE_DESPENSA = '08'
    """
    Vales de despensa.
    """

    DACION_EN_PAGO = '12'
    """
    Dación en pago.
    """

    PAGO_SUBROGACION = '13'
    """
    Pago por subrogación.
    """

    PAGO_CONSIGNACION = '14'
    """
    Pago por consignación.
    """

    CONDONACION = '15'
    """
    Condonación.
    """

    COMPENSACION = '17'
    """
    Compensación.
    """

    NOVACION = '23'
    """
    Novación.
    """

    CONFUSION = '24'
    """
    Confusión.
    """

    REMISION = '25'
    """
    Remisión de deuda.
    """

    PRESCRIPCION = '26'
    """
    Prescripción o caducidad.
    """

    A_SATISFACCION = '27'
    """
    A satisfacción del acreedor.
    """

    TARJETA_DE_DEBITO = '28'
    """
    Tarjeta de débito.
    """

    TARJETA_DE_SERVICIOS = '29'
    """
    Tarjeta de servicios.
    """

    APLICACION_DE_ANTICIPOS = '30'
    """
    Aplicación de anticipos.
    """

    INTERMEDIARIO_PAGOS = '31'
    """
    Intermediario pagos.
    """

    POR_DEFINIR = '99'
    """
    Por definir.
    """
