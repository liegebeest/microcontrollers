from gpiozero import LED, Button, Buzzer
from time import sleep
from signal import pause
led = LED(17)
button = Button(27, bounce_time=0.2)
buzzer = Buzzer(22)

press_count = 0
state_on = False
print("Press button 3 times to enable buzzer")

while True:
    button.wait_for_press()
    led.on()
    press_count += 1
    print("Button pressed count:", press_count)

    if press_count == 3:
        if not state_on:
            buzzer.on()
            state_on = True
            print("Buzzer ON")
        else:
            buzzer.off()
            state_on = False
            print("Buzzer OFF")
        press_count = 0

    button.wait_for_release()
    led.off()
    sleep(0.05)
