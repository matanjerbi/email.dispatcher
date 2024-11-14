from kafka import KafkaProducer
import json
from app.config.config import Config

producer = KafkaProducer(
    bootstrap_servers=Config.KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_to_kafka(topic, message):

    try:
        producer.send(topic, message)
    except Exception as e:
        print(f"Kafka Error: {str(e)}")