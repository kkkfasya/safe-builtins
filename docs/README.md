# Safe Built-ins

This module provides safe wrappers around Python's built-in functions. Each wrapper returns a `Result[T, E]` where `T` is the return type of the original function and `E` is the possible error type(s) that the function can raise.

For error/value matching, if Result library that this package depends is from https://github.com/kkkfasya/result, you can do this below:  
```py
o = safe_dict(a=1, b=2)
if o.match_value({"a": 1, "b": 2}): ...

e = safe_dict({1, 2, 3})
if e.match_err(TypeError): ...
```
if you were to used the ones that is from PyPi, you cant do the above, but you still can use this library.  
To check where Result is from, read your uv.lock file

## Functions

### `safe_abs(value: SupportsAbs[T]) -> Result[T, Union[ValueError, TypeError]]`

A safe version of the built-in `abs()` function. Returns the absolute value of a number.

### `safe_aiter(async_iterable) -> Result[async_iterator, TypeError]`

A safe version of the built-in `aiter()` function. Returns an async iterator for an async iterable.

### `safe_all(iterable) -> Result[bool, TypeError]`

A safe version of the built-in `all()` function. Returns `True` if all elements of the iterable are true (or if the iterable is empty).

### `safe_any(iterable) -> Result[bool, TypeError]`

A safe version of the built-in `any()` function. Returns `True` if any element of the iterable is true. If the iterable is empty, returns `False`.

### `safe_anext(async_iterator) -> Result[next_item, Union[TypeError, StopAsyncIteration]]`

A safe version of the built-in `anext()` function. Retrieves the next item from an async iterator.

### `safe_ascii(obj) -> Result[str, TypeError]`

A safe version of the built-in `ascii()` function. Returns a string containing a printable representation of an object.

### `safe_bin(number) -> Result[str, TypeError]`

A safe version of the built-in `bin()` function. Converts an integer number to a binary string prefixed with "0b".

### `safe_breakpoint() -> Result[None, RuntimeError]`

A safe version of the built-in `breakpoint()` function. Drops into the debugger at the call site.

### `safe_bytearray(source) -> Result[bytearray, Union[TypeError, ValueError]]`

A safe version of the built-in `bytearray()` function. Returns a new array of bytes.

### `safe_bytes(source) -> Result[bytes, Union[TypeError, ValueError]]`

A safe version of the built-in `bytes()` function. Returns a new bytes object.

### `safe_chr(i) -> Result[str, Union[TypeError, ValueError]]`

A safe version of the built-in `chr()` function. Returns the string representing a character whose Unicode code point is the integer `i`.

### `safe_compile(source, filename, mode) -> Result[ast_object, Union[SyntaxError,ValueError, TypeError]]`

A safe version of the built-in `compile()` function. Compiles the source into a code or AST object.

### `safe_complex(real, imag) -> Result[complex, Union[TypeError, ValueError]]`

A safe version of the built-in `complex()` function. Returns a complex number with the value real + imag*1j.

### `safe_delattr(obj, name) -> Result[None, Union[TypeError, AttributeError]]`

A safe version of the built-in `delattr()` function. Deletes the named attribute from the object.

### `safe_dict(mapping) -> Result[dict, Union[TypeError, ValueError]]`

A safe version of the built-in `dict()` function. Creates a new dictionary.

### `safe_dir(obj) -> Result[list, TypeError]`

A safe version of the built-in `dir()` function. Without arguments, returns the list of names in the current local scope. With an argument, returns the list of valid attributes for that object.

### `safe_divmod(a, b) -> Result[tuple, Union[TypeError, ZeroDivisionError]]`

A safe version of the built-in `divmod()` function. Takes two non-complex numbers and returns a pair of numbers consisting of their quotient and remainder.

### `safe_enumerate(iterable) -> Result[enumerate_object, TypeError]`

A safe version of the built-in `enumerate()` function. Returns an enumerate object.

### `safe_eval(expression) -> Result[result, Union[NameError, TypeError]]`

A safe version of the built-in `eval()` function. Parses and evaluates a Python expression.

### `safe_exec(object) -> Result[None, Union[TypeError]]`

A safe version of the built-in `exec()` function. Executes Python code dynamically.

### `safe_filter(function, iterable) -> Result[filter_object, TypeError]`

A safe version of the built-in `filter()` function. Constructs an iterator from elements of iterable for which function returns true.

### `safe_float(value) -> Result[float, Union[TypeError, ValueError]]`

A safe version of the built-in `float()` function. Returns a floating point number constructed from a number or string.

### `safe_format(value, format_spec) -> Result[str, Union[TypeError, ValueError]]`

A safe version of the built-in `format()` function. Converts a value to a formatted representation.

### `safe_frozenset(iterable) -> Result[frozenset, TypeError]`

A safe version of the built-in `frozenset()` function. Returns a new frozenset object, optionally with elements taken from iterable.

### `safe_getattr(obj, name) -> Result[value, Union[TypeError, AttributeError]]`

A safe version of the built-in `getattr()` function. Returns the value of the named attribute of object.

### `safe_hash(obj) -> Result[int, TypeError]`

A safe version of the built-in `hash()` function. Returns the hash value of the object.

### `safe_hex(number) -> Result[str, TypeError]`

A safe version of the built-in `hex()` function. Converts an integer number to a lowercase hexadecimal string prefixed with "0x".

### `safe_id(obj) -> Result[int, TypeError]`

A safe version of the built-in `id()` function. Returns the identity of an object.

### `safe_input(prompt) -> Result[str, Union[EOFError, KeyboardInterrupt, TypeError]]`

A safe version of the built-in `input()` function. Reads a line from input, converts it to a string (stripping a trailing newline), and returns that.

