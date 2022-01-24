# pyright: strict

from typing import Type
from lagom  import Container
from lagom.integrations.fast_api import FastApiIntegration, T



container = Container()
deps = FastApiIntegration(container)

def di(t: Type[T]) -> T:
    return deps.depends(t)
