from truco import Baralho, Jogador

baralho = Baralho()
baralho.embaralhar()
baralho.definirVira(baralho)
baralho.definirManilha()
baralho.definirManilhas(baralho)


print("\nCarta que virou: ")
baralho.printarVira()

print("\nManilhas: ")
baralho.printarManilhas()

anthony = Jogador("Anthony")
anthony.retirarCartas(baralho)
print("\n<< Jogador 1 >>")
anthony.mostrarMao()

riad = Jogador("Riad")
riad.retirarCartas(baralho)
print("\n<< Jogador 2 >>")
riad.mostrarMao()

andy = Jogador("Andy")
andy.retirarCartas(baralho)
print("\n<< Jogador 3 >>")
andy.mostrarMao()

rudy = Jogador("Rudy")
rudy.retirarCartas(baralho)
print("\n<< Jogador 4 >>")
rudy.mostrarMao()


