FROM python:3.6
LABEL maintainer="antoinecabon3@gmail.com"
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt
EXPOSE 8030
ENTRYPOINT ["python"]
CMD ["src/wsgi.py"]
