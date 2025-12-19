package sel_test

import (
	"testing"

	sel "github.com/alrudolph/buildsql/go/select"
)

func TestOrderBy(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name     string
		builder  string
		expected string
	}{
		{
			name: "simple",
			builder: testingNewSelect().Select("1").
				From("users").
				OrderBy(sel.Asc("some-column"), sel.Desc("other-column")).
				Build(),
			expected: "select 1 from users order by some-column asc, other-column desc",
		},
		{
			name: "after where",
			builder: testingNewSelect().
				Select("1").
				From("users").
				Where("some-condition").
				OrderBy(sel.Asc("some-column"), sel.Desc("other-column")).
				Build(),
			expected: "select 1 from users where some-condition order by some-column asc, other-column desc",
		},
		{
			name: "after join",
			builder: testingNewSelect().
				Select("1").
				From("users").
				InnerJoin("inner_table", "match").
				OrderBy(sel.Asc("some-column"), sel.Desc("other-column")).
				Build(),
			expected: "select 1 from users inner join inner_table on match order by some-column asc, other-column desc",
		},
		{
			name: "after group by",
			builder: testingNewSelect().
				Select("1").
				From("users").
				GroupBy("some-column").
				OrderBy(sel.Asc("some-column"), sel.Desc("other-column")).
				Build(),
			expected: "select 1 from users group by some-column order by some-column asc, other-column desc",
		},
	}

	for _, testCase := range tests {
		t.Run(testCase.name, func(t *testing.T) {
			t.Parallel()

			if testCase.builder == testCase.expected {
				return
			}

			t.Fatalf("got %q, want %q", testCase.builder, testCase.expected)
		})
	}
}
