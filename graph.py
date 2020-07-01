from csvReq import returnArray
import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime, timedelta
import locale

import numpy as np
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

def makeGraph():
    x = 1
    xValues = []
    xValuesLable = []
    yConf = []
    yDeath = []
    yRec = []
    yIncrease = [] #hier
    inc = 0 # hier
    val = returnArray()
    while x < len(val)+1:
        xValues.append(x)
        x += 1
    for i in val:
        xValuesLable.append(datetime(2020, int(i[4]), int(i[3])))

    for i in val:
        yConf.append(i[0])
        yDeath.append(i[1])
        yRec.append(i[2])

    yConf = list(map(int, yConf))
    yDeath = list(map(int, yDeath))
    yRec = list(map(int, yRec))

    x = 0
    for i in yConf:
        try:
            inc = i - x
            yIncrease.append(inc)
            x = i
        except:
            print("last Element reached")
            break
    #test ANFANG
    summe = 0
    for i in yIncrease:
        summe += i

    print("Anstieg:", yIncrease)
    print(len(yIncrease))
    print(len(xValues))
    print(summe)
    print(yConf[len(yConf)-1])
    #test ENDE

    # # Initialize the plot
    #
    # # or replace the three lines of code above by the following line:
    # # fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,10))
    #
    # # Plot the data
    # ax1.bar(xValues, yValues)

    #Verlaufsgraph
    fig, ax1 = plt.subplots()

    #log Scale Aktivieren
    # ax1.set_yscale('log')

    # fig = plt.figure(figsize=(20, 10))
    # ax1 = fig.add_subplot(121)

    ax1.plot(xValuesLable,yConf, label="Confirmed Cases" )
    ax1.plot(xValuesLable,yDeath, label="Confirmed Deaths" )
    ax1.plot(xValuesLable,yRec, label="Confirmed Recovered" )

    plt.gcf().autofmt_xdate()

    date_format = dates.DateFormatter('%d, %B, %Y')

    plt.gca().xaxis.set_major_formatter(date_format)

    plt.xlabel("Days")
    plt.ylabel("Humans")

    plt.legend()
    plt.grid(True)

    # plt.tick_params(axis='x', which='major', labelsize=10)
    plt.xticks(rotation=45)
    # ax1.set_xticklabels(xValuesLable)
    # print(xValuesLable)

    fig.tight_layout()

    plt.savefig('crd.png', bbox_inches='tight')

    #####################################################################

    #Anstiegsgraph
    fig2, ax2 = plt.subplots()

    ax2.bar(xValuesLable, yIncrease, label="Increase")

    plt.gcf().autofmt_xdate()

    date_format = dates.DateFormatter('%d, %B, %Y')

    plt.gca().xaxis.set_major_formatter(date_format)

    plt.xlabel("Days")
    plt.ylabel("Humans")

    plt.legend()
    plt.grid(True)

    plt.xticks(rotation=45)


    fig2.tight_layout()


    # plt.ylim(-.5, 1000)

    # Show the plot

    plt.savefig('inc.png', bbox_inches='tight')

    plt.show()

    #####################################################################

    #Ansteckungsrate pro Monat
    months = monthsInc = [0,0,0,0,0,0,0,0,0,0,0,0]

    for i in val:
        if(i[4] == 1):
            months[0] += 1
        elif(int(i[4]) == 2):
            months[1] += 1
        elif (int(i[4]) == 3):
            months[2] += 1
        elif (int(i[4]) == 4):
            months[3] += 1
        elif (int(i[4]) == 5):
            months[4] += 1
        elif (int(i[4]) == 6):
            months[5] += 1
        elif (int(i[4]) == 7):
            months[6] += 1
        elif (int(i[4]) == 8):
            months[7] += 1
        elif (int(i[4]) == 9):
            months[8] += 1
        elif (int(i[4]) == 10):
            months[9] += 1
        elif (int(i[4]) == 11):
            months[10] += 1
        else:
            months[11] += 1

    print("#############")
    print(months)
    print("#############")

    cnt = 0
    prev = 0
    for i in months:
        monthsInc[cnt] = sum(yIncrease[prev:prev+i])
        prev += i
        cnt +=1

    prozAnz = [(i / yConf[len(yConf)-1])*100 for i in monthsInc]


    print(monthsInc)
    print(sum(monthsInc))
    print(prozAnz)
    print(sum(prozAnz))
    test = [1 if i == 0 else 0.03 for i in monthsInc]
    print(test)
    print(sum(test))



    labels = ['Januar', 'Februar', 'März', 'April','Mai', 'Juni', 'Juli', 'August','September', 'Oktober', 'November', 'Dezember']
    plt.pie(monthsInc, labels=labels, explode=test,
            autopct='%1.2f%%', startangle=140)

    plt.axis('equal')
    plt.tight_layout()
    plt.show()


makeGraph()

# req = request()

# print(req)
