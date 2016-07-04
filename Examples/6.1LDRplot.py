import serial

import matplotlib.pyplot as plt
import matplotlib
import msvcrt


""""s = serial.Serial('COM3', 9600)  # check your arduino code baudrate

l = 100  # length
x = range(l)  # x axis
T = [240 for i in range(l)]  # initial temp value

plt.ion()
plt.show()

while True:
    t = int(s.readline().strip())
    T = T[1:]  # pop first value
    T.append(t)  # push at the end keeping list of same size

    plt.axis([0, l, min(T), max(T)])
    sid = plt.scatter(x, T, linewidth=0)
    plt.draw()
    sid.remove()"""

import os
import sys

cwd = os.getcwd()
(setpath, Examples) = os.path.split(cwd)
print setpath
sys.path.append(setpath)

from Arduino.Arduino import Arduino
from time import sleep


class LDR:
    def __init__(self, baudrate):
        self.baudrate = baudrate
        self.setup()
        self.run()
        self.exit()

    def setup(self):
        self.obj_arduino = Arduino()
        self.port = self.obj_arduino.locateport()
        self.obj_arduino.open_serial(1, self.port, self.baudrate)

    def run(self):
        self.ldr = 5

        l = 100  # length
        x = range(l)  # x axis
        T = [420 for i in range(l)]  # initial value
        for i in range(20):

            val = self.obj_arduino.cmd_analog_in(1, self.ldr)
            print val
            sleep(0.5)

            plt.ion()
            plt.show()
            if (msvcrt.kbhit()):
                plt.close()
                break


            t = int(val)
            T.pop(0) # pop first value
            T.append(t) # push at the end keeping list of same size
            plt.title("Reading LDR Data from Arduino...!")
            plt.grid(True)
            plt.ylabel('LDR Readings')
            plt.legend(loc='upper left')
            plt.axis([0, l, 0.55*min(T), 2*max(T)])
            plt.plot(x, T, linewidth=1)
            plt.draw()
            plt.pause(.0001)
            plt.clf()
        plt.close('all')





    def exit(self):
        self.obj_arduino.close_serial()


def main():
    obj_ldr = LDR(115200)


if __name__ == '__main__':
    main()
