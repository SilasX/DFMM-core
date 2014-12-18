class WorkingGrid(object):

    def __init__(self, factor1_size, factor2_size):
        self.factor1_size = factor1_size
        self.factor2_size = factor2_size
        self.width = self.factor1_size + self.factor2_size - 1

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


class InvalidDigit(Exception):

    def __init__(self, digit):
        self.message = "Invalid digit {}; must be an integer \
            in range 0-9.".format(digit)
