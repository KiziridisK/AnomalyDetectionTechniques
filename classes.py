# Class.py file contains all the needed Classes for the project

# DataPoint Class. The base class for defining a data point
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


# Bin class is a structural class for the HBOS statistical method. It is used as a base class for Histogram class
class Bin:

    def __init__(self):
        self.points = []
        self.height = 0


# Histogram class. It defines the components of a Histogram for use in the HBOS method.
class Histogram:
    def __init__(self):
        self.bins = []


# TimeObj class. It defines the time for use in time series anomaly detection.
class TimeObj:
    def __init__(self, h, m):
        self.hour = h
        self.minute = m
