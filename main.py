# Início

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

    # Entrada das notas do aluno
    nota1 = input("Digite a primeira nota: ").replace(",", ".")
    nota2 = input("Digite a segunda nota: ").replace(",", ".")
    nota3 = input("Digite a terceira nota: ").replace(",", ".")

    # Conversão para float
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)

    # Calculo da media das notas do aluno
    media_notas = (nota1 + nota2 + nota3) / 3

    if media_notas >= 7:
        situacao = "aprovado"
    elif media_notas >= 5:
        situacao = "recuperação"
    else:
        situacao = "reprovado"

    # Exibindo a situação do aluno (Aprovado/Em recuperação/Reprovado)
    print(f"O aluno {aluno} obteve média {media_notas:.2f} e a sua situação é de {situacao}!")

# Fim