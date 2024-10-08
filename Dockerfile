FROM python:3.12-alpine
RUN pip install --upgrade pip && pip install setuptools==69.0.1

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]