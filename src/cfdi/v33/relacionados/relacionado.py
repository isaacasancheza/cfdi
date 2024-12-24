from uuid import UUID

from pydantic_xml import attr

from cfdi.v33.base import BaseModel


class CFDIRelacionado(
    BaseModel,
    tag='CfdiRelacionado',
):
    """
    Schema of a "Cfdi Relacionado" of a CFDI v3.3.

    Based on: https://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd
    """

    uuid: UUID = attr('UUID')
    """
    Atributo requerido para registrar el folio fiscal (UUID) de un CFDI relacionado con el presente comprobante,
    por ejemplo: Si el CFDI relacionado es un comprobante de traslado que sirve para registrar el movimiento de la
    mercancía. Si este comprobante se usa como nota de crédito o nota de débito del comprobante relacionado.
    Si este comprobante es una devolución sobre el comprobante relacionado. Si éste sustituye a una factura
    cancelada.
    """
