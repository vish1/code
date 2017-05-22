#! /usr/bin/env python2.7
import urllib2, locale, time, functools, os
import xml.etree.ElementTree as ET
from contextlib import closing

zillow_dir = os.path.join(os.path.expanduser('~'),'.zillow')

def get_zestimate(zpid, ACCESS_TOKEN):

    url = 'http://www.zillow.com/webservice/GetZestimate.htm?zws-id=%s&zpid=%s' % (ACCESS_TOKEN, zpid)
    with closing(urllib2.urlopen(url)) as url_f: response = url_f.read()

    e = ET.fromstring(response)
    for elem in e.findall('response'): 
        for zestimate in elem.findall('zestimate'): 
            value = int(zestimate[0].text)

    return (value if 'value' in locals() else 0)

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    with open(os.path.join(zillow_dir, 'zillow-api-key')) as f: ACCESS_TOKEN = f.read().strip()

    print "For today's date ", time.strftime("%m/%d/%Y")
    with open(os.path.join(zillow_dir, 'friends-data')) as data: houses = dict((a, (b,c,d)) for a,b,c,d  in [line.strip().split(':') for line in data])
    values = sorted([(name, get_zestimate(zpid, ACCESS_TOKEN), sold_price, year) for (name, (zpid, sold_price, year)) in houses.items()], key=lambda tup: tup[1])
    for (name, value, sold_price, year) in values:
        print "Zestimate for %20s's house is: %15s, bought for: %15s, increased %15s in %d years" % (name, "Renting" if value == 0 else locale.currency(value, grouping=True), locale.currency(int(sold_price), grouping=True), locale.currency(int(value)-int(sold_price), grouping=True), 2017 - int(year))
