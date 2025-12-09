from __future__ import annotations

from .base import StrOrTerminal, get_value
from collections.abc import Sequence
from .utils import join_conditions


def and_(condition_1: StrOrTerminal, *conditions: StrOrTerminal) -> StrOrTerminal:
    return join_conditions("and", condition_1, *conditions)


def or_(condition_1: StrOrTerminal, *conditions: StrOrTerminal) -> StrOrTerminal:
    return join_conditions("or", condition_1, *conditions)


def in_(column: StrOrTerminal, values: Sequence[StrOrTerminal]) -> StrOrTerminal:
    vals = ", ".join(get_value(val) for val in values)
    return f"{get_value(column)} in ({vals})"
