class Carta():
    def __init__(self, numero, naipe):
        self.naipe = naipe
        self.numero = numero
        
    def printarCarta(self):
        print(f"{self.numero} de {self.naipe}")

class Baralho():
    def __init__(self):
        self.cartas = []
        self.criarBaralho()

    def criarBaralho(self):
        for i in ["Paus", "Copas", "Espadas", "Ouros"]:
            for x in range(1, 14):
                if x < 8 or x > 10:
                    self.cartas.append(Carta(x, i))
    
    def printarBaralho(self):
        for c in self.cartas:
            c.printarCarta()


class Jogador():
    def __init__(self):
        pass


baralho = Baralho()
baralho.printarBaralho()



