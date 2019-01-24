# Use Case instructions: using Kafka with Python

## Purpose
We want to build an application using Kafka that collects Tweets and dumps them into a folder using Kafka.

## Instructions
We need two files:
* A producer that takes Tweets from Twitter containing a particular term and send them to a given topic in Kafka
* A consumer that will parse the Tweet data and store each Tweet in a different json file in a given folder.

## Insights
Some insights to help you:
* to implement the producer, you can get inspiration from the implementation of the `StdOutListener` in `twitter_listener.py` and add the publishing process in the `on_data` method. 
* to implement the consumer, you can get inspiration from the `consumer_to_json.py` file.
* "trump" is a good subject to perform the streaming as there are a lot of Tweets on this subject.
* the messages in Kafka are written in bytes and not in string so you might have to encode/decode the content of the messages.