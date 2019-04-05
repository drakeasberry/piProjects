import RPi.GPIO as GPIO
import time
from msec_time import millisecond_stamps

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

GPIO.output(21, GPIO.LOW)

counter = 0
awake = 1
sleep = 1
inReceived = 1
startTime = time.time() * 1000
print(startTime)

try:
    while counter < 5:
        print('Count: %d' % counter)
        GPIO.output(21, GPIO.HIGH)
        millisecond_stamps()
        print('The time is ')
        time.sleep(5)
        
        
        GPIO.output(21, GPIO.LOW)
        time.sleep(5)
        #print('Time off %t:' % sleep)
        counter += 1
        awake += 1
        sleep += 1
        #print('One, two, three...')
    print('End of Test reached: %d' % counter)
    
except KeyboardInterrupt:
    print('\n Program aborted at count: %d' % counter)
    
except:
    print('Something went wrong...')

finally:
    GPIO.cleanup()

