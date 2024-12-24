import importlib

import pytest


@pytest.mark.parametrize(
    'module_name',
    [
        'cfdi.v40.catalogos.forma_pago',
        'cfdi.v40.catalogos.moneda',
        'cfdi.v40.catalogos.tipo_de_comprobante',
        'cfdi.v40.catalogos.exportacion',
        'cfdi.v40.catalogos.metodo_pago',
        'cfdi.v40.catalogos.periodicidad',
        'cfdi.v40.catalogos.meses',
        'cfdi.v40.catalogos.tipo_relacion',
        'cfdi.v40.catalogos.regimen_fiscal',
        'cfdi.v40.catalogos.pais',
        'cfdi.v40.catalogos.uso_cfdi',
        'cfdi.v40.catalogos.clave_unidad',
        'cfdi.v40.catalogos.objeto_imp',
        'cfdi.v40.catalogos.impuesto',
        'cfdi.v40.catalogos.aduana',
        'cfdi.v40.catalogos.tipo_factor',
    ],
)
def test_import_catalogos(
    module_name,
):
    """Verifica que los módulos de catálogo puedan importarse sin errores."""
    importlib.import_module(module_name)
