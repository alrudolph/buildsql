package sel

import "fmt"

type Limit interface {
	Buildable
}

type limitExpr struct {
	limit int
}

func (l *limitExpr) Build() string {
	return fmt.Sprintf("limit %d", l.limit)
}

type Limitable interface {
	Buildable
	Limit(limit int) Terminal
}

type limitable struct {
	terminal
}

//nolint:ireturn
func limit(l *terminal, limit int) Limitable {
	l.add(&limitExpr{limit: limit})

	return &limitable{terminal: *l}
}

//nolint:ireturn
func (l *limitable) Limit(lim int) Terminal {
	return limit(&l.terminal, lim)
}
