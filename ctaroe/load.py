def load(flag):

    # инициализация портов gpio
    if flag == True:
        import RPi.GPIO as GPIO
        ports = (18, 19, 20, 21, 200, 200)
        RPIO.setmode(RPIO.BCM)
        for i in ports:
            GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
        ena = GPIO.PWM(ports[4], 50)
        enb = GPIO.PWM(ports[5], 50)
    
    # инициализация com порта лидара
    if flag == True:
        import serial
        ser = serial.Serial('COM1')
