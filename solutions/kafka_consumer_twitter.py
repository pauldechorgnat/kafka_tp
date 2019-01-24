#!/usr/bin/python3

from kafka.consumer import SimpleConsumer
from kafka import SimpleClient
import argparse
import os
import json

if __name__ == '__main__':
    # creating an argument parser to define where to get the messages from and where to dump them
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--topic', type=str, default='test')
    argument_parser.add_argument('--hosts', type=str, default='localhost:9092')
    argument_parser.add_argument('--path', type=str, default='./tweets')

    arguments = argument_parser.parse_args()

    # getting the topic to collect the messages from
    topic_to_collect_from = arguments.topic
    # getting the hosts of the brokers
    kafka_hosts = arguments.hosts
    # getting the path to the file where we will dump the content of topic
    path_to_sink_folder = arguments.path

    # creating the folder if it does not exist
    try:
        os.stat(path_to_sink_folder)
    except FileNotFoundError:
        os.mkdir(path_to_sink_folder)

    # instantiating a Kafka client
    kafka_client = SimpleClient(hosts=kafka_hosts)

    # instantiating a Kafka consumer
    kafka_consumer = SimpleConsumer(client=kafka_client, topic=topic_to_collect_from, group='simple_consumer_group')

    # looping over the values
    fetch_tweets = True
    counter = 0
    while fetch_tweets:
        messages = kafka_consumer.get_messages(count=1)
        counter += 1
        if len(messages) == 0:
            fetch_tweets = False
        else:
            file_name = 'tweet_n_{}.json'.format(counter+1)
            message = json.loads(messages[0].message.value)
            with open(os.path.join(path_to_sink_folder, file_name), 'w') as json_file:
                json.dump(message, json_file)
