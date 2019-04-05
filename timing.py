def millisecond_stamps():

    import time

    i = 0
    startTimeSec = time.time()
    startTimeMS = time.time() * 1000

    print('Start Time in Seconds is ', startTimeSec)
    print('Start Time in Milliseconds is ', startTimeMS)
    time.sleep(5)

    while i < 10:

        tm = time.time() * 1000
        elapsed = tm - startTimeMS
        print('The current time in milliseconds is: ', tm)
        print('Time elasped = ', elapsed)
        time.sleep(1)
        i += 1
