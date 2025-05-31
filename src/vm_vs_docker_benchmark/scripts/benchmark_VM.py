import os
import subprocess
import time
import json
import psutil

def create_results_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def capture_sysinfo():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "used_memory_MB": round(psutil.virtual_memory().used / 1024 / 1024, 2),
        "timestamp": time.time()
    }

def execute_benchmark(label, command, results_path):
    print(f"📌 Executing: {label}")
    start = time.perf_counter()
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    duration = time.perf_counter() - start

    output_file = os.path.join(results_path, f"{label}_vm.txt")
    with open(output_file, "w") as f:
        f.write(process.stdout)

    return {
        "cpu": round(psutil.cpu_percent(interval=1), 2),
        "memory": round(psutil.virtual_memory().used / 1024 / 1024, 2),
        "time": duration
    }

def main():
    output_dir = "../results/vm"
    create_results_dir(output_dir)

    print("🚀 Starting VM benchmark suite...\n")

    # Snapshot before
    before_metrics = capture_sysinfo()
    with open(os.path.join(output_dir, "vm_before_metrics.json"), "w") as f:
        json.dump(before_metrics, f, indent=4)

    results = {
        "cpu_test": execute_benchmark("cpu_test", ["sysbench", "cpu", "--cpu-max-prime=20000", "run"], output_dir),
        "memory_test": execute_benchmark("memory_test", ["sysbench", "memory", "run"], output_dir),
        "disk_test": execute_benchmark("disk_test", [
            "fio", "--name=seqwrite", "--rw=write", "--bs=1M",
            "--size=256M", "--numjobs=1", "--time_based", "--runtime=10s", "--group_reporting"
        ], output_dir),
        "network_test": execute_benchmark("network_test", ["iperf3", "-c", "localhost", "-t", "10"], output_dir)
    }

    # Snapshot after
    after_metrics = capture_sysinfo()
    with open(os.path.join(output_dir, "vm_after_metrics.json"), "w") as f:
        json.dump(after_metrics, f, indent=4)

    with open(os.path.join(output_dir, "summary_metrics_vm.json"), "w") as f:
        json.dump(results, f, indent=4)

    print("\n✅ VM benchmark completed. All results saved to:", output_dir)

if __name__ == "__main__":
    main()
