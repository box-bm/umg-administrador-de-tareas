import psutil

def listar_procesos():
    print(f"{'PID':<9} {'Nombre':<41} {'CPU %':<10} {'Memoria MB':<15} {'Estado'}")
    print("-" * 90)
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'status']):
        try:
            pid = proc.pid
            name = (proc.name().strip()[:37] + '...') if len(proc.name().strip()) > 40 else proc.name().strip()
            cpu = proc.cpu_percent()
            mem = proc.memory_info().rss / (1024 * 1024)
            status = proc.status()
            
            mem_mb = f"{mem:.2f} MB"
            print(f"{pid:<9} {name:<41} {cpu:<10} {mem_mb:<15} {status}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == "__main__":
    listar_procesos()