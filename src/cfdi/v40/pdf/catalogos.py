from functools import cache
from json import loads


@cache
def get_catalog(
    catalogo_name: str,
    /,
) -> dict[str, str]:
    from cfdi import _PACKAGE_ROOT

    with open(
        _PACKAGE_ROOT / 'assets' / 'catalogos_json' / f'{catalogo_name}.json', 'r'
    ) as f:
        return loads(f.read())


def get_catalog_value(
    clave: str,
    catalogo_name: str,
    /,
) -> str:
    catalogo = get_catalog(catalogo_name)
    return catalogo[clave]


def get_aduana(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'aduana')


def get_clave_prod_serv(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'clave_prod_serv')


def get_clave_unidad(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'clave_unidad')


def get_clave_exportacion(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'clave_exportacion')


def get_forma_pago(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'forma_pago')


def get_impuesto(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'impuesto')


def get_meses(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'meses')


def get_metodo_pago(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'metodo_pago')


def get_moneda(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'moneda')


def get_objeto_imp(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'objeto_imp')


def get_pais(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'pais')


def get_peridiocidad(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'periodicidad')


def get_regimen_fiscal(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'regimen_fiscal')


def get_tipo_de_comprobante(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'tipo_de_comprobante')


def get_tipo_relacion(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'tipo_relacion')


def get_uso_cfdi(
    clave: str,
    /,
) -> str:
    return get_catalog_value(clave, 'uso_cfdi')
