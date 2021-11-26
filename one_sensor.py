import RPi. GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = ""
GPIO_ECHO = ""

GPIO.setup(GPIO-TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  StartTime = time.time()
  StopTime = time.time()
  
  while GPIO.input(GPIO_ECHO) == 1:
    StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    
    distance = (TimeElapsed*34300) / 2
    return distance
  
  if __name__ == "__main__":
    try:
      while True:
        dist = distance()
        print("Measured Distance = ", % dist)
        time.sleep(1)
    except KeyboardInterrupt:
      print("Measurement stopped.")
      GPIO.cleanup()
  
  
