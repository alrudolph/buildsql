"""Admin module for buildsql."""

from .create_index import create_index
from .create_schema import create_schema
from .create_table import create_table

__all__ = [
    "create_index",
    "create_schema",
    "create_table",
]
