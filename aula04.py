def ler_dados_alunos(quant):
    alunos = []
    for i in range(quant):
        aluno = {}
        aluno["nome"] = input(f"Nome do aluno {i+1}: ")
        aluno["matricula"] = input(f"Matrícula do ano {i+1}: ")
        alunos.append(aluno)
    return alunos

def ler_notas(alunos, quant):
    notas = []
    for i in range(quant):
        notas_aluno = []
        for j in range(4):
            nota = float(input(f"Nota {j+1} do aluno {i+1}: "))
            notas_aluno.append(nota)
        notas.append(notas_aluno)
    return notas

def calcular_media_ponderada(notas, pesos):
    medias = []
    for notas_aluno in notas:
        soma_ponderada = 0
        for i in range(4):
            soma_ponderada = soma_ponderada + (notas_aluno[i]*pesos[i])
        soma_pesos = sum(pesos)
        media = soma_ponderada / soma_pesos
        medias.append(media)
    return medias

def exibir_dados_alunos(alunos, notas, medias):
    for i, aluno in enumerate(alunos):
        print(f"\nDados do aluno {i+1}: ")
        print(f"Nome: {aluno['nome']}")
        print(f"Matrícula: {aluno['matricula']}")
        print("Notas:", notas[i])
        print(f"Média Final: {medias[i]:.2f}")

quant = 2
alunos = ler_dados_alunos(quant)
notas = ler_notas(alunos, quant)
pesos = (1, 1, 2, 2)
medias = calcular_media_ponderada(notas, pesos)
exibir_dados_alunos(alunos, notas, medias)
