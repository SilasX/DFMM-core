import math


class WorkingGrid(object):

    def __init__(self, factor1_size, factor2_size):
        self.factor1_size = factor1_size
        self.factor2_size = factor2_size
        self.width = self.factor1_size

    def lookup_range(self, row, column):
        """Given a zero-indexed row and column position, return the range of picture numbers that corresponded to that position in DFMM, as a tuple of (low, high)
        """
        # width should be factor1_size + factor2_size - 1
        if column > self.width:  # check too far to left
            return None
        if row > self.factor2_size - 1:  # check too far down
            return None
        low = self._offset(row, column)
        return (low, low + 9)

    def write_index(self, digit, row, column):
        """Given a digit in range 0-9 and a row/col, retun the index of
the picture to be looked at for writing
        """
        if type(digit) not in (int, long) or digit < 0 or digit > 9:
            raise InvalidDigit(digit)
        return self._offset(row, column) + digit

    def _offset(self, row, column):
        """Helper function for finding offset given row and column"""
        return row * 10 * self.width + column * 10


class FinalAnswer(object):

    @classmethod
    def from_int(cls, answer_val):
        """Factory method for setting up FinalAnswer object from integer;
decides size based on largest non-zero digit, so can't be used if you
want the target array answer to have leading zeroes (which appear at the
highest values of the array).
        """
        cur_array = []
        temp_val = answer_val
        size = int(math.floor(math.log10(answer_val))) + 1
        for x in range(size):
            cur_array.append(temp_val % 10)
            temp_val /= 10
        return cls(cur_array)

    def __init__(self, answer_arr):
        """Given array with final answer, `answer_arr`, set up the
attribute .answer_arr (where 0 index is ones place) along with size and
and initizaled array input by the user, .input_arr
the first item is the tens place, and so on."
        """
        self.answer_arr = answer_arr
        self.size = len(answer_arr)
        self.input_arr = [None] * self.size

    def write(self, val, index):
        """Set the value to `val` at `index`"""
        if self.input_arr[index] is not None:
            raise OverwriteAnswer(index)
        self.input_arr[index] = val

    def is_correct(self):
        return all(self.input_arr[i] == self.answer_arr[i]
                   for i, val in enumerate(self.answer_arr))


class InvalidDigit(Exception):

    def __init__(self, digit):
        self.message = "Invalid digit {}; must be an integer \
            in range 0-9.".format(digit)


class OverwriteAnswer(Exception):
    
    def __init__(self, index):
        self.message = "Tried to write answer in position {}, \
            which had already been written.".format(index)
