# splunk-otel-kafka
How to track kafka components with Splunk Observability Cloud and Opentelemetry

## Prerequisites

- docker
- docker-compose

## Up and Running

Set these following variables

```bash
export SPLUNK_ACCESS_TOKEN=YOUR_SPLUNK_ACCESS_TOKEN
export SPLUNK_REALM=YOUR_SPLUNK_REALM
```

Up and build containers

```bash
docker-compose up -d --build --remove-orphans
```

## Clean Up

```bash
docker-compose down --remove-orphans
```
