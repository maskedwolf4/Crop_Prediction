FROM python:3.11
COPY . /CPapp
WORKDIR /CPapp
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["uvicorn", "CPapp.server:CPapp", "--host", "0.0.0.0", "--port", "5001"]