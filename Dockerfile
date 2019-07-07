FROM python:3.7.3-stretch

ADD ./ /velocore
COPY configs /etc/velocore/

WORKDIR /velocore
ENV PYTHONPATH "${PYTONPATH}:/velocore/"

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile
CMD ["python", "velo_core/main.py"]