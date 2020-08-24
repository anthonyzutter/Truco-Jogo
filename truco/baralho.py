from carta import Carta
import random

class Baralho():

    def __init__(self):
        self.vira = []
        self.manilhas = []
        self.cartas = []
        self.criarBaralho() #?

    def criarBaralho(self):
        for i in ["Paus", "Copas", "Espadas", "Moles"]:
            for n in range(1, 14):
                if n < 8 or n > 10:
                    self.cartas.append(Carta(n, i))
    
    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def definirVira(self, baralho):
        self.vira.append(baralho.retirarCarta())

    def definirManilha(self):
        for v in self.vira:
            if v.retornarNumero() == 7:
                return 11
            elif v.retornarNumero() == 13:
                return 1
            else:
                return v.numero + 1

    def definirManilhas(self, manilha):
        for m in self.cartas:
            x = m.retornarNumero()
            if x == manilha:
                self.manilhas.append(m)

    def retirarCarta(self):
        return self.cartas.pop()
    
    def resetarBaralho(self):
        self.vira = []
        self.manilhas = []
        self.cartas = []

    def printarVira(self):
        for v in self.vira:
            v.printarCarta()

    def printarManilhas(self):
        for m in self.manilhas:
            m.printarCarta()
    
    def printarBaralho(self):
        for c in self.cartas:
            c.printarCarta()
