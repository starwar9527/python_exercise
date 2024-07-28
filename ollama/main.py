from pynput import keyboard
from pynput.keyboard import Controller, Key
import pyperclip
import time


controller = Controller()


def fix_text(text):
    return text[::-1]


def fix_selected_text():
    # 1. copy text to clipboard
    with controller.pressed(Key.ctrl):
        controller.tap('c')

    # 2. get the text from clipboard
    time.sleep(0.1)
    text = pyperclip.paste()
    # 3. fix the text
    text = fix_text(text)
    # print(text)
    # 4. copy text back to clipboard
    pyperclip.copy(text)
    # 5. insert text
    with controller.pressed(Key.ctrl):
        controller.tap('v')

# fix the selected line
def on_activate_f11():
    # select the line
    controller.press(Key.home)
    controller.press(Key.shift)
    controller.press(Key.end)

    controller.release(Key.home)
    controller.release(Key.shift)
    controller.release(Key.end)

    # fix the selected text
    fix_selected_text()
    print('f11 pressed')


# fix the selected text
def on_activate_f12():
    # fix the selected text
    fix_selected_text()


with keyboard.GlobalHotKeys({
    '<65480>': on_activate_f11,
    '<65481>': on_activate_f12}) as h:
    h.join()
"""
curl http://localhost:11434/api/generate -d '{
    "model":  "mistral:instruct",
    "prompt": "Why is the sky blue?",
    "stream": False
}'
"""
