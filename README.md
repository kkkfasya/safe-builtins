# safe-builtins

Python's builtins wrapped inside rust-like [Result](https://github.com/montasaurus/result) type

> [!WARNING]
> This library doesn't depend on [original](https://github.com/rustedpy/result) python result library, instead it depends on the one maintained by [@montasaurus](https://github.com/montasaurus/result), as per this README is written, it's still labeled as experimental and unstable, so use this library at your own risk!
> This library is also in development, so expect breaking changes

## Installation

Install the package directly from the GitHub `main` branch using `uv`:

```bash
uv pip install git+https://github.com/kkkfasya/safe-builtins.git
```

## Summary

This library provides safe wrappers for Python's built-in functions using the `Result` type from the [montasaurus/result](https://github.com/montasaurus/result) library. Instead of raising exceptions, these functions return a `Result` that either contains the successful value (`Ok`) or the caught exception (`Err`).

This approach eliminates the need for extensive try/except blocks and makes error handling more explicit and functional in style.

## API

### Creating Safe Builtins

Each Python builtin function has a corresponding `safe_` prefixed version:

```python
from safe_builtins import safe_int, safe_open, safe_len

# Instead of raising ValueError, returns Err(ValueError(...))
result = safe_int("not a number")
# Returns Ok(42)
result = safe_int("42")

# Instead of raising FileNotFoundError, returns Err(FileNotFoundError(...))
result = safe_open("non_existent_file.txt")
# Returns Ok(file_object)
result = safe_open("existing_file.txt")

# Instead of raising TypeError, returns Err(TypeError(...))
result = safe_len(123)  # integers don't have length
# Returns Ok(3)
result = safe_len([1, 2, 3])
```

### Checking Results

You can check if a result is successful or contains an error:

```python
from safe_builtins import safe_int
from result import Ok, Err

result = safe_int("42")

# Using isinstance checks
if isinstance(result, Ok):
    value = result.unwrap()
    print(f"Got value: {value}")
elif isinstance(result, Err):
    error = result.unwrap_err()
    print(f"Got error: {error}")

# Using is_ok/is_err methods
if result.is_ok():
    value = result.unwrap()
    print(f"Got value: {value}")
elif result.is_err():
    error = result.unwrap_err()
    print(f"Got error: {error}")
```

### Accessing Values

```python
from safe_builtins import safe_int
from result import Ok

result = safe_int("42")

# Get the value or raise an exception if it's an error
value = result.unwrap()

# Get the value or a default if it's an error
value = result.unwrap_or(0)

# Get the value or compute a default if it's an error
value = result.unwrap_or_else(lambda err: 0)

# Convert to optional (None if error)
optional_value = result.ok()
```

### Chaining Operations

```python
from safe_builtins import safe_int, safe_open
from result import Ok

# Chain operations that might fail
result = (
    safe_int("42")
    .map(lambda x: x * 2)  # Only executed if the result is Ok
    .map_err(lambda err: f"Error processing number: {err}")  # Only executed if the result is Err
)

# Process file contents safely
result = (
    safe_open("data.txt")
    .map(lambda f: f.read())  # Read file contents
    .map(lambda contents: contents.splitlines())  # Split into lines
    .map(lambda lines: len(lines))  # Count lines
)
```

## Available Safe Builtins

The following Python builtins are available as safe versions:

- `safe_abs`
- `safe_aiter`
- `safe_all`
- `safe_any`
- `safe_anext`
- `safe_ascii`
- `safe_bin`
- `safe_breakpoint`
- `safe_bytearray`
- `safe_bytes`
- `safe_chr`
- `safe_compile`
- `safe_complex`
- `safe_delattr`
- `safe_dict`
- `safe_dir`
- `safe_divmod`
- `safe_enumerate`
- `safe_eval`
- `safe_exec`
- `safe_filter`
- `safe_float`
- `safe_format`
- `safe_frozenset`
- `safe_getattr`
- `safe_hash`
- `safe_hex`
- `safe_id`
- `safe_input`
- `safe_int`
- `safe_isinstance`
- `safe_issubclass`
- `safe_iter`
- `safe_len`
- `safe_list`
- `safe_map`
- `safe_max`
- `safe_memoryview`
- `safe_min`
- `safe_next`
- `safe_object`
- `safe_oct`
- `safe_open`
- `safe_ord`
- `safe_pow`
- `safe_range`
- `safe_reversed`
- `safe_round`
- `safe_set`
- `safe_setattr`
- `safe_slice`
- `safe_sorted`
- `safe_staticmethod`
- `safe_str`
- `safe_sum`
- `safe_super`
- `safe_tuple`
- `safe_type`
- `safe_vars`
- `safe_zip`
- `safe_import`
- `safe_bool`

## `as_result` Integration

Each safe builtin is created using the `@as_result()` decorator from the result library:

```python
from result import as_result

# This is how safe_int is implemented internally
safe_int = as_result(ValueError, TypeError)(int)
```

This means you can easily create your own safe versions of functions that might raise exceptions.

## Do notation

Chain multiple operations that might fail using the `do()` function:

```python
from result import do
from safe_builtins import safe_int, safe_open

@do
def process_data(filename: str, multiplier: str):
    # If any of these operations fail, the function will return Err
    f = yield safe_open(filename)
    contents = yield f.read()
    lines = yield contents.splitlines()
    mult = yield safe_int(multiplier)
    return len(lines) * mult
```

## FAQ

### How do I handle MyPy type narrowing?

Use isinstance checks to help MyPy narrow types:

```python
from safe_builtins import safe_int
from result import Ok

result = safe_int("42")
if isinstance(result, Ok):
    # MyPy knows result is Ok here
    value = result.unwrap()  # value is properly typed as int
```

## Related Projects

- [result](https://github.com/montasaurus/result) - The underlying Result type implementation
- [returns](https://github.com/dry-python/returns) - Another functional approach to error handling in Python

## License

MIT