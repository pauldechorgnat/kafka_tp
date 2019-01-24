# Apache Kafka Practice

This repo is aimed to contain the practical case for Apache Kafka Python API in the the Data Engineering training of DataScientest.

## Description of the files 
* **twitter_listener.py** : custom stream listener that takes a given number of tweets and print them in real time in a terminal.
* **command_line_producer.py** : script that takes a given message, a topic and a list of hosts and publish a message to kafka.
* **consumer_to_json.py** : script that takes a given topic and a list of hosts to get data from kafka and dump them into a json format. 
* **requirements.txt** : list of required python packages.


## Usage 
To use the twitter listener, you need to have a file containing the Twitter Developer API credentials in a separate file.
