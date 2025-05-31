import os
import subprocess
import json
import time
import psutil

RESULTS_PATH = "../results/docker"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_json(filename, data):
    with open(os.path.join(RESULTS_PATH, filename), "w") as f:
        json.dump(data, f, indent=4)

def save_output_txt(filename, content):
    with open(os.path.join(RESULTS_PATH, filename), "w") as f:
        f.write(content)

def capture_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "used_memory_MB": round(psutil.virtual_memory().used / 1024 / 1024, 2),
        "timestamp": time.time()
    }

def run_test(name, command):
    print(f"🧪 Running {name}...")
    start = time.perf_counter()
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    duration = time.perf_counter() - start
    save_output_txt(f"{name}_docker.txt", result.stdout)
    return {
        "cpu": round(psutil.cpu_percent(interval=1), 2),
        "memory": round(psutil.virtual_memory().used / 1024 / 1024, 2),
        "time": duration
    }

def main():
    print("🐳 Starting Docker benchmark...\n")
    ensure_dir(RESULTS_PATH)

    # Metrics before
    docker_before = capture_metrics()
    save_json("docker_before_metrics.json", docker_before)

    results = {}

    results["cpu_test"] = run_test("cpu_test", ["sysbench", "cpu", "--cpu-max-prime=20000", "run"])
    results["stress_test"] = run_test("stress_test", ["stress-ng", "--cpu", "4", "--vm", "2", "--vm-bytes", "512M", "--timeout", "15s"])
    results["disk_test"] = run_test("disk_test", [
        "fio", "--name=seqwrite", "--rw=write", "--bs=1M",
        "--size=256M", "--numjobs=1", "--time_based", "--runtime=10s", "--group_reporting"
    ])
    results["network_test"] = run_test("network_test", ["iperf3", "-c", "localhost", "-t", "10"])

    # Metrics after
    docker_after = capture_metrics()
    save_json("docker_after_metrics.json", docker_after)
    save_json("summary_metrics_docker.json", results)

    print("\n✅ Docker benchmarking complete. Results in 'results/docker/'")

if __name__ == "__main__":
    main()
