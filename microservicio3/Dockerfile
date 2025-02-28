FROM python:alpine
COPY app.py demo.json requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./app.py" ]