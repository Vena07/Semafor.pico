import machine
import time

# senzor
trig = machine.Pin(0, machine.Pin.OUT)
echo = machine.Pin(1, machine.Pin.IN)

# semafor
szelena = machine.Pin(8, machine.Pin.OUT)
szluta = machine.Pin(7, machine.Pin.OUT)
scervena = machine.Pin(6, machine.Pin.OUT)

#RGBb led dioda
lzelena = machine.Pin(3, machine.Pin.OUT)
lmodra = machine.Pin(2, machine.Pin.OUT)
lcervena = machine.Pin(4, machine.Pin.OUT)

# buzzer a button
button = machine.Pin(17,machine.Pin.IN,machine.Pin.PULL_DOWN)
buzzer =  machine.PWM(machine.Pin(16))


def play_tone(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty_u16(1000)
    time.sleep(duration)
    buzzer.duty_u16(0) 


def measure_distance():
    
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    
    
    while echo.value() == 0:
        pass
    start = time.ticks_us()
    
    while echo.value() == 1:
        pass
    end = time.ticks_us()
    
    
    distance = (time.ticks_diff(end, start) * 0.0343) / 2
    return distance

def zvuk_zelena():
    play_tone(784, 0.2)
    time.sleep(0.2)
    play_tone(784, 0.2)

def zvuk_cervena():
    play_tone(784, 0.5)
    time.sleep(0.5)
    play_tone(784, 0.5)

while True:
    dist = measure_distance()
    
    
    if dist < 10:  # Když je něco blíž než 10 cm
        if szelena.value() == 1:
            pass
        else:
            for i in range(10):
                zvuk_zelena()
            lzelena.value(0)
            lcervena.value(1)
            for i in range(3):
                zvuk_cervena()
            scervena.value(1)
            szluta.value(1)
            for i in range(3):
                zvuk_cervena()
            scervena.value(0)
            szluta.value(0)
            szelena.value(1)
            for i in range(6):
                 zvuk_cervena()
    if button.value() == 1 and lzelena.value() == 0:
        for i in range(3):
            zvuk_cervena()
        szelena.value(0)
        szluta.value(1)
        for i in range(3):
            zvuk_cervena()
        szluta.value(0)
        scervena.value(1)
        for i in range(3):
            zvuk_cervena()
        lzelena.value(1)
        lcervena.value(0)
        for i in range(10):
            zvuk_zelena()
