from kafka.consumer import SimpleConsumer
from kafka import SimpleClient
import argparse
import json
import pprint


if __name__ == '__main__':
    # creating an argument parser to define where to get the messages from and where to dump them
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--topic', type=str, default='test')
    argument_parser.add_argument('--hosts', type=str, default='localhost:9092')
    argument_parser.add_argument('--path', type=str, default='./sink.json')
    argument_parser.add_argument('--count', type=int, default=10)

    arguments = argument_parser.parse_args()

    # getting the topic to collect the messages from
    topic_to_collect_from = arguments.topic
    # getting the hosts of the brokers
    kafka_hosts = arguments.hosts
    # getting the path to the file where we will dump the content of topic
    path_to_sink = arguments.path
    # getting the required number of messages to fetch from kafka
    message_count = arguments.count

    # instantiating a Kafka client
    kafka_client = SimpleClient(hosts=kafka_hosts)

    # instantiating a Kafka consumer
    kafka_consumer = SimpleConsumer(client=kafka_client, topic=topic_to_collect_from, group='simple_consumer_group')

    # fetching the messages
    messages_data = kafka_consumer.get_messages(count=message_count)
    # creating a dictionary
    message_dictionary = {}
    # running through the
    for index, message in enumerate(messages_data):
        message_dictionary[index] = {
            'value': message.message.value.decode('utf-8'),
            'offset': message.offset,
        }

    # dumping messages
    with open(path_to_sink, 'w') as sink_file:
        json.dump(message_dictionary, sink_file)

    # printing the content of the json file in the terminal
    pprint.pprint(message_dictionary)
