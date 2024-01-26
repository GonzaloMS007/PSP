import numpy as np
import scipy.stats as stats

# Función para realizar la integración numérica usando la regla de Simpson para la distribución t
def integrar_distribucion_t(x, grados_libertad, num_segmentos):
    # Calcular el ancho del segmento
    W = x / num_segmentos

    # Puntos de evaluación para la distribución t
    puntos = np.arange(0, x + W, W)

    # Calcular los términos correspondientes a F(0) y F(x)
    valores = distribucion_t(puntos, grados_libertad)

    # Calcular los términos con factor 4 en la sumatoria impar
    sum_impares = 4 * np.sum(valores[1:-1:2])

    # Calcular los términos con factor 2 en la sumatoria par
    sum_pares = 2 * np.sum(valores[2:-2:2])

    # Calcular el valor de la integral usando la regla de Simpson
    valor_integral = (W / 3) * (valores[0] + sum_impares + sum_pares + valores[-1])

    return valor_integral

# Función para obtener el valor de la distribución t en varios puntos dados
def distribucion_t(x, grados_libertad):
    # Calcular la densidad de probabilidad en los puntos dados
    return stats.t.pdf(x, df=grados_libertad)

def main():
    x = np.array([1.1, 1.1812, 2.75])
    grados_libertad = np.array([9, 10, 30])
    valores_esperados = np.array([0.35006, 0.36757, 0.49500])

    # Realizar cálculos y mostrar resultados
    for i in range(3):
        actual = integrar_distribucion_t(x[i], grados_libertad[i], 100000)
        print(f"Prueba de 0 a x = {x[i]}, dof = {grados_libertad[i]}")
        print(f"Valor Esperado (p): {valores_esperados[i]}")
        print(f"Valor Actual: {actual}")

if __name__ == "__main__":
    main()
