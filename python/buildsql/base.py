from __future__ import annotations

from typing import Literal, Optional


class Buildable:

    def build(self) -> str:
        raise NotImplementedError()


def get_value(value: int | str | Buildable) -> str:
    if isinstance(value, Buildable):
        return value.build()

    return str(value)


class Terminal(Buildable):

    def __init__(self, parts: Optional[list[StrOrBuildable]] = None) -> None:
        if parts is None:
            parts = []

        self._parts = parts

    def build(self) -> str:
        return "\n".join(get_value(part) for part in self._parts)


StrOrBuildable = str | Buildable
IntOrBuildable = int | Buildable

StrOrTerminal = str | Terminal
IntOrTerminal = int | Terminal

OrderDirection = Literal["asc", "desc"]
BaseOrderT = StrOrTerminal | tuple[StrOrTerminal, OrderDirection]
