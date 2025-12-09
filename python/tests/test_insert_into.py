from buildsql import insert_into


class TestInsertInto:

    def test_insert_into_values(self) -> None:
        sql = insert_into("users", ["id", "name"]).values("1, 'John'").build()
        assert sql == "insert into users (id, name)\nvalues (1, 'John')"

    def test_insert_into_values_returning(self) -> None:
        sql = (
            insert_into("users", ["id", "name"])
            .values("1, 'John'")
            .returning("id, name")
            .build()
        )
        assert (
            sql
            == "insert into users (id, name)\nvalues (1, 'John')\nreturning id, name"
        )

    def test_insert_into_values_on_conflict(self) -> None:
        sql = (
            insert_into("users", ["id", "name"])
            .values("1, 'John'")
            .on_conflict("do update set name = excluded.name")
            .build()
        )
        assert (
            sql
            == "insert into users (id, name)\nvalues (1, 'John')\non conflict do update set name = excluded.name"
        )

    def test_insert_into_values_on_conflict_returning(self) -> None:
        sql = (
            insert_into("users", ["id", "name"])
            .values("1, 'John'")
            .on_conflict("do nothing")
            .returning("id, name")
            .build()
        )
        assert (
            sql
            == "insert into users (id, name)\nvalues (1, 'John')\non conflict do nothing\nreturning id, name"
        )

    def test_insert_into_values_on_conflict_do_nothing_returning(self) -> None:
        sql = (
            insert_into("users", ["id", "name"])
            .values("1, 'John'")
            .on_conflict_do_nothing()
            .returning("id, name")
            .build()
        )
        assert (
            sql
            == "insert into users (id, name)\nvalues (1, 'John')\non conflict do nothing\nreturning id, name"
        )

    def test_insert_into_values_on_conflict_do_update_set_returning(self) -> None:
        sql = (
            insert_into("users", ["id", "name"])
            .values("1, 'John'")
            .on_conflict_do_update_set("name = excluded.name")
            .returning("id, name")
            .build()
        )
        assert (
            sql
            == "insert into users (id, name)\nvalues (1, 'John')\non conflict do update set name = excluded.name\nreturning id, name"
        )
