FROM python:3.9-slim

# Instalar dependencias
RUN pip install mysql-connector-python

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . /app

# Mantener el contenedor encendido para poder entrar a ejecutar los scripts
CMD ["tail", "-f", "/dev/null"]