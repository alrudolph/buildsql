package main

import (
	sql "github.com/alrudolph/buildsql/go/buildsql"
)

func main() {
	strs := []string{
		sql.Query().Limit(1).Build(),
		sql.Query().Order(sql.Col("name")).Build(),
		sql.Query().Order(sql.Col("name"), sql.Desc("age")).Build(),
		sql.Query().Order(sql.Col("name")).Limit(1).Build(),
		sql.Query().
			Order(sql.Col("name"), sql.Desc("age"), sql.Desc("age"), sql.Desc("age"), sql.Desc("age")).
			Limit(2).
			Build(),
	}

	for _, s := range strs {
		println(s)
	}
}
