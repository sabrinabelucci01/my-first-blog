


class Pessoa(object):
    def __init__(self,nome,ano,endereco):
        self.nome = nome
        self.ano_nascimento = ano
        self.endereco = endereco

    def idade(self):
        return 2019 - self.ano_nascimento

class Funcionario(Pessoa):
    def __init__(self,nome,ano,endereco):
        self.cargo = cargo
        self.salario = salario

Joao Silva = Pessoa('Joao', 1987,'Rua araci 728')
