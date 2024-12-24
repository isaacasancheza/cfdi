from pathlib import Path
from typing import overload

from lxml import etree

from cfdi.v40 import CFDI40


def get_cfdi_version(
    xml: bytes,
    /,
) -> str | None:
    # validate valid xml
    try:
        tree = etree.fromstring(xml)
    except etree.XMLSyntaxError:
        return None
    # validate contains namspaces
    namespaces = {key: value for key, value in tree.nsmap.items() if key}
    if not namespaces:
        return None
    # get cfdi
    search = tree.xpath('//cfdi:Comprobante', namespaces=namespaces)
    if not isinstance(search, list):
        return None
    if len(search) > 1:
        return None
    [cfdi] = search
    # make sure it's an element
    if not isinstance(cfdi, etree._Element):
        return None
    # check version
    version = cfdi.get('Version')
    if not version:
        return None
    return version


@overload
def parse_cfdi(
    xml: bytes,
    /,
) -> CFDI40 | None:
    pass


@overload
def parse_cfdi(
    xml: Path,
    /,
) -> CFDI40 | None:
    pass


def parse_cfdi(
    xml: bytes | Path,
    /,
) -> CFDI40 | None:
    # cast input
    match xml:
        case bytes():
            pass
        case Path():
            xml = xml.read_bytes()
        case _:
            raise TypeError(f'Invalid type: {type(xml)}')
    # check version
    version = get_cfdi_version(xml)
    match version:
        case '4.0':
            return CFDI40.from_xml(xml)
