import RPi.GPIO as gpio
import time

IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23
IN5 = 24
IN6 = 25
OUT1 = 26
OUT2 = 16

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(OUT1, gpio.OUT)
gpio.setup(OUT2, gpio.OUT)
gpio.setup(IN1, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(IN2, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(IN3, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(IN4, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(IN5, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(IN6, gpio.IN, pull_up_down=gpio.PUD_UP)

toggle = False

ins = [IN1,IN2,IN3,IN4,IN5,IN6]
in_state = [0,0,0,0,0,0]

timeout = time.time() + 1  # 1 second from now
while True:
    test = 0
    if time.time() > timeout:
        timeout  = timeout + 1
        if(toggle):
            toggle = False
            gpio.output(OUT1, gpio.LOW)
            gpio.output(OUT2, gpio.HIGH)
        else:
            toggle = True
            gpio.output(OUT1, gpio.HIGH)
            gpio.output(OUT2, gpio.LOW)
    for i in range(6):
        pin = gpio.input(ins[i])
        if(in_state[i] != pin and pin == 0):
            print(str(time.time()) + "  "+  str(i))
        in_state[i] = pin
    
