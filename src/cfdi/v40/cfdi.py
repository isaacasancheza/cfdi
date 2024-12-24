from datetime import datetime
from decimal import Decimal
from pathlib import Path
from typing import IO, Annotated, Literal
from urllib.parse import urlencode

from pydantic import StringConstraints
from pydantic_xml import attr, element, wrapped

from cfdi import fields
from cfdi.v40 import catalogos
from cfdi.v40.base import BaseModel
from cfdi.v40.cfdi_relacionados import CFDIRelacionados
from cfdi.v40.complemento import Complemento
from cfdi.v40.concepto import Concepto
from cfdi.v40.emisor import Emisor
from cfdi.v40.impuestos import Impuestos
from cfdi.v40.informacion_global import InformacionGlobal
from cfdi.v40.receptor import Receptor


class CFDI40(
    BaseModel,
    tag='Comprobante',
):
    """
    Schema of a CFDI version 4.0.

    Based on:

    * https://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd
    * https://www.sat.gob.mx/sitio_internet/cfd/tipoDatos/tdCFDI/tdCFDI.xsd
    * https://www.sat.gob.mx/sitio_internet/cfd/catalogos/catCFDI.xsd
    """

    version: Literal['4.0'] = attr('Version')
    """
    Atributo requerido con valor prefijado a 4.0 que indica la versión del estándar bajo el que se encuentra
    expresado el comprobante.
    """

    serie: Annotated[
        str | None,
        StringConstraints(
            min_length=1,
            max_length=25,
            pattern=r'[^|]{1,25}',
        ),
    ] = attr('Serie', default=None)
    """
    Atributo opcional para precisar la serie para control interno del contribuyente. Este atributo acepta
    una cadena de caracteres
    """

    folio: Annotated[
        str | None,
        StringConstraints(
            min_length=1,
            max_length=40,
            pattern=r'[^|]{1,40}',
        ),
    ] = attr('Folio', default=None)
    """
    Atributo opcional para control interno del contribuyente que expresa el folio del comprobante, acepta una
    cadena de caracteres.
    """

    fecha: datetime = attr('Fecha')
    """
    Atributo requerido para la expresión de la fecha y hora de expedición del Comprobante Fiscal Digital por
    Internet. Se expresa en la forma AAAA-MM-DDThh:mm:ss y debe corresponder con la hora local donde se expide el
    comprobante.
    """

    sello: str = attr('Sello')
    """
    Atributo requerido para contener el sello digital del comprobante fiscal, al que hacen referencia las reglas
    de resolución miscelánea vigente. El sello debe ser expresado como una cadena de texto en formato Base 64.
    """

    forma_pago: catalogos.FormaPago | None = attr('FormaPago', default=None)
    """
    Atributo condicional para expresar la clave de la forma de pago de los bienes o servicios amparados por el
    comprobante. Si no se conoce la forma de pago este atributo se debe omitir.
    """

    no_certificado: Annotated[
        str,
        StringConstraints(
            min_length=1,
            max_length=20,
            pattern=r'[0-9]{20}',
        ),
    ] = attr('NoCertificado')
    """
    Atributo requerido para expresar el número de serie del certificado de sello digital que ampara al comprobante,
    de acuerdo con el acuse correspondiente a 20 posiciones otorgado por el sistema del SAT.
    """

    certificado: str = attr('Certificado')
    """
    Atributo requerido que sirve para incorporar el certificado de sello digital que ampara al comprobante, como
    texto en formato base 64.
    """

    condiciones_de_pago: Annotated[
        str | None,
        StringConstraints(
            min_length=1,
            max_length=1000,
            pattern=r'[^|]{1,1000}',
        ),
    ] = attr('CondicionesDePago', default=None)
    """
    Atributo condicional para expresar las condiciones comerciales aplicables para el pago del comprobante fiscal
    digital por Internet. Este atributo puede ser condicionado mediante atributos o complementos.
    """

    sub_total: fields.NonNegativeSixDecimals = attr('SubTotal')
    """
    Atributo requerido para representar la suma de los importes de los conceptos antes de descuentos e impuesto.
    No se permiten valores negativos.
    """

    descuento: fields.NonNegativeSixDecimals = attr('Descuento', default=Decimal(0))
    """
    Atributo condicional para representar el importe total de los descuentos aplicables antes de impuestos. No se
    permiten valores negativos. Se debe registrar cuando existan conceptos con descuento.
    """

    moneda: catalogos.Moneda = attr('Moneda')
    """
    Atributo requerido para identificar la clave de la moneda utilizada para expresar los montos, cuando se usa
    moneda nacional se registra MXN. Conforme con la especificación ISO 4217.
    """

    tipo_cambio: fields.PositiveSixDecimals | None = attr('TipoCambio', default=None)
    """
    Atributo condicional para representar el tipo de cambio conforme con la moneda usada. Es requerido cuando la
    clave de moneda es distinta de MXN y de XXX. El valor debe reflejar el número de pesos mexicanos que equivalen
    a una unidad de la divisa señalada en el atributo moneda. Si el valor está fuera del porcentaje aplicable a la
    moneda tomado del catálogo c_Moneda, el emisor debe obtener del PAC que vaya a timbrar el CFDI, de manera no
    automática, una clave de confirmación para ratificar que el valor es correcto e integrar dicha clave en el
    atributo Confirmacion.
    """

    total: fields.NonNegativeSixDecimals = attr('Total')
    """
    Atributo requerido para representar la suma del subtotal, menos los descuentos aplicables, más las contribuciones
    recibidas (impuestos trasladados - federales o locales, derechos, productos, aprovechamientos, aportaciones de
    seguridad social, contribuciones de mejoras) menos los impuestos retenidos. Si el valor es superior al límite que
    establezca el SAT en la Resolución Miscelánea Fiscal vigente, el emisor debe obtener del PAC que vaya a timbrar
    el CFDI, de manera no automática, una clave de confirmación para ratificar que el valor es correcto e integrar
    dicha clave en el atributo Confirmacion. No se permiten valores negativos.
    """

    tipo_de_comprobante: catalogos.TipoDeComprobante = attr('TipoDeComprobante')
    """
    Atributo requerido para expresar la clave del efecto del comprobante fiscal para el contribuyente emisor.
    """

    metodo_pago: catalogos.MetodoPago | None = attr('MetodoPago', default=None)
    """
    Atributo condicional para precisar la clave del método de pago que aplica para este comprobante fiscal digital
    por Internet, conforme al Artículo 29-A fracción VII incisos a y b del CFF
    """

    lugar_expedicion: str = attr('LugarExpedicion')
    """
    Atributo requerido para incorporar el código postal del lugar de expedición del comprobante (domicilio de la
    matriz o de la sucursal).
    """

    confirmacion: Annotated[
        str | None,
        StringConstraints(
            min_length=5,
            max_length=5,
            pattern=r'[0-9a-zA-Z]{5}',
        ),
    ] = attr('Confirmacion', default=None)
    """
    Atributo condicional para registrar la clave de confirmación que entregue el PAC para expedir el comprobante con
    importes grandes, con un tipo de cambio fuera del rango establecido o con ambos casos. Es requerido cuando se
    registra un tipo de cambio o un total fuera del rango establecido.
    """

    informacion_global: InformacionGlobal | None = None
    """
    Nodo condicional para precisar la información relacionada con el comprobante global.
    """

    cfdi_relacionados: CFDIRelacionados | None = None
    """
    Nodo opcional para precisar la información de los comprobantes relacionados.
    """

    emisor: Emisor
    """
    Nodo requerido para expresar la información del contribuyente emisor del comprobante.
    """

    receptor: Receptor
    """
    Nodo requerido para precisar la información del contribuyente receptor del comprobante
    """

    conceptos: list[Concepto] = wrapped('Conceptos')
    """
    Nodo requerido para listar los conceptos cubiertos por el comprobante.
    """

    impuestos: Impuestos | None = None
    """
    Nodo condicional para expresar el resumen de los impuestos aplicables.
    """

    complemento: Complemento | None = None
    """
    Nodo opcional donde se incluye el complemento Timbre Fiscal Digital de manera obligatoria y los nodos
    complementarios determinados por el SAT, de acuerdo con las disposiciones particulares para un sector o
    actividad específica.
    """

    addenda: dict[str, str] | None = element('Addenda', default=None)
    """
    Nodo opcional para recibir las extensiones al presente formato que sean de utilidad al contribuyente.
    Para las reglas de uso del mismo, referirse al formato origen.
    """

    exportacion: catalogos.Exportacion = attr('Exportacion')
    """
    Atributo requerido para expresar si el comprobante ampara una operación de exportación.
    """

    @property
    def verifica_cfdi_url(self) -> str | None:
        """
        id: is the UUID, tfd:TimbreFiscalDigital/@UUID
        re: is the RFC of the sender, cfdi:Emisor/@Rfc
        rr: is the RFC of the recipient, cfdi:Receptor/@Rfc
        tt: is the Total of the comprobante, cfdi:Comprobante/@Total (this is meant to have leading zeros removed, but we will stick with the example given).
        fe: is the last 8 characters in the Sello field, cfdi:Comprobante/@Sello
        """
        if not self.complemento or not self.complemento.timbre_fiscal_digital:
            return None
        params = {
            'id': self.complemento.timbre_fiscal_digital.uuid,
            're': self.emisor.rfc,
            'rr': self.receptor.rfc,
            'tt': self.total,
            'fe': self.sello[-8:],
        }
        return f'https://verificacfdi.facturaelectronica.sat.gob.mx?{urlencode(params)}'

    def save_pdf(
        self,
        filename: str | IO[bytes],
        /,
        *,
        logo: str | Path | IO[bytes] | None = None,
        logo_size: tuple[int, int] = (50, 50),
        logo_cords: tuple[int, int] | None = None,
    ) -> None:
        from cfdi.v40.pdf import generate_pdf

        return generate_pdf(
            self,
            filename,
            logo=logo,
            logo_size=logo_size,
            logo_cords=logo_cords,
        )
