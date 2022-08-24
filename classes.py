class DataPoint:

    def __init__(self, dimensions, values):
        self.neighbors = []
        self.dimensions = dimensions
        self.distances = []
        self.values = []
        self.isOutlier = False
        for i in range(dimensions):
            self.values.append(values[i])
        self.score = 0
        self.bin_x = 0
        self.bin_y = 0


class Bin:

    def __init__(self):
        self.points = []
        self.height = 0


class Histogram:
    def __init__(self):
        self.bins = []

