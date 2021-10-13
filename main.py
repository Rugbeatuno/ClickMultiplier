from pynput.mouse import Controller, Button
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
# mac - "pip3 install pynput"
# windows - "pip install pynput"
import time


controller = Controller()
last_click = time.time()
additional_clicks = int(input("Enter additional clicks: ") or 1)

left = False
right = False

def on_click(x, y, button, pressed):
    global last_click
    time_since_click = time.time() - last_click

    if time_since_click > 0.06 and pressed:
        for i in range(additional_clicks):
            time.sleep(0.03)  # add this time

            if str(button)[-4:] == 'left' and left:
                controller.press(Button.left)
                time.sleep(0.03)  # add this time
                controller.release(Button.left)
                last_click = time.time()

            if str(button)[-5:] == 'right' and right:
                controller.press(Button.right)
                time.sleep(0.03)
                controller.release(Button.right)
                last_click = time.time()

def on_press(key):
    global left, right

    try:
        if key.char == '[':  # toggle left click
            left = not left
            status()

        if key.char == 'r':  # right click
            right = not right
            status()

    except AttributeError:
        pass




def status():
    print('-----------------')
    print(f'Left: {left}')
    print(f'Right: {right}')


mouse_listener = MouseListener(on_click=on_click)
keyboard_listener = KeyboardListener(on_press=on_press)
mouse_listener.start()
keyboard_listener.start()
mouse_listener.join()
keyboard_listener.join()



