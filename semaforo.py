import time
from gpiozero import LED

# Configuración de los pines GPIO (BCM) de la Raspberry Pi
# Ajusta los números de pin según las conexiones físicas de tu circuito
LED_ROJO = LED(17)     # Pin GPIO 17
LED_AMARILLO = LED(27) # Pin GPIO 27
LED_VERDE = LED(22)    # Pin GPIO 22

def encender_solo(led_activo):
    """Apaga todos los LEDs y enciende únicamente el indicado."""
    LED_ROJO.off()
    LED_AMARILLO.off()
    LED_VERDE.off()
    led_activo.on()

def ciclo_semaforo():
    print("Iniciando secuencia de semáforo... (Presiona Ctrl+C para detener)")
    try:
        while True:
            # 1. Luz Verde (Permiso de paso)
            print("[+] Verde: Avanzar")
            encender_solo(LED_VERDE)
            time.sleep(5)  # Tiempo en verde (segundos)

            # Parpadeo de advertencia en Verde
            for _ in range(3):
                LED_VERDE.off()
                time.sleep(0.3)
                LED_VERDE.on()
                time.sleep(0.3)

            # 2. Luz Amarilla (Precaución)
            print("[!] Amarillo: Precaución")
            encender_solo(LED_AMARILLO)
            time.sleep(2)  # Tiempo en amarillo

            # 3. Luz Roja (Alto total)
            print("[-] Rojo: Alto")
            encender_solo(LED_ROJO)
            time.sleep(5)  # Tiempo en rojo

    except KeyboardInterrupt:
        # Apagado seguro de los LEDs al presionar Ctrl+C
        print("\nDeteniendo semáforo y apaga todos los LEDs...")
        LED_ROJO.off()
        LED_AMARILLO.off()
        LED_VERDE.off()

if __name__ == "__main__":
    ciclo_semaforo()