package sel

import (
	"strings"
)

type groupByExpr struct {
	columns []string
}

func (g *groupByExpr) Build() string {
	return "group by " + strings.Join(g.columns, ", ")
}

type GroupByable interface {
	Orderable
	GroupBy(cols ...string) Orderable
}

type groupByable struct {
	terminal
}

//nolint:ireturn
func groupBy(g *terminal, cols ...string) Orderable {
	g.add(&groupByExpr{columns: cols})

	return &orderable{terminal: *g}
}

//nolint:ireturn
func (g *groupByable) GroupBy(cols ...string) Orderable {
	return groupBy(&g.terminal, cols...)
}

//nolint:ireturn
func (g *groupByable) OrderBy(col orderColumn, cols ...orderColumn) Limitable {
	return orderBy(&g.terminal, col, cols...)
}

//nolint:ireturn
func (g *groupByable) Limit(lim int) Terminal {
	return limit(&g.terminal, lim)
}
