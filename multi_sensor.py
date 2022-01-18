import RPi.GPIO as gpio
import time

def distance(measure"cm"):
  try:
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(16, gpio.IN)
    #input the pin location we're using#
    #trigger is out, echo is in#
    #we need to set all the ultrasound to have the same trigger pin so they can run at once#
    
    gpio.output(12, False)
    while gpio.input(16) == 0:
      StartTime = time.time()
    
    while gpio.input(16) == 1:
      StopTime = time.time()
      
    TimeTaken = StopTime - StartTime
    
    distance = TimeTaken / 0.000058
    #this converts it to cm#

    gpio.cleanup()
    return distance
  
  except:
    distance = 100
    gpio.cleanup()
    return distance
  
  if __name__ == "__main__":
    try:
      while True:
        dist = distance()
        print(dist, "cm")
    except KeyboardInterrupt:
      print("Measurement stopped by User")
      gpio.cleanup()
  
