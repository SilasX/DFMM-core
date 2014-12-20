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

        expected3 = (30, 39)
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


class TestWorkingGridArbitrary(unittest.TestCase):

    def setUp(self):
        self.wg_obj = models.WorkingGrid(5, 3)

    def test_position_to_range_within_grid(self):
        expected1 = (60, 69)
        actual1 = self.wg_obj.lookup_range(1, 1)
        self.assertEqual(expected1, actual1)


class TestFinalAnswer(unittest.TestCase):

    def setUp(self):
        self.fa_obj = models.FinalAnswer([5, 4, 3, 0, 1])

    def test_check_is_correct(self):
        self.fa_obj.write(5, 0)
        self.assertFalse(self.fa_obj.is_correct())

    def test_cant_overwrite_answer(self):
        with self.assertRaises(models.OverwriteAnswer) as cm:
            self.fa_obj.write(4, 3)
            self.fa_obj.write(9, 3)


class TestProblem(unittest.TestCase):

    def test_work_through_prob1(self):
        # 386 * 27 = 9126
        prob = models.Problem(386, 27)
        expected_width = 3
        actual_width = prob.working_grid.width
        self.assertEqual(expected_width, actual_width)

        expected_ans_array = [2, 2, 4, 0, 1]
        actual_ans_array = prob.final_answer.answer_arr
        self.assertEqual(expected_ans_array, actual_ans_array)

    def test_work_through_prob2(self):
        # 54 * 199 = 10746
        prob = models.Problem(54, 199)
        expected_width = 2
        actual_width = prob.working_grid.width
        self.assertEqual(expected_width, actual_width)

        expected_ans_array = [6, 4, 7, 0, 1]
        actual_ans_array = prob.final_answer.answer_arr
        self.assertEqual(expected_ans_array, actual_ans_array)


if __name__ == "__main__":
    unittest.main()
