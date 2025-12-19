package sel_test

import "testing"

func TestGroupBy(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name     string
		builder  string
		expected string
	}{
		{
			name:     "simple",
			builder:  testingNewSelect().Select("1").From("users").GroupBy("some-column").Build(),
			expected: "select 1 from users group by some-column",
		},
		{
			name: "after where",
			builder: testingNewSelect().
				Select("1").
				From("users").
				Where("some-condition").
				GroupBy("some-column").
				Build(),
			expected: "select 1 from users where some-condition group by some-column",
		},
		{
			name: "after join",
			builder: testingNewSelect().
				Select("1").
				From("users").
				InnerJoin("inner_table", "match").
				GroupBy("some-column").
				Build(),
			expected: "select 1 from users inner join inner_table on match group by some-column",
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
