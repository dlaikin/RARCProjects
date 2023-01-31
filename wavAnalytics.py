# Authors: Drew Laikin
# Using code from https://www.geeksforgeeks.org/plotting-various-sounds-on-graphs-using-python-and-matplotlib/
# For basic signal reading and plotting in showBasic()
import wave
import sys
import matplotlib.pyplot as plt
import numpy
#comment

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def showBasic(path: str):
    file = wave.open(path)
    signal = file.readframes(-1)
    signal = numpy.frombuffer(signal, dtype="int16")
    f_rate = file.getframerate()

    # to Plot the x-axis in seconds
    # you need get the frame rate
    # and divide by size of your signal
    # to create a Time Vector
    # spaced linearly with the size
    # of the audio file
    time = numpy.linspace(0, len(signal) / f_rate, num=len(signal))

    plt.figure(1)
    plt.title("Sound Wave")
    plt.xlabel("Time")
    plt.plot(time, signal)
    plt.show()


def showReduced(path: str):
    file = wave.open(path)
    signal = file.readframes(-1)
    signal = numpy.frombuffer(signal, dtype="int16")
    f_rate = file.getframerate()

    max = 0
    for index in signal:
        if index > max:
            max = index
    print(max)
    xVals = []
    yVals = []
    count = 0
    for index in signal:
        count += 1
        if index >= max*0.95 and index%max != 0:
            xVals.append(count)
            print(index%max)
            yVals.append(index%max)

    time = numpy.linspace(0, len(signal) / f_rate, num=len(signal))

    plt.figure(1)
    plt.title("Sound Wave")
    plt.xlabel("Time")
    plt.plot(xVals, yVals)
    plt.show()

# you can also save
# the plot using
# plt.savefig('filename')


if __name__ == "__main__":
    # gets the command line Value
    path = 'blip.wav'

    showReduced(path)
