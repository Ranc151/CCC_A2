FROM python:3.9

WORKDIR /backend

COPY . /backend

RUN pip install couchdb;\
    pip install flask;\
    pip install flask-restful;\
    pip install flask_script;\
    pip install flask_migrate;\
    pip install flask-cors;\
    pip install pandas; \
    pip install mpi4py; \
    pip install mastodon.py


EXPOSE 8080
EXPOSE 5000

CMD ["python", "./app.py"]