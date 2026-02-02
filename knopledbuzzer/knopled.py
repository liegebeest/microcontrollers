from gpiozero import LED, Button
from signal import pause
led = LED(17)
button = Button(27)

button.when_pressed = led.on
button.when_released = led.off

print("press the button to turn the LED on")
pause()
