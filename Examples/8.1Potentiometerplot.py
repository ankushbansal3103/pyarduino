import os
import sys
import matplotlib.pyplot as plt

cwd=os.getcwd()
(setpath,Examples)=os.path.split(cwd)
print setpath
sys.path.append(setpath)

from Arduino.Arduino import Arduino
from time import sleep

class POT:
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
        self.pot=2
        self.blue=9
        self.green=10
        self.red=11


        l = 100  # length
        x = range(l)  # x axis
        T = [420 for i in range(l)]  # initial value


        for i in range(35):
            val=self.obj_arduino.cmd_analog_in(1,self.pot)
            print val

            if (int(val) >= 0 and int(val)< 320):
                self.obj_arduino.cmd_digital_out(1,self.blue,1)
                sleep(.25)
                self.obj_arduino.cmd_digital_out(1,self.blue,0)
            elif (int(val) >= 320 and int(val) < 900):
                self.obj_arduino.cmd_digital_out(1,self.green,1)
                sleep(.25)
                self.obj_arduino.cmd_digital_out(1,self.green,0)
            else:
                self.obj_arduino.cmd_digital_out(1,self.red,1)
                sleep(.25)
                self.obj_arduino.cmd_digital_out(1,self.red,0)


            plt.ion()
            plt.show()

            t = int(val)
            T.pop(0)  # pop first value
            T.append(t)  # push at the end keeping list of same size
            plt.title("Reading Potentiometer from Arduino...!")
            plt.grid(True)
            plt.yticks([0,100,200,300,400,500,600,700,800,900,1000,1100])
            plt.xticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
            plt.ylabel('Potentiometer Readings')
            plt.legend(loc='upper left')
            plt.axis([0, l, 0.55 * min(T), 1.2 * max(T)])
            plt.plot(x, T, linewidth=1)
            plt.draw()
            plt.pause(.0001)
            plt.clf()
        


    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_pot=POT(115200)

if __name__=='__main__':
    main()
