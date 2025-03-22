# Administrador de Tareas en Python

Este proyecto es un **Administrador de Tareas** desarrollado en Python como parte del curso de **Sistemas Operativos**. Permite visualizar, monitorear y gestionar los procesos del sistema mediante una interfaz gráfica.

## 🚀 Funcionalidades

- 🔍 **Listado de procesos activos** con ID, nombre, uso de CPU y memoria, y estado.
- 🔄 **Actualización en tiempo real** de los procesos en ejecución.
- 🛑 **Control de procesos**:
  - Finalizar (Kill)
  - Suspender (Suspend)
  - Reanudar (Resume)
- 🖼️ **Interfaz gráfica amigable** construida con `tkinter` o `PyQt`.

## 🧰 Tecnologías usadas

- Python 3.x
- [`psutil`](https://pypi.org/project/psutil/): para obtener información de procesos del sistema.
- [`tkinter`](https://docs.python.org/3/library/tkinter.html): para la interfaz gráfica (alternativamente se puede usar PyQt5).

## 📦 Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/administrador-tareas-python.git
    cd administrador-tareas-python
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

3. Ejecuta el script principal:

    ```bash
    python main.py
    ```
