import numpy as np
import matplotlib.pyplot as plt

# 1. Definición de la función de costo computacional (Tiempo de respuesta en ms)
# Modelamos una curva donde 'x' es el número de consultas jerárquicas concurrentes
def costo_servidor(x):
    return 0.05 * (x**3) - 0.2 * (x**2) + 10 * x + 50

# 2. Cálculo de la derivada numérica (Tasa de cambio instantánea del rendimiento)
def tasa_de_cambio_rendimiento(x, dx=0.001):
    return (costo_servidor(x + dx) - costo_servidor(x)) / dx

# --- Simulación del Entorno ---
# Generamos un rango de carga simulada de 0 a 50 consultas concurrentes
consultas = np.linspace(0, 50, 500)
tiempos = costo_servidor(consultas)
tasas_cambio = tasa_de_cambio_rendimiento(consultas)

# 3. Análisis de Optimización (Buscar el punto crítico antes del colapso)
# Si la tasa de cambio (velocidad de degradación) supera los 200 ms/consulta, alertamos
limite_alerta = 200
puntos_criticos = consultas[tasas_cambio > limite_alerta]

print("=== SIMULADOR DE RENDIMIENTO LOGÍSTICO (CÁLCULO DIFERENCIAL) ===")
if len(puntos_criticos) > 0:
    print(f"[ALERTA INFRALÓGICA] El servidor entra en degradación crítica a las {puntos_criticos[0]:.2f} consultas concurrentes.")
    print(f"Velocidad de crecimiento del costo en ese punto: {tasas_cambio[tasas_cambio > limite_alerta][0]:.2f} ms por consulta.")
else:
    print("[ESTADO] El servidor se mantiene bajo los límites asintóticos estables.")

# --- Renderizado Visual de las Curvas (Para tus diapositivas 8, 9 y 10) ---
plt.figure(figsize=(12, 6))

# Gráfico 1: Función Original C(x)
plt.subplot(1, 2, 1)
plt.plot(consultas, tiempos, label="C(x): Tiempo de Respuesta (ms)", color="blue", linewidth=2)
plt.title("Costo Computacional vs Carga")
plt.xlabel("Consultas Concurrentes (x)")
plt.ylabel("Tiempo (ms)")
plt.grid(True)
plt.legend()

# Gráfico 2: Derivada C'(x)
plt.subplot(1, 2, 2)
plt.plot(consultas, tasas_cambio, label="C'(x): Tasa de Cambio (ms/query)", color="red", linewidth=2)
plt.axhline(y=limite_alerta, color='purple', linestyle='--', label='Límite de Alerta Crítica')
plt.title("Derivada Instantánea del Rendimiento")
plt.xlabel("Consultas Concurrentes (x)")
plt.ylabel("Velocidad de Crecimiento")
plt.grid(True)
plt.legend()

plt.tight_layout()
# Guardamos la gráfica en tu carpeta para que la pegues directo en el PPT
plt.savefig("grafico_rendimiento.png")
print("\n[ÉXITO] Gráfica de optimización exportada como 'grafico_rendimiento.png'")
plt.show()