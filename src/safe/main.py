from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    BinaryIO,
    IO,
    Any,
    Sized,
    TypeAlias,
    Callable,
    Literal,
)

# TODO: get types from _typeshed
if TYPE_CHECKING:
    from _typeshed import (
        FileDescriptorOrPath,
        OpenBinaryModeReading,
        OpenTextMode,
        OpenBinaryMode,
        OpenBinaryModeWriting,
        OpenBinaryModeUpdating,
    )

from result import (
    Result,
    Ok,
    Err,
    is_err,
    is_ok
)

from io import (
    TextIOWrapper,
    FileIO,
    BufferedWriter,
    BufferedReader,
    BufferedRandom,
)

ErrMsg: TypeAlias = str
_Opener: TypeAlias = Callable[[str, int], int]


def safe_open(
    file: FileDescriptorOrPath,
    mode: OpenTextMode
    | OpenBinaryMode
    | OpenBinaryModeReading
    | OpenBinaryModeWriting
    | OpenBinaryModeUpdating
    | str,
    buffering: Literal[-1, 1] = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,
    opener: _Opener | None = None,
) -> Result[
    TextIOWrapper
    | FileIO
    | BufferedWriter
    | BufferedReader
    | BufferedRandom
    | BinaryIO
    | IO[Any],
    FileNotFoundError
    | IsADirectoryError
    | NotADirectoryError
    | PermissionError
    | FileExistsError
    | OSError
    | ValueError
    | TypeError,
]:
    try:
        return Ok(
            open(
                file,
                mode,
                buffering,
                encoding,
                errors,
                newline,
                closefd,
                opener,
            )
        )

    except (
        FileNotFoundError,
        IsADirectoryError,
        NotADirectoryError,
        PermissionError,
        FileExistsError,
        OSError,
        ValueError,
        TypeError,
    ) as e:
        return Err(e)


def safe_len(obj: Sized, /) -> Result[int, OverflowError]:
    try:
        r = len(obj)
        return Ok(r)

    except OverflowError as e:
        return Err(e)


def test_safe_open():
    # BUG: why pyright flag this as error?
    return safe_open("nonexistent_file", "r").err_value


# TODO:create something like this, modify the result library
def test_safe_open_2():
    match safe_open("nonexistent_file", "r"):
        case Err(e).match_err(FileNotFoundError):
            # handle err

print(test_safe_open())
