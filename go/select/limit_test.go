package sel_test

import (
	"testing"

	sel "github.com/alrudolph/buildsql/go/select"
)

func TestLimit(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name     string
		builder  string
		expected string
	}{
		{
			name:     "simple",
			builder:  testingNewSelect().Select("1").From("users").Limit(10).Build(),
			expected: "select 1 from users limit 10",
		},
		{
			name: "after where",
			builder: testingNewSelect().
				Select("1").
				From("users").
				Where("some-condition").
				Limit(5).
				Build(),
			expected: "select 1 from users where some-condition limit 5",
		},
		{
			name: "after join",
			builder: testingNewSelect().
				Select("1").
				From("users").
				Join("inner", "inner_table", "match").
				Limit(20).
				Build(),
			expected: "select 1 from users inner join inner_table on match limit 20",
		},
		{
			name: "after group by",
			builder: testingNewSelect().
				Select("1").
				From("users").
				GroupBy("some-column").
				Limit(15).
				Build(),
			expected: "select 1 from users group by some-column limit 15",
		},
		{
			name: "after order by",
			builder: testingNewSelect().
				Select("1").
				From("users").
				OrderBy(sel.Asc("some-column")).
				Limit(25).
				Build(),
			expected: "select 1 from users order by some-column asc limit 25",
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
