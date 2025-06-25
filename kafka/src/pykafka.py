from kafka import KafkaClient, KafkaConsumer, KafkaProducer


#client = KafkaClient(bootstrap_servers="127.0.0.1:9092", client_id="pykafka")

consumer = KafkaConsumer(bootstrap_servers="127.0.0.1:9092", client_id="pykafka")

topics = consumer.topics()
print(f"{topics=}")

for topic in topics:
    partitions = consumer.partitions_for_topic(topic)
    print(f"{topic=} -> {partitions=}")