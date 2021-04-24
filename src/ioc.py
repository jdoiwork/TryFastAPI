# pyright: strict

from typing import Any, Callable, Type, TypeVar
from lagom   import Container
from lagom.integrations.fast_api import FastApiIntegration

T = TypeVar('T')

Resolver = Callable[[Type[T]], T]

def register(setup: Callable[[Container], Any]):
    c = Container()

    setup(c)

    deps = FastApiIntegration(c)

    def resolve(cls: Type[T]) -> T:
        return deps.depends(cls)

    return resolve
