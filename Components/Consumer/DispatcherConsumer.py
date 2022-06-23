from Components.Base.DispatcherBase import DispatcherBase
from kafka import KafkaConsumer
from json import loads

class DispatcherConsumer(DispatcherBase):
    def __init__ (self, ip_address, port, topic, key, callback):
        super().__init__(ip_address, port, topic)
        self.key = key
        self.callback = callback 
        self.start()

    def start(self):
        consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers = [self.kafka_server],
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )
        
        for message in consumer:
            key = message.key.decode()
            if self.key == "*":
                self.callback(key, message)
            elif key == self.key:
                self.callback(message.value)
