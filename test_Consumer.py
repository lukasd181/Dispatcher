from ipaddress import ip_address
from Components.DispatcherStore import DispatcherStore

def callback(message):
    print(f'Received: {message}')

consumer = DispatcherStore.createModelConsumer("predict", callback=callback)
