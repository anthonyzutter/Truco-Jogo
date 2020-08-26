from baralho import Baralho
from carta import Carta
from jogador import Jogador
from jogo import Jogo
import os

def reiniciarJogo():
    jogador1.resetar()
    jogador2.resetar()
    baralho.resetarBaralho()
    baralho.criarBaralho()
    baralho.embaralhar()
    baralho.definirVira(baralho)
    manilha = baralho.definirManilha()
    baralho.definirManilhas(manilha)
    jogador1.criarMao(baralho)
    jogador2.criarMao(baralho)

def limpar():
    os.system("cls")

if __name__ == '__main__':
    jogo = Jogo()
    baralho = Baralho()
    baralho.embaralhar()
    baralho.definirVira(baralho)
    manilha = baralho.definirManilha()
    baralho.definirManilhas(manilha)

    carta1 = 0
    carta2 = 0
    ganhador = 0

    nome = str(input("\nNome Jogador 1: "))
    jogador1 = jogo.criarJogador(nome, baralho)
    
    nome = str(input("Nome Jogador 2: "))
    jogador2 = jogo.criarJogador(nome, baralho)

    limpar()

    while True:

        print("\nCarta que virou: ")
        baralho.printarVira()

        print("\nManilhas: ")
        baralho.printarManilhas()

        jogo.quemJogaPrimeiro(jogador1, jogador2, carta1, carta2, ganhador)

        if jogador1.primeiro == True:
            print(f"\n<< {jogador1.nome} - Jogador 1 >>")
            jogador1.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
            carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
            limpar()

            print(f"\n{jogador1.nome} jogou a carta: ")
            carta_jogador_01.printarCarta()
            print(f"\n<< {jogador2.nome} - Jogador 1 >>")
            jogador2.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador2.nome} Qual carta você quer jogar? "))
            carta_jogador_02 = jogador2.jogarCarta(carta_escolhida)
            limpar()

        else:
            print(f"\n<< {jogador2.nome} - Jogador 1 >>")
            jogador2.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador2.nome} Qual carta você quer jogar? "))
            carta_jogador_02 = jogador2.jogarCarta(carta_escolhida)
            limpar()

            print(f"\n{jogador2.nome} jogou a carta: ")
            carta_jogador_02.printarCarta()
            print(f"\n<< {jogador1.nome} - Jogador 1 >>")
            jogador1.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
            carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
            limpar()

        print(f"\n{jogador1.nome} jogou a carta: ")
        carta_jogador_01.printarCarta()

        print(f"\n{jogador2.nome} jogou a carta: ")
        carta_jogador_02.printarCarta()

        carta1 = Carta(carta_jogador_01.retornarNumero(), carta_jogador_01.retornarNaipe())
        carta2 = Carta(carta_jogador_02.retornarNumero(), carta_jogador_02.retornarNaipe())

        print("\nCarta ganhadora: ")
        ganhador = jogo.verificarGanhador(carta1, carta2, manilha)
        jogo.adicionarPonto(jogador1, jogador2, carta1, carta2, ganhador)

        if jogador1.pontos == 2:
            jogador1.adicionarRodada()
            print(f"\n{jogador1.nome} ganhou a rodada")
            reiniciarJogo()

        elif jogador2.pontos == 2:
            jogador2.adicionarRodada()
            print(f"\n{jogador2.nome} ganhou a rodada")
            reiniciarJogo()
        
        print(f"\n{jogador1.nome} Pontos {jogador1.pontos}, Rodadas {jogador1.rodadas}")
        print(f"{jogador2.nome} Pontos {jogador2.pontos}, Rodadas {jogador2.rodadas}")

        if jogador1.rodadas >= 12:
            print(f"\n{jogador1.nome} ganhou o jogo")
            break

        elif jogador2.rodadas >= 12:
            print(f"\n{jogador2.nome} ganhou o jogo")
            break
