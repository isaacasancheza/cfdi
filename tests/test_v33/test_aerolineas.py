from decimal import Decimal
from pathlib import Path

from dateutil import parser

from cfdi import parse_cfdi


def test_aerolineas():
    cfdi = parse_cfdi(Path('tests/samples/v33/aerolineas.xml'))
    assert cfdi
    assert cfdi.version == '3.3'

    assert cfdi.lugar_expedicion == '06300'
    assert cfdi.tipo_de_comprobante == 'I'
    assert cfdi.metodo_pago == 'PUE'
    assert cfdi.total == Decimal('94.40')
    assert cfdi.moneda == 'MXN'
    assert cfdi.descuento == Decimal('9.99')
    assert cfdi.sub_total == Decimal('89.99')
    assert cfdi.condiciones_de_pago == 'Condiciones de pago'
    assert (
        cfdi.certificado
        == 'MIIFxTCCA62gAwIBAgIUMjAwMDEwMDAwMDAzMDAwMjI4MTUwDQYJKoZIhvcNAQELBQAwggFmMSAwHgYDVQQDDBdBLkMuIDIgZGUgcHJ1ZWJhcyg0MDk2KTEvMC0GA1UECgwmU2VydmljaW8gZGUgQWRtaW5pc3RyYWNpw7NuIFRyaWJ1dGFyaWExODA2BgNVBAsML0FkbWluaXN0cmFjacOzbiBkZSBTZWd1cmlkYWQgZGUgbGEgSW5mb3JtYWNpw7NuMSkwJwYJKoZIhvcNAQkBFhphc2lzbmV0QHBydWViYXMuc2F0LmdvYi5teDEmMCQGA1UECQwdQXYuIEhpZGFsZ28gNzcsIENvbC4gR3VlcnJlcm8xDjAMBgNVBBEMBTA2MzAwMQswCQYDVQQGEwJNWDEZMBcGA1UECAwQRGlzdHJpdG8gRmVkZXJhbDESMBAGA1UEBwwJQ295b2Fjw6FuMRUwEwYDVQQtEwxTQVQ5NzA3MDFOTjMxITAfBgkqhkiG9w0BCQIMElJlc3BvbnNhYmxlOiBBQ0RNQTAeFw0xNjEwMjUyMTUyMTFaFw0yMDEwMjUyMTUyMTFaMIGxMRowGAYDVQQDExFDSU5ERU1FWCBTQSBERSBDVjEaMBgGA1UEKRMRQ0lOREVNRVggU0EgREUgQ1YxGjAYBgNVBAoTEUNJTkRFTUVYIFNBIERFIENWMSUwIwYDVQQtExxMQU43MDA4MTczUjUgLyBGVUFCNzcwMTE3QlhBMR4wHAYDVQQFExUgLyBGVUFCNzcwMTE3TURGUk5OMDkxFDASBgNVBAsUC1BydWViYV9DRkRJMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgvvCiCFDFVaYX7xdVRhp/38ULWto/LKDSZy1yrXKpaqFXqERJWF78YHKf3N5GBoXgzwFPuDX+5kvY5wtYNxx/Owu2shNZqFFh6EKsysQMeP5rz6kE1gFYenaPEUP9zj+h0bL3xR5aqoTsqGF24mKBLoiaK44pXBzGzgsxZishVJVM6XbzNJVonEUNbI25DhgWAd86f2aU3BmOH2K1RZx41dtTT56UsszJls4tPFODr/caWuZEuUvLp1M3nj7Dyu88mhD2f+1fA/g7kzcU/1tcpFXF/rIy93APvkU72jwvkrnprzs+SnG81+/F16ahuGsb2EZ88dKHwqxEkwzhMyTbQIDAQABox0wGzAMBgNVHRMBAf8EAjAAMAsGA1UdDwQEAwIGwDANBgkqhkiG9w0BAQsFAAOCAgEAJ/xkL8I+fpilZP+9aO8n93+20XxVomLJjeSL+Ng2ErL2GgatpLuN5JknFBkZAhxVIgMaTS23zzk1RLtRaYvH83lBH5E+M+kEjFGp14Fne1iV2Pm3vL4jeLmzHgY1Kf5HmeVrrp4PU7WQg16VpyHaJ/eonPNiEBUjcyQ1iFfkzJmnSJvDGtfQK2TiEolDJApYv0OWdm4is9Bsfi9j6lI9/T6MNZ+/LM2L/t72Vau4r7m94JDEzaO3A0wHAtQ97fjBfBiO5M8AEISAV7eZidIl3iaJJHkQbBYiiW2gikreUZKPUX0HmlnIqqQcBJhWKRu6Nqk6aZBTETLLpGrvF9OArV1JSsbdw/ZH+P88RAt5em5/gjwwtFlNHyiKG5w+UFpaZOK3gZP0su0sa6dlPeQ9EL4JlFkGqQCgSQ+NOsXqaOavgoP5VLykLwuGnwIUnuhBTVeDbzpgrg9LuF5dYp/zs+Y9ScJqe5VMAagLSYTShNtN8luV7LvxF9pgWwZdcM7lUwqJmUddCiZqdngg3vzTactMToG16gZA4CWnMgbU4E+r541+FNMpgAZNvs2CiW/eApfaaQojsZEAHDsDv4L5n3M1CC7fYjE/d61aSng1LaO6T1mh+dEfPvLzp7zyzz+UgWMhi5Cs4pcXx1eic5r7uxPoBwcCTt3YI1jKVVnV7/w='
    )
    assert cfdi.no_certificado == '20001000000300022815'
    assert cfdi.forma_pago == '01'
    assert (
        cfdi.sello
        == 'Eq1UwwnoQ+W/M8M6oEqVfq4GwMo0Aa3KxnIc35G6IP2yzwzCuouU9fhVdFyrjz581eSxUMZMdFyn4ujUrkltXKP/yD5EQq4WH/8Ol2AQeqtgOoLKttNW3bUzDmiPxcu1mNJX5n+TctYn33ecpBVI4m4X0zfXEClwsc4jX2S6DVs1PNUSpgjzxDyVJvEFUGNvqwfd1OhWkGKh/yS9MjZAjV5itLOQaNCvcGt56kEYYXIImsOvfAxTCALev/scaVq4v3Gb0/R2kiZsXNuedHuXhLr80GzQ1zygzWK0WjNmq4ozfpp2uJTls9bRqIBJrU3qh1hKirVxtu0eIKiX6o28yg=='
    )
    assert cfdi.fecha == parser.parse('2017-07-14T13:45:49')
    assert cfdi.folio == '12358'
    assert cfdi.serie == 'LO'

    assert cfdi.emisor.regimen_fiscal == '601'
    assert cfdi.emisor.nombre == 'CINDEMEX SA DE CV'
    assert cfdi.emisor.rfc == 'LAN7008173R5'

    assert cfdi.receptor.uso_cfdi == 'G01'
    assert cfdi.receptor.nombre == 'Público en General'
    assert cfdi.receptor.rfc == 'XAXX010101000'

    assert cfdi.conceptos[0].clave_prod_serv == '01010101'
    assert cfdi.conceptos[0].clave_unidad == 'H87'
    assert cfdi.conceptos[0].descuento == Decimal('9.99')
    assert cfdi.conceptos[0].importe == Decimal('89.99')
    assert cfdi.conceptos[0].valor_unitario == 89.99
    assert cfdi.conceptos[0].descripcion == 'Servicio'
    assert cfdi.conceptos[0].no_identificacion == '1'
    assert cfdi.conceptos[0].cantidad == Decimal('1')

    assert cfdi.conceptos[0].impuestos
    assert cfdi.conceptos[0].impuestos.traslados[0].importe == Decimal('14.40')
    assert cfdi.conceptos[0].impuestos.traslados[0].tasa_o_cuota == Decimal('0.160000')
    assert cfdi.conceptos[0].impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.conceptos[0].impuestos.traslados[0].impuesto == '002'
    assert cfdi.conceptos[0].impuestos.traslados[0].base == Decimal('90.00')

    assert cfdi.impuestos
    assert cfdi.impuestos.traslados[0].importe == Decimal('14.40')
    assert cfdi.impuestos.traslados[0].tasa_o_cuota == Decimal('0.160000')
    assert cfdi.impuestos.traslados[0].tipo_factor == 'Tasa'
    assert cfdi.impuestos.traslados[0].impuesto == '002'
    assert cfdi.impuestos.traslados[0].base == Decimal('90.00')
