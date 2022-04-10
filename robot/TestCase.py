class TestCase:

    def test_add_string_no_return(self, case: str, expected: str) -> None:
        """
        Check if function returns passed argument + "test" in the end
        Args:
            case: string to add "test" to
            expected: what string to expect on return
        """
        actual_result = str(case) + "test"
        assert actual_result == expected, f"Actual result: {actual_result} is not equal to expected: {expected}"

    def test_add_string_return(self, case: str) -> str:
        """
        Check if function returns passed argument + "test" in the end
        Args:
            case: string to add "test" to
        Returns:
            string = case + "test"
        """
        return case + "test"


print(TestCase.test_add_string_return.__doc__)