#! /usr/bin/env python2.7

import urllib2, locale, time, functools
import xml.etree.ElementTree as ET

from contextlib import closing

def get_zestimate(zpid):
    with open('secrets') as f: ACCESS_TOKEN = f.read().strip()

    url = 'http://www.zillow.com/webservice/GetZestimate.htm?zws-id=%s&zpid=%s' % (ACCESS_TOKEN, zpid)
    with closing(urllib2.urlopen(url)) as url_f: response = url_f.read()

    value = 0
    e = ET.fromstring(response)
    for elem in e.findall('response'):
        for zestimate in elem.findall('zestimate'):
            value = int(zestimate[0].text)

    return value 

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')

    print "For today's date ", time.strftime("%m/%d/%Y")
    with open('data') as data: houses = dict([line.strip().split(':') for line in data])
    values = sorted([(name, get_zestimate(zpid)) for (name, zpid) in houses.items()], key=lambda tup: tup[1])
    for (name, value) in values:
        print "Zestimate for %20s's house is: %15s" % (name, locale.currency(value, grouping=True))
