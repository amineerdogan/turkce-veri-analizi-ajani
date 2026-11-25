FROM python:3.11-slim

RUN pip install --no-cache-dir pandas matplotlib plotly numpy openpyxl xlrd

RUN useradd -m runner
USER runner
WORKDIR /work
