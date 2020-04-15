from csvReq import returnArray
import matplotlib.pyplot as plt
import numpy as np


def makeGraph():
    x = 1
    xValues = []
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
            print("lasr Element reached")
            break

    print("Anstieg:", yIncrease)
    print(len(yIncrease))
    print(len(xValues))

    # # Initialize the plot
    #
    # # or replace the three lines of code above by the following line:
    # # fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,10))
    #
    # # Plot the data
    # ax1.bar(xValues, yValues)

    #Verlaufsgraph
    fig, ax1 = plt.subplots()

    ax1.set_yscale('log')

    # fig = plt.figure(figsize=(20, 10))
    # ax1 = fig.add_subplot(121)

    ax1.plot(xValues,yConf, label="Confirmed Cases" )
    ax1.plot(xValues,yDeath, label="Confirmed Deaths" )
    ax1.plot(xValues,yRec, label="Confirmed Recovered" )

    plt.xlabel("Days")
    plt.ylabel("Humans in 'log' scale")

    plt.legend()
    plt.grid(True)

    fig.tight_layout()

    #####################################################################

    #Anstiegsgraph
    fig2, ax2 = plt.subplots()

    ax2.bar(xValues, yIncrease, label="Increase")

    plt.xlabel("Days")
    plt.ylabel("Humans")

    plt.legend()
    plt.grid(True)

    fig2.tight_layout()


    # plt.ylim(-.5, 1000)

    # Show the plot
    plt.show()

makeGraph()

# req = request()

# print(req)
