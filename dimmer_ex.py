#Chris Buckley w   4d1
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT) 

pwm_led = GPIO.PWM(17,500)
pwm_led.start(0)


try:
	while True:
		duty_s=input("Enter the LED Brightness: ")
		duty = int(duty_s)
		pwm_led.ChangeDutyCycle(duty)

finally:
	print("cleaning up")
	GPIO.celanup()
