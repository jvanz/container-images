FROM openjdk:11

RUN mkdir /app
WORKDIR /app

COPY MainClass.java MainClass.java

RUN javac MainClass.java

ENTRYPOINT ["java", "-XX:+UseContainerSupport", "-XX:MaxRAMPercentage=75"]
CMD ["MainClass"]
