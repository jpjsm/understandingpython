from kafka import KafkaConsumer, KafkaProducer
from typing import Any, Generator
from json import loads


class KafkaMessaging():
    def __init__(self, bootstrap_servers: str| list[str], client_id:str):
        self.bootstrap_servers = bootstrap_servers
        self.client_id = client_id

    def Topics(self) -> list[str]:
        consumer=KafkaConsumer(            
            bootstrap_servers=self.bootstrap_servers, 
            client_id=self.client_id,
            group_id="test_group",
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: loads(x.decode('utf-8')))

        return [t for t in consumer.topics()]
    
    def SendMsg(self, topic: str, msg:str):
        kproducer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers, 
            client_id=self.client_id,
        )
        if not kproducer.bootstrap_connected():
            raise Exception(f"Not connected to Kafka: {self.bootstrap_servers}")

        kproducer.send(topic=topic, value=msg.encode("utf-8"))

    def GetMsgs(self, topic: str) -> list[Any]:
        consumer=KafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers, 
            client_id=self.client_id,
            group_id="test_group",
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            request_timeout_ms=10001,
            session_timeout_ms=10000)
        if not consumer.bootstrap_connected():
            raise Exception(f"Not connected to Kafka: {self.bootstrap_servers}")

        msgs = []

        msg_pack = consumer.poll(timeout_ms=1000)
        for tp, messages in msg_pack.items():
            for message in messages:
                _msg = {
                    'topic': str(tp.topic), 
                    'partition': str(tp.partition),
                    'msg_offset': str(message.offset),
                    'msg_key': str(message.key),
                    'msg_content': str(message.value)
                    }
                msgs.append( _msg)

        #print(f"{msgs=}")
        return msgs
