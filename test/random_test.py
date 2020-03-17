# Python script to fetch data from API
from kafka import KafkaProducer
import json
import time
import random


def generate_data():

    message = {
        'userId': random.randint(0, 200),
        'name': "pickachu",
        'value': random.randint(0, 10)
    }

    print("TYPE OF MESSAGE", type(message))

    return message


def publish_message(producer_instance, topic_name, data):

    # value is unit

    try:
        for key, value in data.items():
            producer_instance.send('jsontopic', {key: value})
            producer_instance.flush()
            print('Message published successfully.')
    except Exception as E:
        print('Exception in publishing message', E)


def connect_kafka_producer():
    producer = None
    try:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))
    except Exception as E:
        print('Exception while connecting Kafka', E)

    return producer


def main():

    # Call API and fetch data here
    for _ in range(100):
        data = generate_data()

        print("DATA", data)

        if data:
            print("CONNECTING PRODUCER")
            kafka_producer = connect_kafka_producer()
            publish_message(kafka_producer, 'jsontopic', data)
            if kafka_producer is not None:
                kafka_producer.close()
            else:
                print("[NO KAFKA PRODUCER]")

        time.sleep(5)


if __name__ == '__main__':
    main()
