class SparseArray:

    def __init__(self, arr, size):
        self.size = size
        self.map = {}

        orig_arr_size = len(arr)
        for i, e in enumerate(arr):
            if i >= orig_arr_size:
                break
            if e != 0:
                map[i] = e

    def check_bounds(self, i):
        if i < 0 or i >= self.size:
            raise IndexError()

    def set(self, i, val):
        self.check_bounds(i)
        self.map[i] = val

    def get(self, i):
        self.check_bounds(i)
        v = self.map.get(i)
        if v is None:
            return 0
        return v
