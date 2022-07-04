class DataPoint:

    def __init__(self, dimensions, values):
        self.neighbors = []
        self.dimensions = dimensions
        self.distances = []
        self.values = []
        self.isOutlier = False
        for i in range(dimensions):
            self.values.append(values[i])
