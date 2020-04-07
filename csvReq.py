from urllib.request import urlopen
import os


def request():
    month = 2
    day = 1
    maxday = 0
    curday = 5
    curmonth = 4
    dataArray = []
    array = []
    while month <= curmonth:
        print("-- fetching Data -- this might take a while -- ")
        print("currently fetching data for Month: "+ str(month))
        if month == 3:
            maxday = 31
        elif month == 2:
            maxday = 29
        elif month == curmonth:
            maxday = curday

        while day <= maxday:
            if day < 10:
                curfile = "0" + str(month) + "-0" + str(day) + "-2020.csv"
                curfile = str(curfile)
            else:
                curfile = "0" + str(month) + "-" + str(day) + "-2020.csv"
                curfile = str(curfile)
            f = urlopen(
                'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + curfile)
            f = str(f.read()).replace('\\r\\n', '!').replace('\\n', '!').split('!')
            for row in f:
                row = row.split(',')
                if len(row) > 1:
                    if row[3] == "Germany" or row[1] == "Germany":
                        if len(row) > 8:
                            i = 7
                            while i < 10:
                                array.append(row[i])
                                i += 1
                        else:
                            i = 3
                            while i < 6:
                                array.append(row[i])
                                i += 1
                        array.append(day)
                        array.append(month)
            day += 1
            dataArray.append(array)
            array = []
        month += 1
        day = 1
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