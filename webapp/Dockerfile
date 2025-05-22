FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt

ENV PIP_NO_PROGRESS_BAR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_PROGRESS_BAR=off

RUN pip install --no-cache-dir --progress-bar=off -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
