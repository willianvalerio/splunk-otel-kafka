FROM maven:3.6.0-jdk-8-slim AS build
WORKDIR /app
COPY . .
RUN mvn clean package

FROM openjdk:8-jre-slim
COPY --from=build /app/target/consumer-1.0-SNAPSHOT.jar /usr/local/lib/consumer.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","/usr/local/lib/consumer.jar"]