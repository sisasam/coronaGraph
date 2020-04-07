from csvReq import returnArray
import matplotlib.pyplot as plt
import numpy as np


def plot():
    x = 1
    xValues = []
    yValues = []
    val = returnArray()
    while x < len(val)+1:
        xValues.append(x)
        x += 1
    print(xValues)

    for i in val:
        yValues.append(i[1])

    # Initialize the plot
    fig = plt.figure(figsize=(20, 10))
    ax1 = fig.add_subplot(121)

    # or replace the three lines of code above by the following line:
    # fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,10))

    # Plot the data
    ax1.bar(xValues, yValues)

    # Show the plot
    plt.show()

plot()

# req = request()

# print(req)
