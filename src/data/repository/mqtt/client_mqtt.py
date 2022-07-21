import random

from paho.mqtt import client as mqtt_client


def _on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


class MQTTClient:

    def __init__(self, broker, port) -> None:
        super().__init__()

        client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.client = mqtt_client.Client(client_id)
        self.client.on_connect = _on_connect

    def connect_safe(self, broker, port, username, password):
        self.client.username_pw_set(username, password)
        self.connect(broker, port)

    def connect(self, broker, port):
        self.client.connect(broker, port)

    def subscribe(self, topic, callback):
        """
        example of a callback:
        def callback(client, userdata, msg):
             print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        """
        self.client.subscribe(topic)
        self.client.on_message = callback

    def publish(self, topic, data):
        result = self.client.publish(topic, data)
        status = result[0]
        if status == 0:
            print(f"Send `{data}` to topic `{topic}`")
            return True
        else:
            print(f"Failed to send message to topic {topic}")
            return False
