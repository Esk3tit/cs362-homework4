import unittest
import cube_volume


# Test Class inheriting from unittest.TestCase
class TestCubeVolume(unittest.TestCase):

    # Since there are only 3 required test cases, each one is its own function def
    def test_cube_negative(self):
        self.assertEqual(cube_volume.vol_cube(-3), -27)
        self.assertEqual(cube_volume.vol_cube(-1), -1)

    # Test out regular values or values that were expected to be used
    def test_cube_expected(self):
        self.assertEqual(cube_volume.vol_cube(4), 64)
        self.assertEqual(cube_volume.vol_cube(0), 0)

    # Test out possible type errors (floats, strings)
    # Type error on the string, test fails
    def test_cube_type(self):
        self.assertEqual(cube_volume.vol_cube(2.5), 15.625)
        self.assertEqual(cube_volume.vol_cube('5'), 125)


if __name__ == "__main__":
    unittest.main()
