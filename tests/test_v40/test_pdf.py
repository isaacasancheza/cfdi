from pathlib import Path

from boto3 import resource

import cfdi.v40.pdf
from cfdi import parse_cfdi
from cfdi.v40 import CFDI40

dynamodb = resource('dynamodb')

cfdi.v40.pdf.table = dynamodb.Table('pruebas')


def test_uber():
    cfdi = parse_cfdi(Path('tests/samples/v40/uber.xml'))
    assert isinstance(cfdi, CFDI40)
    assert cfdi.version == '4.0'

    cfdi.save_pdf('cfdi.pdf')
