class WorkingGrid(object):

    def __init__(self, factor1_size, factor2_size):
        self.factor1_size = factor1_size
        self.factor2_size = factor2_size

    def lookup(self, row, column):
        """Given a zero-indexed row and column position, return the range of picture numbers that corresponded to that position in DFMM, as a tuple of (low, high)
        """
        # width should be factor1_size + factor2_size - 1
        width = self.factor1_size + self.factor2_size - 1
        low = 10 * width * row + 10 * column
        return (low, low + 9)