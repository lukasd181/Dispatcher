class DispatcherBase:
    def __init__(self, ip_address="localhost", port="29092", topic="general"):
        self.ip_address = ip_address
        self.port = port
        self.kafka_server = f"{self.ip_address}:{self.port}"
        self.topic = topic
