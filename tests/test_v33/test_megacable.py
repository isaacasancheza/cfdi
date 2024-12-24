from decimal import Decimal
from pathlib import Path

from dateutil import parser

from cfdi import parse_cfdi


def test_megacable():
    cfdi = parse_cfdi(Path('tests/samples/v33/megacable.xml'))
    assert cfdi
    assert cfdi.version == '3.3'

    assert cfdi.lugar_expedicion == '06300'
    assert cfdi.tipo_de_comprobante == 'I'
    assert cfdi.metodo_pago == 'PUE'
    assert cfdi.total == Decimal('640.00')
    assert cfdi.moneda == 'MXN'
    assert cfdi.sub_total == Decimal('551.73')
    assert cfdi.certificado == 'a1b2c3d4e5f67890123456789abcde1234567890abcdef'
    assert cfdi.no_certificado == '12345678901234567890'
    assert cfdi.forma_pago == '04'
    assert (
        cfdi.sello == 'GfY2Bsc6j2KnZkpB45g7I1nvdy9pTge5VdLX9QfhJHgV7u1Xs3BxlL4y5B3lW7Jz'
    )
    assert cfdi.fecha == parser.parse('2016-06-14T13:45:49')
    assert cfdi.folio == '2025003150001'
    assert cfdi.serie == 'LO'

    assert cfdi.emisor.regimen_fiscal == '601'
    assert cfdi.emisor.nombre == 'TELEFONIA POR CABLE, S.A. DE C.V.'
    assert cfdi.emisor.rfc == 'XAXX010101000'

    assert cfdi.receptor.uso_cfdi == 'G03'
    assert cfdi.receptor.nombre == 'HOMERO SANCHEZ'
    assert cfdi.receptor.rfc == 'XAXX010101000'

    # 1
    assert cfdi.conceptos[0].clave_prod_serv == '01010101'
    assert cfdi.conceptos[0].clave_unidad == 'E48'
    assert cfdi.conceptos[0].descuento is None
    assert cfdi.conceptos[0].importe == Decimal('299.00')
    assert cfdi.conceptos[0].valor_unitario == 299.000000
    assert (
        cfdi.conceptos[0].descripcion
        == 'Internet Internet Resid. 50 Mbps Mensualidad Princ'
    )
    assert cfdi.conceptos[0].no_identificacion == '1'
    assert cfdi.conceptos[0].cantidad == Decimal('1')

    assert cfdi.conceptos[0].impuestos
    assert cfdi.conceptos[0].impuestos.traslados[0].importe == Decimal('47.84')
    assert cfdi.conceptos[0].impuestos.traslados[0].tasa_o_cuota == Decimal('0.160000')
    assert cfdi.conceptos[0].impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[0].impuestos.traslados[0].impuesto == '002'
    assert cfdi.conceptos[0].impuestos.traslados[0].base == Decimal('299.000000')

    # 2
    assert cfdi.conceptos[1].clave_prod_serv == '01010101'
    assert cfdi.conceptos[1].clave_unidad == 'E48'
    assert cfdi.conceptos[1].descuento is None
    assert cfdi.conceptos[1].importe == Decimal('45.83')
    assert cfdi.conceptos[1].valor_unitario == 45.830000
    assert (
        cfdi.conceptos[1].descripcion
        == 'Telefonia Telefonía Res Ilim Plus Mensualidad Princ'
    )
    assert cfdi.conceptos[1].no_identificacion == '1'
    assert cfdi.conceptos[1].cantidad == Decimal('1')

    assert cfdi.conceptos[1].impuestos
    assert cfdi.conceptos[1].impuestos.traslados[0].importe == Decimal('7.33')
    assert cfdi.conceptos[1].impuestos.traslados[0].tasa_o_cuota == Decimal('0.160000')
    assert cfdi.conceptos[1].impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[1].impuestos.traslados[0].impuesto == '002'
    assert cfdi.conceptos[1].impuestos.traslados[0].base == Decimal('45.830000')

    # 3
    assert cfdi.conceptos[2].clave_prod_serv == '01010101'
    assert cfdi.conceptos[2].clave_unidad == 'E48'
    assert cfdi.conceptos[2].descuento is None
    assert cfdi.conceptos[2].importe == Decimal('103.45')
    assert cfdi.conceptos[2].valor_unitario == 103.450000
    assert (
        cfdi.conceptos[2].descripcion
        == 'Telefonia Movil Plan 120 Plus Mensualidad Princ'
    )
    assert cfdi.conceptos[2].no_identificacion == '1'
    assert cfdi.conceptos[2].cantidad == Decimal('1')

    assert cfdi.conceptos[2].impuestos
    assert cfdi.conceptos[2].impuestos.traslados[0].importe == Decimal('16.55')
    assert cfdi.conceptos[2].impuestos.traslados[0].tasa_o_cuota == Decimal('0.160000')
    assert cfdi.conceptos[2].impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[2].impuestos.traslados[0].impuesto == '002'
    assert cfdi.conceptos[2].impuestos.traslados[0].base == Decimal('103.450000')

    # 4
    assert cfdi.conceptos[3].clave_prod_serv == '01010101'
    assert cfdi.conceptos[3].clave_unidad == 'E48'
    assert cfdi.conceptos[3].descuento is None
    assert cfdi.conceptos[3].importe == Decimal('103.45')
    assert cfdi.conceptos[3].valor_unitario == 103.450000
    assert (
        cfdi.conceptos[3].descripcion
        == 'Telefonia Movil Plan 120 Plus Mensualidad Adic'
    )
    assert cfdi.conceptos[3].no_identificacion == '1'
    assert cfdi.conceptos[3].cantidad == Decimal('1')

    assert cfdi.conceptos[3].impuestos
    assert cfdi.conceptos[3].impuestos.traslados[0].importe == Decimal('16.55')
    assert cfdi.conceptos[3].impuestos.traslados[0].tasa_o_cuota == Decimal('0.160000')
    assert cfdi.conceptos[3].impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[3].impuestos.traslados[0].impuesto == '002'
    assert cfdi.conceptos[3].impuestos.traslados[0].base == Decimal('103.450000')

    assert cfdi.impuestos
    assert cfdi.impuestos.total_impuestos_trasladados == Decimal('88.27')
    assert cfdi.impuestos.traslados[0].importe == Decimal('88.27')
    assert cfdi.impuestos.traslados[0].tasa_o_cuota == Decimal('0.160000')
    assert cfdi.impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.impuestos.traslados[0].impuesto == '002'
    assert cfdi.impuestos.traslados[0].base is None
