class ProgramaPSP0:
    media = 0.0
    varianza = 0.0
    desviacion = 0.0
    nVeces = 0

    def media_y_desviacion_estandar(self):
        
        nVeces = int(input("\n¿Cuantos numeros desea calcular?"))
        
        # Array para almacenar los valores
        numeros = [0.0] * nVeces
        
        for i in range(nVeces):
            numeros[i] = float(input("Ingrese el numero: "))
        
        # Cálculo de la media
        suma = sum(numeros)
        self.media = suma / nVeces
        print("La media es:", self.media)
        
        # Cálculo de la varianza
        self.varianza = sum((x - self.media) ** 2 for x in numeros) / (nVeces - 1)
        
        # Cálculo de la desviación estándar
        self.desviacion = self.varianza ** 0.5
        redondeo = round(self.desviacion, 2)
        print("LA DESVIACION ESTANDAR ES:", redondeo)

def main():
    psp0 = ProgramaPSP0()
    psp0.media_y_desviacion_estandar()

if __name__ == "__main__":
    main()
