from calculo import Calculo


def main():
    calc = Calculo()

    distancia = float(input("Distância em Quilômetros a ser percorrida? \n"))
    consumo = float(input("Consumo de combustível do veículo (Km/l)? \n"))
    combustivel = float(input("Escolha o combustivel: 1-Alcool, 2-Gasolina, 3-Diesel ou 4-Todos: "))


    if combustivel == 1:
        print("O seu gasto em Álcool será de R$", (calc.calcular_gasto_alcool(distancia, consumo)))
    elif combustivel == 2:
        print("O seu gasto em Gasolina será de R$", (calc.calcular_gasto_gasolina(distancia, consumo)))
    elif combustivel == 3:
        print("O seu gasto em Díesel será de R$", (calc.calcular_gasto_diesel(distancia, consumo)))
    elif combustivel == 4:
        print("Segue a relação de todos os combustiveis:")
        print("Alcool R$ ", calc.calcular_gasto_alcool(distancia, consumo))
        print("Gasolina R$ ", calc.calcular_gasto_gasolina(distancia, consumo))
        print("Diesel R$ ", calc.calcular_gasto_diesel(distancia, consumo))
    else:
        print("Opção errada! Escolha uma das opções acima.")
        exit()

if __name__ == "__main__":
    main()