# 🧪 Proyecto TIC – Comparativa de Rendimiento entre Máquinas Virtuales y Contenedores Docker

Este repositorio contiene el desarrollo completo del proyecto final de la asignatura "Tecnologías de la Información y la Comunicación" (TIC), centrado en el análisis de rendimiento entre máquinas virtuales (VMs) y contenedores Docker. El objetivo es realizar una evaluación cuantitativa del uso de recursos y la eficiencia operativa de ambos entornos bajo diferentes escenarios prácticos.

---

## 📌 Objetivos del Proyecto

**Objetivo general:**

* Comparar de forma empírica el rendimiento y consumo de recursos de máquinas virtuales y contenedores Docker usando pruebas de benchmarking.

**Objetivos específicos:**

* Evaluar el rendimiento de la CPU (en pruebas mono y multinúcleo).
* Medir el uso de memoria RAM en escenarios de carga alta y baja.
* Comparar el rendimiento de disco mediante pruebas secuenciales de escritura y lectura.
* Analizar el uso de recursos en estado inactivo.
* Evaluar la latencia y rendimiento en creación masiva de procesos.
* Comparar el rendimiento de red con transferencia simulada local.
* Analizar las métricas de sistema antes y después de las pruebas.

---

## ⚙️ Metodología y Entorno de Pruebas

Todas las pruebas se han ejecutado en el mismo sistema anfitrión para mantener coherencia en las métricas obtenidas:

* **Host físico:**

  * CPU: AMD Ryzen
  * RAM: 16 GB DDR4
  * Sistema Operativo: Windows 11

* **Entorno virtualizado:**

  * VirtualBox con Ubuntu Server 22.04

* **Entorno en contenedor:**

  * Docker Engine con imagen `ubuntu:22.04`

* **Entorno WSL (Windows Subsystem for Linux):**

  * Ubuntu 22.04

* **Lenguajes/Scripts:**

  * Bash, Python 3
  * Notebooks en Jupyter para visualización

---

## 🧰 Herramientas Utilizadas

| Herramienta | Propósito                          |
| ----------- | ---------------------------------- |
| sysbench    | Benchmark de CPU y memoria         |
| stress-ng   | Carga combinada de CPU y RAM       |
| fio         | Escritura secuencial en disco      |
| iperf3      | Simulación de transferencia de red |
| psutil      | Extracción de métricas del sistema |
| Jupyter     | Visualización de resultados        |
| Git/GitHub  | Control de versiones               |

---

## 📦 Estructura del Repositorio

```
Proyecto_TIC
├── src
│   ├── benchmark_vm.py
│   ├── benchmark_docker.py
│   ├── prepare_vm_environment.sh
│   └── configure_docker_env.sh
├── scripts
│   └── Dockerfile
├── pruebas
│   ├── vm
│   │   ├── cpu_test_vm.txt
│   │   ├── memory_test_vm.txt
│   │   ├── disk_test_vm.txt
│   │   └── network_test_vm.txt
│   ├── docker
│   │   ├── cpu_test_docker.txt
│   │   ├── memory_test_docker.txt
│   │   ├── disk_test_docker.txt
│   │   └── network_test_docker.txt
│   └── wsl
│       ├── cpu_test_wsl.txt
│       ├── memory_test_wsl.txt
│       ├── disk_test_wsl.txt
│       └── network_test_wsl.txt
├── results
│   ├── vm_before_metrics.json
│   ├── vm_after_metrics.json
│   ├── docker_before_metrics.json
│   ├── docker_after_metrics.json
│   ├── wsl_before_metrics.json
│   ├── wsl_after_metrics.json
├── notebooks
│   ├── analyze_docker_performance.ipynb
│   ├── analyze_vm_performance.ipynb
│   └── compare_vm_vs_docker.ipynb
└── README.md
```

---

## 🧪 Pruebas Realizadas

Cada entorno (VM, Docker y WSL) se sometió a los siguientes tests:

1. **Idle (reposo):** Captura del consumo sin carga.
2. **CPU Stress (sysbench):** Uso intensivo de CPU con `--cpu-max-prime=20000`.
3. **CPU Multi-Core (stress-ng):** Prueba de carga simultánea.
4. **Memory Stress (stress-ng):** Uso de hasta 1GB de RAM.
5. **Memory Large (sysbench):** Lectura/escritura secuencial.
6. **Disk I/O (fio):** Escritura de 256MB con bloques de 1MB.
7. **Disk Read (fio):** Lectura secuencial del archivo generado.
8. **Network Download (iperf3):** Simulación de transferencia a localhost.
9. **Process Spawn (stress-ng):** Creación masiva de procesos.

Todos los resultados se almacenan como `.txt` (output) y `.json` (métricas cuantitativas).

---

## 📊 Resultados Ejemplo (Docker CPU test):

```json
"cpu_stress": {
  "cpu": 91.28,
  "memory": 50.79,
  "time": 5.01
}
```

---

## 📈 Análisis y Conclusiones

* **CPU:** Docker demostró ser más eficiente en tareas monohilo y multihilo.
* **Memoria:** VM tiene mayor consumo base. Docker solo escala en uso cuando se requiere.
* **Disco:** Docker mostró mayor velocidad de escritura y lectura que la VM.
* **Red:** En pruebas localhost, Docker se comportó ligeramente mejor.
* **WSL:** Rendimiento intermedio entre VM y Docker.

**Conclusión:**

* Docker es ideal para entornos ligeros y desarrollo rápido.
* Las VM ofrecen mejor aislamiento del sistema.
* La elección depende del contexto: rendimiento puro (Docker) vs compatibilidad y aislamiento (VM).

---

## 📚 Recursos Adicionales

* [Sysbench](https://github.com/akopytov/sysbench)
* [Docker Documentation](https://docs.docker.com)
* [VirtualBox](https://www.virtualbox.org/)
* [stress-ng](https://manpages.ubuntu.com/manpages/jammy/man1/stress-ng.1.html)
* [fio](https://github.com/axboe/fio)
* [iperf3](https://iperf.fr/)

---

## 👨‍💻 Autor

* Sergio Puente
* Universidad Europea del Atlántico (UNEATLANTICO)
* Curso: 2024/2025 – Ingeniería Informática – 1º curso
