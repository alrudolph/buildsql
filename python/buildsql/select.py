from __future__ import annotations
from typing import Literal, Optional
from .base import (
    BaseOrderT,
    Buildable,
    IntOrTerminal,
    StrOrTerminal,
    Terminal,
    get_value,
    StrOrBuildable,
)
from .utils import join_with_commas

FetchDirection = Literal["first", "next"]
FetchTieType = Literal["only", "with ties"]


class Fetch(Buildable):

    def __init__(
        self, direction: FetchDirection, fetch: IntOrTerminal, tie: FetchTieType
    ) -> None:
        self._direction = direction
        self._fetch = fetch
        self._tie = tie

    def build(self) -> str:
        fetch = get_value(self._fetch)

        if fetch == 1 and self._tie == "only":
            return f"fetch {self._direction} row only"

        return f"fetch {self._direction} {fetch} rows {self._tie}"


class Fetchable(Terminal):

    def fetch(
        self,
        direction: FetchDirection,
        fetch: IntOrTerminal,
        tie: FetchTieType,
    ) -> Terminal:
        return Terminal([*self._parts, Fetch(direction, fetch, tie)])


class Offset(Buildable):

    def __init__(self, offset: IntOrTerminal) -> None:
        self._offset = offset

    def build(self) -> str:
        offset = get_value(self._offset)

        if offset == 0:
            return "offset 1 row"

        return f"offset {offset} rows"


class Offsetable(Fetchable):

    def offset(self, offset: IntOrTerminal) -> Fetchable:
        return Fetchable([*self._parts, Offset(offset)])


class Limit(Buildable):

    def __init__(self, limit: IntOrTerminal) -> None:
        self._limit = limit

    def build(self) -> str:
        limit = get_value(self._limit)
        return f"limit {limit}"


class Limitable(Offsetable):

    # TODO: required 1 or optional 1
    # limit 2 - only 1...
    def limit(self, limit: IntOrTerminal) -> Offsetable:
        return Offsetable([*self._parts, Limit(limit)])


class Order(Buildable):

    def __init__(self, col_1: BaseOrderT, *columns: BaseOrderT) -> None:
        self._columns = (col_1, *columns)

    def build(self) -> str:
        cols: list[str] = []

        for col in self._columns:
            if isinstance(col, tuple):
                column, direction = col
                cols.append(f"{get_value(column)} {direction}")
            else:
                cols.append(get_value(col))

        return f"order by {join_with_commas(cols)}"


class Orderable(Limitable):

    def order_by(self, col_1: BaseOrderT, *columns: BaseOrderT) -> Limitable:
        return Limitable([*self._parts, Order(col_1, *columns)])


class Having(Buildable):

    def __init__(self, condition: StrOrTerminal) -> None:
        self._condition = condition

    def build(self) -> str:
        having = get_value(self._condition)
        return f"having {having}"


class Havingable(Orderable):

    def having(self, condition: StrOrTerminal) -> Orderable:
        return Orderable([*self._parts, Having(condition)])


class GroupBy(Buildable):

    def __init__(self, *columns: StrOrTerminal) -> None:
        self._columns = columns

    def build(self) -> str:
        return f"group by {join_with_commas(self._columns)}"


class GroupByable(Orderable):

    def group_by(self, col_1: StrOrTerminal, *columns: StrOrTerminal) -> Havingable:
        return Havingable([*self._parts, GroupBy(col_1, *columns)])


class Where(Buildable):

    def __init__(self, condition: StrOrTerminal) -> None:
        self._condition = condition

    def build(self) -> str:
        where = get_value(self._condition)
        return f"where {where}"


class Whereable(GroupByable):

    def where(self, condition: StrOrTerminal) -> GroupByable:
        return GroupByable([*self._parts, Where(condition)])


#
# TODO: JOINS
#


class BaseJoin(Buildable):

    def __init__(
        self,
        join_type: str,
        table: StrOrTerminal,
        *,
        on: StrOrTerminal,
    ) -> None:
        self._join_type = join_type
        self._table = table
        self._on = on

    def build(self) -> str:
        table = get_value(self._table)
        on = get_value(self._on)
        return f"{self._join_type} join {table} on {on}"


class LeftJoin(BaseJoin):

    def __init__(self, table: StrOrTerminal, *, on: StrOrTerminal) -> None:
        super().__init__("left", table, on=on)


