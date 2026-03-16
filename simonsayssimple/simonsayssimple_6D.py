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

def read_input(timeout=5):
    start = monotonic()
    while monotonic() - start < timeout:
        if button.wait_for_press(timeout=0.1):
            t0 = monotonic()
            button.wait_for_release()
            dur = monotonic() - t0
            return "A" if dur < 0.4 else "B"
    return None

def start_signal():
    print("Klaar? Boots de lampjes na")
    print("Rode LED betekent: kort drukken, Groene LED betekent: lang drukken")
    print("Veel succes!")
    sleep(1)


def main():
    sequence = []
    start_signal()
    teller=0
    while True:
        print("Je hebt al:", teller, "punt(en)")
        print("Kijk naar de lampjes binnen 1 seconde")
        sleep(1)
        sequence.append(random.choice(["A", "B"]))
        play_sequence(sequence)
        for expected in sequence:
            got = read_input()
            if got != expected:
                print("---")
                print("Game over, je score is:", teller)
                print("---")
                return
        teller += 1
    print("end logic")

main()
