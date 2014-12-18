import unittest

import models


class TestWorkingGrid(unittest.TestCase):

    def setUp(self):
        self.wg_obj = models.WorkingGrid(3, 2)

    def test_position_to_range_within_grid(self):
        expected1 = (0, 9)
        actual1 = self.wg_obj.lookup_range(0, 0)
        self.assertEqual(expected1, actual1)

        expected2 = (10, 19)
        actual2 = self.wg_obj.lookup_range(0, 1)
        self.assertEqual(expected2, actual2)

        expected3 = (40, 49)
        actual3 = self.wg_obj.lookup_range(1, 0)
        self.assertEqual(expected3, actual3)

    def test_position_to_range_invalid(self):
        expected1 = None
        actual1 = self.wg_obj.lookup_range(1, 5)
        self.assertEqual(expected1, actual1)

        expected2 = None
        actual2 = self.wg_obj.lookup_range(2, 3)
        self.assertEqual(expected2, actual2)

    def test_write_picture(self):
        expected1 = 12
        actual1 = self.wg_obj.write_index(2, 0, 1)
        self.assertEqual(expected1, actual1)

    def test_write_picture_invalid(self):
        for digit in [10, -1, "a"]:
            with self.assertRaises(models.InvalidDigit) as cm:
                self.wg_obj.write_index(digit, 1, 2)


if __name__ == "__main__":
    unittest.main()
