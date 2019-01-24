#!/usr/bin/python3

from tweepy.streaming import StreamListener, Stream
from tweepy import OAuthHandler
import json
import argparse


def parsing_authentication(path='credentials.auth'):
    # opening the file containing the Twitter credentials
    with open(path, 'r') as credentials_file:
        credentials = credentials_file.read()
    credentials = credentials.split('\n')[:4]

    # making the credentials into a dictionary
    name_of_credentials = ['consumer_key', 'consumer_secret', 'access_token_key', 'access_token_secret']
    credentials = dict(zip(name_of_credentials, credentials))

    return credentials


class StdOutListener(StreamListener):
    """
    Custom Listener of streaming Tweets that will print the data into the terminal
    """
    def __init__(self, count=10000):
        """
        creates a Custom Listener of Tweets that will end after a given amount of streamed Tweets
        :param count: number of Tweets to stream
        """
        # instantiating the super class StreamListener
        StreamListener.__init__(self)
        self.max_count = count
        self.counter = 0

    def on_data(self, data):
        """
        prints name of the author of the Tweet and content in the terminal
        :param data: full data of the Tweet
        :return: True if there are still Tweets to stream, else False ending the stream
        """
        # incrementing the counter
        self.counter += 1

        # if we reach the counter maximum, we need to end the stream
        if self.counter == self.max_count:
            return False

        # else we print the content of the Tweet
        # first we need to parse the data into a dictionary
        data_dictionary = json.loads(data)
        print('\nTweet\t{}/{}'.format(self.counter+1, self.max_count))
        print('Author:\t', data_dictionary['user']['screen_name'])
        print('Content:', data_dictionary['text'])
        return True

    def on_error(self, status):
        """
        ends the stream and prints the error code
        :param status: error code
        :return: False ending the stream
        """
        print('The stream ended with status error:' + status)
        return False


if __name__ == '__main__':

    # defining an argument parser to take the number of Tweets to stream,
    # the path to the credentials file,
    # the subjects to stream
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--count', type=int, default=1000)
    argument_parser.add_argument('--path', type=str, default='credentials.auth')
    argument_parser.add_argument('--subjects', type=str, default='trump',
                                 help='you can define several subjects by separating them with comma.')

    # getting the limit of tweets and the path to credentials
    arguments = argument_parser.parse_args()
    tweets_count = arguments.count
    path_to_credentials = arguments.path
    subjects_to_stream = arguments.subjects.split(',')

    print('streaming {} Tweets on "{}"'.format(tweets_count, '", "'.join(subjects_to_stream)))

    # getting the credentials
    twitter_credentials = parsing_authentication(path=path_to_credentials)

    # creating an authentication handler
    authentication_handler = OAuthHandler(consumer_key=twitter_credentials['consumer_key'],
                                          consumer_secret=twitter_credentials['consumer_secret'])
    authentication_handler.set_access_token(key=twitter_credentials['access_token_key'],
                                            secret=twitter_credentials['access_token_secret'])

    # instantiating a listener
    stdout_listener = StdOutListener(count=tweets_count)

    # creating a stream object
    stream = Stream(auth=authentication_handler, listener=stdout_listener)

    # stream Tweets
    stream.filter(track=subjects_to_stream)
