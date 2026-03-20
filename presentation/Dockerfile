FROM python:3.13-slim

RUN pip install --no-cache-dir python-pptx

WORKDIR /presentation

ENTRYPOINT ["python", "scripts/generate_presentation.py"]
