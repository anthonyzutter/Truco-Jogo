from baralho import Baralho
from jogador import Jogador

class Jogo():

    def __init__(self):
        self.rodadas = []
    
    def iniciarRodada(self):
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
            print("A rodada empatou")
        elif ganhador == carta1:
            jogador1.adicionarPonto()
            ganhador.printarCarta()
        elif ganhador == carta2:
            jogador2.adicionarPonto()
            ganhador.printarCarta()
        else:
            print("Erro")