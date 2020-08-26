from baralho import Baralho
from jogador import Jogador
import random

class Jogo():

    def __init__(self):
        self.rodadas = []
    
    def iniciarJogo(self):
        pass

    def criarJogador(self, nome, baralho):
        jogador = Jogador(nome)
        jogador.criarMao(baralho)
        return jogador

    def verificarGanhador(self, carta1, carta2, manilha):
        if carta1.numero == manilha and carta2.numero == manilha:
            ganhador = carta1.verificarManilha(carta1, carta2)
            return ganhador
        elif carta1.numero == manilha:
            ganhador = carta1
            return ganhador
        elif carta2.numero == manilha:
            ganhador = carta2
            return ganhador
        else:
            ganhador = carta1.verificarCarta(carta1, carta2)
            if ganhador == "Empate":
                return "Empate"
            else:
                return ganhador
    
    def adicionarPonto(self, jogador1, jogador2, carta1, carta2, ganhador):
        if ganhador == "Empate":
            jogador1.adicionarPonto()
            jogador2.adicionarPonto()
            print("Empate")
        elif ganhador == carta1:
            jogador1.adicionarPonto()
            ganhador.printarCarta()
        elif ganhador == carta2:
            jogador2.adicionarPonto()
            ganhador.printarCarta()
        else:
            print("Erro")
    
    def quemJogaPrimeiro(self, jogador1, jogador2, carta1, carta2, ganhador):
        if jogador1.pontos == 0 and jogador2.pontos == 0:
            if jogador1.rodadas == 0 and jogador2.rodadas == 0:
                jogadores = ["jogador1", "jogador2"]
                if random.choice(jogadores) == "jogador1":
                    jogador1.primeiro = True
                else:
                    jogador2.primeiro = True     
            elif jogador1.primeiro == True:
                jogador1.primeiro = False
                jogador2.primeiro = True
            elif jogador2.primeiro == True:
                jogador1.primeiro = True
                jogador2.primeiro = False
        elif jogador1.pontos == 1 and jogador2.pontos == 0:
            jogador1.primeiro = True
            jogador2.primeiro = False
        elif jogador1.pontos == 0 and jogador2.pontos == 1:
            jogador1.primeiro = False
            jogador2.primeiro = True
        elif jogador1.pontos == 1 and jogador2.pontos == 1:
            if ganhador == carta1:
                jogador1.primeiro = True
                jogador2.primeiro = False
            elif ganhador == carta2:
                jogador1.primeiro = False
                jogador2.primeiro = True