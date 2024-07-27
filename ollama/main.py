from pynput import keyboard


def on_activate_f11():
    print('f11 pressed')


def on_activate_f12():
    print('f12 pressed')


with keyboard.GlobalHotKeys({
    '<65480>': on_activate_f11,
    '<65481>': on_activate_f12}) as h:
    h.join()
