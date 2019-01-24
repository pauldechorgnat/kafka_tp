from kafka import SimpleProducer, SimpleClient
import argparse

if __name__ == '__main__':
    # defining a argument parser to choose what message to send
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--message', type=str, default='test message')
    arguments = argument_parser.parse_args()

    # getting the text to publish
    text_to_publish = arguments.message

    # instantiating a Kafka Client
    kafka_client = SimpleClient(hosts='localhost:9092')

    # instantiating a Kafka Producer
    kafka_producer = SimpleProducer(kafka_client)

    # publishing the message
    kafka_producer.send_messages('test', text_to_publish.encode('utf-8'))

    # stopping the kafka producer
    kafka_producer.stop()
