
def ler_notas():
    notas = []
    for i in range(1,4):
        if i == 1:
            nota = float(input(f"Digite a primeira nota: ").replace(",","."))
            notas.append(nota)
        elif i == 2:
            nota = float(input(f"Digite a segunda nota: ").replace(",", "."))
            notas.append(nota)
        else:
            nota = float(input(f"Digite a terceira nota: ").replace(",", "."))
            notas.append(nota)
    return notas

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def verificar_situacao(media_notas):
    if media_notas >= 7:
        situacao_aluno = "aprovado"
    elif media_notas >= 5:
        situacao_aluno = "recuperação"
    else:
        situacao_aluno = "reprovado"
    return situacao_aluno

def mostrar_resultado(nome, media, resultado):
    print(f"O aluno {nome} obteve média {media:.2f} e a sua situação é de {resultado}!")