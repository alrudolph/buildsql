from buildsql import select, select_distinct


class TestSelect:

    # TODO: combinations of statements

    def test_select_only(self) -> None:
        sql = select("1").build()
        assert sql == "select 1"

    def test_select_from(self) -> None:
        sql = select("1").from_("table1").build()
        assert sql == "select 1\nfrom table1"

    def test_select_where(self) -> None:
        sql = select("1").from_("table1").where("id = 10").build()
        assert sql == "select 1\nfrom table1\nwhere id = 10"

    def test_select_group_by(self) -> None:
        sql = select("1").from_("table1").group_by("col1").build()
        assert sql == "select 1\nfrom table1\ngroup by col1"

    def test_select_having(self) -> None:
        sql = (
            select("1")
            .from_("table1")
            .group_by("col1")
            .having("count(col1) > 1")
            .build()
        )
        assert sql == "select 1\nfrom table1\ngroup by col1\nhaving count(col1) > 1"

    def test_select_order_by(self) -> None:
        sql = select("1").from_("table1").order_by("col1", ("col2", "desc")).build()
        assert sql == "select 1\nfrom table1\norder by col1, col2 desc"

    def test_select_limit(self) -> None:
        sql = select("1").from_("table1").limit(10).build()
        assert sql == "select 1\nfrom table1\nlimit 10"

    def test_select_offset(self) -> None:
        sql = select("1").from_("table1").offset(5).build()
        assert sql == "select 1\nfrom table1\noffset 5 rows"

    def test_select_fetch(self) -> None:
        sql = select("1").from_("table1").fetch("first", 10, "only").build()
        assert sql == "select 1\nfrom table1\nfetch first 10 rows only"


class TestSelectDistinct:

    # TODO: add more here...

    def test_select_distinct_only(self) -> None:
        sql = select_distinct("1").build()
        assert sql == "select distinct 1"

    def test_select_distinct_from(self) -> None:
        sql = select_distinct("1").from_("table1").build()
        assert sql == "select distinct 1\nfrom table1"

    def test_select_distinct_on_from(self) -> None:
        sql = select_distinct("col1").on("col2").from_("table1").build()
        assert sql == "select distinct on (col2) col1\nfrom table1"
