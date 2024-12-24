from datetime import datetime
from re import sub
from uuid import UUID

from pydantic_xml import BaseXmlModel, attr


class TimbreFiscalDigital(
    BaseXmlModel,
    ns='tfd',
    nsmap={
        'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital',
    },
    tag='TimbreFiscalDigital',
):
    """
    Complemento requerido para el Timbrado Fiscal Digital que da validez al Comprobante fiscal digital por Internet.

    https://www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd
    """

    version: str = attr('Version')
    """
    Atributo requerido para la expresión de la versión del estándar del Timbre Fiscal Digital
    """

    uuid: UUID = attr('UUID')
    """
    Atributo requerido para expresar los 36 caracteres del folio fiscal (UUID) de la transacción de timbrado
    conforme al estándar RFC 4122
    """

    fecha_timbrado: datetime = attr('FechaTimbrado')
    """
    Atributo requerido para expresar la fecha y hora, de la generación del timbre por la certificación digital del
    SAT. Se expresa en la forma AAAA-MM-DDThh:mm:ss y debe corresponder con la hora de la Zona Centro del
    Sistema de Horario en México.
    """

    rfc_prov_certif: str = attr('RfcProvCertif')
    """
    Atributo requerido para expresar el RFC del proveedor de certificación de comprobantes fiscales digitales que
    genera el timbre fiscal digital.
    """

    leyenda: str | None = attr('Leyenda', default=None)
    """
    Atributo opcional para registrar información que el SAT comunique a los usuarios del CFDI.
    """

    sello_cfd: str = attr('SelloCFD')
    """
    Atributo requerido para contener el sello digital del comprobante fiscal o del comprobante de retenciones,
    que se ha timbrado. El sello debe ser expresado como una cadena de texto en formato Base 64.
    """

    no_certificado_sat: str = attr('NoCertificadoSAT')
    """
    Atributo requerido para expresar el número de serie del certificado del SAT usado para generar el sello digital
    del Timbre Fiscal Digital.
    """

    sello_sat: str = attr('SelloSAT')
    """
    Atributo requerido para contener el sello digital del Timbre Fiscal Digital, al que hacen referencia las reglas
    de la Resolución Miscelánea vigente. El sello debe ser expresado como una cadena de texto en formato Base 64.
    """

    @property
    def cadena_original(self) -> str:
        """
        ## Reglas Generales

        1. Ninguno de los atributos que conforman al comprobante fiscal digital deberá contener el carácter | (“pipe”) debido a que este será utilizado como carácter de control en la formación de la cadena original.

        2. La cadena original resultante del complemento será integrada a la cadena original del comprobante de acuerdo con lo especificado en el anexo 20 de la Resolución Miscelánea Fiscal

        3. Se expresará únicamente la información del dato sin expresar el atributo al que hace referencia. Esto es, si el atributo tipoOperación tiene el valor “monedero” solo se expresará |monedero| y nunca |tipoOperacion monedero|.

        4. Cada dato individual se encontrará separado de su dato anterior, en caso de existir, mediante un carácter | (“pipe” sencillo).

            a. Los espacios en blanco que se presenten dentro de la cadena original serán tratados de la siguiente manera:

            b. Se deberán remplazar todos los tabuladores, retornos de carro y saltos de línea por espacios en blanco.

            c. Se deberán remplazar todos los tabuladores, retornos de carro y saltos de línea por espacios en blanco.

            d. Acto seguido se elimina cualquier carácter en blanco al principio y al final de cada separador | (“pipe” sencillo).

            e. Los datos opcionales, cuando no existan, no aparecerán expresados en la cadena original y no tendrán delimitador alguno.

        5. Toda la cadena de original se expresará en el formato de codificación UTF-8.

        6. Finalmente, toda secuencia de caracteres en blanco intermedias se sustituyen por un único carácter en blanco.

        ## Secuencia de Formación

        La secuencia de formación será siempre en el orden que se expresa a continuación, tomando en cuenta las reglas generales expresadas en el párrafo anterior.

        - Atributos del elemento raíz TimbreFiscalDigital
            1. versión
            2. UUID
            3. FechaTimbrado
            4. selloCFD
            5. noCertificadoSAT

        # Nota

        El atributo selloCFD será el sello previo del Comprobante Fiscal Digital, el sello del timbre será guardado dentro del atributo selloSAT. Esta cadena original será sellada utilizando el algoritmo de digestión SHA-1.
        """
        campos = [
            self.version,
            str(self.uuid).upper(),
            self.fecha_timbrado.strftime('%Y-%m-%dT%H:%M:%S'),
            self.sello_sat,
            self.no_certificado_sat,
        ]
        cadena_original = '|'.join(campos)
        cadena_original = sub(r'\s', ' ', cadena_original)
        cadena_original = sub(r'\s+', ' ', cadena_original)
        cadena_original.strip()
        return f'||{cadena_original}||'
