from truco import Baralho, Jogador, Carta

baralho = Baralho()
baralho.embaralhar()
baralho.definirVira(baralho)
manilha = baralho.definirManilha()
baralho.definirManilhas(manilha)


print("\nCarta que virou: ")
baralho.printarVira()

print("\nManilhas: ")
baralho.printarManilhas()

"""
anthony = Jogador("Anthony")
anthony.criarMao(baralho)
print("\n<< Jogador 1 >>")
anthony.mostrarMao()

riad = Jogador("Riad")
riad.criarMao(baralho)
print("\n<< Jogador 2 >>")
riad.mostrarMao()
"""

#Testes

jogador1 = Jogador("Andy")
jogador1.criarMao(baralho)
print("\n<< Jogador 1 >>")
jogador1.mostrarMao()

jogador2 = Jogador("Rudy")
jogador2.criarMao(baralho)
print("\n<< Jogador 2 >>")
jogador2.mostrarMao()

carta_escolhida = int(input("\nQual carta você quer jogar? "))
carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
print(f"\nO jogador {jogador1.nome} jogou a carta: ")
carta_jogador_01.printarCarta()

carta_escolhida = int(input("\nQual carta você quer jogar? "))
carta_jogador_02 = jogador2.jogarCarta(carta_escolhida)
print(f"\nO jogador {jogador2.nome} jogou a carta: ")
carta_jogador_02.printarCarta()


carta1 = Carta(carta_jogador_01.retornarNumero(), carta_jogador_01.retornarNaipe())
carta2 = Carta(carta_jogador_02.retornarNumero(), carta_jogador_02.retornarNaipe())

print("\nCarta ganhadora: ")
if carta1.numero == manilha and carta2.numero == manilha:
    m = carta1.verificarManilha(carta1, carta2)
    m.printarCarta()
elif carta1.numero == manilha:
    jogador1.adicionarPonto()
    carta1.printarCarta()
elif carta2.numero == manilha:
    jogador2.adicionarPonto()
    carta2.printarCarta()
else:
    c = carta1.verificarCarta(carta1, carta2)
    if c == "Empate":
        jogador1.adicionarPonto()
        jogador2.adicionarPonto()
        print("Empate")
    else:
        c.printarCarta()

print(jogador1.retortarPontos())
print(jogador2.retortarPontos())
