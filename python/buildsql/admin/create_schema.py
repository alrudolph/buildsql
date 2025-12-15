"""Create a new schema in the database."""

# https://www.postgresql.org/docs/current/sql-createschema.html
# TODO: [schema_element [ ... ]]

from buildsql.base import Buildable, Terminal
from typing import Literal, NewType

RoleSpecification = Literal["CURRENT_USER", "SESSION_USER", "CURRENT_ROLE"]
UserName = NewType("UserName", str)

class Authorization(Buildable):
    """Represents an AUTHORIZATION clause of a CREATE SCHEMA statement."""

    def __init__(self, role_specification: UserName | RoleSpecification) -> None:
        self._role_specification = role_specification

    def build(self) -> str:
        """Create an AUTHORIZATION clause."""
        return f"authorization {self._role_specification}"

class AuthorizationAble(Terminal):
    """Defines the AUTHORIZATION clause of a CREATE SCHEMA statement."""

    def authorization(self, role_specification: str) -> Terminal:
        """Specify the role that will own the created schema.

        TODO: link to docs.
        TODO: example usage
        """
        return Terminal([*self._parts, Authorization(role_specification)])

class IfNotExists(Buildable):
    """Represents an IF NOT EXISTS clause of a CREATE SCHEMA statement."""

    def build(self) -> str:
        """Create an IF NOT EXISTS clause."""
        return "if not exists"

class IfNotExistsAble(AuthorizationAble):
    """Defines the IF NOT EXISTS clause of a CREATE SCHEMA statement."""

    def if_not_exists(self) -> AuthorizationAble:
        """Specify that the schema should only be created if it does not already exist.

        TODO: link to docs.
        TODO: example usage
        """
        return AuthorizationAble([*self._parts, IfNotExists()])

# TODO: should this just be create_schema("...", if_not_exists=True) ???

class CreateSchema(Buildable):
    """Represents a CREATE SCHEMA statement."""

    def __init__(self, schema_name: str) -> None:
        self._schema_name = schema_name

    def build(self) -> str:
        """Create a CREATE SCHEMA statement."""
        return f"create schema {self._schema_name}"

def create_schema(schema_name: str) -> IfNotExistsAble:
    """Create a new schema in the database.

    TODO: link to docs.
    TODO: example usage
    """
    return IfNotExistsAble([CreateSchema(schema_name)])