class RightJoin(BaseJoin):

    def __init__(self, table: StrOrTerminal, *, on: StrOrTerminal) -> None:
        super().__init__("right", table, on=on)


class InnerJoin(BaseJoin):

    def __init__(self, table: StrOrTerminal, *, on: StrOrTerminal) -> None:
        super().__init__("inner", table, on=on)


class FullJoin(BaseJoin):

    def __init__(self, table: StrOrTerminal, *, on: StrOrTerminal) -> None:
        super().__init__("full", table, on=on)


class LateralJoin(BaseJoin):

    def __init__(self, table: StrOrTerminal, *, on: StrOrTerminal) -> None:
        super().__init__("lateral", table, on=on)


class CrossJoin(Buildable):

    def __init__(self, table: StrOrTerminal) -> None:
        self._table = table

    def build(self) -> str:
        table = get_value(self._table)
        return f"cross join {table}"


# TODO: natural_join


class BaseJoinable(Whereable):

    def left_join(self, table: StrOrTerminal, *, on: StrOrTerminal) -> BaseJoinable:
        return BaseJoinable([*self._parts, LeftJoin(table, on=on)])

    def right_join(self, table: StrOrTerminal, *, on: StrOrTerminal) -> BaseJoinable:
        return BaseJoinable([*self._parts, RightJoin(table, on=on)])

    def inner_join(self, table: StrOrTerminal, *, on: StrOrTerminal) -> BaseJoinable:
        return BaseJoinable([*self._parts, InnerJoin(table, on=on)])

    def full_join(self, table: StrOrTerminal, *, on: StrOrTerminal) -> BaseJoinable:
        return BaseJoinable([*self._parts, FullJoin(table, on=on)])

    def cross_join(self, table: StrOrTerminal) -> BaseJoinable:
        return BaseJoinable([*self._parts, CrossJoin(table)])

    def lateral_join(self, table: StrOrTerminal, *, on: StrOrTerminal) -> BaseJoinable:
        return BaseJoinable([*self._parts, LateralJoin(table, on=on)])


class From(Buildable):

    def __init__(self, table: StrOrTerminal) -> None:
        self._table = table

    def build(self) -> str:
        table = get_value(self._table)
        return f"from {table}"


class Fromable(Terminal):

    def __init__(self, select: Select) -> None:
        self._parts = [select]

    def from_(self, table: StrOrTerminal) -> BaseJoinable:
        return BaseJoinable([*self._parts, From(table)])


class MustFromable:

    def __init__(self, parts: Optional[list[StrOrBuildable]] = None) -> None:
        if parts is None:
            parts = []

        self._parts = parts

    def from_(self, table: StrOrTerminal) -> BaseJoinable:
        return BaseJoinable([*self._parts, From(table)])


class SelectDistinctOnable(Fromable):

    def __init__(self, select_distinct: SelectDistinct) -> None:
        self._parts = [select_distinct]
        self._select_distinct = select_distinct

    def on(self, on_col_1: StrOrTerminal, *on_columns: StrOrTerminal) -> MustFromable:
        return MustFromable(
            [
                SelectDistinctOn(
                    [on_col_1, *on_columns],
                    self._select_distinct._columns,
                )
            ]
        )


class Select(Buildable):

    # TODO: could also be numbers etc...
    def __init__(self, *columns: StrOrTerminal) -> None:
        self._columns = columns

    def build(self) -> str:
        return f"select {join_with_commas(self._columns)}"


class SelectDistinct(Buildable):

    def __init__(self, *columns: StrOrTerminal) -> None:
        self._columns = columns

    def build(self) -> str:
        return f"select distinct {join_with_commas(self._columns)}"


class SelectDistinctOn(Buildable):

    def __init__(
        self,
        on_columns: list[StrOrTerminal],
        columns: StrOrTerminal,
    ) -> None:
        self._on_columns = on_columns
        self._columns = columns

    def build(self) -> str:
        return f"select distinct on ({join_with_commas(self._on_columns)}) {join_with_commas(self._columns)}"


def select(col_1: StrOrTerminal, *columns: StrOrTerminal) -> Fromable:
    return Fromable(Select(col_1, *columns))


def select_distinct(
    col_1: StrOrTerminal,
    *columns: StrOrTerminal,
) -> SelectDistinctOnable:
    return SelectDistinctOnable(SelectDistinct(col_1, *columns))


# TODO: https://www.postgresql.org/docs/current/sql-select.html
#
# * window
# * union / intersect / except
# * for
