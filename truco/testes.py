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

andy = Jogador("Andy")
andy.criarMao(baralho)
print("\n<< Jogador 1 >>")
andy.mostrarMao()

rudy = Jogador("Rudy")
rudy.criarMao(baralho)
print("\n<< Jogador 2 >>")
rudy.mostrarMao()

#Testes

carta_jogador_01 = rudy.jogarCarta(3)
print(f"\nO jogador {rudy.nome} jogou a carta: ")
carta_jogador_01.printarCarta()

carta_jogador_02 = andy.jogarCarta(3)
print(f"\nO jogador {andy.nome} jogou a carta: ")
carta_jogador_02.printarCarta()

carta1 = Carta(carta_jogador_01.retornarNumero(), carta_jogador_01.retornarNaipe())
carta2 = Carta(carta_jogador_02.retornarNumero(), carta_jogador_02.retornarNaipe())

print("\nCarta ganhadora: ")
if carta1.numero == manilha and carta2.numero == manilha:
    m = carta1.verificarManilha(carta1, carta2)
    m.printarCarta()
elif carta1.numero == manilha:
    carta1.printarCarta()
elif carta2.numero == manilha:
    carta2.printarCarta()
else:
    c = carta1.verificarCarta(carta1, carta2)
    if c == "Empate":
        print("Empate")
    else:
        c.printarCarta()

