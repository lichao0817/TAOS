# TAOS API Server

## Overview
This is the documentation for TAOS API. The API has 2 parts: owners (accounting firms) and clients.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 init_db.py
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/lichao0817/TAOS/1.0.0/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/lichao0817/TAOS/1.0.0/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```
