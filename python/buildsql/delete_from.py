from __future__ import annotations

from .base import Buildable, StrOrTerminal, Terminal, get_value, StrOrBuildable
from typing import Optional


class Returning(Buildable):

    def __init__(self, returning: StrOrTerminal) -> None:
        self._returning = returning

    def build(self) -> str:
        returning = get_value(self._returning)
        return f"returning {returning}"


class ReturningAble(Terminal):

    def returning(self, returning: StrOrTerminal) -> Terminal:
        # hmm i'm thinking this should take in args
        return Terminal([*self._parts, Returning(returning)])


class Where(Buildable):

    def __init__(self, condition: StrOrTerminal) -> None:
        self._condition = condition

    def build(self) -> str:
        where = get_value(self._condition)
        return f"where {where}"


class Whereable(ReturningAble):

    def where(self, condition: StrOrTerminal) -> ReturningAble:
        return ReturningAble([*self._parts, Where(condition)])


class MustWhereable:

    def __init__(self, parts: Optional[list[StrOrBuildable]] = None) -> None:
        if parts is None:
            parts = []

        self._parts = parts

    def where(self, condition: StrOrTerminal) -> ReturningAble:
        return ReturningAble([*self._parts, Where(condition)])


class Using(Buildable):

    def __init__(self, using_clause: StrOrTerminal) -> None:
        self._using_clause = using_clause

    def build(self) -> str:
        using_clause = get_value(self._using_clause)
        return f"using {using_clause}"


class Usingable(Whereable):

    def __init__(self, delete_from: DeleteFrom) -> None:
        self._parts = [delete_from]

    def using(self, using_clause: StrOrTerminal) -> MustWhereable:
        return MustWhereable([*self._parts, Using(using_clause)])


class DeleteFrom(Buildable):

    def __init__(self, table_name: str) -> None:
        self._table_name = table_name

    def build(self) -> str:
        return f"delete from {self._table_name}"


def delete_from(table_name: str) -> Usingable:
    return Usingable(DeleteFrom(table_name))
