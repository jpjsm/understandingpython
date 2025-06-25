from messaging import KafkaMessaging

print("test begins")

kafka_messaging = KafkaMessaging("localhost:9092", "test_messaging")

msgs = kafka_messaging.GetMsgs(topic="test_04")

for msg in msgs:
    print(msg)

print("test completed")    