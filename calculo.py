class Calculo:
    __gasto_gasolina = float
    __gasto_alcool = float
    __gasto_diesel = float

    def __init__(self):
        self.__valor_gasolina = 4.80
        self.__valor_alcool = 3.80
        self.__valor_diesel = 3.90


    def calcular_gasto_gasolina(self, distancia, consumo):
        self.__gasto_gasolina = round((distancia / consumo) * self.__valor_gasolina, 2)
        return self.__gasto_gasolina

    def calcular_gasto_alcool(self, distancia, consumo):
        self.__gasto_alcool = round((distancia / consumo) * self.__valor_alcool, 2)
        return self.__gasto_alcool

    def calcular_gasto_diesel(self, distancia, consumo):
        self.__gasto_diesel = round((distancia / consumo) * self.__valor_diesel, 2)
        return self.__gasto_diesel
