FROM python:3-alpine

COPY netcat.py /programa/netcat.py
COPY proba.py /programa/proba.py

RUN mkdir datuak

WORKDIR /programa

#CMD ["tail","-f","/dev/null"]
CMD ["python3","proba.py"]