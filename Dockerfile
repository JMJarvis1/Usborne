FROM python:3.11

# Install Java
RUN apt update && apt install -y sudo && sudo apt install default-jdk -y

## Pip dependencies
# Upggrade pip
RUN pip install --upgrade pip
# Install production dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirments.txt
# Install development dependencies
COPY requirements-dev.txt /tmp/requiremnts-dev.txt
RUN pip install -r /tmp/requirements-dev.txt && rm /tmp/requirements-dev.txt
