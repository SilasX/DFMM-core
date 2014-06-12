import unittest

import models


class TestWorkingGrid(unittest.TestCase):

    def setUp(self):
        self.wg_obj = models.WorkingGrid(3, 2)

    def test_position_to_range_within_grid(self):
        expected1 = (0, 9)
        actual1 = self.wg_obj.lookup(0, 0)
        self.assertEqual(expected1, actual1)

        expected2 = (10, 19)
        actual2 = self.wg_obj.lookup(0, 1)
        self.assertEqual(expected2, actual2)

        expected3 = (40, 49)
        actual3 = self.wg_obj.lookup(1, 0)
        self.assertEqual(expected3, actual3)

    def test_position_to_range_invalid(self):
        expected1 = None
        actual1 = self.wg_obj.lookup(1, 5)
        self.assertEqual(expected1, actual1)

        expected2 = None
        actual2 = self.wg_obj.lookup(2, 3)
        self.assertEqual(expected2, actual2)


if __name__ == "__main__":
    unittest.main()
