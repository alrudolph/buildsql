package buildsql

import "fmt"

type Buildable interface {
	Build() string
}

type S string

func (s S) Build() string {
	return string(s)
}

type Terminal interface {
	Buildable
}

type terminal struct {
	parts []Buildable
}

func NewTerminal() Terminal {
	return &terminal{
		parts: []Buildable{},
	}
}

func (t *terminal) add(part Buildable) {
	t.parts = append(t.parts, part)
}

func (t *terminal) Build() string {
	fmt.Println("\n\nBuilding SQL...")
	result := ""
	for _, part := range t.parts {
		result += part.Build()
		fmt.Println(">", result)
	}
	return result
}

type Limit interface {
	Buildable
}

type limitExpr struct {
	limit int
}

func (l *limitExpr) Build() string {
	return fmt.Sprintf(" limit %d", l.limit)
}

type Limitable interface {
	Buildable
	Limit(limit int) Terminal
}

type limitable struct {
	terminal
}

func (l *limitable) Limit(limit int) Terminal {
	l.add(&limitExpr{limit: limit})
	return &l.terminal
}

type Order interface {
	Buildable
}

type orderColumn struct {
	Column    string
	Direction *string
}

// this can't be sql.Col but like order.Col
// because we'll need sepearte col for select etc...

func Col(column string) orderColumn {
	return orderColumn{Column: column}
}

func Asc(column string) orderColumn {
	dir := "asc"
	return orderColumn{Column: column, Direction: &dir}
}

func Desc(column string) orderColumn {
	dir := "desc"
	return orderColumn{Column: column, Direction: &dir}
}

type orderExpr struct {
	columns []orderColumn
}

func (o *orderExpr) Build() string {
	result := " order by "

	for i, col := range o.columns {
		if i > 0 {
			result += ", "
		}

		result += col.Column

		if col.Direction != nil {
			result += " " + *col.Direction
		}
	}

	return result
}

type Orderable interface {
	Buildable
	Limitable
	Order(col orderColumn, cols ...orderColumn) Limitable
}

type orderable struct {
	limitable
	terminal
}

func (o *orderable) Order(col orderColumn, cols ...orderColumn) Limitable {
	o.add(&orderExpr{columns: append([]orderColumn{col}, cols...)})
	return &limitable{terminal: o.terminal}
}

func Query() Orderable {
	return &orderable{}
}
