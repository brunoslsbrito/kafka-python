from kafka import KafkaConsumer
consumer = KafkaConsumer('python', group_id='python', bootstrap_servers='localhost:9092')
for msg in consumer:
 print (msg)