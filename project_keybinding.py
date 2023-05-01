import pyperclip
from pynput.keyboard import Listener, Key, KeyCode

def copy_text():
     print(pyperclip.paste())

def on_press(key):
    #try:
    #    print('alphanumeric key {0} pressed'.format(
    #        key.char))
    #except AttributeError:
    #    print('special key {0} pressed'.format(
    #        key))
    pass

def on_release(key):
    print('{0} released'.format(
        key))
    if key == KeyCode(char='\x03'): # 지금은 키코드로 컨트롤 c를 지정했지만 딕셔너리로 지정해서 함수를 불러올 수도 있는거 같다.
        # Stop listener
        copy_text()
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()