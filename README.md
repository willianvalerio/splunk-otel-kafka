# splunk-otel-kafka
How to track kafka components with Splunk Observability Cloud and Opentelemetry

## Prerequisites

- docker
- docker-compose

## Up and Running

Set these following variables

```bash
export SPLUNK_ACCESS_TOKEN=YOUR_SPLUNK_ACCESS_TOKEN
```

```bash
export SPLUNK_REALM=YOUR_SPLUNK_REALM
```

Up and build containers

```bash
docker-compose up -d --build --remove-orphans
```

## Outcomes

After some seconds, your Service Map in Splunk Observability Cloud will looks like this:

![servicemap](/img/servicemap.png)

## Kafka test/troubleshooting

You can use the `kafkacat` container to perform tests, create new topics and troubleshooting in an easy way.

Open a terminal and execute the following commands:

```bash
docker exec -ti kafka-cat bash
kafkacat -P -b kafka:9092 -t test
message1
message2
```

In a second terminal execute the following commands:

```bash
docker exec -ti kafka-cat bash
kafkacat -b kafka:9092 -t test
```
At the second terminal you should see the messages being consumed

## Clean Up

```bash
docker-compose down --remove-orphans
```
