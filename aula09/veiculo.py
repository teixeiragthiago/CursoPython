class Veiculo:

    #Construtor, o self possui o msm conceito de 'this'
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def buzinar(self):
        print("BIBI!")

    def exibirdados(self):
        print("A cor do carro é:", self.cor)
        print("A quantidade de rodas do carro é:", self.rodas)
        print("A marca do carro é:", self.marca)
        print("O tanto de combustível tem:", self.tanque, "litros")

    def abastecer(self, lts):
        self.tanque += lts