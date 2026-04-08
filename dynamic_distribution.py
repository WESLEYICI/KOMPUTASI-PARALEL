import random
import time

# Simulasi jumlah task yang berubah-ubah (dynamic)
def generate_tasks(n):
    return [random.randint(1, 100) for _ in range(n)]

# Simulasi proses distribusi (misalnya ke beberapa worker)
def dynamic_distribution(tasks, workers):
    start_time = time.time()
    
    worker_load = [0] * workers
    
    for task in tasks:
        # pilih worker dengan beban terkecil (dynamic balancing)
        min_worker = worker_load.index(min(worker_load))
        worker_load[min_worker] += task
    
    end_time = time.time()
    
    total_time = end_time - start_time
    return worker_load, total_time

# Simulasi beberapa kali untuk cari waktu optimal
workers = 4
results = []

for i in range(5, 51, 5):  # jumlah task berubah
    tasks = generate_tasks(i)
    load, exec_time = dynamic_distribution(tasks, workers)
    
    results.append((i, exec_time))
    print(f"Jumlah Task: {i}")
    print(f"Distribusi Load: {load}")
    print(f"Waktu Eksekusi: {exec_time:.6f} detik\n")

# Cari waktu optimal (minimum)
optimal = min(results, key=lambda x: x[1])

print("=== HASIL OPTIMAL ===")
print(f"Jumlah Task Optimal: {optimal[0]}")
print(f"Waktu Tercepat: {optimal[1]:.6f} detik")