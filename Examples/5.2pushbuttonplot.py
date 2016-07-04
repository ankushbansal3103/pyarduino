import os
import sys
import matplotlib.pyplot as plt
cwd=os.getcwd()
(setpath,Examples)=os.path.split(cwd)
print setpath
sys.path.append(setpath)

from Arduino.Arduino import Arduino
from time import sleep

class PUSHBUTTON_LED:

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
        self.blue=9
        self.green=10
        self.red=11
        self.pushbutton=12


        l = 10  # length
        x = range(l)  # x axis
        T = [0 for i in range(l)]  # initial value
        for i in range(20):
            val=self.obj_arduino.cmd_digital_in(1,self.pushbutton)
            #sleep(0.5)
            print val
            self.obj_arduino.cmd_digital_out(1,self.blue,val)
            sleep(0.5)


            plt.ion()
            #plt.show()

            t = int(val)
            T.pop(0)  # pop first value
            T.append(t)  # push at the end keeping list of same size
            plt.title("Is Pushbutton pressed ?")
            plt.grid(True)
            plt.ylabel('Pushbutton')
            plt.legend(loc='upper left')
            plt.axis([0, l, 0, 2])
            plt.scatter(x, T, linewidth=5)
            plt.draw()
            plt.pause(.0001)
            plt.clf()
        plt.close('all')


    def exit(self):
        self.obj_arduino.close_serial()

def main():
    obj_pushbutton=PUSHBUTTON_LED(115200)

if __name__=='__main__':
    main()
