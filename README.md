# Fast API Mailer backend

The project consists of a backend controller to manage email sending in Python.

## Requirements

- Python (3.11.3)
- Docker (optional, for running in a container)

## Environment variables

- Create two environment variable configuration files named .env.dev and .env.prod, using the template.env file as a reference

## Installation without docker

- 1. Clone the repository:

```bash
    git clone https://github.com/x4leqxinn/mailer-backend.git
```
- 2. Go to project path:

```bash
    cd project-name-path
```
- 3. Virtual environment:

```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
```

- 4. Install requirements:

```bash
    pip install -r docker/development/requirements.txt
```

## Usage

- 1. Run app
```bash
    python app/main.py
```

## Usage with Docker (optional)
- 1. Run docker compose:

```bash
    docker compose up --build
```

## Server

- 2. Open your web browser and access http://localhost:8000 to interact with the application.

## Credits
Author: Jorge Quintui
