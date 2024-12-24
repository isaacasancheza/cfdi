from decimal import Decimal
from pathlib import Path
from uuid import UUID

from dateutil import parser

from cfdi import parse_cfdi
from cfdi.v40 import CFDI40


def test_base():
    cfdi = parse_cfdi(Path('tests/samples/v40/base.xml'))
    assert isinstance(cfdi, CFDI40)
    assert cfdi.version == '4.0'

    assert cfdi.lugar_expedicion == '99999'
    assert cfdi.metodo_pago == 'PPD'
    assert cfdi.confirmacion == 'A1234'
    assert cfdi.moneda == 'MXN'
    assert cfdi.descuento == Decimal('0.00')
    assert cfdi.folio == '123ABC'
    assert cfdi.tipo_cambio == Decimal('1.0')
    assert cfdi.serie == 'A'
    assert cfdi.exportacion == '03'
    assert cfdi.tipo_de_comprobante == 'P'
    assert cfdi.forma_pago == '99'
    assert cfdi.condiciones_de_pago == 'CONDICIONES'
    assert cfdi.fecha == parser.parse('2021-12-07T23:59:59')
    assert cfdi.sub_total == Decimal('1000')
    assert cfdi.total == Decimal('1500')
    assert cfdi.no_certificado == '30001000000300023708'
    assert cfdi.certificado == ''
    assert cfdi.sello == ''

    # informacion global
    assert cfdi.informacion_global
    assert cfdi.informacion_global.periodicidad == '05'
    assert cfdi.informacion_global.meses == '18'
    assert cfdi.informacion_global.año == 2021

    # cfdis relacionados
    assert cfdi.cfdi_relacionados
    assert cfdi.cfdi_relacionados.tipo_relacion == '02'
    assert cfdi.cfdi_relacionados.cfdi_relacionados
    assert cfdi.cfdi_relacionados.cfdi_relacionados[0].uuid == UUID(
        'ED1752FE-E865-4FF2-BFE1-0F552E770DC9'
    )

    # emisor
    assert cfdi.emisor.fac_atr_adquirente == '0123456789'
    assert cfdi.emisor.nombre == 'Esta es una demostración'
    assert cfdi.emisor.regimen_fiscal == '621'
    assert cfdi.emisor.rfc == 'AAA010101AAA'

    # receptor
    assert cfdi.receptor.residencia_fiscal == 'MEX'
    assert cfdi.receptor.domicilio_fiscal_receptor == '99999'
    assert cfdi.receptor.regimen_fiscal_receptor == '621'
    assert cfdi.receptor.nombre == 'Juanito Bananas De la Sierra'
    assert cfdi.receptor.num_reg_id_trib == '0000000000000'
    assert cfdi.receptor.rfc == 'BASJ600902KL9'
    assert cfdi.receptor.uso_cfdi == 'S01'

    # conceptos
    assert len(cfdi.conceptos) == 3  # We have 3 concepts in the XML

    # Concepto 1
    assert cfdi.conceptos[0].objeto_imp == '01'
    assert cfdi.conceptos[0].clave_prod_serv == '01010101'
    assert cfdi.conceptos[0].clave_unidad == 'C81'
    assert cfdi.conceptos[0].no_identificacion == '00001'
    assert cfdi.conceptos[0].cantidad == Decimal('1.5')
    assert cfdi.conceptos[0].unidad == 'TONELADA'
    assert cfdi.conceptos[0].descripcion == 'ACERO'
    assert cfdi.conceptos[0].valor_unitario == Decimal('1500000')
    assert cfdi.conceptos[0].importe == Decimal('2250000')
    assert cfdi.conceptos[0].impuestos

    assert len(cfdi.conceptos[0].impuestos.traslados) == 1
    assert cfdi.conceptos[0].impuestos.traslados[0].base == Decimal('2250000')
    assert cfdi.conceptos[0].impuestos.traslados[0].impuesto == '002'
    assert cfdi.conceptos[0].impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[0].impuestos.traslados[0].tasa_o_cuota == Decimal('1.600000')
    assert cfdi.conceptos[0].impuestos.traslados[0].importe == Decimal('360000')

    assert len(cfdi.conceptos[0].impuestos.retenciones) == 1
    assert cfdi.conceptos[0].impuestos.retenciones[0].base == Decimal('2250000')
    assert cfdi.conceptos[0].impuestos.retenciones[0].impuesto == '001'
    assert cfdi.conceptos[0].impuestos.retenciones[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[0].impuestos.retenciones[0].tasa_o_cuota == Decimal(
        '0.300000'
    )
    assert cfdi.conceptos[0].impuestos.retenciones[0].importe == Decimal('247500')

    assert len(cfdi.conceptos[0].cuenta_predial) == 1
    assert cfdi.conceptos[0].cuenta_predial[0].numero == '51888'

    # Concepto 2
    assert cfdi.conceptos[1].objeto_imp == '02'
    assert cfdi.conceptos[1].clave_prod_serv == '95141904'
    assert cfdi.conceptos[1].clave_unidad == 'WEE'
    assert cfdi.conceptos[1].no_identificacion == '00002'
    assert cfdi.conceptos[1].cantidad == Decimal('1.6')
    assert cfdi.conceptos[1].unidad == 'TONELADA'
    assert cfdi.conceptos[1].descripcion == 'ALUMINIO'
    assert cfdi.conceptos[1].valor_unitario == Decimal('1500')
    assert cfdi.conceptos[1].importe == Decimal('2400')

    assert cfdi.conceptos[1].impuestos

    assert len(cfdi.conceptos[1].impuestos.traslados) == 1
    assert cfdi.conceptos[1].impuestos.traslados[0].base == Decimal('2400')
    assert cfdi.conceptos[1].impuestos.traslados[0].impuesto == '002'
    assert cfdi.conceptos[1].impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[1].impuestos.traslados[0].tasa_o_cuota == Decimal('1.600000')
    assert cfdi.conceptos[1].impuestos.traslados[0].importe == Decimal('384')

    assert len(cfdi.conceptos[1].impuestos.retenciones) == 1
    assert cfdi.conceptos[1].impuestos.retenciones[0].base == Decimal('2400')
    assert cfdi.conceptos[1].impuestos.retenciones[0].impuesto == '001'
    assert cfdi.conceptos[1].impuestos.retenciones[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[1].impuestos.retenciones[0].tasa_o_cuota == Decimal(
        '0.300000'
    )
    assert cfdi.conceptos[1].impuestos.retenciones[0].importe == Decimal('264')

    assert len(cfdi.conceptos[1].a_cuenta_terceros) == 1
    assert (
        cfdi.conceptos[1].a_cuenta_terceros[0].regimen_fiscal_a_cuenta_terceros == '621'
    )
    assert (
        cfdi.conceptos[1].a_cuenta_terceros[0].nombre_a_cuenta_terceros
        == 'NombreACuentaTerceros'
    )
    assert (
        cfdi.conceptos[1].a_cuenta_terceros[0].domicilio_fiscal_a_cuenta_terceros
        == '99999'
    )
    assert (
        cfdi.conceptos[1].a_cuenta_terceros[0].rfc_a_cuenta_terceros == 'AAA010101AAA'
    )

    assert len(cfdi.conceptos[1].informacion_aduanera) == 1
    assert (
        cfdi.conceptos[1].informacion_aduanera[0].numero_pedimento
        == '15  48  4567  6001234'
    )

    # Concepto 3
    assert cfdi.conceptos[2].objeto_imp == '03'
    assert cfdi.conceptos[2].clave_prod_serv == '84101604'
    assert cfdi.conceptos[2].clave_unidad == 'G66'
    assert cfdi.conceptos[2].no_identificacion == '00003'
    assert cfdi.conceptos[2].cantidad == Decimal('1.7')
    assert cfdi.conceptos[2].unidad == 'TONELADA'
    assert cfdi.conceptos[2].descripcion == 'ZAMAC'
    assert cfdi.conceptos[2].valor_unitario == Decimal('10000')
    assert cfdi.conceptos[2].importe == Decimal('17000')
    assert cfdi.conceptos[2].descuento == Decimal('0')

    assert cfdi.conceptos[2].impuestos

    assert len(cfdi.conceptos[2].impuestos.traslados) == 1
    assert cfdi.conceptos[2].impuestos.traslados[0].base == Decimal('17000')
    assert cfdi.conceptos[2].impuestos.traslados[0].impuesto == '002'
    assert cfdi.conceptos[2].impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[2].impuestos.traslados[0].tasa_o_cuota == Decimal('1.600000')
    assert cfdi.conceptos[2].impuestos.traslados[0].importe == Decimal('2720')

    assert len(cfdi.conceptos[2].impuestos.retenciones) == 1
    assert cfdi.conceptos[2].impuestos.retenciones[0].base == Decimal('17000')
    assert cfdi.conceptos[2].impuestos.retenciones[0].impuesto == '001'
    assert cfdi.conceptos[2].impuestos.retenciones[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[2].impuestos.retenciones[0].tasa_o_cuota == Decimal(
        '0.300000'
    )
    assert cfdi.conceptos[2].impuestos.retenciones[0].importe == Decimal('1870')

    assert len(cfdi.conceptos[2].parte) == 1
    assert cfdi.conceptos[2].parte[0].clave_prod_serv == '25201513'
    assert cfdi.conceptos[2].parte[0].no_identificacion == '055155'
    assert cfdi.conceptos[2].parte[0].cantidad == Decimal('1.0')
    assert cfdi.conceptos[2].parte[0].descripcion == 'PARTE EJEMPLO'
    assert cfdi.conceptos[2].parte[0].unidad == 'UNIDAD'
    assert cfdi.conceptos[2].parte[0].valor_unitario == Decimal('1.00')
    assert cfdi.conceptos[2].parte[0].importe == Decimal('1.00')

    assert len(cfdi.conceptos[2].parte[0].informacion_aduanera) == 1
    assert (
        cfdi.conceptos[2].parte[0].informacion_aduanera[0].numero_pedimento
        == '15  48  4567  6001235'
    )

    # impuestos
    assert cfdi.impuestos
    assert cfdi.impuestos.total_impuestos_retenidos == Decimal('247500')
    assert cfdi.impuestos.total_impuestos_trasladados == Decimal('360000')

    # retenciones
    assert len(cfdi.impuestos.retenciones) == 2
    assert cfdi.impuestos.retenciones[0].impuesto == '001'
    assert cfdi.impuestos.retenciones[0].importe == Decimal('247000')
    assert cfdi.impuestos.retenciones[1].impuesto == '003'
    assert cfdi.impuestos.retenciones[1].importe == Decimal('500')

    # traslados
    assert len(cfdi.impuestos.traslados) == 1
    assert cfdi.impuestos.traslados[0].base == Decimal('1.00')
    assert cfdi.impuestos.traslados[0].impuesto == '002'
    assert cfdi.impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.impuestos.traslados[0].tasa_o_cuota == Decimal('1.600000')
    assert cfdi.impuestos.traslados[0].importe == Decimal('360000')
