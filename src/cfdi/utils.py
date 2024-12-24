from pathlib import Path
from typing import overload

from lxml import etree

from cfdi.v33 import CFDI33
from cfdi.v40 import CFDI40


def get_cfdi_version(
    xml: bytes,
    /,
) -> str | None:
    """
    Get the CFDI version from the XML.

    Args:
        xml (bytes): The XML to get the CFDI version from.

    Returns:
        str | None: The CFDI version or None if not found.
    """
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
) -> CFDI33 | CFDI40 | None:
    pass


@overload
def parse_cfdi(
    xml: Path,
    /,
) -> CFDI33 | CFDI40 | None:
    pass


def parse_cfdi(
    xml: bytes | Path,
    /,
) -> CFDI33 | CFDI40 | None:
    """
    Parse the CFDI from the XML.

    Args:
        xml (bytes | Path): The XML to parse.

    Returns:
        CFDI33 | CFDI40 | None: The CFDI or None if not found.
    """
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
        case '3.3':
            return CFDI33.from_xml(xml)
        case '4.0':
            return CFDI40.from_xml(xml)
