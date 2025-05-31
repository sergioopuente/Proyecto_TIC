FROM python:3.10-slim

# Actualizar paquetes e instalar herramientas necesarias
RUN apt update && apt install -y sysbench git curl procps stress-ng fio iperf3 \
    && pip install --upgrade pip \
    && pip install jupyter matplotlib pandas psutil seaborn

# Establecer directorio de trabajo
WORKDIR /app/scripts

# Copiar el contenido actual del directorio al contenedor
COPY . .

# Comando por defecto al iniciar el contenedor
CMD ["python3", "benchmark_docker.py"]
