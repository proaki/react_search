FROM python:3.8

EXPOSE 5000

COPY . .

RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]