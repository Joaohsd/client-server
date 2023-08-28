# client-server

This repository is used to present the development of first work in "C115 - Conceitos e Tecnologias para Dispostivos Conectados" subject from INATEL.

## **Pre-requirements**
*   Python 3.8+
*   Make
*   Docker

## **Docker**
In order to start the containers of mongo application and mongo-express application run the command above. Maybe, it is necessary to execute as **sudo** if your user is not in the docker group.

```shell
docker compose -f docker/docker-compose.yml up
```

## **Makefile**
For each **client** and **server**, in order to **start** project run the command below. This command will create a new virtual environment with all required modules used in this project.

```shell
make start
```

If you do not have **make** installed, you can use (**for Linux environment**):

```shell
chmod +x scripts/start.sh
./scripts/start.sh
```

In order to run this project, after started the virtual environment that contains all required external dependencies, just use make:

*   Running Server
```shell
make runServer
```

*   Running Client
```shell
make runClient
```

If you do not have **make** installed, you can use (**for Linux environment**):

*   Running Server
```shell
python3 src/server/server.py
```

*   Running Client
```shell
python3 src/client/client.py
```