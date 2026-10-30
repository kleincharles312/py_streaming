import argparse
from pynput.keyboard import Key, Listener

argument_parser = argparse.ArgumentParser(description='Keystroke listener.')

argument_parser.add_argument('-s', '--source', type=str, help='Arbitrary source name', required=True)
argument_parser.add_argument('-u', '--username', type=str, help='Name of the user at the keyboard', required=True)

args = argument_parser.parse_args()

def on_press(key):
    if key == Key.esc:
        return False # Stop listener
    else:
        
