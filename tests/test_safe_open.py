from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import OpenBinaryMode


def decorator_factory(*, mode: "OpenBinaryMode") -> int:
    """
    Decorator factory is invoked with arguments like this:
      @decorator_factory(mode="easy")
      def my_function(): ...
    """
    return 0


print(decorator_factory(mode="a+b"))
