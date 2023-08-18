# Usa la imagen oficial de Python como base
FROM python:3.8

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]