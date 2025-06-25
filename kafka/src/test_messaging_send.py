from messaging import KafkaMessaging
from datetime import datetime, timezone
from json import dumps
from uuid import uuid4

kafka_messaging = KafkaMessaging("localhost:9092", "test_messaging")

print(f"Topics: {kafka_messaging.Topics()}")

for i in range(100):
    value = {
        "sequence": i, 
        "timestamp": datetime.now(timezone.utc).isoformat(), 
        "content": uuid4().hex
        }
    msg = dumps(value)
    kafka_messaging.SendMsg(topic="test_04", msg=msg)
    print(f"Sent to '{kafka_messaging.bootstrap_servers}': {msg}")

print("test completed")