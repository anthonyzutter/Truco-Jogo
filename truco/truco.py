import random

class Carta():
    def __init__(self, numero, naipe):
        self.naipe = naipe
        self.numero = numero
        
    def printarCarta(self):
        print(f"{self.numero} de {self.naipe}")


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

    def definirManilha(self, baralho):
        #Função não finalizada
        
        """for c in self.cartas:
            self.manilhas.append(baralho.retirarCarta())"""
        pass

    def retirarCarta(self):
        return self.cartas.pop()

    def printarVira(self):
        for v in self.vira:
            v.printarCarta()

    def printarManilhas(self):
        print(str(self.manilhas))
        #for m in self.manilhas:
            #m.printarCarta()
    
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
    
    def mostrarMao(self):
        for carta in self.mao:
            carta.printarCarta()


class Jogo():
    def __init__(self):
        self.rodadas = []
    
    def iniciarRodada(self):
        pass

    def jogarCarta(self):
        pass





#Testes
#baralho = Baralho()
#baralho.embaralhar()


#baralho.definirVira()
#baralho.definirManilha(baralho)
#baralho.printarManilhas()



