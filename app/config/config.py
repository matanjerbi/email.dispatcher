class Config:
    # חיבור למונגו על localhost עם הפורט הדיפולטיבי
    MONGO_URI = 'mongodb://localhost:27017/email_dispatcher'

    # חיבור לקפקא על localhost עם הפורט הדיפולטיבי
    KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'