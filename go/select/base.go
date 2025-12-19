package sel

import "strings"

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
	return &terminal{parts: []Buildable{}}
}

func (t *terminal) Build() string {
	built := []string{}

	for _, part := range t.parts {
		built = append(built, part.Build())
	}

	return strings.Join(built, " ")
}

func (t *terminal) add(part Buildable) {
	t.parts = append(t.parts, part)
}
