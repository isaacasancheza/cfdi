from enum import StrEnum


class RegimenFiscal(StrEnum):
    """
    Catálogo de "Regimen Fiscal".

    http://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    R601 = '601'
    """
    General de Ley Personas Morales.
    """

    R603 = '603'
    """
    Personas Morales con Fines no Lucrativos.
    """

    R605 = '605'
    """
    Sueldos y Salarios e Ingresos Asimilados a Salarios.
    """

    R606 = '606'
    """
    Arrendamiento.
    """

    R607 = '607'
    """
    Régimen de Enajenación o Adquisición de Bienes.
    """

    R608 = '608'
    """
    Demás ingresos.
    """

    R609 = '609'
    """
    Consolidación.
    """

    R610 = '610'
    """
    Residentes en el Extranjero sin Establecimiento Permanente en México.
    """

    R611 = '611'
    """
    Ingresos por Dividendos (socios y accionistas).
    """

    R612 = '612'
    """
    Personas Físicas con Actividades Empresariales y Profesionales.
    """

    R614 = '614'
    """
    Ingresos por intereses.
    """

    R615 = '615'
    """
    Régimen de los ingresos por obtención de premios.
    """

    R616 = '616'
    """
    Sin obligaciones fiscales.
    """

    R620 = '620'
    """
    Sociedades Cooperativas de Producción que optan por diferir sus ingresos.
    """

    R621 = '621'
    """
    Incorporación Fiscal.
    """

    R622 = '622'
    """
    Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras.
    """

    R623 = '623'
    """
    Opcional para Grupos de Sociedades.
    """

    R624 = '624'
    """
    Coordinados.
    """

    R625 = '625'
    """
    Régimen de las Actividades Empresariales con ingresos a través de Plataformas Tecnológicas.
    """

    R626 = '626'
    """
    Régimen Simplificado de Confianza.
    """

    R628 = '628'
    """
    Hidrocarburos.
    """

    R629 = '629'
    """
    De los Regímenes Fiscales Preferentes y de las Empresas Multinacionales.
    """

    R630 = '630'
    """
    Enajenación de acciones en bolsa de valores.
    """
