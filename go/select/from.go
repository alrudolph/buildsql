package sel

type fromExpr struct {
	table string
}

func (f *fromExpr) Build() string {
	return "from " + f.table
}

type Fromable interface {
	Terminal
	From(table string) Joinable
}

type fromable struct {
	terminal
}

//nolint:ireturn
func from(f *terminal, table string) Joinable {
	f.add(&fromExpr{table: table})

	return &joinable{terminal: *f}
}

//nolint:ireturn
func (f *fromable) From(table string) Joinable {
	return from(&f.terminal, table)
}
