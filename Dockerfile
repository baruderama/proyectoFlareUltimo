
FROM python:3.8


WORKDIR /app

# Copia los archivos de requerimientos (requirements) y el archivo manage.py
COPY requirements.txt ./
COPY manage.py .

# Instala las dependencias de la aplicación
RUN pip install -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expon el puerto en el que se ejecutará la aplicación (por ejemplo, el puerto 8000)
EXPOSE 8000

# Ejecuta el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
