FROM python:3

ADD src /src

RUN pip install pystrich

RUN pip install pandas

CMD ["python", "./src/name_script.py"]
