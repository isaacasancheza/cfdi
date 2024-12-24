try:
    import reportlab as reportlab
except ModuleNotFoundError as e:
    raise RuntimeError(
        'The `pdf` module requires additional dependencies to be installed. You can install it with "uv add '
        'cfdi[pdf]".'
    ) from e


from decimal import Decimal
from io import BytesIO
from pathlib import Path
from typing import IO, TYPE_CHECKING, Literal, cast

import qrcode
import qrcode.constants
from boto3 import resource
from num2words import num2words
from reportlab.lib import colors, enums
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Image, Paragraph, Table, TableStyle

if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import Table as DynamodbTable

    from cfdi.v40 import CFDI40


table: 'None | DynamodbTable' = None
dynamodb = resource('dynamodb')


type Catalogo = Literal[
    'FORMA_PAGO',
    'MONEDA',
    'TIPO_DE_COMPROBANTE',
    'EXPORTACION',
    'METODO_PAGO',
    'CODIGO_POSTAL',
    'PERIODICIDAD',
    'MESES',
    'TIPO_RELACION',
    'REGIMEN_FISCAL',
    'PAIS',
    'USO_CFDI',
    'CLAVE_PROD_SERV',
    'CLAVE_UNIDAD',
    'OBJETO_IMP',
    'IMPUESTO',
    'TIPO_FACTOR',
    'ADUANA',
    'COLONIA',
    'ESTADO',
    'LOCALIDAD',
    'MUNICIPIO',
]


def get_description(
    value: str,
    catalogo: Catalogo,
    /,
) -> str:
    assert table is not None
    item = table.get_item(
        Key={
            'pk': catalogo,
            'sk': value,
        },
    ).get('Item')
    assert item
    return cast(str, item['name'])


def format_as_number(
    decimal: Decimal,
    /,
):
    return f'{decimal:.2f}'


def format_as_percentage(
    decimal: Decimal,
    /,
):
    return f'{decimal * 100:.2f}%'


def format_as_words(
    decimal: Decimal,
) -> str:
    pesos, centavos = divmod(decimal, 1)
    pesos_as_words = num2words(pesos, lang='es').upper()
    centavos = int(centavos * 100)
    resultado = f'{pesos_as_words} PESOS CON {centavos:02d}/100 MXN'
    return resultado


