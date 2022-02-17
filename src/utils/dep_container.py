# pyright: strict, reportGeneralTypeIssues=false

from typing import Any, Callable, cast
from lagom import Container

Factory = Callable[..., Any]

class DepContainer:
    def __init__(self, container: Container) -> None:
        self.c = container

    def get(self, key: Factory, default: Factory) -> Factory:
        try:
            # TODO: resolve `reportGeneralTypeIssues`
            return lambda: self.c[key]
        except Exception:
            return default

    def to_dependency_overrides(self) -> dict[Factory, Factory]:
        return cast(dict[Factory, Factory], self)
