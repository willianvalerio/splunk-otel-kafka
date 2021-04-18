FROM maven:3.6.0-jdk-8-slim AS build
WORKDIR /app
COPY . .
RUN mvn clean package
RUN curl -L https://github.com/signalfx/splunk-otel-java/releases/latest/download/splunk-otel-javaagent-all.jar \
     -o splunk-otel-javaagent.jar

FROM openjdk:8-jre-slim
WORKDIR /app
COPY --from=build /app/target/producer-1.0-SNAPSHOT.jar producer.jar
COPY --from=build /app/splunk-otel-javaagent.jar splunk-otel-javaagent.jar

ENTRYPOINT ["java","-javaagent:./splunk-otel-javaagent.jar","-jar","./producer.jar"]