# FROM python
FROM --platform=linux/x86-64 python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "src/app.py"]