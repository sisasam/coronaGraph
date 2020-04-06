# import urllib
# urllib.urlretrieve('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/04-04-2020.csv', 'csv.csv') as csvfile:


import wget
import csv
from pathlib import Path
month = 2
day = 1
maxday = 0
curday = 5
firstFlag = True
while month <= 4:
    if month == 3:
        maxday = 31
    elif month == 2:
        maxday = 29
    elif month == 4:
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
            csvfile = wget.download('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+curfile)
        try:
            with open(curfile, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if firstFlag:
                        print(row)
                    firstFlag = False
                    if row[3] == "Germany" or row[1] == "Germany":
                        print(row)
        except:
            print("file does not exist")
        day += 1
    month += 1
    day = 1



# spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# for row in spamreader:
#     print(', '.join(row))
