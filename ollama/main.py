from pynput import keyboard
from pynput.keyboard import Controller, Key
import pyperclip
import time


controller = Controller()


def fix_text():
    pass


def fix_selected_text():
    # 1. copy text to clipboard
    with controller.pressed(Key.ctrl):
        controller.tap('c')
    # 2. get the text from clipboard
    time.sleep(0.1)
    text = pyperclip.paste()
    print(text)
    # 3. fix the text
    # 4. copy text back to clipboard
    # pyperclip.copy('text to be copied back to clipboard')
    # 5. insert text


# fix the selected line
def on_activate_f11():
    # select the line
    # fix the selected text
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
