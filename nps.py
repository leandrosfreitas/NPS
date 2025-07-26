class Nps:
    def __init__(self):
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print("A nota precisa ser um valor entra 0 e 10")

    def calcular_nps(self):
        detratores = [n for n in self.notas if n <= 6]
        promotores = [n for n in self.notas if n >= 9]

        percentual_detratores = (len(detratores)) / (len(self.notas)) * 100
        percentual_promotores = (len(promotores)) / (len(self.notas)) * 100

        nps = percentual_promotores - percentual_detratores
        return nps
    
    def avaliar_classificacao(self):
        nps = self.calcular_nps()

        if nps < 0:
            print("Zona crítica")
        elif nps < 50:
            print("Zona neutra (Razoável)")
        elif nps < 75:
            print("Zona de qualidade (Muito bom)")
        else:
            print("Zona de excelência (Excelente)")
if __name__ == '__main__':

    print('-----Execunto teste na clase Nps-----')
    avaliação1 = Nps()

    avaliação1.adicionar_nota(10)
    avaliação1.adicionar_nota(10)
    avaliação1.adicionar_nota(10)
    avaliação1.adicionar_nota(9)
    avaliação1.adicionar_nota(10)
    avaliação1.adicionar_nota(9)
    avaliação1.adicionar_nota(9)
    avaliação1.adicionar_nota(8)
    avaliação1.adicionar_nota(10)
    avaliação1.adicionar_nota(8)
    avaliação1.adicionar_nota(10)
    print(avaliação1.notas)
    print(avaliação1.calcular_nps())
    avaliação1.avaliar_classificacao()
