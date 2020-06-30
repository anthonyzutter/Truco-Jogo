import random

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
    
    def embaralhar(self):
        random.shuffle(self.cartas)

    def retirarCarta(self):
        return self.cartas.pop()
    
    def printarBaralho(self):
        for c in self.cartas:
            c.printarCarta()


class Jogador():
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
    
    def retirarCartas(self, baralho):
        for i in range(3):
            self.mao.append(baralho.retirarCarta())
        #self.mao.append(baralho.retirarCarta())
        #self.mao.append(baralho.retirarCarta())
    
    def mostrarMao(self):
        for carta in self.mao:
            carta.printarCarta()


#Testes
baralho = Baralho()
baralho.embaralhar()

anthony = Jogador("Anthony")
anthony.retirarCartas(baralho)
print("<< Jogador 1 >>")
anthony.mostrarMao()
print(" ")

mario = Jogador("Mario")
mario.retirarCartas(baralho)
print("<< Jogador 2 >>")
mario.mostrarMao()
print(" ")

andy = Jogador("Andy")
andy.retirarCartas(baralho)
print("<< Jogador 3 >>")
andy.mostrarMao()
print(" ")

rudy = Jogador("Rudy")
rudy.retirarCartas(baralho)
print("<< Jogador 4 >>")
rudy.mostrarMao()
print(" ")


