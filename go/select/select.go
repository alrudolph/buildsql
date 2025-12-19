package sel

import (
	"strings"
)

type selectExpr struct {
	columns []string
}

func (s *selectExpr) Build() string {
	return "select " + strings.Join(s.columns, ", ")
}

type Selectable struct{}

//nolint:ireturn
func (s *Selectable) Select(cols ...string) Fromable {
	t := terminal{parts: []Buildable{}}
	t.add(&selectExpr{columns: cols})

	return &fromable{terminal: t}
}
