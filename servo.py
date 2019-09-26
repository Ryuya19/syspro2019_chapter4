import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

def setservo(deg):
    servo = GPIO.PWM(2, 50)
    servo.start(0.0)
    servo.ChangeDutyCycle(((deg + 90) / 180 + 0.5) * 5)
    time.sleep(1)


for i in range(10):
    setservo(-90)
    setservo(90)

GPIO.cleanup()
