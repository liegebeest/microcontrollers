from gpiozero import LED, Button
from time import sleep, monotonic
import random

# GPIO pins (BCM)
LED_A_PIN = 17
LED_B_PIN = 18
BUTTON_PIN = 27

led_a = LED(LED_A_PIN)
led_b = LED(LED_B_PIN)
button = Button(BUTTON_PIN, pull_up=True, bounce_time=0.05)

FLASH = 0.3
GAP = 0.2

def flash(led, dur=FLASH):
    led.on()
    sleep(dur)
    led.off()
    sleep(GAP)

def play_signal(sig):
    #print("will play", sig)
    if sig == "A":
        flash(led_a)
    else:
        flash(led_b)

def play_sequence(seq):
    #print(seq)
    sleep(0.6)
    for sig in seq:
        play_signal(sig)

def read_input(timeout=10):
    start = monotonic()
    while monotonic() - start < timeout:
        if button.wait_for_press(timeout=0.1):
            t0 = monotonic()
            button.wait_for_release()
            dur = monotonic() - t0
            return "A" if dur < 0.4 else "B"
    return None

def start_signal():
    print("Klaar?")
    print("Rode LED betekent: kort, Groene LED betekent: lang")
    print("Veel succes!")
    sleep(1)


def main():
    print("start logic")

    print("end logic")

main()
