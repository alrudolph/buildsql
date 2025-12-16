"""Create an index on a specified table and column in the database."""

# https://www.postgresql.org/docs/current/sql-createindex.html
# TODO: missing a lot of values...

from buildsql.base import Buildable, Terminal

# TODO: where to put column / expression....


class Using(Buildable):
    """Represents a USING clause of a CREATE INDEX statement."""

    def __init__(self, method: str) -> None:
        self._method = method

    def build(self) -> str:
        """Create a USING clause."""
        return f"using {self._method}"


class UsingAble(Terminal):
    """Defines the USING clause of a CREATE INDEX statement."""

    def using(self, method: str) -> Terminal:
        """Specify the index method to use.

        TODO: link to docs.
        TODO: example usage
        """
        return Terminal([*self._parts, Using(method)])


class CreateIndex(Buildable):

    def __init__(
        self,
        index_name: str,
        on: str,
        unique: bool,
        concurrently: bool,
        if_not_exists: bool,
    ) -> None:
        self._index_name = index_name
        self._on = on
        self._unique = unique
        self._concurrently = concurrently
        self._if_not_exists = if_not_exists

    def build(self) -> str:
        """Create a CREATE INDEX statement."""
        parts = ["create"]

        if self._unique:
            parts.append("unique")

        parts.append("index")

        if self._concurrently:
            parts.append("concurrently")

        if self._if_not_exists:
            parts.append("if not exists")

        parts.append(self._index_name)
        parts.append(f"on {self._on}")

        return " ".join(parts)


def create_index(
    index_name: str,
    on: str,
    *,
    unique: bool = False,
    concurrently: bool = False,
    if_not_exists: bool = False,
) -> UsingAble:
    """Create an index on a specified table and column.

    TODO: link to docs.
    TODO: example usage
    """
    return UsingAble(CreateIndex(index_name, on, unique, concurrently, if_not_exists))
