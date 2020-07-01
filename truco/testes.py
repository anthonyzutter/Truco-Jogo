from truco import Baralho, Jogador

baralho = Baralho()
baralho.embaralhar()
baralho.definirVira(baralho)
baralho.definirManilha(baralho)

baralho.printarVira()
baralho.printarManilhas()



anthony = Jogador("Anthony")
anthony.retirarCartas(baralho)
print("<< Jogador 1 >>")
anthony.mostrarMao()
print(" ")

riad = Jogador("Riad")
riad.retirarCartas(baralho)
print("<< Jogador 2 >>")
riad.mostrarMao()
print(" ")

andy = Jogador("Andy")
andy.retirarCartas(baralho)
print("<< Jogador 3 >>")
andy.mostrarMao()
print(" ")

rudy = Jogador("Rudy")
rudy.retirarCartas(baralho)
print("<< Jogador 4 >>")
rudy.mostrarMao()
print(" ")

