import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)


x1 = 2
x2 = 3
x3 = 4
x4 = 17
x5 = 18
x6 = 27
x7 = 22
x8 = 23

y1 = 10
y2 = 9
y3 = 11
y4 = 25
y5 = 5
y6 = 6
y7 = 13
y8 = 19


GPIO.setup(x1,GPIO.OUT)
GPIO.setup(x2,GPIO.OUT)
GPIO.setup(x3,GPIO.OUT)
GPIO.setup(x4,GPIO.OUT)
GPIO.setup(x5,GPIO.OUT)
GPIO.setup(x6,GPIO.OUT)
GPIO.setup(x7,GPIO.OUT)
GPIO.setup(x8,GPIO.OUT)

GPIO.setup(y1,GPIO.OUT)
GPIO.setup(y2,GPIO.OUT)
GPIO.setup(y3,GPIO.OUT)
GPIO.setup(y4,GPIO.OUT)
GPIO.setup(y5,GPIO.OUT)
GPIO.setup(y6,GPIO.OUT)
GPIO.setup(y7,GPIO.OUT)
GPIO.setup(y8,GPIO.OUT)

power = 2 ** 10
wait =  1 / power

for i in range(400):
    GPIO.output(x1,False)
    GPIO.output(y3,True)
    GPIO.output(y4,True)
    GPIO.output(y5,True)
    GPIO.output(y6,True)
    sleep(wait)
    GPIO.output(x1,True)
    GPIO.output(y3,False)
    GPIO.output(y4,False)
    GPIO.output(y5,False)
    GPIO.output(y6,False)
   
    GPIO.output(x2,False)
    GPIO.output(y2,True)
    GPIO.output(y7,True)
    sleep(wait)
    GPIO.output(x2,True)
    GPIO.output(y2,False)
    GPIO.output(y7,False)
   
    GPIO.output(x3,False)
    GPIO.output(y1,True)
    GPIO.output(y3,True)
    GPIO.output(y6,True)
    GPIO.output(y8,True)
    sleep(wait)
    GPIO.output(x3,True)
    GPIO.output(y1,False)
    GPIO.output(y3,False)
    GPIO.output(y6,False)
    GPIO.output(y8,False)
   
    GPIO.output(x4,False)
    GPIO.output(y1,True)
    GPIO.output(y8,True)
    sleep(wait)
    GPIO.output(x4,True)
    GPIO.output(y1,False)
    GPIO.output(y8,False)
   
    GPIO.output(x5,False)
    GPIO.output(y1,True)
    GPIO.output(y3,True)
    GPIO.output(y6,True)
    GPIO.output(y8,True)
    sleep(wait)
    GPIO.output(x5,True)
    GPIO.output(y1,False)
    GPIO.output(y3,False)
    GPIO.output(y6,False)
    GPIO.output(y8,False)
   
    GPIO.output(x6,False)
    GPIO.output(y1,True)
    GPIO.output(y4,True)
    GPIO.output(y5,True)
    GPIO.output(y8,True)
    sleep(wait)
    GPIO.output(x6,True)
    GPIO.output(y1,False)
    GPIO.output(y4,False)
    GPIO.output(y5,False)
    GPIO.output(y8,False)
   
    GPIO.output(x7,False)
    GPIO.output(y2,True)
    GPIO.output(y7,True)
    sleep(wait)
    GPIO.output(x7,True)
    GPIO.output(y2,False)
    GPIO.output(y7,False)
   
    GPIO.output(x8,False)
    GPIO.output(y3,True)
    GPIO.output(y4,True)
    GPIO.output(y5,True)
    GPIO.output(y6,True)
    sleep(wait)
    GPIO.output(x8,True)
    GPIO.output(y3,False)
    GPIO.output(y4,False)
    GPIO.output(y5,False)
    GPIO.output(y6,False)
   
    GPIO.output(x1,True)
    GPIO.output(x2,True)
    GPIO.output(x3,True)
    GPIO.output(x4,True)
    GPIO.output(x5,True)
    GPIO.output(x6,True)
    GPIO.output(x7,True)
    GPIO.output(x8,True)
    sleep(wait)
   
   

GPIO.cleanup()