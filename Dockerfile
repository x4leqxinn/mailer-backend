FROM python:3.9
WORKDIR /workspace
COPY requirements.txt /workspace
RUN pip install pip --upgrade && \ 
    pip install -r requirements.txt --no-cache-dir
COPY . .