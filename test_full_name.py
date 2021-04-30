import unittest
import full_name


# Test Class inheriting from unittest.TestCase
class TestFullName(unittest.TestCase):

    # Since there are only 3 required test cases, each one is its own function def
    def test_empty_name(self):
        self.assertEqual(full_name.full_name("", ""), " ")

    # Test out regular values or values that were expected to be used
    def test_full_name_expected(self):
        self.assertEqual(full_name.full_name("John", "Doe"), "John Doe")
        self.assertEqual(full_name.full_name("Foo", "Bar"), "Foo Bar")

    # Test out non strings (integers, floats)
    # Type error from all cases in this function because of the attempt to concatenate
    # a space
    def test_non_string(self):
        self.assertEqual(full_name.full_name(3, "Smith"), "3 Smith")
        self.assertEqual(full_name.full_name(1.5, 1.5), 3)


if __name__ == "__main__":
    unittest.main()