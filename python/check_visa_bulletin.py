#!/usr/bin/python
" Program to check the latest visa bulletin and get priority dates "
import urllib2, datetime, pprint, calendar, prettytable
from bs4 import BeautifulSoup
from contextlib import closing

class_name = "visabulletinemploymenttable parbase employment_table_data"
url_string = "http://travel.state.gov/content/visas/english/law-and-policy/bulletin/%s/visa-bulletin-for-%s-%s.html"

def get_bulletin_for_month(date=datetime.datetime.today()):
    month, calendar_year = (date.strftime("%B"), date.strftime("%Y"))
    visa_year = int(calendar_year)+1 if month in ['October', 'November', 'December'] else calendar_year
    url = url_string % (str(visa_year), month.lower(), calendar_year)
    with closing(urllib2.urlopen(url)) as conn:
        if conn.geturl() != url:
            return "NA" 
        page_data = conn.read()

    return datetime.datetime.strptime(\
            BeautifulSoup(page_data, "html.parser").\
            find_all("div", class_=class_name)[0].\
            find_all("tr")[2].\
            find_all("td")[3].\
            get_text(), '%d%b%y').strftime('%d %b %Y')

def dates_for_year(year):
    return [get_bulletin_for_month(datetime.date(year, month, 1)) for month in range(1, 13)]

if __name__ == "__main__":
    print "Current date is: ", datetime.datetime.today().strftime('%d %b %Y')
    print "Priority date for current month is: ", get_bulletin_for_month()
    today = datetime.datetime.today()
    next_month = get_bulletin_for_month(today)
    if next_month == "NA":
        print "Priority date for next month is not available"
        print "Possible release date for next bulletin is" 
    else:
        print "Priority date for next month is: ", next_month

    print "Priority dates for the past 3 years"
    table = prettytable.PrettyTable()
    table.add_column("Year", [calendar.month_name[month] for month in range(1, 13)])
    table.align['Year'] = "l"
    for past in reversed(range(3)):
        year = datetime.date.today().year - past 
        table.add_column(str(year), dates_for_year(year))
    print table 


