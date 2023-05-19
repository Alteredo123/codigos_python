class Aluno:

    def __init__(self, nome, matricula, telefone):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone
    
    def exibirDados(self):
        print(f"Seja bem vindo a nossa escola senhor(a) {self.nome}, sua matricula é {self.matricula} e seu telefone {self.telefone} ")