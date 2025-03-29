import psutil

# Function que se encarga de listar los procesos en ejecución
def listar_procesos():
    procesos = []
    print(f"{'PID':<9} {'Nombre':<41} {'CPU %':<10} {'Memoria MB':<15} {'Estado'}")
    print("-" * 90)
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'status']):
        try:
            # Obtenemos el PID
            pid = proc.pid
            
            # Obtenemos el nombre del proceso
            name = proc.name()
            # Recortamos el nombre para no desordenar la tabla
            showed_name = (name.strip()[:37] + '...') if len(proc.name().strip()) > 40 else proc.name().strip()
            
            # Obtenemos el CPU %
            cpu = proc.cpu_percent()
            
            # Obtenemos la memoria en MB
            mem = proc.memory_info().rss / (1024 * 1024)
            mem_mb = f"{mem:.2f} MB" # Redondeamos a 2 decimales y agregamos MB para mostrar un listado
            
            # Obtenemos el estado del proceso
            status = proc.status()
        
            # Agregamos a la lista de procesos para retornarlo mas adelante.
            procesos.append((pid, name, cpu, mem, status))
            
            # Mostramos la información del proceso
            print(f"{pid:<9} {showed_name:<41} {cpu:<10} {mem_mb:<15} {status}")
            
        # En caso de que el proceso no exista o no tengamos permisos para acceder a el, continuamos con el siguiente proceso.
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort the processes by RAM usage in descending order
    procesos.sort(key=lambda x: x[3], reverse=True)
    return procesos