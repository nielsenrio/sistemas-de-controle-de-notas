# Início

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

def verificar_situacao():
    if media_notas >= 7:
        situacao_aluno = "aprovado"
    elif media_notas >= 5:
        situacao_aluno = "recuperação"
    else:
        situacao_aluno = "reprovado"
    return situacao_aluno

def mostrar_resultado(nome, media, resultado):
    print(f"O aluno {nome} obteve média {media:.2f} e a sua situação é de {resultado}!")

print("\n***** Sistema de Controle de Notas *****")

while True:
    print("\nEscolha a opção")
    print("1 - Entrada de notas do aluno")
    print("2 - Encerrar o programa")

    opcao = input("Opção: ")

    if opcao == "2":
        print("\nEncerrando o programa...")
        break

    # Exibe mensagem para o caso de não ser digitado as opções do menu
    if opcao not in ["1", "2"]:
        print("Opção inválida! Tente novamente!!!")
        continue

    # Entrada do nome do aluno
    aluno = input("\nDigite o nome do aluno: ")

    # Funcao entrada das notas do aluno
    lista_notas_aluno = ler_notas()
    nota1 = lista_notas_aluno[0]
    nota2 = lista_notas_aluno[1]
    nota3 = lista_notas_aluno[2]

    # Funcao calculo da media das notas do aluno
    media_notas = calcular_media(nota1, nota2, nota3)

    # Funcao para verificar a situação do aluno (Aprovado/Recuperação/Reprovado)
    situacao = verificar_situacao()

    # Duncao exibir nome do aluno, media da nota e a situacao do aluno (Aprovado/Recuperação/Reprovado)
    mostrar_resultado(aluno,media_notas,situacao)

# Fim