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

    def verificarGanhador(self, carta1, carta2, carta3, carta4, manilha):
        #Verifica se a carta 1 e a carta 3 são manilhas
        if carta1.numero == manilha and carta3.numero == manilha: #posso tirar o .numero ???
            ganhador = carta1.verificarManilha(carta1, carta3)
            #Se a carta 1 for maior que a carta 3
            if carta1 == ganhador:
                #Verifica se a carta 2 e a carta 4 são manilhas
                if carta2.numero == manilha and carta4.numero == manilha:
                    ganhador = carta1.verificarManilha(carta2, carta4)
                    if ganhador == carta2:
                        ganhador = carta1.verificarManilha(carta1, carta2)
                        return ganhador
                    else:
                        ganhador = carta1.verificarManilha(carta1, carta4)
                        return ganhador
                elif carta2.numero == manilha:
                    ganhador = carta1.verificarManilha(carta1, carta2)
                    return ganhador
                elif carta4.numero == manilha:
                    ganhador = carta1.verificarManilha(carta1, carta4)
                    return ganhador
            #Se a carta 3 for maior que a carta 1
            else:
                if carta2.numero == manilha and carta4.numero == manilha:
                    ganhador = carta1.verificarManilha(carta2, carta4)
                    if ganhador == carta2:
                        ganhador = carta1.verificarManilha(carta3, carta2)
                        return ganhador
                    else:
                        ganhador = carta1.verificarManilha(carta3, carta4)
                        return ganhador
                elif carta2.numero == manilha:
                    ganhador = carta1.verificarManilha(carta3, carta2)
                    return ganhador
                elif carta4.numero == manilha:
                    ganhador = carta1.verificarManilha(carta3, carta4)
                    return ganhador
        #Se a carta 1 for manilha
        elif carta1.numero == manilha:
                if carta2.numero == manilha and carta4.numero == manilha:
                    ganhador = carta1.verificarManilha(carta2, carta4)
                    if ganhador == carta2:
                        ganhador = carta1.verificarManilha(carta1, carta2)
                        return ganhador
                    else:
                        ganhador = carta1.verificarManilha(carta1, carta4)
                        return ganhador
                elif carta2.numero == manilha:
                    ganhador = carta1.verificarManilha(carta1, carta2)
                    return ganhador
                elif carta4.numero == manilha:
                    ganhador = carta1.verificarManilha(carta1, carta4)
                    return ganhador
                else:
                    ganhador = carta1
                    return ganhador
        #Se a carta 3 são manilha
        elif carta3.numero == manilha:
                if carta2.numero == manilha and carta4.numero == manilha:
                    ganhador = carta1.verificarManilha(carta2, carta4)
                    if ganhador == carta2:
                        ganhador = carta1.verificarManilha(carta3, carta2)
                        return ganhador
                    else:
                        ganhador = carta1.verificarManilha(carta3, carta4)
                        return ganhador
                elif carta2.numero == manilha:
                    ganhador = carta1.verificarManilha(carta3, carta2)
                    return ganhador
                elif carta4.numero == manilha:
                    ganhador = carta1.verificarManilha(carta3, carta4)
                    return ganhador
                else:
                    ganhador = carta3
                    return ganhador
        #Se a carta 2 ou a carta 4 são manilha
        elif carta2.numero == manilha and carta4.numero == manilha:
            ganhador = carta1.verificarManilha(carta2, carta4)
            return ganhador
        #Se a carta 2 for manilha
        elif carta2.numero == manilha:
            ganhador = carta2
            return ganhador
        #Se a carta 4 for manilha
        elif carta4.numero == manilha:
            ganhador = carta4
            return ganhador
        #Se nenhuma carta for manilha
        else:
            dupla1 = carta1.verificarCarta(carta1, carta3)
            if dupla1 == "Empate":
                dupla1 = carta1
            dupla2 = carta1.verificarCarta(carta2, carta4)
            if dupla2 == "Empate":
                dupla2 = carta2
            ganhador = carta1.verificarCarta(dupla1, dupla2)
            if ganhador == "Empate":
                return "Empate"
            else:
                return ganhador
    
    def adicionarPonto(self, jogador1, jogador2, jogador3, jogador4, carta1, carta2, carta3, carta4, ganhador):
        if ganhador == "Empate":
            jogador1.adicionarPonto()
            jogador2.adicionarPonto()
            jogador3.adicionarPonto()
            jogador4.adicionarPonto()
            return "Empate"
        elif ganhador == carta1 or ganhador == carta3:
            jogador1.adicionarPonto()
            jogador3.adicionarPonto()
            ganhador.printarCarta()
        elif ganhador == carta2 or ganhador == carta4:
            jogador2.adicionarPonto()
            jogador4.adicionarPonto()
            ganhador.printarCarta()
        else:
            return "Erro"
    
    def quemJogaPrimeiro(self, jogador1, jogador2, jogador3, jogador4, carta1, carta2, carta3, carta4, ganhador):
        #Se for a primeira rodada quem começa jogando é aleatorio
        if jogador1.pontos == 0 and jogador2.pontos == 0:
            if jogador1.ultimo == True:
                jogador2.ultimo = True
                jogador1.ultimo = False
            elif jogador2.ultimo == True:
                jogador3.ultimo = True
                jogador2.ultimo = False
            elif jogador3.ultimo == True:
                jogador4.ultimo = True
                jogador3.ultimo = False
            elif jogador4.ultimo == True:
                jogador1.ultimo = True
                jogador4.ultimo = False
        elif carta1 == ganhador:
            jogador1.primeiro = True
            jogador2.primeiro = False
            jogador3.primeiro = False
            jogador4.primeiro = False
        elif carta2 == ganhador:
            jogador1.primeiro = False
            jogador2.primeiro = True
            jogador3.primeiro = False
            jogador4.primeiro = False
        elif carta3 == ganhador:
            jogador1.primeiro = False
            jogador2.primeiro = False
            jogador3.primeiro = True
            jogador4.primeiro = False
        elif carta4 == ganhador:
            jogador1.primeiro = False
            jogador2.primeiro = False
            jogador3.primeiro = False
            jogador4.primeiro = True
        elif ganhador == "Empate":
            pass
