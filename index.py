class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_notas(self, nota):
        self.notas.append(nota)
        print(f'Nota do aluno {self.nome} adicionada com sucesso')

    def calcular_media(self):
        if len(self.notas) > 0:
            media = sum(self.notas) / len(self.notas)#sum soma todas as notas que esta dentro de "notas[]"
            return media
        else:
            return 0.0