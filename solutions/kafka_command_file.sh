#!/usr/bin/env bash

# creating a Kafka path to ease the following
export KAFKA_HOME=/home/hduser/kafka

# launching zookeeper server

echo "launching zookeeper server"
${KAFKA_HOME}/bin/zookeeper-server-start.sh ${KAFKA_HOME}/config/zookeeper.properties >> ~/log.zookeeper &

# launching kafka server
echo "launching kafka server"
${KAFKA_HOME}/bin/kafka-server-start.sh ${KAFKA_HOME}/config/server.properties >> ~/log.kafka &

# creating the topic
echo "creating the topic trump"
${KAFKA_HOME}/bin/kafka-topics.sh \
--create --topic trump \
--zookeeper localhost:2181 \
--partitions 1 \
--replication-factor 1