''' Circuitous (tm)                     # Name of the company is important
Advanced Circle Analytics Company       # Elevator Pitch -- Mission Statement
'''

import math
from collections import namedtuple
Version = namedtuple('Version', ['major', 'minor'])

class Circle(object):
    ''' Create a circle instance from a radius

        Part of an advanced circle analytics toolkit
    '''

    __slots__ = ['diameter']
    version = Version(0, 10)

    def __init__(self, radius):            # the docstring for the class is shown not the __init__
        self.radius = radius

    def area(self):
        'Compute area for circle'
        p = self.__perimeter()
        radius = p / 2.0 / math.pi
        return math.pi * (radius ** 2.0)

    def perimeter(self):
        'Compute the circumference for circle'
        return math.pi * self.radius * 2.0

    __perimeter = perimeter

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.radius)

    @staticmethod
    def angle_to_grade(angle):                      # Use case: to improve findability
        'Convert an inclinometer reading in degrees into a percent grade'
        return math.tan(math.radians(angle)) * 100

    @classmethod
    def from_bbd(cls, bbd):                         # Reprograms the dot to add cls as the first argument
        'Make a new circle from the bounding box diagonal'
        radius = bbd / math.sqrt(2.0) / 2.0
        return cls(radius)               

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0
