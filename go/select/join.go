package sel

import "fmt"

type joinExpr struct {
	joinType string
	table    string
	on       string
}

func (j *joinExpr) Build() string {
	return fmt.Sprintf("%s join %s on %s", j.joinType, j.table, j.on)
}

type Joinable interface {
	Whereable
	LeftJoin(table string, on string) Joinable
	RightJoin(table string, on string) Joinable
	InnerJoin(table string, on string) Joinable
	Join(joinType string, table string, on string) Joinable
}

type joinable struct {
	terminal
}

//nolint:ireturn
func join(j *terminal, joinType string, table string, on string) Joinable {
	j.add(&joinExpr{joinType: joinType, table: table, on: on})

	return &joinable{terminal: *j}
}

//nolint:ireturn
func (j *joinable) LeftJoin(table string, on string) Joinable {
	return j.Join("left", table, on)
}

//nolint:ireturn
func (j *joinable) RightJoin(table string, on string) Joinable {
	return j.Join("right", table, on)
}

//nolint:ireturn
func (j *joinable) InnerJoin(table string, on string) Joinable {
	return j.Join("inner", table, on)
}

//nolint:ireturn
func (j *joinable) Join(joinType string, table string, on string) Joinable {
	return join(&j.terminal, joinType, table, on)
}

//nolint:ireturn
func (j *joinable) Where(condition string) GroupByable {
	return where(&j.terminal, condition)
}

//nolint:ireturn
func (j *joinable) GroupBy(cols ...string) Orderable {
	return groupBy(&j.terminal, cols...)
}

//nolint:ireturn
func (j *joinable) OrderBy(col orderColumn, cols ...orderColumn) Limitable {
	return orderBy(&j.terminal, col, cols...)
}

//nolint:ireturn
func (j *joinable) Limit(lim int) Terminal {
	return limit(&j.terminal, lim)
}
