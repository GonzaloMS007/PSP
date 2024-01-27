import numpy as np
from scipy.stats import t

def distribucion_t(x, dof):
    t_distribution = t(dof)
    return t_distribution.pdf(x)

def integrar_distribucion_t(a, b, dof, E):
    num_seg = 10
    h = (b - a) / num_seg
    valor_integral = calcular_valor_integral(h, a, dof, num_seg)

    while True:
        num_seg *= 2
        h = (b - a) / num_seg
        nuevo_valor_integral = calcular_valor_integral(h, a, dof, num_seg)

        if np.abs(nuevo_valor_integral - valor_integral) < E:
            break

        valor_integral = nuevo_valor_integral

    return valor_integral

def calcular_valor_integral(h, a, dof, num_seg):
    valor_integral = 0.0

    for i in range(num_seg + 1):
        x = a + i * h
        if i == 0 or i == num_seg:
            valor_integral += distribucion_t(x, dof)
        elif i % 2 == 0:
            valor_integral += 2 * distribucion_t(x, dof)
        else:
            valor_integral += 4 * distribucion_t(x, dof)

    valor_integral *= h / 3

    return valor_integral

def encontrar_x_para_probabilidad(p, dof, E):
    x_adivinanza = 1.0
    d = 0.51

    while True:
        p_actual = integrar_distribucion_t(0, x_adivinanza, dof, E)

        if np.abs(p_actual - p) < E:
            break

        if p_actual < p:
            x_adivinanza += d
        else:
            x_adivinanza -= d

        nueva_p = integrar_distribucion_t(0, x_adivinanza, dof, E)

        if np.sign(nueva_p - p) != np.sign(p_actual - p):
            d /= 2.0

    return x_adivinanza

def main():
    p = [0.20, 0.45, 0.495]
    dof = [6, 15, 4]
    resultado = np.zeros(len(p))

    print("RESULTADOS")
    print("|  p    | dof  | Resultado         |")
    for i in range(len(p)):
        probabilidad_objetivo = p[i]
        grados_libertad = int(dof[i])
        x_para_probabilidad = encontrar_x_para_probabilidad(probabilidad_objetivo, grados_libertad, 0.00001)

        # Almacenar el resultado en el arreglo
        resultado[i] = x_para_probabilidad
        print(f"| {p[i]:.3f} | {grados_libertad:<4} | {resultado[i]:<17.5f} |")

if __name__ == "__main__":
    main()
