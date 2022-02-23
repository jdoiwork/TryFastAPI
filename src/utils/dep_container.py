# pyright: strict, reportGeneralTypeIssues=false, reportUnknownMemberType=false

from typing import Any, Callable, cast
from lagom import Container

Factory = Callable[..., Any]

class DepContainer:
    def __init__(self, container: Container) -> None:
        self.c = container

    def get(self, key: Factory, default: Factory) -> Factory:
        if key in self.c.defined_types:
            return lambda: self.c[key]
        else:
            return default

    def to_dependency_overrides(self) -> dict[Factory, Factory]:
        return cast(dict[Factory, Factory], self)
