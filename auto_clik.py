import pynput
import time

mouse = pynput.mouse.Controller()
time.sleep(3)

for i in range(2000):
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)
    time.sleep(0.01)