import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import*
import time

tempC = []
pressure = []
height = []
arduinoData = serial.Serial("/dev/ttyACM0", 115200)
plt.ion()
count = 0

def makePlot():
    plt.ylim(0,3)
    plt.title("Altitude Sensor")
    plt.grid(True)
    plt.ylabel("Height in meter")
    plt.plot(height, 'b^-',label= "Height")
    plt.legend(loc="upper left")
    pltp=plt.twinx()
    plt.ylim(25,35)
    pltp.set_ylabel("Temp-C")
    pltp.plot(tempC, 'ro-', label="Temp-C")
    pltp.legend(loc="upper right")
    
tempBucket = 0
pBucket = 0


print ("Place Sensor on ground for calibration")
print ("5")
time.sleep(1)
print ("4")
time.sleep(1)
print ("3")
time.sleep(1)
print ("2")
time.sleep(1)
print ("1")
time.sleep(1)
print("Claibrating initialized.....")


for i in np.arange(1,11,1):

    while (arduinoData.inWaiting()==0):
        pass

    arduinoString = arduinoData.readline()
    dataArray = arduinoString.decode().split(" , ")
    temp = float(dataArray[0])
    ph = float(dataArray[1])
    
    tempBucket=tempBucket+temp
    pBucket = pBucket+ ph

P0=pBucket/10
tempK= ((tempBucket/10)+273.15)


while True:
    while (arduinoData.inWaiting()==0):
        pass

    arduinoString = arduinoData.readline()
    dataArray = arduinoString.decode().split(" , ")
    temp = float(dataArray[0])
    ph = float(dataArray[1]) 

    h=(29.2714639*tempK*(np.log(P0/ph)))
    
    height.append(h)
    tempC.append(temp)
    pressure.append(ph)
    drawnow (makePlot)
    plt.pause(0.000001)
    count = count+1
    print("height= ",h, " , Temp = ", temp)
    

    if count>50:
        tempC.pop(0)
        height.pop(0)