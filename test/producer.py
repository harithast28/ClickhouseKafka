# Python script to fetch data from API
from kafka import KafkaProducer
import requests
import json
import time


def fetch_data():

    # AUTH
    response = requests.get('https://app.xpatron-test.de/api/token', auth=('prometeon@prometeon', 'Iphae5noh8ahng3poephoutie6uHaeJa'))
    response = response.json()
    token = response['token']
    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Accept': 'application/json',
    }

    # UNITS
    r_units = requests.get('https://app.xpatron-test.de/api/unit', headers=headers)
    d_units = r_units.json()

    return d_units['units']


def publish_message(producer_instance, topic_name, keys, value):

    # value is unit

    try:
        for key, value in value.items():
            producer_instance.send('json-topic', {key: value})
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
        units = fetch_data()

        if units:
            kafka_producer = connect_kafka_producer()
            for unit in units:
                print(" UNIT", unit)
                publish_message(kafka_producer, 'json-topic', 'raw', unit)
            if kafka_producer is not None:
                kafka_producer.close()
            else:
                print("[NO KAFKA PRODUCER]")

        time.sleep(5)


if __name__ == '__main__':
    main()
