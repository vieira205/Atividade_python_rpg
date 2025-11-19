class arma():
    def __init__(self,nome:str,dano:float):
        self.nome = nome
        self.dano = dano
        self.claimed = False

class porcao():
    def __init__(self,nivel):
        self.cura = 15*nivel
        self.nome = f"porção de cura nivel {nivel}"
    
    def curar(self,usuario):
        if self in usuario.inventario.itens:
            usuario.curar(self.cura)
            usuario.inventario.itens.remove(self)
        else:
            print("porcão não pertence ao jogador")

class inventario():
    def __init__(self,limite):
        self.limite = limite
        self.itens = []


    def pegar_item(self,item):
        if len(self.itens) < self.limite:
            self.itens.append(item)
        else:
            print("inventário cheio")
        
    
    def mostrar_inventario(self):
        print("itens no inventário:")
        for item in self.itens:
            if item != self.itens[-1]:
                print(item.nome,end=", ")
            else:
                print(item.nome)