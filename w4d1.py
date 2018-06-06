#Chris Buckley w   4d1
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT) 
n=50
pwm_led = GPIO.PWM(17,500)
pwm_led.start(n)



while True:
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	if GPIO.input(23) == False:
		while n<100:
			pwm_led.ChangeDutyCycle(n)
			n=n+5
			pwm_led.ChangeDutyCycle(n)
			time.sleep(0.5)		
			n=n+5
			pwm_led.ChangeDutyCycle(n)
	if GPIO.input(24) == False:
		while n>0:
			n=n-5
			pwm_led.ChangeDutyCycle(n)
			time.sleep(0.5)
			n=n-5
			pwm_led.ChangeDutyCycle(n)
			time.sleep(0.5)
			n=n-5
			pwm_led.ChangeDutyCycle(n)


