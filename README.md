# client-server

This repository is used to present the development of first work in "C115 - Conceitos e Tecnologias para Dispostivos Conectados" subject from INATEL.

## **Pre-requirements**
---
*   Python 3.8+
*   Make

## **Docker**
---
In order to start the containers of mongo application and mongo-express application run the command above.

```shell
docker compose -f docker/docker-compose.yml up
```

## **Makefile**
---
In order to **start** project run the command below. This command will create a new virtual environment with all required modules used in this project.

```shell
make start
```

If you do not have **make** installed, you can use (**for Linux environment**):

```shell
chmod +x scripts/start.sh
./scripts/start.sh
```

In order to run this project, after installed all required dependencies, just use make:

```shell
make run
```

If you do not have **make** installed, you can use (**for Linux environment**):

```shell
python3 src/main.py
```