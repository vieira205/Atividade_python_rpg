import itens
import aleatorio

class Habilidade():
    def usar(self, usuario, alvo):
        pass

class personagem():
    def __init__(self,nome:str,vida:int,forca:float,defesa:float):
        self.nome = nome
        self.__vida = vida
        self.__vida_maxima = vida
        self.forca = forca
        self.defesa = defesa
        self.inventario = itens.inventario(15)
        self.arma : object
        self.habilidades = []

    def adicionar_habilidade(self, habilidade:Habilidade):
        self.habilidades.append(habilidade)

    def usar_habilidade(self, indice, alvo):
        if indice < 0 or indice >= len(self.habilidades):
            print("Habilidade inválida!")
            return

        habilidade = self.habilidades[indice]
        habilidade.usar(self, alvo)


    def get_vida(self):
        return self.__vida
    
    def esta_vivo(self):
        vivo : bool = True
        if self.__vida <= 0:
            vivo = False
        return vivo
    
    def get_vida_max(self):
        return self.__vida_maxima
    
    def pegar_arma(self,arma):
        self.arma = arma
        arma.claimed = True
    
    def curar(self,cura):
        if self.__vida + cura >= self.__vida_maxima:
            self.__vida = self.__vida_maxima
        else:
            self.__vida += cura

    def status(self):
        print(f"nome: {self.nome}\nvida: {self.__vida}\nforça: {self.forca}")

    def atacar(self, alvo, mult):
        variacao = aleatorio.dado1.random(1, 100) / 100

        dano = (self.forca - alvo.defesa) + (self.arma.dano * mult) + variacao

        dano = max(0, dano)

        alvo.receber_dano(dano)
        return dano


    def receber_dano(self,dano):
        self.__vida -= dano
        if not self.esta_vivo():
            self.__vida = 0
            print(self.nome,"morreu")
        print("vida de",self.nome,self.__vida)

        

class guerreiro(personagem):
    def __init__(self, nome, vida, forca, defesa):
        super().__init__(nome, vida, forca, defesa)
        self.multiplicador_ataque = 1.1
    def ataque_fisico(self,alvo):
        dan = self.atacar(alvo,self.multiplicador_ataque)
        print(f"{alvo.nome} recebeu {dan} de dano físico")
        

class mago(personagem):
    def __init__(self, nome, vida, forca, defesa):
        super().__init__(nome, vida, forca, defesa)
        self.multiplicador_ataque = 1.2
    def ataque_magico(self,alvo):
        dan = self.atacar(alvo,self.multiplicador_ataque)
        print(f"{alvo} recebeu {dan} de dano mágico")

        
class arqueiro(personagem):
    def __init__(self, nome, vida, forca, defesa):
        super().__init__(nome, vida, forca, defesa)
        self.multiplicador_ataque = 1.3
    def ataque_arco(self,alvo):
        dan = self.atacar(alvo,self.multiplicador_ataque)
        print(f"{alvo} recebeu {dan} de dano com arco")
        

class inimigo():
    def __init__(self,nome:str,vida:int,forca:float,defesa:float,chance_critico:int):
        self.nome = nome
        self.__vida = vida
        self.forca = forca
        self.defesa = defesa
        self.chance_critico = chance_critico
    
    def ataque(self,alvo:object):
        
        valor_aleatorio = aleatorio.dado1.random(1, 100)
        variacao = aleatorio.dado1.random(1, 100) / 100
        dano_base = self.forca - alvo.defesa + variacao

        if valor_aleatorio <= self.chance_critico: 
            dano = dano_base * 2
            alvo.receber_dano(dano)
            print("Dano crítico",dano,"em",alvo.nome,"vida atual",alvo.get_vida())
        else:
            dano = dano_base
            alvo.receber_dano(dano)
            print("Dano",dano,"em",alvo.nome,"vida atual",alvo.get_vida())
        
                
    def esta_vivo(self):
        vivo : bool = True
        if self.__vida <= 0:
            vivo = False
        return vivo

    def get_vida(self):
        return self.__vida
    def receber_dano(self,dano):
        self.__vida -= dano
        if not self.esta_vivo():
            self.__vida = 0
            print(self.nome,"morreu")
            
        print("vida de",self.nome,self.__vida)
        
class fabrica():
    def __init__(self):
        pass

    def criar_goblin(self):
        return inimigo("goblin",10,10.0,2,0)
    
    def criar_orc(self):
        return inimigo("orc",100,5,5,50)
    


class AtaqueForte(Habilidade):
    def usar(self, usuario, alvo):
        mult = 1.5
        dano = usuario.atacar(alvo, mult)
        print(f"{usuario.nome} usou Ataque Forte em {alvo.nome} causando {dano:.2f} de dano!")
        return dano


class BolaDeFogo(Habilidade):
    def usar(self, usuario, alvo):
        mult = 2.0
        dano = usuario.atacar(alvo, mult)
        print(f"{usuario.nome} lançou uma Bola de Fogo em {alvo.nome}, causando {dano:.2f} de dano!")
        return dano
