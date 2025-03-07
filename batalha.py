import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)

    def especial(self, inimigo):
        print(f"{self.nome} usa Golpe Poderoso em {inimigo.nome} e causa {self.ataque + 15} de Dano!")
        inimigo.vida-=self.ataque + 15


class Mago(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)

    def especial(self):
        if self.vida <= 0:
            print(f"{self.nome} não pode usar habilidade")
            return
        self.vida+=25
        print(f"{self.nome} usa Cura e Ganha {25} Pontos de Vida!")


class Arqueiro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)

    def especial(self, inimigos):
         if self.vida <= 0:
            print(f"{self.nome} não pode usar habilidade")
            return 
         for inimigos in inimigos:
             if self != inimigos:
                inimigos.vida-=15
                print(f"{self.nome} usa Chuva de Flechas e Causa {15} de Dano a Todos os Inimigos!")



def importar_personagens(caminho):
    """
        Função que importa personagens a partir de um ficheiro JSON.
        O ficheiro contém uma lista de personagens com informações de nome, vida, ataque e classe.
        - caminho: Caminho para o ficheiro JSON que contém os dados dos personagens.
        Retorna:
        - lista de personagens.
        - quantidade total de personagens importados.
    """
    with open(caminho, 'r')as personagens:
        infos = json.load(personagens)
    personagens = []
    for info in infos:
        classe = info['classe']
        if classe == 'Guerreiro':
            personagens.append(Guerreiro(info['nome'], info['vida'], info['ataque']))
        elif classe == 'Mago':
            personagens.append(Mago(info['nome'], info['vida'], info['ataque']))
        elif classe == 'Arqueiro':
            personagens.append(Arqueiro(info['nome'], info['vida'], info['ataque']))
            return personagens, len(personagens)



   

def ordenar_personagens_por_vida(personagens):
    """
        Função que ordena a lista de personagens de acordo com os pontos de vida (do menor para o maior).
        - personagens: Lista de personagens.
        Retorna:
        - lista de personagens ordenada por vida.
    """
    def ordenar_personagens_por_vida(personagens):
        for i in range(len(personagens)):
            for j in range(0,len(personagens) -i -1):
                if personagens[j].vida > personagens[j + 1].vida:
                    personagens[j], personagens[j + 1] = personagens[j + 1], personagens[j]
    return personagens

personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[1]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])