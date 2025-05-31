#!/bin/bash

echo "🔧 Configurando entorno de benchmarking en máquina virtual..."

# Actualizar repositorios e instalar herramientas necesarias
sudo apt update && sudo apt install -y \
    sysbench \
    stress-ng \
    fio \
    iperf3 \
    python3 \
    python3-pip \
    python3-psutil \
    curl \
    git \
    nano \
    htop

# Crear estructura de carpetas para resultados si no existe
mkdir -p ~/benchmark_vm/scripts
mkdir -p ~/benchmark_vm/results

echo "✅ Entorno en VM listo. Puedes comenzar las pruebas."
