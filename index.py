
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_notas(self, nota):
        self.notas.append(nota)
        print(f'Nota do aluno {self.nome} adicionada com sucesso')

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            print(f'Aluno {self.nome} esta aprovado com media {media}')
        elif media >=5:
            print(f'Aluno {self.nome} esta de recuperacao com media {media}')
        else:
            print(f'Aluno {self.nome} esta reprovado com media {media}')

    def mostrar_dados(self):
        print(f"\nAluno: {self.nome}")
        print(f"Notas: {self.notas}")
        print(f"Média: {self.calcular_media():.2f}")
        print(f"Situação: {self.verificar_situacao()}")

#usando na pratica
lista_alunos = []

while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Ver alunos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        aluno = Aluno(nome)

        for i in range(3):
            nota = float(input(f"Digite a nota {i + 1}: "))
            aluno.adicionar_notas(nota)

        lista_alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        for aluno in lista_alunos:
            aluno.mostrar_dados()
    
    elif opcao == "3":
        break
    
    else:
        print("Opção inválida. Tente novamente.")
        
