FROM python:3.8-slim

# Instala las dependencias necesarias 
RUN apt-get update && \
    apt-get install -y \
    ansible \
    && rm -rf /var/lib/apt/lists/*

# Copia tu aplicacion Flask al contenedor 
WORKDIR /app
COPY . .

# Instala las dependencias de Python 
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre tu aplicacion Flask
EXPOSE 5000

# Comando para ejecutar tu aplicacion Flask 
CMD ["python", "app.py"]


