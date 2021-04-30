import unittest
import avg_list_elem


# Test Class inheriting from unittest.TestCase
class TestAvgListElement(unittest.TestCase):

    # Since there are only 3 required test cases, each one is its own function def
    def test_empty_list(self):
        self.assertEqual(avg_list_elem.avg_elements([]), 0)

    # Test out regular values or values that were expected to be used
    def test_avg_list_expected(self):
        self.assertEqual(avg_list_elem.avg_elements([1, 2, 3]), 2)
        self.assertEqual(avg_list_elem.avg_elements([5, 7, 9, 4]), 6.25)

    # Test out possible type errors (floats, strings)
    # Type error on the list with strings, test fails
    def test_mixed_list(self):
        self.assertEqual(avg_list_elem.avg_elements([-1, 3.5, 7.25, 10]), 4.9375)
        self.assertEqual(avg_list_elem.avg_elements([1, 2, 3, '4', 'String']), 2)


if __name__ == "__main__":
    unittest.main()