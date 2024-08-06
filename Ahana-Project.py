#Set pin names and board values
relay = 21
room = 23
flame = 5
buzzer = 24
green = 19
red = 16
#import libraries
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
scan = SimpleMFRC522()
#Set pins as input and output accordingly
GPIO.setup(relay, GPIO.OUT)
GPIO.setup(room, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(flame, GPIO.IN)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

while True:
	GPIO.output(relay, GPIO.HIGH)
	fire=GPIO.input(flame)
	if fire == GPIO.HIGH:
		GPIO.output(buzzer, GPIO.LOW)
	else:
		GPIO.output(buzzer, GPIO.HIGH)
	print(“Place your card - “)
	id, Tag=scan.read()
	print(id)
	pre_set=“166061473145”
	if str(id)!=pre_set:
		GPIO.output(green,GPIO.LOW)
		GPIO.output(red,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(red,GPIO.LOW)
		continue
	elif str(id)==pre_set:
		GPIO.output(green,GPIO.HIGH)
		GPIO.output(red,GPIO.LOW)
		time.sleep()
		GPIO.output(green,GPIO.LOW)
		while True:
			motion = GPIO.input(room)
			fire = GPIO.input(flame)
			if motion == GPIO.HIGH:
				print(“Motion detected.”)
				GPIO.output(relay, GPIO.LOW) #switches on
				if fire == GPIO.HIGH:
					GPIO.output(buzzer, GPIO.LOW)
				else:
					GPIO.output(buzzer, GPIO.HIGH)
			elif motion == GPIO.LOW:
				print(“No motion.”)
				GPIO.output(relay, GPIO.HIGH)  #switches off
				if fire == GPIO.HIGH:
					GPIO.output(buzzer, GPIO.LOW)
				else:
					GPIO.output(buzzer, GPIO.HIGH)

		

	
	
