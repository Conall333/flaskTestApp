FROM python:3.6
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python3 -m pip install --user --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]