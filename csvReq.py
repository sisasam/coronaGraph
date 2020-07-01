from urllib.request import urlopen
import os
import datetime
from pandas import DataFrame, read_csv
import pandas as pd

def request():
    f = None
    now = datetime.datetime.now()
    month = 2
    day = 1
    maxday = 0
    curday = now.day
    curmonth = now.month
    dataArray = []
    array = []
    notFoundDay = None
    while month <= curmonth:
        print("-- fetching Data -- this might take a while -- ")
        print("currently fetching data for Month: "+ str(month))
        if month == 3:
            maxday = 31
        elif month == 2:
            maxday = 29
        elif month == 4:
            maxday = 30
        elif month == 5:
            maxday = 31
        elif month == 6:
            maxday = 30
        elif month == curmonth:
            maxday = curday

        while day <= maxday:
            if day < 10:
                curfile = "0" + str(month) + "-0" + str(day) + "-2020.csv"
                curfile = str(curfile)
            else:
                curfile = "0" + str(month) + "-" + str(day) + "-2020.csv"
                curfile = str(curfile)
            try:
                if month < 3 or month == 3 and day < 22:
                    f = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + curfile
                    df = pd.read_csv(f, usecols = [ "Country/Region" , "Confirmed" , "Deaths" , "Recovered"], sep=',')
                    res = df[df["Country/Region"] == "Germany"]
                else:
                    f = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + curfile
                    df = pd.read_csv(f, usecols=["Country_Region", "Confirmed", "Deaths", "Recovered"], sep=',')
                    res = df[df["Country_Region"] == "Germany"]
                print(res)
                totalc = 0
                totald = 0
                totalr = 0
                for i in res.values:
                    totalc = totalc + i[1]
                    totald = totald + i[2]
                    totalr = totalr + i[3]
                    print(i[1])
                print(totalc)
                array.extend((totalc, totald, totalr, day, month))
            except:
                print("No file for", f, "found")
                notFoundDay = True
            day += 1
            dataArray.append(array)
            array = []
        month += 1
        day = 1
    #Hier ist nur falls der letzte Tag nicht gefunden wird, wird das letzte Element gelöscht.
    #Eventuelle Verbesserung benötigt
    if notFoundDay:
        dataArray.pop(len(dataArray)-1)
    return dataArray


def makeFile(array):
    file = open("dataString", 'w')
    for item in array:
        for i in item:
            file.write("%s," %i)
        file.write("\n")


def checkFile(file):

    if os.path.isfile(file):
        return True
    else:
        return False


def returnArray():
    if not checkFile("dataString"):
        dataarray = request()
        makeFile(dataarray)
        return dataarray
    else:
        dataarray = []
        innerarray = []
        fh = open("dataString", "r")
        data = fh.read().split('\n')
        fh.close()
        for i in data:
            innerarray = i.split(',')
            innerarray.remove('')
            dataarray.append(innerarray)
        dataarray.remove([])
        return dataarray