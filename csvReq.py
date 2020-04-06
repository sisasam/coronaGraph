# import urllib
# urllib.urlretrieve('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/04-04-2020.csv', 'csv.csv') as csvfile:


from urllib.request import urlopen
import csv
from pathlib import Path
month = 2
day = 1
maxday = 0
curday = 5
curmonth = 4
firstFlag = True
while month <= curmonth:
    if month == 3:
        maxday = 31
    elif month == 2:
        maxday = 29
    elif month == curmonth:
        maxday = curday

    while day <= maxday:
        if day < 10:
            curfile = "0"+str(month)+"-0"+str(day)+"-2020.csv"
            curfile = str(curfile)
        else:
            curfile = "0"+ str(month)+"-"+str(day)+"-2020.csv"
            curfile = str(curfile)
        file = Path(curfile)
        if not file.is_file():
            f = urlopen('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+curfile)
        f = str(f.read()).replace('\\r\\n','!').replace('\\n','!').split('!')
        for row in f:
            row = row.split(',')
            if len(row) > 1:
                if firstFlag:
                    print(row, day, month)
                firstFlag = False
                if row[3] == "Germany" or row[1] == "Germany":
                    print(row, day, month)
        day += 1
    month += 1
    day = 1



# spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# for row in spamreader:
#     print(', '.join(row))
