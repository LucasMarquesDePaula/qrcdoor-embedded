'''
Created on 8 de set de 2017

@author: Lucas
'''

import RPi.GPIO as GPIO
import time

def test(target):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(target, GPIO.OUT)
	GPIO.output(target, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(target, GPIO.LOW)


# Relê
test(22)

# Amarelo
test(4)

# Verde
test(27)

# Vermelho
test(17)

# Buzz
test(23)