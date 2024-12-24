from decimal import Decimal
from typing import Annotated

from pydantic import Field, StringConstraints

from cfdi import patterns

type RFC = Annotated[
    str,
    StringConstraints(
        pattern=patterns.RFC_PATTERN,
        strip_whitespace=True,
    ),
]

type CURP = Annotated[
    str,
    StringConstraints(
        pattern=patterns.CURP_PATTERN,
        strip_whitespace=True,
    ),
]

type NonNegativeSixDecimals = Annotated[
    Decimal,
    Field(
        ge=Decimal(0),
        decimal_places=6,
    ),
]

type PositiveSixDecimals = Annotated[
    Decimal,
    Field(
        ge=Decimal(0.000001),
        decimal_places=6,
    ),
]