def generate_pdf(
    cfdi: 'CFDI40',
    filename: str | IO[bytes],
    /,
    *,
    logo: str | Path | IO[bytes] | None = None,
    logo_size: tuple[int, int] = (50, 50),
    logo_cords: tuple[int, int] | None = None,
) -> None:
    mx = 40
    my = 50
    width, height = letter
    gray_color = colors.HexColor(0x666666)

    pdf = Canvas(filename, pagesize=letter)

    # init offsets
    x_offset = width
    y_offset = height

    # logo
    if logo:
        logo_width, logo_height = logo_size
        if isinstance(logo, str):
            with open(logo, 'rb') as f:
                image = Image(f, logo_width, logo_height)
        else:
            image = Image(logo, logo_width, logo_height)

        logo_x_offset = 0
        logo_y_offset = height - logo_height
        if logo_cords:
            logo_x, logo_y = logo_cords
            logo_x_offset += logo_x
            logo_y_offset -= logo_y
        image.drawOn(pdf, logo_x_offset, logo_y_offset)

    # comprobante section
    font_size = 12
    x_offset -= mx
    y_offset -= my

    # folio
    pdf.setFont('Helvetica', font_size)
    pdf.drawRightString(
        x_offset,
        y_offset,
        f'Factura: {cfdi.serie}-{cfdi.folio}',
    )

    # fecha de expedicion
    py = 2
    font_size = 8
    y_offset -= py + font_size

    pdf.setFont('Helvetica', font_size)
    pdf.setFillColor(gray_color)
    pdf.drawRightString(
        x_offset,
        y_offset,
        f'Fecha de Expedición: {cfdi.fecha.strftime("%Y-%m-%dT%H:%M:%S")}',
    )

    # lugar de expedicion
    # y_offset -= py + font_size
    # pdf.drawRightString(
    #     x_offset,
    #     y_offset,
    #     f'Lugar de Expedición: {cfdi.lugar_expedicion}',  # TODO location name
    # )

    # tipo de comprobante
    y_offset -= py + font_size

    pdf.drawRightString(
        x_offset,
        y_offset,
        f'Tipo de Comprobante: {cfdi.tipo_de_comprobante} - {get_description(cfdi.tipo_de_comprobante, 'TIPO_DE_COMPROBANTE')}',
    )

    # separador
    y_offset -= py + font_size
    pdf.setLineWidth(0.5)
    pdf.line(
        mx,
        y_offset,
        width - mx,
        y_offset,
    )

    # emisor
    py = 12
    font_size = 8
    x_offset = mx
    y_offset -= py + font_size
    pdf.setFont('Helvetica-Bold', font_size)
    pdf.setFillColor(colors.black)
    pdf.drawString(
        x_offset,
        y_offset,
        'EMISOR',
    )

    # receptor
    x_offset = width / 2
    pdf.drawString(
        x_offset,
        y_offset,
        'RECEPTOR',
    )

    # nombre emisor
    py = 2
    font_size = 8
    x_offset = mx
    y_offset -= py + font_size
    pdf.setFont('Helvetica', font_size)
    pdf.setFillColor(gray_color)
    pdf.drawString(
        x_offset,
        y_offset,
        cfdi.emisor.nombre,
    )

    # nombre receptor
    x_offset = width / 2
    pdf.drawString(
        x_offset,
        y_offset,
        cfdi.receptor.nombre,
    )

    # rfc emisor
    x_offset = mx
    y_offset -= py + font_size
    pdf.drawString(
        x_offset,
        y_offset,
        f'RFC: {cfdi.emisor.rfc}',
    )

    # rfc receptor
    x_offset = width / 2
    pdf.drawString(
        x_offset,
        y_offset,
        f'RFC: {cfdi.receptor.rfc}',
    )

    # regimen emisor
    x_offset = mx
    y_offset -= py + font_size

    pdf.drawString(
        x_offset,
        y_offset,
        f'{cfdi.emisor.regimen_fiscal} - {get_description(cfdi.emisor.regimen_fiscal, 'REGIMEN_FISCAL')}',
    )

    # uso cfdi receptor
    x_offset = width / 2
    pdf.drawString(
        x_offset,
        y_offset,
        f'USO CFDI: {cfdi.receptor.uso_cfdi} - {get_description(cfdi.receptor.uso_cfdi, 'USO_CFDI')}',
    )

    # domicilio fiscal receptor
    y_offset -= py + font_size
    pdf.drawString(
        x_offset,
        y_offset,
        f'Domicilio Fiscal: {cfdi.receptor.domicilio_fiscal_receptor}',
    )

    # regimen fiscal receptor
    y_offset -= py + font_size
    pdf.drawString(
        x_offset,
        y_offset,
        f'Régimen fiscal: {cfdi.receptor.regimen_fiscal_receptor} - {get_description(cfdi.receptor.regimen_fiscal_receptor, 'REGIMEN_FISCAL')}',
    )

    # separador
    y_offset -= py + font_size
    pdf.setLineWidth(0.5)
    pdf.line(
        mx,
        y_offset,
        width - mx,
        y_offset,
    )

    # conceptos table
    concepts_table_width = width - mx * 2
    cantidad_column_width = concepts_table_width * 0.09
    unidad_column_width = concepts_table_width * 0.09
    descripcion_colun_width = concepts_table_width * 0.40
    v_unitario_column_width = concepts_table_width * 0.12
    impuestos_column_width = concepts_table_width * 0.18
    importe_column_width = concepts_table_width * 0.12

    concepts_table_colummns_width = [
        cantidad_column_width,
        unidad_column_width,
        descripcion_colun_width,
        v_unitario_column_width,
        impuestos_column_width,
        importe_column_width,
    ]

    font_size = 8
    concepts_table_headers_style = ParagraphStyle(
        'concepts_table_headers_style',
        fontName='Helvetica-Bold',
        fontSize=font_size,
        alignment=enums.TA_CENTER,
        textColor=colors.white,
    )

    concepts_table_body_style = ParagraphStyle(
        'concepts_table_body_style',
        fontName='Helvetica',
        fontSize=font_size,
        textColor=gray_color,
    )

    concepts_table_body_left_style = ParagraphStyle(
        'concepts_table_body_left_style',
        parent=concepts_table_body_style,
        alignment=enums.TA_LEFT,
    )

    concepts_table_body_center_style = ParagraphStyle(
        'concepts_table_body_center_style',
        parent=concepts_table_body_style,
        alignment=enums.TA_CENTER,
    )

    concepts_table_body_right_style = ParagraphStyle(
        'concepts_table_body_right_style',
        parent=concepts_table_body_style,
        alignment=enums.TA_RIGHT,
    )

    concepts_table_body_left_black_style = ParagraphStyle(
        'concepts_table_body_left_black_style',
        parent=concepts_table_body_left_style,
        textColor=colors.black,
    )

    concepts_table_headers = [
        Paragraph(
            'Cantidad',
            concepts_table_headers_style,
        ),
        Paragraph(
            'Unidad',
            concepts_table_headers_style,
        ),
        Paragraph(
            'Descripción',
            concepts_table_headers_style,
        ),
        Paragraph(
            'V. Unitario',
            concepts_table_headers_style,
        ),
        Paragraph(
            'Impuestos',
            concepts_table_headers_style,
        ),
        Paragraph(
            'Importe',
            concepts_table_headers_style,
        ),
    ]

    conceptos = []
    for concepto in cfdi.conceptos:
        # cantidad
        cantidad = Paragraph(
            str(concepto.cantidad),
            concepts_table_body_center_style,
        )

        # unidad
        unidad = Paragraph(
            f'{concepto.clave_unidad} - {get_description(concepto.clave_unidad, 'CLAVE_UNIDAD')}',
            concepts_table_body_center_style,
        )

        # descripcion
        descripcion = [
            Paragraph(
                f'{concepto.clave_prod_serv} - {get_description(concepto.clave_prod_serv, 'CLAVE_PROD_SERV')}'.upper(),
                concepts_table_body_left_black_style,
            ),
            Paragraph(
                concepto.descripcion,
                concepts_table_body_left_style,
            ),
        ]

        # valor unitario
        v_unitario = Paragraph(
            format_as_number(concepto.valor_unitario),
            concepts_table_body_right_style,
        )

        # impuestos
        assert concepto.impuestos is not None
        [traslado] = concepto.impuestos.traslados
        assert traslado.importe
        assert traslado.tasa_o_cuota
        tasa_o_cuota = traslado.tasa_o_cuota * 100

        impuestos = [
            Paragraph(
                f'{traslado.impuesto} - {get_description(traslado.impuesto, 'IMPUESTO')} {format_as_percentage(traslado.tasa_o_cuota)}%',
                concepts_table_body_right_style,
            ),
            Paragraph(
                format_as_number(traslado.importe),
                concepts_table_body_right_style,
            ),
        ]

        # importe
        importe = Paragraph(
            format_as_number(concepto.importe),
            concepts_table_body_right_style,
        )

        conceptos.append(
            [
                cantidad,
                unidad,
                descripcion,
                v_unitario,
                impuestos,
                importe,
            ],
        )

    # subtotal
    subtotal_header = Paragraph(
        'Subtotal',
        concepts_table_body_right_style,
    )

    subtotal = Paragraph(
        format_as_number(cfdi.sub_total),
        concepts_table_body_right_style,
    )

    # iva
    iva_header = Paragraph(
        'IVA',
        concepts_table_body_right_style,
    )

    assert cfdi.impuestos is not None
    iva = Paragraph(
        format_as_number(cfdi.impuestos.total_impuestos_trasladados),
        concepts_table_body_right_style,
    )

    # descuento
    descuento_header = Paragraph(
        'Descuento',
        concepts_table_body_right_style,
    )

    descuento = Paragraph(
        format_as_number(cfdi.descuento),
        concepts_table_body_right_style,
    )

    # total
    total_header = Paragraph(
        'Total',
        concepts_table_body_right_style,
    )

    total = Paragraph(
        format_as_number(cfdi.total),
        concepts_table_body_right_style,
    )

    # importe con letra
    importe_con_letra_header = Paragraph(
        'Importe con letra',
        concepts_table_headers_style,
    )

    importe_con_letra = Paragraph(
        format_as_words(cfdi.total),
        concepts_table_body_center_style,
    )

    # metodo de pago
    assert cfdi.metodo_pago
    metodo_de_pago = Paragraph(
        f'Método de Pago: {cfdi.metodo_pago} - {get_description(cfdi.metodo_pago, 'METODO_PAGO')}',
        concepts_table_body_center_style,
    )

    # forma de pago
    assert cfdi.forma_pago
    forma_de_pago = Paragraph(
        f'Forma de Pago: {cfdi.forma_pago} - {get_description(cfdi.forma_pago, 'FORMA_PAGO')}',
        concepts_table_body_center_style,
    )

    concepts_data = [
        concepts_table_headers,
        *conceptos,
        [importe_con_letra_header, '', '', '', subtotal_header, subtotal],
        [importe_con_letra, '', '', '', iva_header, iva],
        [metodo_de_pago, '', '', '', descuento_header, descuento],
        [forma_de_pago, '', '', '', total_header, total],
    ]

    concepts_table_style = TableStyle(
        [
            # header
            ('BACKGROUND', (0, 0), (-1, 0), colors.black),
            # importe con letra
            ('BACKGROUND', (0, 2), (3, 2), colors.black),
            # general
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor(0xC8C8C8)),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('LEFTPADDING', (0, 0), (-1, -1), 3),
            ('RIGHTPADDING', (0, 0), (-1, -1), 3),
            # colspan
            ('SPAN', (0, 2), (3, 2)),
            ('SPAN', (0, 3), (3, 3)),
            ('SPAN', (0, 4), (3, 4)),
            ('SPAN', (0, 5), (3, 5)),
        ]
    )

    concepts_table = Table(
        concepts_data,
        colWidths=concepts_table_colummns_width,
        style=concepts_table_style,
    )

    x_offset = mx
    y_offset -= font_size
    _, concepts_table_height = concepts_table.wrapOn(pdf, x_offset, y_offset)
    y_offset -= concepts_table_height

    concepts_table.drawOn(pdf, x_offset, y_offset)

    # traslados table
    traslados_table_width = (width - mx * 2) / 2
    traslados_table_columns_width = traslados_table_width / 4

    traslados_table_headers_style = ParagraphStyle(
        'traslados_table_headers_style',
        fontName='Helvetica-Bold',
        fontSize=font_size,
        alignment=enums.TA_CENTER,
        textColor=gray_color,
    )

    traslados_table_body_style = ParagraphStyle(
        'traslados_table_body_style',
        fontName='Helvetica',
        fontSize=font_size,
        textColor=gray_color,
        alignment=enums.TA_CENTER,
    )

    traslados_table_head = [
        Paragraph(
            'Traslados',
            traslados_table_headers_style,
        ),
        '',
        '',
        '',
    ]

    traslados_table_headers = [
        Paragraph(
            'Impuesto',
            traslados_table_headers_style,
        ),
        Paragraph(
            'Tipo Factor',
            traslados_table_headers_style,
        ),
        Paragraph(
            'Tasa o cuota',
            traslados_table_headers_style,
        ),
        Paragraph(
            'Importe',
            traslados_table_headers_style,
        ),
    ]

    traslados = []
    for traslado in cfdi.impuestos.traslados:
        # impuesto
        impuesto = Paragraph(
            traslado.impuesto,
            traslados_table_body_style,
        )

        # tipo factor
        tipo_factor = Paragraph(
            traslado.tipo_factor,
            traslados_table_body_style,
        )

        # tasa o cuota
        tasa_o_cuota = Paragraph(
            format_as_percentage(traslado.tasa_o_cuota),
            traslados_table_body_style,
        )

        # importe
        importe = Paragraph(
            format_as_number(traslado.importe),
            traslados_table_body_style,
        )

        traslados.append(
            [
                impuesto,
                tipo_factor,
                tasa_o_cuota,
                importe,
            ],
        )

    traslados_data = [
        traslados_table_head,
        traslados_table_headers,
        *traslados,
    ]

    traslados_table_style = TableStyle(
        [
            # head
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
            # colspan
            ('SPAN', (0, 0), (3, 0)),
        ]
    )

    traslados_table = Table(
        traslados_data,
        colWidths=traslados_table_columns_width,
        style=traslados_table_style,
    )

    _, traslados_table_height = traslados_table.wrapOn(pdf, x_offset, y_offset)

    py = 5
    y_offset -= py
    y_offset -= traslados_table_height
    traslados_table.drawOn(pdf, x_offset, y_offset)

    # qr
    py = 200
    y_offset = my + py
    x_offset = mx

    qr_width = 100
    qr_height = 100

    assert cfdi.verifica_cfdi_url
    with BytesIO() as buffer:
        qr = qrcode.QRCode(
            version=10,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(cfdi.verifica_cfdi_url)
        qr.make()

        m = qr.make_image()
        m.save(buffer, 'PNG')

        image = Image(buffer, qr_width, qr_height)
        image.drawOn(pdf, x_offset, y_offset)

    # qr text
    px = 10
    py = 15
    x_offset += qr_width + px
    y_offset += qr_height - py

    pdf.drawString(
        x_offset, y_offset, 'Este documento es una representación impresa de un CFDI'
    )

    y_offset -= font_size
    pdf.drawString(x_offset, y_offset, 'Efectos fiscales al pago')

    y_offset -= font_size
    pdf.drawString(x_offset, y_offset, f'Moneda: {cfdi.moneda}')

    # separador
    y_offset -= font_size
    pdf.setLineWidth(0.5)
    pdf.line(
        x_offset,
        y_offset,
        x_offset + (width / 2),
        y_offset,
    )

    # numero de certificado
    py = 8
    y_offset -= py + font_size
    pdf.drawString(x_offset, y_offset, f'Número de Certificado: {cfdi.no_certificado}')

    # folio fiscal
    y_offset -= font_size
    assert cfdi.complemento
    assert cfdi.complemento.timbre_fiscal_digital
    pdf.drawString(
        x_offset,
        y_offset,
        f'Folio Fiscal: {str(cfdi.complemento.timbre_fiscal_digital.uuid).upper()}',
    )

    # serie certificado sat
    y_offset -= font_size
    pdf.drawString(
        x_offset,
        y_offset,
        f'Serie Certificado SAT: {cfdi.complemento.timbre_fiscal_digital.no_certificado_sat}',
    )

    y_offset -= font_size
    pdf.drawString(
        x_offset,
        y_offset,
        f'RFC Proveedor de Certificación: {cfdi.complemento.timbre_fiscal_digital.rfc_prov_certif}',
    )

    py = 20
    y_offset -= py + font_size

    sellos_table_width = width - (mx * 2)
    sellos_table_headers_style = ParagraphStyle(
        'sellos_table_headers_style',
        fontName='Helvetica',
        fontSize=font_size,
        alignment=enums.TA_CENTER,
        textColor=colors.white,
    )

    sellos_table_body_style = ParagraphStyle(
        'sellos_table_body_style',
        fontName='Helvetica',
        fontSize=font_size,
        textColor=gray_color,
        alignment=enums.TA_CENTER,
    )

    # sello sat
    sello_sat_header = Paragraph(
        'Sello del SAT',
        sellos_table_headers_style,
    )
    sello_sat = Paragraph(
        cfdi.complemento.timbre_fiscal_digital.sello_sat,
        sellos_table_body_style,
    )

    # sello digital del cfdi
    sello_cfdi_header = Paragraph(
        'Sello digital del CFDI',
        sellos_table_headers_style,
    )
    sello_cfdi = Paragraph(
        cfdi.complemento.timbre_fiscal_digital.sello_cfd,
        sellos_table_body_style,
    )

    # cadena original del complemento de certificación digital del sat
    cadena_header = Paragraph(
        'Cadena original del complemento de certificación digital del SAT',
        sellos_table_headers_style,
    )
    cadena = Paragraph(
        cfdi.complemento.timbre_fiscal_digital.cadena_original,
        sellos_table_body_style,
    )

    sellos_table_data = (
        [sello_sat_header],
        [sello_sat],
        [sello_cfdi_header],
        [sello_cfdi],
        [cadena_header],
        [cadena],
    )

    sellos_table_style = TableStyle(
        [
            # headers
            ('BACKGROUND', (0, 0), (0, 0), colors.black),
            ('BACKGROUND', (0, 2), (0, 2), colors.black),
            ('BACKGROUND', (0, 4), (0, 4), colors.black),
            # general
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor(0xC8C8C8)),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('LEFTPADDING', (0, 0), (-1, -1), 40),
            ('RIGHTPADDING', (0, 0), (-1, -1), 40),
        ]
    )

    sellos_table = Table(
        sellos_table_data,
        colWidths=sellos_table_width,
        style=sellos_table_style,
    )

    _, sellos_table_height = sellos_table.wrapOn(pdf, x_offset, y_offset)
    x_offset = mx
    y_offset -= sellos_table_height
    sellos_table.drawOn(pdf, x_offset, y_offset)

    pdf.save()
