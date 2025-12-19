package sel

type whereExpr struct {
	condition string
}

func (w *whereExpr) Build() string {
	return "where " + w.condition
}

type Whereable interface {
	GroupByable
	Where(condition string) GroupByable
}

type whereable struct {
	terminal
}

//nolint:ireturn
func where(w *terminal, condition string) GroupByable {
	w.add(&whereExpr{condition: condition})

	return &groupByable{terminal: *w}
}

//nolint:ireturn
func (w *whereable) Where(condition string) GroupByable {
	return where(&w.terminal, condition)
}

//nolint:ireturn
func (w *whereable) GroupBy(cols ...string) Orderable {
	return groupBy(&w.terminal, cols...)
}

//nolint:ireturn
func (w *whereable) OrderBy(col orderColumn, cols ...orderColumn) Limitable {
	return orderBy(&w.terminal, col, cols...)
}

//nolint:ireturn
func (w *whereable) Limit(lim int) Terminal {
	return limit(&w.terminal, lim)
}
