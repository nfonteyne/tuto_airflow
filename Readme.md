# Airflow instance with docker

## Creating directories

```shell
mkdir -p ./dags ./logs ./plugins ./config
```

## Initialize the database

```shell
docker compose up airflow-init
```

## Running Airflow

```shell
docker compose up -d
```

## Cleaning up

```shell
docker compose down --volumes --rmi all
```

## Extend python dependencies

Create a requirements.txt with de python libraries that you want to add
Create a Dockerfile :

```Dockerfile
FROM apache/airflow:2.10.0
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt
```

Build the DockerFile :
```shell
docker build . --tag extending_airflow:latest
```

rebuild the webserveur and the scheduler tu update de python dependencies :

```
docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler
```
