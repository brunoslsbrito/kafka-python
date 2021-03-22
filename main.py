from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'foobar',
     bootstrap_servers=['localhost:9092'],
     enable_auto_commit=True,
     group_id='py_consumer',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print('{} added to {}'.format(message))