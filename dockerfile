FROM jupyter/scipy-notebook:latest

USER root

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    pip install pyspark python-dotenv pandas && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

USER $NB_UID
