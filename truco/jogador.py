class Jogador():

    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.pontos = 0
    
    def criarMao(self, baralho):
        for i in range(3):
            self.mao.append(baralho.retirarCarta())
    
    def jogarCarta(self, carta_escolhida):
        return self.mao.pop(carta_escolhida - 1)
    
    def mostrarMao(self):
        for carta in self.mao:
            carta.printarCarta()
    
    def adicionarPonto(self):
        self.pontos += 1
    
    def retortarPontos(self):
        return self.pontos
