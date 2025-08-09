from typing import BinaryIO, IO, Any, TypeAlias, TypeIs
import typing_extensions
from result import Result, Ok, Err, as_result

from io import (
    TextIOWrapper,
    FileIO,
    BufferedWriter,
    BufferedReader,
    BufferedRandom,
)
# NOTE: since result used typing_extensions means it still supports < 3.10 python < 3.12, i may try to support that too since only supporting >=3.12 kinda sucks
# ill find a way around type aliasing

ErrMsg: TypeAlias = str


def safe_open() -> Result[
    TextIOWrapper
    | FileIO
    | BufferedWriter
    | BufferedReader
    | BufferedRandom
    | BinaryIO
    | IO[Any],
    ErrMsg,
]: ...
