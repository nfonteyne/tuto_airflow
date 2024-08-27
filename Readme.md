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
