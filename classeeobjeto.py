class Usuario():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
usuario1 = Usuario(input('Nome do usuário: '))

print('Usuário: ', usuario1.nome)
