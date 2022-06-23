from Components.DispatcherStore import DispatcherStore

producer = DispatcherStore.createAmazonDataDispatcherProducer(key="predict")
data = {
    "symbol": "AMZ",
    "o": 123,
    "c": 5345,
    "asdas": "asdasd"
}
producer.send(data)

