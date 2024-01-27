def calcularParametrosRegresion(x, y, xk):
    # Calcula la media de x e y
    mediaX = sum(x) / len(x)
    mediaY = sum(y) / len(y)

    # Calcula el coeficiente de correlación (r)
    numerador = sum((xi - mediaX) * (yi - mediaY) for xi, yi in zip(x, y))
    denominadorX = sum((xi - mediaX) ** 2 for xi in x)
    denominadorY = sum((yi - mediaY) ** 2 for yi in y)
    r = numerador / (denominadorX ** 0.5 * denominadorY ** 0.5)

    # Calcula la pendiente (beta1) y el intercepto (beta0)
    beta1 = numerador / denominadorX
    beta0 = mediaY - beta1 * mediaX

    # Calcula el coeficiente de determinación (r^2)
    r2 = r ** 2

    # Realiza la predicción de y (yk) para el valor xk
    yk = beta0 + beta1 * xk

    return beta0, beta1, r, r2, yk

if __name__ == "__main__":
    # Definimos los conjuntos de datos y valores xk para las pruebas
    conjuntos_de_datos = [
        ([130, 650, 99, 150, 128, 302, 95, 945, 368, 961], [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601], 386),
        ([130, 650, 99, 150, 128, 302, 95, 945, 368, 961], [15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2], 386),
        ([163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130], [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601], 386),
        ([163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130], [15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2], 386)
    ]

    for i, (x, y, xk) in enumerate(conjuntos_de_datos):
        beta0, beta1, r, r2, yk = calcularParametrosRegresion(x, y, xk)
        print(f"Resultados para el conjunto {i + 1}:")
        print(f"B_0 = {round(beta0, 5)}")
        print(f"B_1 = {round(beta1, 5)}")
        print(f"r_(x,y) = {round(r, 5)}")
        print(f"r^2 = {round(r2, 5)}")
        print(f"y_k = {round(yk, 5)}")
