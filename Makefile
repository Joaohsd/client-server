start:
	chmod +x setup/start.sh
	./setup/start.sh

runServer:
	chmod +x venv/bin/activate
	./venv/bin/activate
	python3 src/server/server.py

runClient:
	chmod +x venv/bin/activate
	./venv/bin/activate
	python3 src/client/client.py
