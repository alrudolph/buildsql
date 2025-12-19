package sel_test

import "testing"

func TestFrom(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name     string
		builder  string
		expected string
	}{
		{
			name:     "simple",
			builder:  testingNewSelect().Select("col_a").From("users").Build(),
			expected: "select col_a from users",
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
