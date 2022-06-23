from Components.Base.DispatcherBase import DispatcherBase
from time import sleep
from json import dumps

from kafka import KafkaProducer


class DispatcherProducer(DispatcherBase):
    def __init__(self, ip_address, port, topic, key):
        super().__init__(ip_address, port, topic)
        self.key = key
        self.producer = KafkaProducer(
            bootstrap_servers= [self.kafka_server],
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )
    
    def send(self, data):
        self.producer.send(self.topic, value = data, key = self.key.encode())
        self.producer.flush()
    