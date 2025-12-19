package sel_test

import "testing"

func TestJoin(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name     string
		builder  string
		expected string
	}{
		{
			name: "left join",
			builder: testingNewSelect().Select("1").
				From("users").
				LeftJoin("left_table", "match").
				Build(),
			expected: "select 1 from users left join left_table on match",
		},
		{
			name: "right join",
			builder: testingNewSelect().Select("1").
				From("users").
				RightJoin("right_table", "match").
				Build(),
			expected: "select 1 from users right join right_table on match",
		},
		{
			name: "inner join",
			builder: testingNewSelect().Select("1").
				From("users").
				InnerJoin("inner_table", "match").
				Build(),
			expected: "select 1 from users inner join inner_table on match",
		},
		{
			name: "custom join",
			builder: testingNewSelect().Select("1").
				From("users").
				Join("custom", "custom_table", "match").
				Build(),
			expected: "select 1 from users custom join custom_table on match",
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
