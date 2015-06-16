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




