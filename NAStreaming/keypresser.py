from pykeyboard import PyKeyboard
from time import sleep
class keyPresser():

    def pressKey(self,key):

        k = PyKeyboard()
        keyMap = {'up':'k',
                'down':',',
                'right':'.',
                'left':'m',
                'start':'s',
                'select':'d',
                'a':'z',
                'b':'x',
                'l':'a',
                'r':'c'}

        if (key in keyMap):
            k.press_key(keyMap[key])
            sleep(0.1)
            k.press_key(keyMap[key])

