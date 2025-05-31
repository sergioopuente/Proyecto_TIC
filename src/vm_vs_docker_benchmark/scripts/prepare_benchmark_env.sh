#!/bin/bash

echo "📦 Actualizando sistema y preparando entorno en Docker..."

# Actualización e instalación de paquetes
apt update && apt install -y \
    sysbench \
    stress-ng \
    fio \
    iperf3 \
    curl \
    git \
    procps \
    python3 \
    python3-pip \
    python3-psutil \
    nano

# Crear estructura de directorios
mkdir -p /app/results/docker
mkdir -p /app/scripts

echo "✅ Entorno Docker listo para benchmarking."
