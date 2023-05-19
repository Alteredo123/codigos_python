class Pessoa:
    # atributos
    nome = "Kleidimar"
    idade = 30
    alturo = 1.65

    # métodos( todo método é uma função "def")
    def falar(self, texto):# O self é um parâmetro obrigatório do python que informa que o método pertence à própria classe que foi criada
        print(texto)


# instanciar é criar um objeto a parti de uma classe
pessoa1 = Pessoa()
pessoa1.nome = "Kekel"
print(pessoa1.nome, pessoa1.idade)

pessoa1.falar("Olá mundo")