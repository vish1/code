#!/usr/bin/python
" Program to check the latest visa bulletin and get priority dates "
import urllib2, datetime
from bs4 import BeautifulSoup

search_text ="<tr><td>2nd</td>"
class_name = "visabulletinemploymenttable parbase employment_table_data"
months = [
        "october",
        "november",
        "december",
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september"
        ]

def get_page_data(url):
    conn = urllib2.urlopen(url)
    if conn.geturl() != url:
        return None
    return conn.read()

def extract_priority_date(page_data):
    page_soup = BeautifulSoup(page_data)
    table = page_soup.find_all("div",  class_=class_name)
    rows = table[0].find_all("tr")
    print "%10s" % (rows[2].find_all("td")[3].get_text())

def add_month(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    return datetime.date(year,month,1)

def get_bulletin_for_month(month, year):
    month = month.lower()
    year1 = str(int(year)+1)
    if month in months[:3]:
        year2 = year
    else:
        year2 = year1
    url = "http://travel.state.gov/content/visas/english/law-and-policy/bulletin/%s/visa-bulletin-for-%s-%s.html" % (year1, month, year2)
    print "%s %s, PD for EB2I is: " % (month, year2), 
    page_data = get_page_data(url)
    if page_data is not None:
        extract_priority_date(page_data)
    else:
        print "<Bulletin not available>"

def get_month_year(date):
    month = curr_month.strftime("%B")
    year = curr_month.strftime("%Y")
    return (month, year)


if __name__ == "__main__":
    curr_month = datetime.datetime.today()
    month = get_month_year(curr_month)

    print "Current month ",
    get_bulletin_for_month(month[0], month[1])

    next_month = add_month(curr_month, 1)
    month = get_month_year(next_month)

    print "Next month ",
    get_bulletin_for_month(month[0], month[1])

#    for year in range(2013, 2015):
#        for month in months:
