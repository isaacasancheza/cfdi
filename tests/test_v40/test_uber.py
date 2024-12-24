from decimal import Decimal
from pathlib import Path
from uuid import UUID

from dateutil import parser

from cfdi import parse_cfdi
from cfdi.v40 import CFDI40


def test_uber():
    cfdi = parse_cfdi(Path('tests/samples/v40/uber.xml'))
    assert isinstance(cfdi, CFDI40)
    assert cfdi.version == '4.0'

    # cfdi
    assert cfdi.serie == 'EATS'
    assert cfdi.folio == '2025003150001'
    assert cfdi.fecha == parser.parse('2024-03-01T01:42:00')
    assert cfdi.forma_pago == '27'
    assert cfdi.condiciones_de_pago == 'Pago en una sola exhibición'
    assert cfdi.sub_total == Decimal('131.72')
    assert cfdi.moneda == 'MXN'
    assert cfdi.total == Decimal('152.80')
    assert cfdi.tipo_de_comprobante == 'I'
    assert cfdi.metodo_pago == 'PUE'
    assert cfdi.lugar_expedicion == '11510'
    assert cfdi.exportacion == '01'
    assert cfdi.certificado == 'a1b2c3d4e5f67890123456789abcde1234567890abcdef'
    assert cfdi.no_certificado == '12345678901234567890'
    assert (
        cfdi.sello == 'GfY2Bsc6j2KnZkpB45g7I1nvdy9pTge5VdLX9QfhJHgV7u1Xs3BxlL4y5B3lW7Jz'
    )

    # emisor
    assert cfdi.emisor.rfc == 'XAXX010101000'
    assert cfdi.emisor.nombre == 'UBER PORTIER MEXICO'
    assert cfdi.emisor.regimen_fiscal == '601'

    # receptor
    assert cfdi.receptor.rfc == 'XAXX010101000'
    assert cfdi.receptor.nombre == 'HOMERO SANCHEZ'
    assert cfdi.receptor.domicilio_fiscal_receptor == '99999'
    assert cfdi.receptor.regimen_fiscal_receptor == '626'
    assert cfdi.receptor.uso_cfdi == 'G03'

    # concepto
    assert len(cfdi.conceptos) == 1
    assert cfdi.conceptos[0].clave_prod_serv == '80141706'
    assert cfdi.conceptos[0].cantidad == Decimal('1')
    assert cfdi.conceptos[0].clave_unidad == 'E48'
    assert cfdi.conceptos[0].unidad == 'Unidad de servicio'
    assert (
        cfdi.conceptos[0].descripcion
        == 'Tasa de Servicio uso de la plataforma Uber Eats 01/02/24 - 01/03/24 - Negocio'
    )
    assert cfdi.conceptos[0].valor_unitario == Decimal('131.72')
    assert cfdi.conceptos[0].importe == Decimal('131.72')
    assert cfdi.conceptos[0].objeto_imp == '02'

    assert cfdi.conceptos[0].impuestos
    assert cfdi.conceptos[0].impuestos.traslados[0].base == Decimal('131.72')
    assert cfdi.conceptos[0].impuestos.traslados[0].impuesto == '002'
    assert cfdi.conceptos[0].impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[0].impuestos.traslados[0].tasa_o_cuota == Decimal('0.160000')
    assert cfdi.conceptos[0].impuestos.traslados[0].importe == Decimal('21.08')

    # impuestos
    assert cfdi.impuestos
    assert cfdi.impuestos.total_impuestos_trasladados == Decimal('21.08')
    assert cfdi.impuestos.traslados[0].base == Decimal('131.72')
    assert cfdi.impuestos.traslados[0].impuesto == '002'
    assert cfdi.impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.impuestos.traslados[0].tasa_o_cuota == Decimal('0.160000')
    assert cfdi.impuestos.traslados[0].importe == Decimal('21.08')

    # complemento
    assert cfdi.complemento
    assert cfdi.complemento.timbre_fiscal_digital
    assert cfdi.complemento.timbre_fiscal_digital.version == '1.1'
    assert cfdi.complemento.timbre_fiscal_digital.sello_cfd == (
        'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7ZxhYsd5T+wmf9Ylj9wLhXxE12eEsYNnExnCBgj3+0fMGrdPLZk3M2m6dGqFlE5Wnsdq4FyD5h9u8Nw/0S5G6lIKjBMbXXsdR8v9f6mEbdc0LtQwETNE4m6lzRhyDd8IcazA7ruvdZODfN1rcsBHpIWj0FhgA3X+f4O09rbAmdmn1bsHqAhGFZmZZP4fRzj4FtmT2w8r4JloByLgU+/ZG4pl6iHZYvshqJl3nDpw2MEjiLeNEkeShbqHbL4kFk7uSP8RmPqF9lEjcS0UM0o1vPoxYwTrwJw9sJOMlxnU4Ffi1NnggECzUChUpgq1b2K7pGd3LDl8l3fZ4uDRcHVZy6YkmWVg9H6wA=='
    )
    assert cfdi.complemento.timbre_fiscal_digital.no_certificado_sat == (
        '20001000000300012345'
    )
    assert cfdi.complemento.timbre_fiscal_digital.rfc_prov_certif == 'AAA010101AAA'
    assert cfdi.complemento.timbre_fiscal_digital.uuid == UUID(
        'B5471F7B-1BB9-4928-A17F-D4C3A1A07E9D'
    )
    assert cfdi.complemento.timbre_fiscal_digital.fecha_timbrado == parser.parse(
        '2024-03-01T01:42:00'
    )
    assert cfdi.complemento.timbre_fiscal_digital.sello_sat == (
        'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7f72sdL5F9rDROdQ+IK2PscTjzToE35c6ZmD2OqH7M5FkT3kk9Y1zYH1yKddOtK/cKLr5dO//dXyD6TRyVEJrZnoCKbWQLy2bgAeWIqBQnPjXB2F5XJIpNqLr+Zk++xIX+4od9X8Gz8X9TLt4t08Jdl0tI8hpJ2p3D9chAkmq4s3sv1ts7zCmcNkOXtO5bTWWkINh+NB2gGi57PBsXMtx+kpIRdf5Fq6wTzjvNEPM0zG6Zm+pWnoUhncoNABg7YZgBjiw6cdNl0nqtSkLlQm9pCzD8E0vqJ6dtmQ71EOHXzLTm7fyjx2Qw3H9pVu8uYFA=='
    )
