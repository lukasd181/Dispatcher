from Components.DispatcherStore import DispatcherStore

def callback(message):
    print(f'Received: {message}')

consumer = DispatcherStore.createAmazonDataDispatcherConsumer("pre-processing", callback=callback)