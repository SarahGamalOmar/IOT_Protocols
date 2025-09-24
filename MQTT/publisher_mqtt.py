import time, random
import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
topic = "iot/temperature"

client = mqtt.Client()
client.connect(broker, 1883, 60)

try:
    while True:
        temp = random.uniform(20, 30)
        client.publish(topic, temp)
        print(f"Published: {temp}")
        time.sleep(2)
except KeyboardInterrupt:
    client.disconnect()

