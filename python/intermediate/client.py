from __future__ import division
from circuitous import Circle

c = Circle(10)
print u'Tutorial for Circuitous\N{trade mark sign}'
print 'Version %d.%d'% Circle.version
print 'A circle with a radius of', c.radius
print 'has an area of', c.area()
print


## Academic Friends ####

from random import random, seed
from pprint import pprint

jenny = 8675309
n = 10
print 'DARPA Grant Proposal to compute the average area of random circles'
print 'Proof of concept with %d randomly chosen circles' % n
print "Seeded with Jenny's number:", jenny
seed(jenny)
circles = [Circle(random()) for i in xrange(n)]
areas = [c.area() for c in circles]
average_area = sum(areas) / n
print 'The average area is %.1f' % average_area
print

## Rubber Sheet #######

print 'Rubber sheet cut template spec sheet'
cut_template = [0.1, 0.2, 0.7]
print 'Template:', cut_template
circles = [Circle(cut_radius) for cut_radius in cut_template]
for circle in circles:
    print 'A rubber circle with a cut radius of', circle.radius
    print 'has a perimeter of', circle.perimeter()
    print 'and a cold area of', circle.area()
    circle.radius *= 1.1
    print 'and a warm area of', circle.area()
    print 

## National Tire Change ######

class Tire(Circle):
    'A variant of a circle that tracks inner radius and area, but outer perimeter'

    RUBBER_RATIO = 1.25

    def perimeter(self):
        'Odometer correct perimeter that accounts for the rubber on tire'
        # Overriding -- don't call the parent method
        # Extending -- call the parent method and then modify it's result
        return Circle.perimeter(self) * self.RUBBER_RATIO

    __perimeter = perimeter

t = Tire(30)
print 'A tire with an inner radius of', t.radius
print 'and inner area of', t.area()
print 'and an outer perimeter of', t.perimeter()
print

## National Trucking Company #####

print u'A 5\N{DEGREE SIGN} degree inclinometer reading',
print 'is %.1f%% grade' % Circle.angle_to_grade(5)
print 

## National Graphic Company #########

c = Circle.from_bbd(40)
print 'A circle with a bounding box diagonal of 40'
print 'has a perimeter of', c.perimeter()
print 'and a radius of', c.radius
print 'and an area of', c.area()
print


## US Government ###########

# ISO 10111: All circle software SHALL NOT access the radius directly.
# It MUST call perimeter() and infer the radius indirectly



