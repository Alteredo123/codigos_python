class Funcionario:
  
    def __init__(self, nome, cargo, salario):
        # estamos criando os atributos da class utilizando o método construtor. Nesse caso precisamos passar os parâmetros que serão usados como valores dos atributos da classe.
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

        


    def exibirDados(self):
        print(f"Olá {self.nome} seu cargo é {self.cargo} seu salário é {self.salario}") # usa-se o self para informar que as variáveis pertecem a class que a função se encontra
