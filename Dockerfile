# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Install pip requirements
COPY requirements.txt .
COPY ./src /app

RUN python -m pip install -r requirements.txt
WORKDIR /app

# biblioteca para conexao com sqlserver
ADD odbcinst.ini /etc/odbcinst.ini
RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev iputils-ping
RUN apt install unixodbc-bin -y
RUN apt-get clean -y

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi"]
CMD ["streamlit","run","datascience.py","--server.port", "8000"]