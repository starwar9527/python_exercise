from pynput import keyboard
from pynput.keyboard import Controller, Key
import pyperclip
import time
import httpx
from string import Template

controller = Controller()

HOST = 'http://localhost:11434/api/generate'
CONFIG = {"model": "mistral:instruct",
          "keep_alive": "5m",
          "stream": False
          }
PROMPT_TEMPLATE = Template(
    """Fix all typos, casing and punctuation in this text, but preserve all new line characters:
    
    $text
    
    Return only the corrected text, don't include a preamble.
    """)


def fix_text(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    response = httpx.post(HOST,
                          json={"prompt": prompt, **CONFIG},
                          headers={"Content-Type": "application/json"},
                          timeout=10)
    if response.status_code != 200:
        return None
    return response.json()["response"].strip()


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


# fix the selected text
def on_activate_f12():
    # fix the selected text
    fix_selected_text()


with keyboard.GlobalHotKeys({
    '<65480>': on_activate_f11,
    '<65481>': on_activate_f12}) as h:
    h.join()
