# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim-buster AS base

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Install pip requirements
COPY ./src /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
# biblioteca para conexao com sqlserver
ADD odbcinst.ini /etc/odbcinst.ini
RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev iputils-ping
RUN apt install unixodbc-bin -y


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

#################### START NEW IMAGE: DEBUG #################################

FROM base as debug
EXPOSE 5678
RUN python -m pip install ptvsd

CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m streamlit run datascience.py --server.port 8000
#################### START NEW IMAGE: PROD #################################
FROM base as prod

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi"]
CMD streamlit run datascience.py --server.port 8000