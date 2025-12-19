package sel

import (
	"strings"
)

type Order interface {
	Buildable
}

type orderColumn struct {
	column    string
	direction string
}

func Asc(column string) orderColumn {
	return orderColumn{column: column, direction: "asc"}
}

func Desc(column string) orderColumn {
	return orderColumn{column: column, direction: "desc"}
}

type orderExpr struct {
	columns []orderColumn
}

func (o *orderExpr) Build() string {
	cols := []string{}

	for _, col := range o.columns {
		cols = append(cols, col.column+" "+col.direction)
	}

	return "order by " + strings.Join(cols, ", ")
}

type Orderable interface {
	Limitable
	OrderBy(col orderColumn, cols ...orderColumn) Limitable
}

type orderable struct {
	terminal
}

//nolint:ireturn
func orderBy(o *terminal, col orderColumn, cols ...orderColumn) Limitable {
	o.add(&orderExpr{columns: append([]orderColumn{col}, cols...)})

	return &limitable{terminal: *o}
}

//nolint:ireturn
func (o *orderable) OrderBy(col orderColumn, cols ...orderColumn) Limitable {
	return orderBy(&o.terminal, col, cols...)
}

//nolint:ireturn
func (o *orderable) Limit(lim int) Terminal {
	return limit(&o.terminal, lim)
}
