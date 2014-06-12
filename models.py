class WorkingGrid(object):

    def __init__(self, factor1_size, factor2_size):
        self.factor1_size = factor1_size
        self.factor2_size = factor2_size

    def lookup(self, row, column):
        """Given a zero-indexed row and column position, return the range of picture numbers that corresponded to that position in DFMM, as a tuple of (low, high)
        """
        low = 10 * column * (row + 1)
        return (low, low + 9)
