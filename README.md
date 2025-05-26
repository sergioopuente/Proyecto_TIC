# Proyecto TIC
- Comparativa de Rendimiento entre Máquinas Virtuales y Docker

Este repositorio contiene el proyecto realizado para la asignatura de TIC, centrado en una comparativa de rendimiento entre máquinas virtuales (VMs) ejecutadas con VirtualBox y contenedores Docker. El objetivo principal es analizar el comportamiento de ambos entornos frente a distintas cargas de trabajo.

- Objetivo del proyecto
El fin de este estudio es cuantificar y comparar de forma empírica la eficiencia de las VM frente a Docker, mediante el uso de herramientas de benchmarking y análisis sistemático de datos.

Objetivos específicos:

* Medir el rendimiento de la CPU y la memoria en escenarios controlados.
* Evaluar la velocidad de escritura en disco.
* Analizar el rendimiento de red local.
* Comparar tiempos de ejecución y consumo de recursos.

⚙- Metodología
Todas las pruebas se han realizado en el mismo host físico para garantizar imparcialidad:

* **CPU:** AMD Ryzen (host)
* **RAM:** 16 GB
* **Sistema Operativo:** Windows 11
* **VM:** Ubuntu Server 22.04 en VirtualBox
* **Docker:** Imagen `ubuntu:22.04`

Herramientas utilizadas:

* `sysbench` para test de CPU
* `stress-ng` para carga combinada de CPU y RAM
* `fio` para rendimiento de escritura secuencial en disco
* `iperf3` para ancho de banda de red local

🛦 Estructura del repositorio

```
Proyecto_TIC
├── src
│   └── setup_vm.sh / setup_docker.sh (vacíos)
├── pruebas
│   

```
