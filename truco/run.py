from baralho import Baralho
from carta import Carta
from jogador import Jogador
from jogo import Jogo

if __name__ == '__main__':
    jogo = Jogo()
    baralho = Baralho()
    baralho.embaralhar()
    baralho.definirVira(baralho)
    manilha = baralho.definirManilha()
    baralho.definirManilhas(manilha)

    nome = str(input("\nNome Jogador 1: "))
    jogador1 = jogo.criarJogador(nome, baralho)
    
    nome = str(input("Nome Jogador 2: "))
    jogador2 = jogo.criarJogador(nome, baralho)

    print(f"\n<< {jogador1.nome} - Jogador 1 >>")
    jogador1.mostrarMao()

    print(f"\n<< {jogador2.nome} - Jogador 1 >>")
    jogador2.mostrarMao()

    print("\nCarta que virou: ")
    baralho.printarVira()

    print("\nManilhas: ")
    baralho.printarManilhas()

    carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
    carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
    print(f"\nO jogador {jogador1.nome} jogou a carta: ")
    carta_jogador_01.printarCarta()

    carta_escolhida = int(input(f"\n{jogador2.nome} Qual carta você quer jogar? "))
    carta_jogador_02 = jogador2.jogarCarta(carta_escolhida)
    print(f"\nO jogador {jogador2.nome} jogou a carta: ")
    carta_jogador_02.printarCarta()

    carta1 = Carta(carta_jogador_01.retornarNumero(), carta_jogador_01.retornarNaipe())
    carta2 = Carta(carta_jogador_02.retornarNumero(), carta_jogador_02.retornarNaipe())

    print("\nCarta ganhadora: ")
    ganhador = jogo.verificarGanhador(carta1, carta2, manilha)
    jogo.adicionarPonto(jogador1, jogador2, carta1, carta2, ganhador)

    print(f"Pontos {jogador1.nome}: {jogador1.retortarPontos()}")
    print(f"Pontos {jogador2.nome}: {jogador2.retortarPontos()}")
