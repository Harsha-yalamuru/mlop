FROM python:3.9-slim 
WORKDIR /app 
COPY requirements.txt . 
RUN pip install -r requirements.txt 
COPY . . 
CMD ["python", "predict_api.py"] 
# Build and run 
#docker build -t iris-api . 
#docker run -p 5000:5000 iris-api 