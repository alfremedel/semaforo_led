Sistema de Semáforo con Raspberry Pi y Python
Proyecto desarrollado para la materia de Sistemas Embebidos, enfocado en el control de hardware mediante los pines GPIO de una Raspberry Pi utilizando Python y la librería gpiozero.

📋 Descripción del Proyecto
Este repositorio contiene scripts orientados a la práctica de sistemas embebidos, destacando el control secuencial de un semáforo (LEDs rojo, amarillo y verde) con retardos de tiempo y gestión segura de interrupciones, además de otras prácticas complementarias de parpadeo y recorridos de luces.

🧰 Componentes Utilizados
Raspberry Pi (cualquier modelo con pines GPIO de 40 pines).

LEDs:

1x LED Rojo

1x LED Amarillo

1x LED Verde

Resistencias: 3x resistencias de 220Ω o 330Ω.

Cables de conexión (Jumpers) y Protoboard.

⚡ Esquema de Conexiones (Pines BCM)
Componente	Pin GPIO (Raspberry Pi)	Conexión Física
LED Rojo	GPIO 17	Ánodo → Resistencia → GPIO 17
LED Amarillo	GPIO 27	Ánodo → Resistencia → GPIO 27
LED Verde	GPIO 22	Ánodo → Resistencia → GPIO 22
Cátodos (GND)	GND	Común a todos los LEDs
🚀 Instalación y Ejecución
Actualizar el sistema e instalar la librería GPIO:

Bash
sudo apt update
sudo apt install python3-gpiozero
Clonar el repositorio:


cd semaforo_led
Ejecutar el script del semáforo:

Bash
python3 semaforo.py
(Presiona Ctrl + C para detener la ejecución y apagar los LEDs de forma segura).

📂 Estructura del Repositorio
semaforo.py - Control cíclico de las tres luces del semáforo con advertencia y apagado seguro.

PRACTICALEDBLINK.PY - Práctica básica de parpadeo (Blink) de un LED.

recorridoled.py - Secuencia de desplazamiento de luces.

BOARD.PY - Script de configuración inicial y mapeo de pines.

👤 Autor
Alumno: Medel Rosas Alfredo
