from __future__ import annotations

import sys

sys.path.append(".")

from typing import Literal, Optional

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from buildsql import select, and_

# Create in-memory SQLite engine
eng = create_engine("sqlite:///:memory:", echo=True)

with eng.begin() as conn:
    conn.execute(
        text(
            """
        create table users (
            id integer primary key
            , name text
        );
    """
        )
    )
    conn.execute(text("insert into users (name) values ('Alex');"))
    conn.execute(text("insert into users (name) values ('Rita');"))


# Query using SQLAlchemy select()
with Session(eng) as ses:
    root = select("*").from_("users").where("id > 0").limit(10)

    sql = root.build()

    print("---------------------")
    print(sql)
    print("---------------------")

    # stmt = select(text("*")).select_from(text("users"))
    rows = ses.execute(text(sql)).fetchall()
    print(rows)

quit()


# warn by default? pass in warnings_off=True to disable? -- like if passing in a comma or something...
#
# have (param) ??

root = select("*").from_("users").where("id > 0").limit(10)
root = (
    select("*")
    .from_("users")
    .left_join("table", on="users.id = table.user_id")
    # TODO: way to insert condition ...
    .where(and_("id > 0", "name != 'Rita'"))
    .limit(10)
)

# import buildsql as sql

# sql.select()
# sql.all()
# sql.and() sql.or()
# sql.asc() sql.desc() <-------
# sql.param()
#
# window functions - over() , partition_by(), order_by()
#
# gtt, lt, gte, lte, eq, neq
# is_null, is_not_null
# between, in_, not_in
# like, ilike
# exists, not_exists
# case_when, case_else, case_end
# aggregate functions: count, sum, avg, min, max
# date functions: now, date_add, date_sub, datediff
# string functions: concat, substring, length, lower, upper, trim
# math functions: abs, ceil, floor, round, sqrt
# json functions: json_extract, json_set, json_remove
# array functions: array_length, array_append, array_prepend
# etc.
# 
# Date helpers -- timezone, interval, trunc, format...
#
# create table, schema, index, user, ... (admin)

print(root.build())
quit()
root = (
    select("*")
    .from_("users")
    .where("id > 0")
    .group_by("col1")
    .order_by(("a", "desc"))
    .limit(10)
)
root = (
    select("*")
    .from_("users")
    .where("id > 0")
    .group_by("col1")
    .having("some-cond")
    .limit(10)
)
root = (
    select("*")
    .from_("users")
    .group_by("col1")
    .having("some-cond")
    .order_by(("asd", "desc"))
    .limit(10)
)

root = select("*").from_("users").having("some-cond")
# TODO: need to handle subquery builds.....
select("*").from_(select("1"))

print(root._build())

quit()

# Create a table and insert a row for testing
with eng.begin() as conn:
    conn.execute(
        text(
            """
        create table users (
            id integer primary key
            , name text
        );
    """
        )
    )
    conn.execute(text("insert into users (name) values ('Alex');"))
    conn.execute(text("insert into users (name) values ('Rita');"))


# Query using SQLAlchemy select()
with Session(eng) as ses:
    root = select("*").from_("users").where("id > 0").limit(10)

    sql = root.build()

    print(sql)

    # stmt = select(text("*")).select_from(text("users"))
    rows = ses.execute(text(sql)).fetchall()
    print(rows)
