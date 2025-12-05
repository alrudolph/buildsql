# from __future__ import annotations

# from .base import Buildable, Terminal, StrOrTerminal, IntOrTerminal, get_value, BaseOrderT, OrderDirection


# class Limit(Buildable):

#     def __init__(self, limit: IntOrTerminal) -> None:
#         self._limit = limit

#     def build(self) -> str:
#         limit = get_value(self._limit)
#         return f"limit {limit}"


# class Limitable(Terminal):

#     # TODO: required 1 or optional 1
#     # limit 2 - only 1...
#     def limit(self, limit: IntOrTerminal) -> Terminal:
#         return Terminal([*self._parts, Limit(limit)])


# class Order(Buildable):

#     def __init__(self, col_1: BaseOrderT, *columns: BaseOrderT) -> None:
#         self._columns = (col_1, *columns)

#     def build(self) -> str:
#         cols: list[str] = []

#         for col in self._columns:
#             if isinstance(col, tuple):
#                 column, direction = col
#                 cols.append(f"{get_value(column)} {direction}")
#             else:
#                 cols.append(get_value(col))

#         return f"order by {', '.join(cols)}"


# class Orderable(Limitable):

#     def order_by(self, col_1: BaseOrderT, *columns: BaseOrderT) -> Limitable:
#         return Limitable([*self._parts, Order(col_1, *columns)])


# class Having(Buildable):

#     def __init__(self, condition: StrOrTerminal) -> None:
#         self._condition = condition

#     def build(self) -> str:
#         having = get_value(self._condition)
#         return f"having {having}"


# class Havingable(Orderable):

#     def having(self, condition: StrOrTerminal) -> Orderable:
#         return Orderable([*self._parts, Having(condition)])


# class GroupBy(Buildable):

#     def __init__(self, *columns: StrOrTerminal) -> None:
#         self._columns = columns

#     def build(self) -> str:
#         cols = [get_value(col) for col in self._columns]
#         return f"group by {', '.join(cols)}"


# class GroupByable(Orderable):

#     def group_by(self, col_1: StrOrTerminal, *columns: StrOrTerminal) -> Havingable:
#         return Havingable([*self._parts, GroupBy(col_1, *columns)])


# class Where(Buildable):

#     def __init__(self, condition: StrOrTerminal) -> None:
#         self._condition = condition

#     def build(self) -> str:
#         where = get_value(self._condition)
#         return f"where {where}"


# class Whereable(GroupByable):

#     def where(self, condition: StrOrTerminal) -> GroupByable:
#         return GroupByable([*self._parts, Where(condition)])


# #
# # TODO: JOINS
# #


# class BaseJoin(Buildable):

#     def __init__(
#         self,
#         join_type: str,
#         table: StrOrTerminal,
#         *,
#         on: StrOrTerminal,
#     ) -> None:
#         self._join_type = join_type
#         self._table = table
#         self._on = on

#     def build(self) -> str:
#         table = get_value(self._table)
#         on = get_value(self._on)
#         return f"{self._join_type} join {table} on {on}"


# class LeftJoin(BaseJoin):

#     def __init__(self, table: StrOrTerminal, *, on: StrOrTerminal) -> None:
#         super().__init__("left", table, on=on)


# class RightJoin(BaseJoin):

#     def __init__(self, table: StrOrTerminal, *, on: StrOrTerminal) -> None:
#         super().__init__("right", table, on=on)


# class InnerJoin(BaseJoin):

#     def __init__(self, table: StrOrTerminal, *, on: StrOrTerminal) -> None:
#         super().__init__("inner", table, on=on)


# class FullJoin(BaseJoin):

#     def __init__(self, table: StrOrTerminal, *, on: StrOrTerminal) -> None:
#         super().__init__("full", table, on=on)


# class LateralJoin(BaseJoin):

#     def __init__(self, table: StrOrTerminal, *, on: StrOrTerminal) -> None:
#         super().__init__("lateral", table, on=on)


# class CrossJoin(Buildable):

#     def __init__(self, table: StrOrTerminal) -> None:
#         self._table = table

#     def build(self) -> str:
#         table = get_value(self._table)
#         return f"cross join {table}"


# class BaseJoinable(Whereable):

#     def left_join(self, table: StrOrTerminal, *, on: StrOrTerminal) -> BaseJoinable:
#         return BaseJoinable([*self._parts, LeftJoin(table, on=on)])

#     def right_join(self, table: StrOrTerminal, *, on: StrOrTerminal) -> BaseJoinable:
#         return BaseJoinable([*self._parts, RightJoin(table, on=on)])

#     def inner_join(self, table: StrOrTerminal, *, on: StrOrTerminal) -> BaseJoinable:
#         return BaseJoinable([*self._parts, InnerJoin(table, on=on)])

#     def full_join(self, table: StrOrTerminal, *, on: StrOrTerminal) -> BaseJoinable:
#         return BaseJoinable([*self._parts, FullJoin(table, on=on)])

#     def cross_join(self, table: StrOrTerminal) -> BaseJoinable:
#         return BaseJoinable([*self._parts, CrossJoin(table)])

#     def lateral_join(self, table: StrOrTerminal, *, on: StrOrTerminal) -> BaseJoinable:
#         return BaseJoinable([*self._parts, LateralJoin(table, on=on)])


# class From(Buildable):

#     def __init__(self, table: StrOrTerminal) -> None:
#         self._table = table

#     def build(self) -> str:
#         table = get_value(self._table)
#         return f"from {table}"


# class Fromable:

#     def __init__(self, select: Select) -> None:
#         self._parts = [select]

#     def from_(self, table: StrOrTerminal) -> BaseJoinable:
#         return BaseJoinable([*self._parts, From(table)])


# class Select(Buildable):

#     # TODO: could also be numbers etc...
#     def __init__(self, *columns: StrOrTerminal) -> None:
#         self._columns = columns

#     def build(self) -> str:
#         cols = [get_value(col) for col in self._columns]
#         return f"select {', '.join(cols)}"


# class Selectable:

#     def select(self, col_1: StrOrTerminal, *columns: StrOrTerminal) -> Fromable:
#         return Fromable(Select(col_1, *columns))


# class Root(Selectable): ...


# def select(col_1: StrOrTerminal, *columns: StrOrTerminal) -> Fromable:
#     return Fromable(Select(col_1, *columns))
