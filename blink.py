import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

GPIO.output(21, GPIO.LOW)

counter = 0

try:
    while counter < 5:    
        GPIO.output(21, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(21, GPIO.LOW)
        time.sleep(5)
        counter += 1
    print('End of Test reached: %d' % counter)
    
except KeyboardInterrupt:
    print('\n Program aborted at count: %d' % counter)
    
except:
    print('Something went wrong...')

finally:
    GPIO.cleanup()

