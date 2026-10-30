from kafka_factory import get_keystroke_consumer, get_producer, initialize
from repository import get_oracle_db_connection

initialize()

print('Setting up Oracle DB connection...')
oracle_db = get_oracle_db_connection()
oracle_db.connect()

print('Setting up consumer...')
consumer = get_keystroke_consumer()

producer = get_producer()

for i in range(10):
    producer.send_keystroke_message(source='test_source', username='test_user', keytroke=f"{i}")

producer.flush()

print('Consuming messages...')
for message in consumer:
    print(f"Received message: {message.value}")
    if message:
        oracle_db.write_keystroke_message(source=message.value['source'], username=message.value['username'], keystroke=message.value['keystroke'])

oracle_db.close()