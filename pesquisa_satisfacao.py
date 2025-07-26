from nps import Nps

pesquisa_nps = Nps()

print("------- Pesquisa de Satisfação -------")

while True:
    nota = input("Em uma escala de 0 a 10, o quanto você recomendaria essa empresa a um amigo ou colega\nDigite sair para encerrar a pesquisa: ")

    if nota.lower() == 'sair':
        break

    pesquisa_nps.adicionar_nota(int(nota))

print(pesquisa_nps.notas)
print(pesquisa_nps.calcular_nps())
pesquisa_nps.avaliar_classificacao()
