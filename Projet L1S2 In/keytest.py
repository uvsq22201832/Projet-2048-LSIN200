# Créé par ys000, le 20/02/2023 en Python 3.7
from pynput import keyboard
from pynput.keyboard import Key

#C'est juste un truc volé sur Internet pour voir si les boutons fonctionne.
#Par contre, il réagit pour n'importe quel click, donc faut placer des conditions quand on l'utilise.

def on_key_release(key):
    if key == Key.right:
        print("Right key clicked")
    elif key == Key.left:
        print("Left key clicked")
    elif key == Key.up:
        print("Up key clicked")
    elif key == Key.down:
        print("Down key clicked")
    elif key == Key.esc:
        exit()


with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()

