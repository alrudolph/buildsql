package main

import (
	"fmt"

	sql "github.com/alrudolph/buildsql/go/buildsql"
	sel "github.com/alrudolph/buildsql/go/select"
)

func main() {
	strs := []string{
		// sql.Query().Limit(1).Build(),
		// sql.Query().OrderBy(sql.Asc("name")).Build(),
		// sql.Query().OrderBy(sql.Asc("name"), sql.Desc("age")).Build(),
		// sql.Query().OrderBy(sql.Asc("name")).Limit(1).Build(),
		// sql.Query().
		// 	OrderBy(sql.Asc("name"), sql.Desc("age")).
		// 	Limit(2).
		// 	Build(),
		sql.Query().
			Select("a", "b", "c").
			From("asdasda").
			LeftJoin("left_table", "asdas").
			Where("some_condition").
			GroupBy("asdad").
			OrderBy(sel.Asc("table"), sel.Desc("condition")).
			Limit(1).
			Build(),
	}

	for _, s := range strs {
		fmt.Println(s)
	}
}
