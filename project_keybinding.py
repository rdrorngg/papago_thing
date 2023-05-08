import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from project_main import Ui_MainWindow
from project_papago import PapagoApi 
import pyperclip
from pynput.keyboard import Listener, Key, KeyCode


def on_press(key):
    #try:
    #    print('alphanumeric key {0} pressed'.format(
    #        key.char))
    #except AttributeError:
    #    print('special key {0} pressed'.format(
    #        key))
    pass

papatran = PapagoApi()

def on_release_copy(key):
    if key == KeyCode(char='\x03'): # 지금은 키코드로 컨트롤 c를 지정했지만 딕셔너리로 지정해서 함수를 불러올 수도 있는거 같다.
        # Stop listener
        text = pyperclip.paste()
        return papatran.get_trans(text)
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release_copy) as listener:
        listener.join()