### `safe_int(value) -> Result[int, Union[TypeError, ValueError]]`

A safe version of the built-in `int()` function. Returns an integer object constructed from a number or string.

### `safe_isinstance(obj, class_or_tuple) -> Result[bool, TypeError]`

A safe version of the built-in `isinstance()` function. Returns `True` if the object is an instance of the class or of a subclass thereof.

### `safe_issubclass(cls, class_or_tuple) -> Result[bool, TypeError]`

A safe version of the built-in `issubclass()` function. Returns `True` if the class is a subclass of the class or of a subclass thereof.

### `safe_iter(obj) -> Result[iterator, TypeError]`

A safe version of the built-in `iter()` function. Returns an iterator object.

### `safe_len(obj) -> Result[int, Union[TypeError, OverflowError]]`

A safe version of the built-in `len()` function. Returns the length (the number of items) of an object.

### `safe_list(iterable) -> Result[list, TypeError]`

A safe version of the built-in `list()` function. Returns a list.

### `safe_map(function, iterable) -> Result[map_object, TypeError]`

A safe version of the built-in `map()` function. Returns an iterator that applies function to every item of iterable.

### `safe_max(iterable) -> Result[max_item, Union[TypeError, ValueError]]`

A safe version of the built-in `max()` function. Returns the largest item in an iterable or the largest of two or more arguments.

### `safe_memoryview(obj) -> Result[memoryview, Union[TypeError, ValueError]]`

A safe version of the built-in `memoryview()` function. Returns a memory view object.

### `safe_min(iterable) -> Result[min_item, Union[TypeError, ValueError]]`

A safe version of the built-in `min()` function. Returns the smallest item in an iterable or the smallest of two or more arguments.

### `safe_next(iterator) -> Result[next_item, Union[TypeError, StopIteration]]`

A safe version of the built-in `next()` function. Retrieves the next item from the iterator.

### `safe_object() -> Result[object, TypeError]`

A safe version of the built-in `object()` function. Returns a new featureless object.

### `safe_oct(number) -> Result[str, TypeError]`

A safe version of the built-in `oct()` function. Converts an integer number to an octal string prefixed with "0o".

### `safe_open(file, mode) -> Result[file_object, Union[FileNotFoundError, IsADirectoryError, NotADirectoryError, PermissionError, FileExistsError, OSError, ValueError, TypeError]]`

A safe version of the built-in `open()` function. Opens a file and returns a corresponding file object.

### `safe_print(*objects, sep, end, file, flush) -> Result[None, Union[TypeError, UnicodeError, ValueError, OSError, IOError]]`

A safe version of the built-in `print()` function. Prints the values to a stream.

### `safe_hasattr(obj, name) -> Result[bool, Union[TypeError, ValueError]]`

A safe version of the built-in `hasattr()` function. Returns `True` if the object has the given named attribute.

### `safe_ord(c) -> Result[int, Union[TypeError, ValueError]]`

A safe version of the built-in `ord()` function. Returns the Unicode code point of the character.

### `safe_bool(value) -> Result[bool, TypeError]`

A safe version of the built-in `bool()` function. Returns a boolean value.

### `safe_pow(base, exp, mod) -> Result[result, Union[TypeError, ValueError]]`

A safe version of the built-in `pow()` function. Returns base to the power exp; if mod is present, returns base to the power exp, modulo mod.

### `safe_range(stop) -> Result[range_object, Union[TypeError, ValueError]]`

A safe version of the built-in `range()` function. Returns a sequence of numbers.

### `safe_reversed(seq) -> Result[reversed_object, TypeError]`

A safe version of the built-in `reversed()` function. Returns a reverse iterator.

### `safe_round(number) -> Result[float, TypeError]`

A safe version of the built-in `round()` function. Returns the floating point value number rounded to the nearest integer.

### `safe_set(iterable) -> Result[set, TypeError]`

A safe version of the built-in `set()` function. Returns a new set object.

### `safe_setattr(obj, name, value) -> Result[None, Union[TypeError, AttributeError, ValueError]]`

A safe version of the built-in `setattr()` function. Sets the value of the named attribute of the object.

### `safe_slice(start, stop, step) -> Result[slice_object, TypeError]`

A safe version of the built-in `slice()` function. Returns a slice object.

### `safe_sorted(iterable) -> Result[list, TypeError]`

A safe version of the built-in `sorted()` function. Returns a new sorted list from the items in iterable.

### `safe_str(obj) -> Result[str, Union[TypeError, UnicodeError]]`

A safe version of the built-in `str()` function. Returns a string version of the object.

### `safe_sum(iterable) -> Result[sum_result, TypeError]`

A safe version of the built-in `sum()` function. Sums the items of an iterable.

### `safe_super(type, obj) -> Result[super_object, TypeError]`

A safe version of the built-in `super()` function. Returns a proxy object that delegates method calls to a parent or sibling class.

### `safe_tuple(iterable) -> Result[tuple, TypeError]`

A safe version of the built-in `tuple()` function. Returns a tuple.

### `safe_type(obj) -> Result[type, TypeError]`

A safe version of the built-in `type()` function. Returns the type of the object.

### `safe_vars(obj) -> Result[dict, TypeError]`

A safe version of the built-in `vars()` function. Returns the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.

### `safe_zip(*iterables) -> Result[zip_object, TypeError]`

A safe version of the built-in `zip()` function. Returns an iterator of tuples.

### `safe_import(name, globals, locals, fromlist, level) -> Result[module, Union[ImportError, ModuleNotFoundError]]`

A safe version of the built-in `__import__()` function. Imports a module.

> this docs is auto-generated by Qwen Code
