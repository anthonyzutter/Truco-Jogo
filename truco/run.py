from baralho import Baralho
from carta import Carta
from jogador import Jogador
from jogo import Jogo
import random
import os

def reiniciarJogo():
    jogador1.resetar()
    jogador2.resetar()
    jogador3.resetar()
    jogador4.resetar()
    baralho.resetarBaralho()
    baralho.criarBaralho()
    baralho.embaralhar()
    baralho.definirVira(baralho)
    manilha = baralho.definirManilha()
    baralho.definirManilhas(manilha)
    jogador1.criarMao(baralho)
    jogador2.criarMao(baralho)
    jogador3.criarMao(baralho)
    jogador4.criarMao(baralho)

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
    carta3 = 0
    carta4 = 0
    ganhador = 0

    nome = str(input("\nNome Jogador 1: "))
    jogador1 = jogo.criarJogador(nome, baralho)
    
    nome = str(input("Nome Jogador 2: "))
    jogador2 = jogo.criarJogador(nome, baralho)

    nome = str(input("Nome Jogador 3: "))
    jogador3 = jogo.criarJogador(nome, baralho)

    nome = str(input("Nome Jogador 4: "))
    jogador4 = jogo.criarJogador(nome, baralho)

    limpar()

    while True:

        print("\nCarta que virou: ")
        baralho.printarVira()

        print("\nManilhas: ")
        baralho.printarManilhas()

        #Sorteio pra ver quem joga na primeira rodada
        if jogador1.rodadas == 0 and jogador2.rodadas == 0:
            if jogador1.pontos == 0 and jogador2.pontos == 0:
                jogadores = ["jogador1", "jogador2", "jogador3", "jogador4"]
                sorteado = random.choice(jogadores)
                if sorteado == "jogador1":
                    jogador1.primeiro = True
                    jogador1.ultimo = True
                elif sorteado == "jogador2":
                    jogador2.primeiro = True
                    jogador1.ultimo = True
                elif sorteado == "jogador3":
                    jogador3.primeiro = True
                    jogador1.ultimo = True
                else:
                    jogador4.primeiro = True
                    jogador1.ultimo = True

        if jogador1.primeiro == True:
            print(f"\n<< {jogador1.nome} - Jogador 1 >>")
            jogador1.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
            carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador1.nome} jogou a carta: ")
            carta_jogador_01.printarCarta()
            
            print(f"\n<< {jogador2.nome} - Jogador 2 >>")
            jogador2.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador2.nome} Qual carta você quer jogar? "))
            carta_jogador_02 = jogador2.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador2.nome} jogou a carta: ")
            carta_jogador_02.printarCarta()

            print(f"\n<< {jogador3.nome} - Jogador 3 >>")
            jogador3.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador3.nome} Qual carta você quer jogar? "))
            carta_jogador_03 = jogador3.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador3.nome} jogou a carta: ")
            carta_jogador_03.printarCarta()

            print(f"\n<< {jogador4.nome} - Jogador 4 >>")
            jogador4.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador4.nome} Qual carta você quer jogar? "))
            carta_jogador_04 = jogador4.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador4.nome} jogou a carta: ")
            carta_jogador_04.printarCarta()

        elif jogador2.primeiro == True:
            print(f"\n<< {jogador2.nome} - Jogador 2 >>")
            jogador2.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador2.nome} Qual carta você quer jogar? "))
            carta_jogador_02 = jogador2.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador2.nome} jogou a carta: ")
            carta_jogador_02.printarCarta()

            print(f"\n<< {jogador3.nome} - Jogador 3 >>")
            jogador3.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador3.nome} Qual carta você quer jogar? "))
            carta_jogador_03 = jogador3.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador3.nome} jogou a carta: ")
            carta_jogador_03.printarCarta()

            print(f"\n<< {jogador4.nome} - Jogador 4 >>")
            jogador4.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador4.nome} Qual carta você quer jogar? "))
            carta_jogador_04 = jogador4.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador4.nome} jogou a carta: ")
            carta_jogador_04.printarCarta()

            print(f"\n<< {jogador1.nome} - Jogador 1 >>")
            jogador1.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
            carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador1.nome} jogou a carta: ")
            carta_jogador_01.printarCarta()

        elif jogador3.primeiro == True:
            print(f"\n<< {jogador3.nome} - Jogador 3 >>")
            jogador3.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador3.nome} Qual carta você quer jogar? "))
            carta_jogador_03 = jogador3.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador3.nome} jogou a carta: ")
            carta_jogador_03.printarCarta()

            print(f"\n<< {jogador4.nome} - Jogador 4 >>")
            jogador4.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador4.nome} Qual carta você quer jogar? "))
            carta_jogador_04 = jogador4.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador4.nome} jogou a carta: ")
            carta_jogador_04.printarCarta()

            print(f"\n<< {jogador1.nome} - Jogador 1 >>")
            jogador1.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
            carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador1.nome} jogou a carta: ")
            carta_jogador_01.printarCarta()            

            print(f"\n<< {jogador2.nome} - Jogador 2 >>")
            jogador2.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador2.nome} Qual carta você quer jogar? "))
            carta_jogador_02 = jogador2.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador2.nome} jogou a carta: ")
            carta_jogador_02.printarCarta()

        elif jogador4.primeiro == True:
            print(f"\n<< {jogador4.nome} - Jogador 4 >>")
            jogador4.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador4.nome} Qual carta você quer jogar? "))
            carta_jogador_04 = jogador4.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador4.nome} jogou a carta: ")
            carta_jogador_04.printarCarta()

            print(f"\n<< {jogador1.nome} - Jogador 1 >>")
            jogador1.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
            carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador1.nome} jogou a carta: ")
            carta_jogador_01.printarCarta()            

            print(f"\n<< {jogador2.nome} - Jogador 2 >>")
            jogador2.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador2.nome} Qual carta você quer jogar? "))
            carta_jogador_02 = jogador2.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador2.nome} jogou a carta: ")
            carta_jogador_02.printarCarta()

            print(f"\n<< {jogador3.nome} - Jogador 3 >>")
            jogador3.mostrarMao()
            carta_escolhida = int(input(f"\n{jogador3.nome} Qual carta você quer jogar? "))
            carta_jogador_03 = jogador3.jogarCarta(carta_escolhida)
            limpar()
            print(f"\n{jogador3.nome} jogou a carta: ")
            carta_jogador_03.printarCarta()
        
        else:
            print("Erro")

        print(f"\n{jogador1.nome} jogou a carta: ")
        carta_jogador_01.printarCarta()

        print(f"\n{jogador2.nome} jogou a carta: ")
        carta_jogador_02.printarCarta()

        print(f"\n{jogador3.nome} jogou a carta: ")
        carta_jogador_03.printarCarta()

        print(f"\n{jogador4.nome} jogou a carta: ")
        carta_jogador_04.printarCarta()

        carta1 = Carta(carta_jogador_01.retornarNumero(), carta_jogador_01.retornarNaipe())
        carta2 = Carta(carta_jogador_02.retornarNumero(), carta_jogador_02.retornarNaipe())
        carta3 = Carta(carta_jogador_03.retornarNumero(), carta_jogador_03.retornarNaipe())
        carta4 = Carta(carta_jogador_04.retornarNumero(), carta_jogador_04.retornarNaipe())

        print("\nCarta ganhadora: ")
        ganhador = jogo.verificarGanhador(carta1, carta2, carta3, carta4, manilha)
        jogo.quemJogaPrimeiro(jogador1, jogador2, jogador3, jogador4, carta1, carta2, carta3, carta4, ganhador)
        jogo.adicionarPonto(jogador1, jogador2, jogador3, jogador4, carta1, carta2, carta3, carta4, ganhador)

        if jogador1.pontos == 2:
            jogador1.adicionarRodada()
            jogador3.adicionarRodada()
            print(f"\n{jogador1.nome} e {jogador3.nome} ganharam a rodada")
            reiniciarJogo()

        elif jogador2.pontos == 2:
            jogador2.adicionarRodada()
            jogador4.adicionarRodada()
            print(f"\n{jogador2.nome} e {jogador4.nome} ganharam a rodada")
            reiniciarJogo()
        
        

        print(f"\n{jogador1.nome} e {jogador3.nome} Pontos {jogador1.pontos}, Rodadas {jogador1.rodadas}")
        print(f"{jogador2.nome} e {jogador4.nome} Pontos {jogador2.pontos}, Rodadas {jogador2.rodadas}")

        if jogador1.rodadas >= 12:
            print(f"\n{jogador1.nome} e {jogador3.nome} ganharam o jogo")
            break

        elif jogador2.rodadas >= 12:
            print(f"\n{jogador2.nome} e {jogador4.nome} ganharam o jogo")
            break
