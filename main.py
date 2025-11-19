import personagens
import itens



personagem1 = personagens.guerreiro("personagem",100,5,3)
personagem1.status()

fabricaS = personagens.fabrica()
goblin = fabricaS.criar_goblin()

long_sword = itens.arma("Espada longa",2.5)
cajado_magico = itens.arma("Cajado Mágico",3.2)

personagem1.pegar_arma(long_sword)
personagem1.inventario.mostrar_inventario()

goblin.ataque(personagem1)

porcao = itens.porcao(1)
personagem1.inventario.pegar_item(porcao)

personagem1.status()


porcao.curar(personagem1)
personagem1.status()
personagem1.inventario.mostrar_inventario()


personagem1.ataque_fisico(goblin)
personagem1.ataque_fisico(goblin)

print("personagem vivo?:",personagem1.esta_vivo())

orc = fabricaS.criar_orc()

personagem1.adicionar_habilidade(personagens.AtaqueForte())
personagem1.usar_habilidade(0, orc)
personagem1.usar_habilidade(0, orc)

print("")
print("")
orc.ataque(personagem1)
print("")
orc.ataque(personagem1)

