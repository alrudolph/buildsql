from __future__ import annotations

from .base import StrOrTerminal, get_value


def and_(*conditions: StrOrTerminal) -> StrOrTerminal:
    return "(" + " and ".join(get_value(cond) for cond in conditions) + ")"


def or_(*conditions: StrOrTerminal) -> StrOrTerminal:
    return "(" + " or ".join(get_value(cond) for cond in conditions) + ")"


def in_(column: StrOrTerminal, *values: StrOrTerminal) -> StrOrTerminal:
    vals = ", ".join(get_value(val) for val in values)
    return f"{get_value(column)} in ({vals})"
