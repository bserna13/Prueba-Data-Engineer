# Usa una imagen base oficial de PostgreSQL
#FROM postgres

# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requerimientos.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requerimientos.txt

#RUN psql -h db -U brahian -f prueba.sql prueba

# Copia el resto de la aplicación
COPY . .

# Comando para correr la aplicación
CMD ["python", "main.py"]


