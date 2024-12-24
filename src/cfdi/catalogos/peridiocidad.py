from enum import StrEnum


class Periodicidad(StrEnum):
    """
    Catálogo de "Periodicidad".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    P01 = '01'
    """
    Mensual.
    """

    P02 = '02'
    """
    Bimestral.
    """

    P03 = '03'
    """
    Trimestral.
    """

    P04 = '04'
    """
    Cuatrimestral.
    """

    P05 = '05'
    """
    Semestral.
    """

    P06 = '06'
    """
    Semestral por Liquidación.
    """

    P07 = '07'
    """
    Del Ejercicio.
    """

    P08 = '08'
    """
    Del ejercicio por liquidación.
    """

    P09 = '09'
    """
    Ajuste.
    """

    P10 = '10'
    """
    Sin Periodo.
    """
