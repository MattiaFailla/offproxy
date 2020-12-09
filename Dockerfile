FROM python:3.8.2
RUN useradd -ms /bin/bash admin
COPY --chown=admin:admin . /docker_app
WORKDIR /docker_app

RUN pip install -r requirements.txt && \

EXPOSE 3000

USER admin

CMD python ./app.py