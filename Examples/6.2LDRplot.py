import os
import msvcrt
import sys
import matplotlib.pyplot as plt
cwd=os.getcwd()
(setpath,Examples)=os.path.split(cwd)
print setpath
sys.path.append(setpath)

from Arduino.Arduino import Arduino
from time import sleep

class LDR:
    def __init__(self,baudrate):
        self.baudrate=baudrate
        self.setup()
        self.run()
        self.exit()

    def setup(self):
        self.obj_arduino=Arduino()
        self.port=self.obj_arduino.locateport()
        self.obj_arduino.open_serial(1,self.port,self.baudrate)

    def run(self):
        self.ldr=5
        self.blue=9
        self.green=10
        self.red=11

        l = 100  # length
        x = range(l)  # x axis
        T = [420 for i in range(l)]  # initial value

        for i in range(20):
            val=self.obj_arduino.cmd_analog_in(1,self.ldr)
            print val
            if int(val) < 300:
                self.obj_arduino.cmd_digital_out(1,self.blue,1)
            else:
                self.obj_arduino.cmd_digital_out(1,self.blue,0)
            sleep(0.5)

            plt.ion()
            #plt.show()

            t = int(val)
            T.pop(0)  # pop first value
            T.append(t)  # push at the end keeping list of same size
            plt.title("Reading LDR Data from Arduino...!")
            plt.grid(True)
            plt.ylabel('LDR Readings')
            plt.legend(loc='upper left')
            plt.axis([0, l, 0.55 * min(T), 2 * max(T)])
            plt.plot(x, T ,linewidth=1)
            plt.draw()
            plt.pause(.0001)
            plt.clf()
        plt.close('all')


    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_ldr=LDR(115200)

if __name__=='__main__':
    main()
