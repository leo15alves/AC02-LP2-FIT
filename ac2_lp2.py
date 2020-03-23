# Linguagem de Programação II
# Atividade Contínua 02 - Classes e Herança
#
# e-mail: djalma.lima@aluno.faculdadeimpacta.com.br

"""
Implementar aqui as cinco classes filhas de Mamifero ou Reptil,
de acordo com o caso, conforme dado no diagrama apresentado no padrão UML.

Os atributos específicos de cada classe filha devem ser recebidos
como parâmetros no momento da criação, a única exceção é o número de vidas
do gato, que sempre começa em 7.

Os métodos de cada classe filha devem sempre RETORNAR uma string
no seguinte formato '<nome do animal> <método em questão no gerúndio>'
Sem nenhuma pontuação, conforme os exemplos a seguir.

Exemplo:
método trocar_pele() retorna '<nome> trocando de pele'
método dormir() retorna '<nome> dormindo'
método miar() retorna '<nome> miando'
Onde <nome> é o nome dado para cada animal (o valor atributo nome de
cada instância, não o nome da classe)
"""

class Reptil:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)

class Mamifero:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        return '{} correndo'.format(self.nome)

    def mamar(self):
        if self.idade <= 1:
            return '{} mamando'.format(self.nome)
        else:
            return '{} já desmamou'.format(self.nome)

class Camaleao(Reptil):
    """
    Exemplo de solução do exercício:

    Além dos atributos da classe mãe, possui o atributo:
    inseto_favorito, do tipo string.

    Implementa os métodos específicos:
    mudar_de_cor() e comer_inseto()
    """
    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)

class Cavalo(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    cor_crina, do tipo string.

    Implementa os métodos específicos:
    galopar() e relinchar()
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina

    def galopar(self):
        return '{} galopando'.format(self.nome)

    def relinchar(self):
        return '{} relinchando'.format(self.nome)

class Cobra(Reptil):
    """
    Além dos atributos da classe mãe, possui o atributo:
    veneno, do tipo booleano.

    Implementa os métodos específicos:
    rastejar() e trocar_pele()
    """
    def __init__(self, nome, cor, idade, veneno):
        super().__init__(nome, cor, idade)
        self.veneno = veneno

    def rastejar(self):
        return '{} rastejando'.format(self.nome)

    def trocar_pele(self):
        return '{} trocando de pele'.format(self.nome)

class Cachorro(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    raca, do tipo string. (raça, porém sem o ç)

    Implementa os métodos específicos:
    latir() e rosnar()
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.raca = raca

    def latir(self):
        return '{} latindo'.format(self.nome)

    def rosnar(self):
        return '{} rosnando'.format(self.nome)

class Jacare(Reptil):
    """
    Além dos atributos da classe mãe, possui o atributo:
    num_dentes, do tipo inteiro.

    Implementa os métodos específicos:
    atacar() e dormir()
    """
    def __init__(self, nome, cor, idade, num_dentes):
        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes

    def atacar(self):
        return '{} atacando'.format(self.nome)

    def dormir(self):
        return '{} dormindo'.format(self.nome)

class Gato(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    vidas, do tipo inteiro.

    Implementa os métodos específicos:
    miar() e morrer()

    No método morrer, você deve verificar quantas vidas o gato ainda
    tem sobrando, se for igual a zero, retornar:
    '<nome> morreu'
    se ainda houver vidas sobrando, retirar uma vida (que começa em 7),
    e retornar:
    '<nome> tem <vidas> vidas sobrando'
    Onde <vidas> é o número de vidas restantes do gato em questão.
    """
    
    def __init__(self, nome, cor_pelo, idade, tipo_pata, vidas=7):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.vidas = vidas
                
    def miar(self):
        return '{} miando'.format(self.nome)

    def morrer(self):
        self.vidas -= 1
        if self.vidas <=0:
            return '{} morrreu'.format(self.nome)
        else:
            return '{} tem {} vidas sobrando'.format(self.nome, self.vidas)

def main():
    #Teste do Camaleao
    print("Teste do Camaleão:")
    Jonny=Camaleao("Jonny", "preto", 7, "grilo")
    print(Jonny.__dict__)
    print(Jonny.comer_inseto())
    print(Jonny.mudar_de_cor())
    print(Jonny.tomar_sol())
    print(Jonny.botar_ovo())
    
    #Teste do Jacaré
    print("Teste do jacaré:")
    GabbyGator=Jacare("GabbyGator", "amarelo", 1, 76)
    print(GabbyGator.__dict__)
    print(GabbyGator.tomar_sol())
    print(GabbyGator.botar_ovo())
    print(GabbyGator.atacar())
    print(GabbyGator.dormir())

    #Teste da Cobra
    print("Teste da Cobra:")
    Celeste=Cobra("Celeste", "rosa", 3, True)
    print(Celeste.__dict__)
    print(Celeste.tomar_sol())
    print(Celeste.botar_ovo())
    print(Celeste.rastejar())
    print(Celeste.trocar_pele())

    #Teste do Cachorro
    print("Teste do Cachorro:")
    Spike=Cachorro("Spike", "prata", 4, "garra", "Buldogue Inglês")
    print(Spike.__dict__)
    print(Spike.correr())
    print(Spike.mamar())
    print(Spike.latir())
    print(Spike.rosnar())

    #Teste do Cavalo
    print("Teste do Cavalo:")
    PedePano=Cavalo("Pé de Pano", "branco", 3, "Casco", "preto")
    print(PedePano.__dict__)
    print(PedePano.correr())
    print(PedePano.mamar())
    print(PedePano.galopar())
    print(PedePano.relinchar())
    
    #Teste do Gato
    print("Iniciando os testes do Gato...")
    #Primeiro Gato chamado Tom
    print("Primeiro teste do Gato:")
    Tom=Gato("Tom", "branco", 5, "garra")
    print(Tom.__dict__)
    print(Tom.correr())
    print(Tom.mamar())
    print(Tom.miar())

    #Matando o Tom 7 vezes com método de repetição e verificando 2 vezes se ele morreu
    print("{} nasceu com {} vidas".format(Tom.nome, Tom.vidas))
    # Essa primeira linha (anterior) serve para mostrar com quantas vidas Tom foi criado
    print(Tom.morrer())
    print(Tom.morrer())
    print(Tom.morrer())
    print(Tom.morrer())
    print(Tom.morrer())
    print(Tom.morrer())
    print(Tom.morrer())
    print(Tom.morrer())
    print(Tom.morrer())

    #Segundo gato chamado Geni
    print("Segundo teste do Gato:")
    Geni=Gato("Geni", "marrom", 1, "garra")
    print(Geni.__dict__)
    print(Geni.correr())
    print(Geni.mamar())
    print(Geni.miar())
    
    #Matando a Geni 7 vezes com método de loop e verificando 2 vezes se ela morreu
    print("{} nasceu com {} vidas".format(Geni.nome, Geni.vidas))
    # Essa linha (anterior) serve para mostrar com quantas vidas Geni foi criada
    for i in range(0, 9):
        print(Geni.morrer())
        i=i-1

if __name__ == "__main__":
    main()
    
# fim dos testes

# Fim do exercício Ac2_lp2
