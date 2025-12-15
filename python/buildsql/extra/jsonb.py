# https://www.postgresql.org/docs/current/functions-json.html

from buildsql.base import Terminal, StrOrTerminal, BoolOrTerminal, IntOrTerminal
from buildsql.utils import join_with_commas


class JsonB(Terminal):

    def at(self, index: int) -> JsonB:
        """Access a key in a JSONB column.

        TODO: link to docs.
        TODO: example usage
        """
        return JsonB([*self._parts, f"-> {index}"])

    def get(self, key: str) -> JsonB:
        """Access a key in a JSONB column.

        TODO: link to docs.
        TODO: example usage
        """
        return JsonB([*self._parts, f"-> '{key}'"])

    def extract(self, key1: str | int, *keys: str | int) -> JsonB:
        """Extract nested keys from a JSONB column.

        TODO: link to docs.
        TODO: example usage
        """
        all_keys = [key1, *keys]
        path = join_with_commas([str(k) for k in all_keys])
        return JsonB([*self._parts, f"#> '{{{path}}}'"])

    def text_at(self, index: int) -> StrOrTerminal:
        """Access a key in a JSONB column and return text.

        TODO: link to docs.
        TODO: example usage
        """
        return JsonB([*self._parts, f"->> {index}"])

    def text_get(self, key: str) -> StrOrTerminal:
        """Access a key in a JSONB column and return text.

        TODO: link to docs.
        TODO: example usage
        """
        return JsonB([*self._parts, f"->> '{key}'"])

    def text_extract(self, key1: str | int, *keys: str | int) -> StrOrTerminal:
        """Extract nested keys from a JSONB column and return text.

        TODO: link to docs.
        TODO: example usage
        """
        all_keys = [key1, *keys]
        path = join_with_commas([str(k) for k in all_keys])
        return JsonB([*self._parts, f"#>> '{{{path}}}'"])


# TODO: jsonb only operators


def value(value: str) -> JsonB:
    """Create a JSONB value.

    TODO: link to docs.
    TODO: example usage
    """
    return JsonB([f"'{value}'::jsonb"])


def col(col: str) -> JsonB:
    """Create a JSONB column reference.

    TODO: link to docs.
    TODO: example usage
    """
    return JsonB([f"{col}::jsonb"])
