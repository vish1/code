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

    version = Version(0, 4)

    def __init__(self, radius):            # the docstring for the class is shown not the __init__
        self.radius = radius

    def area(self):
        'Compute area for circle'
        return math.pi * (self.radius ** 2.0)

    def perimeter(self):
        'Compute the circumference for circle'
        return math.pi * self.radius * 2.0

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.radius)
   
    def angle_to_grade(angle):                      # Use case: to improve findability
        'Convert an inclinometer reading in degrees into a percent grade'
        return math.tan(math.radians(angle)) * 100

    angle_to_grade = staticmethod(angle_to_grade)   # reprograms the dot to NOT add self as the first argument
