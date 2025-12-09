from __future__ import annotations

from .base import (
    Buildable,
    StrOrTerminal,
    Terminal,
    get_value,
)


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


class From(Buildable):

    def __init__(self, table: StrOrTerminal) -> None:
        self._table = table

    def build(self) -> str:
        table = get_value(self._table)
        return f"from {table}"


class Fromeable(Whereable):

    def from_(self, table: StrOrTerminal) -> Whereable:
        return Whereable([*self._parts, From(table)])


class Set(Buildable):

    def __init__(self, set_clause: StrOrTerminal) -> None:
        self._set_clause = set_clause

    def build(self) -> str:
        set_clause = get_value(self._set_clause)
        return f"set {set_clause}"


class Setable:

    def __init__(self, update: Update) -> None:
        self._parts = [update]

    def set(self, set_clause: StrOrTerminal) -> Fromeable:
        # hmm i'm thinking this should take in args
        return Fromeable([*self._parts, Set(set_clause)])


class Update(Buildable):

    def __init__(self, table_name: str) -> None:
        self._table_name = table_name

    def build(self) -> str:
        return f"update {self._table_name}"


def update(table_name: str) -> Setable:
    return Setable(Update(table_name))
