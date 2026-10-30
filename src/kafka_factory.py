from kafka import KafkaConsumer, KafkaProducer, JsonSerializer
from kafka.admin import KafkaAdminClient, NewTopic

# TODO: most of this is configuration and should be elsewhere
__broker = 'localhost:9092'

__keystroke_topic = 'keystroke'

def initialize():
    admin_client = KafkaAdminClient(bootstrap_servers=__broker)

    expected_topics = [__keystroke_topic]
    existing_topics = admin_client.list_topics()

    for topic in expected_topics:
        if topic not in existing_topics:
            new_topic = NewTopic(name=topic, num_partitions=1, replication_factor=1)
            admin_client.create_topics([new_topic])
            print(f"Created topic: {topic}")
        else:
            print(f"Topic '{topic}' already exists.")

    admin_client.close()


class MessageProducer:
    def __init__(self, bootstrap_servers, keystroke_topic):
        print(f"Initializing MessageProducer with bootstrap servers: {bootstrap_servers}")

        self._keystroke_topic = keystroke_topic
        self._producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=JsonSerializer())

    def send_keystroke_message(self, source, username, keytroke):
        self._producer.send(self._keystroke_topic, {
            'source': source,
            'username': username,
            'keystroke': keytroke
        })

    def flush(self):
        self._producer.flush()

def get_producer():
    return MessageProducer(bootstrap_servers=__broker, keystroke_topic=__keystroke_topic)

def get_keystroke_consumer():
    consumer = KafkaConsumer(bootstrap_servers=__broker,
                               enable_auto_commit=True,
                               auto_offset_reset='earliest',
                               value_deserializer=JsonSerializer()
                               )

    consumer.subscribe([__keystroke_topic])

    return consumer
