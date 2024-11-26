FROM tensorflow/tensorflow:2.18.0
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]