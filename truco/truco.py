import random

class Carta():
    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe
        
    def printarCarta(self):
        if self.numero == 1:
            self.numero = "A"
        elif self.numero == 13:
            self.numero = "K"
        elif self.numero == 12:
            self.numero = "J"
        elif self.numero == 11:
            self.numero = "Q"
        print(f"{self.numero} de {self.naipe}")

    def retornarNumero(self):
        return self.numero
    
    def retornarNaipe(self):
        return self.naipe


class Baralho():
    def __init__(self):
        self.vira = []
        self.manilhas = []
        self.cartas = []
        self.criarBaralho()

    def criarBaralho(self):
        for i in ["Paus", "Copas", "Espadas", "Ouros"]:
            for n in range(1, 14):
                if n < 8 or n > 10:
                    self.cartas.append(Carta(n, i))
    
    def embaralhar(self):
        random.shuffle(self.cartas)
    
    def definirVira(self, baralho):
        self.vira.append(baralho.retirarCarta())

    def definirManilha(self):
        for v in self.vira:
            return v.retornarNumero() + 1

    def definirManilhas(self, baralho):
        #Coloca as cartas na lista manilhas porém não remove elas do baralho
        manilha = baralho.definirManilha()
        for m in self.cartas:
            x = m.retornarNumero()
            if x == manilha:
                self.manilhas.append(m)

    def retirarCarta(self):
        return self.cartas.pop()

    def printarVira(self):
        for v in self.vira:
            v.printarCarta()

    def printarManilhas(self):
        for m in self.manilhas:
            m.printarCarta()
    
    def printarBaralho(self):
        for c in self.cartas:
            c.printarCarta()


class Jogador():
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
    
    def criarMao(self, baralho):
        for i in range(3):
            self.mao.append(baralho.retirarCarta())
    
    def jogarCarta(self, carta_escolhida):
        return self.mao.pop(carta_escolhida - 1)
    
    def mostrarMao(self):
        for carta in self.mao:
            carta.printarCarta()


class Jogo():
    def __init__(self):
        self.rodadas = []
    
    def iniciarRodada(self):
        pass

