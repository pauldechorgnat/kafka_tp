from kafka import SimpleProducer, SimpleClient
import argparse

if __name__ == '__main__':
    # defining a argument parser to choose what message to send
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--message', type=str, default='test message')
    argument_parser.add_argument('--hosts', type=str, default='localhost:9092')
    argument_parser.add_argument('--topic', type=str, default='test')
    arguments = argument_parser.parse_args()

    # getting the text to publish
    text_to_publish = arguments.message

    # getting the hosts for Kafka
    kafka_hosts = arguments.hosts

    # getting the topic to publish in
    topic_to_publish_in = arguments.topic

    # instantiating a Kafka Client
    kafka_client = SimpleClient(hosts=kafka_hosts)

    # instantiating a Kafka Producer
    kafka_producer = SimpleProducer(kafka_client)

    # printing what we are doing
    print('publishing "{}" \nto topic "{}" on broker(s) "{}"'.format(text_to_publish,
                                                                     topic_to_publish_in,
                                                                     '", "'.join(kafka_hosts.split(','))
                                                                     )
          )

    # publishing the message
    kafka_producer.send_messages(topic_to_publish_in, text_to_publish.encode('utf-8'))

    # stopping the kafka producer
    kafka_producer.stop()
