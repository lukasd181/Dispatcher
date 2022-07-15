from ipaddress import ip_address
from Components.DispatcherStore import DispatcherStore
producer = DispatcherStore.createModelProducer(key="predict")

data = {
    "symbol": "AMZ",
    "o": 123,
    "c": 5345,
    "asdas": "asdasd"
}
producer.send(data)
print("sent")

