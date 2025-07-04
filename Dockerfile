FROM python:3.10-slim

WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y ffmpeg git && apt-get clean

# Copia los archivos
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
