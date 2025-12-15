"""Create a table in the database."""

# https://www.postgresql.org/docs/current/sql-createtable.html
# TODO: Missing a lot...

from buildsql.base import Buildable, Terminal
from typing import Literal

# TODO: pass in column names, types, constraints

class IfNotExists(Buildable):
    """Represents an IF NOT EXISTS clause of a CREATE SCHEMA statement."""

    def build(self) -> str:
        """Create an IF NOT EXISTS clause."""
        return "if not exists"

class IfNotExistsAble(Terminal):
    """Defines the IF NOT EXISTS clause of a CREATE SCHEMA statement."""

    def if_not_exists(self) -> Terminal:
        """Specify that the schema should only be created if it does not already exist.

        TODO: link to docs.
        TODO: example usage
        """
        return Terminal([*self._parts, IfNotExists()])

# TODO: Temporary / Temp, Unlogged

class GlobalLocal(Buildable):
    """Represents a GLOBAL or LOCAL clause of a CREATE TABLE statement."""

    def __init__(self, global_local: Literal["global", "local"]) -> None:
        self._global_local = global_local

    def build(self) -> str:
        """Create a GLOBAL or LOCAL clause."""
        return self._global_local

class GlobalLocalAble(IfNotExistsAble):
    """Defines the GLOBAL or LOCAL clause of a CREATE TABLE statement."""

    def global_(self) -> IfNotExistsAble:
        """Specify that the table is a GLOBAL temporary table.

        TODO: link to docs.
        TODO: example usage
        """
        return IfNotExistsAble([*self._parts, GlobalLocal("global")])
    
    def local(self) -> IfNotExistsAble:
        """Specify that the table is a LOCAL temporary table.

        TODO: link to docs.
        TODO: example usage
        """
        return IfNotExistsAble([*self._parts, GlobalLocal("local")])


class CreateTable(Buildable):
    """Represents a CREATE TABLE statement."""

    def __init__(self, table_name: str) -> None:
        self._table_name = table_name

    def build(self) -> str:
        """Create a CREATE TABLE statement."""
        return f"create table {self._table_name}"
    

def create_table(table_name: str) -> GlobalLocalAble:
    """Create a CREATE TABLE statement.

    TODO: link to docs.
    TODO: example usage
    """
    return GlobalLocalAble([CreateTable(table_name)])


