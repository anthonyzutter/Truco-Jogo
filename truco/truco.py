import random

class Carta():

    CARTAS_VALORES = {
        "3": 10,
        "2": 9,
        "1": 8,
        "13": 7,
        "12": 6,
        "11": 5,
        "7": 4,
        "6": 3,
        "5": 2,
        "4": 1
    }  

    NAIPES_VALORES = {
        "Paus": 4,
        "Copas": 3,
        "Espadas": 2,
        "Moles": 1
    }

    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe
    
    def verificarCarta(self, carta_jogador_01, carta_jogador_02):
        if self.CARTAS_VALORES[str(carta_jogador_01.numero)] > self.CARTAS_VALORES[str(carta_jogador_02.numero)]:
            return carta_jogador_01
        elif self.CARTAS_VALORES[str(carta_jogador_01.retornarNumero())] < self.CARTAS_VALORES[str(carta_jogador_02.retornarNumero())]:
            return carta_jogador_02
        else:
            return "Empate"
    
    def verificarManilha(self, carta_jogador_01, carta_jogador_02):
        if self.NAIPES_VALORES[carta_jogador_01.naipe] > self.NAIPES_VALORES[carta_jogador_02.naipe]:
            return carta_jogador_01
        elif self.NAIPES_VALORES[carta_jogador_01.naipe] < self.NAIPES_VALORES[carta_jogador_02.naipe]:
            return carta_jogador_02
        else:
            raise "Erro"
        
    def printarCarta(self):
        if self.numero == 1:
            print(f"A de {self.naipe}")
        elif self.numero == 13:
            print(f"K de {self.naipe}")
        elif self.numero == 12:
            print(f"J de {self.naipe}")
        elif self.numero == 11:
            print(f"Q de {self.naipe}")
        else:
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
    
    def adicionarPonto(self):
        pass


class Jogo():

    def __init__(self):
        self.rodadas = []
    
    def iniciarRodada(self):
        pass

    def verificarGanhador(self):
        pass

