# -*- coding: utf-8 -*-


from serial import Serial
from serial.tools.list_ports import comports
from time import sleep

baudrate = 9600    #Choose a proper baudrate
p1=0               #Initial Position of servo motor 
p2=0               #Final Position of servo motor

def locateport():
    ports = list(comports())
    for i in ports:
        for j in i:
            if 'Arduino' in j:
                port = i[0]
    return port


def arduino_open(PortNo,baudrate):
    global ser
    ser = Serial(PortNo,baudrate)
    sleep(2)

def arduino_close():
    ser.close()

def digitalRead(x):
    a=''    
    if(x <10):
        a = '1'+'0'+str(x) 
    else:
        a = '1'+str(x)
        
    a = a +'0' +'0'+'0'+'1'      
    ser.write(a)    
    a = ser.readline()
    return(a)
    
def digitalWrite(x,y):
    a=''    
    if(x <10):
        a = '0'+'0'+str(x) 
    else:
        a = '0'+str(x) 
    a = a +'0'+'0'+str(y)+'1'      
    ser.write(a)


def analogWrite(x,y):
    a=''    
    if(x <10):
        a = '0'+'0'+str(x) 
    else:
        a = '0'+str(x)
        
    if(y>=100):
       a = a +str(y)+'0'      
       ser.write(a)
     
    elif(y>=10):
       a = a +'0'+str(y)+'0'      
       ser.write(a)

    elif(y<10):
       a = a +'0' +'0'+str(y)+'0'      
       ser.write(a)    
    
def analogRead(x):
    a=''    
    if(x <10):
        a = '1'+'0'+str(x) 
    else:
        a = '1'+str(x)
    a = a +'0' +'0'+'0'+'0'      
    ser.write(a)    
    c=ser.readline()
    return(c)
 
def rotateDCM(P1,P2,dirc):
    if(dirc=='CW'):
        digitalWrite(P1,1)
        sleep(1.1)
        digitalWrite(P2,0)
    elif(dirc=='CCW'):
        digitalWrite(P1,0)
        sleep(1.1)
        digitalWrite(P2,1)        
    elif(dirc=='ST'):
        digitalWrite(P1,0)
        sleep(1.1)
        digitalWrite(P2,0)
        
def servo(pin,pos):
    analogWrite(pin,pos)
