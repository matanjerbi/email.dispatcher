from kafka import KafkaConsumer
import json
from config.config import Config


def start_listening():
    # יצירת צרכן קפקא שמאזין לשני הנושאים
    consumer = KafkaConsumer(
        'messages.hostage',
        'messages.explosive',
        bootstrap_servers=Config.KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("Starting to listen for messages...")

    # לולאת האזנה אינסופית
    for message in consumer:
        topic = message.topic
        data = message.value

        print(f"Received message from topic: {topic}")
        if topic == 'messages.hostage':
            handle_hostage_message(data)
        elif topic == 'messages.explosive':
            handle_explosive_message(data)


def handle_hostage_message(data):
    print(f"Processing hostage message: {data['sentences']}")
    # כאן תוכל להוסיף את הלוגיקה לטיפול בהודעות hostage


def handle_explosive_message(data):
    print(f"Processing explosive message: {data['sentences']}")
    # כאן תוכל להוסיף את הלוגיקה לטיפול בהודעות explosive


if __name__ == "__main__":
    start_listening()