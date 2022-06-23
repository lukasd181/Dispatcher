from Components.Producer.DispatcherProducer import DispatcherProducer
from Components.Consumer.DispatcherConsumer import DispatcherConsumer

class DispatcherStore:
    #Amazon dispatcher
    @staticmethod
    def createAmazonDataDispatcherProducer(key, ip_address="localhost", port="29092"):
        return DispatcherProducer(ip_address=ip_address, port=port, topic="Amazon", key=key)

    @staticmethod
    def createAmazonDataDispatcherConsumer(key, callback, ip_address="localhost", port="29092"):
        return DispatcherConsumer(ip_address=ip_address, port=port, topic="Amazon", key=key, callback=callback)

        