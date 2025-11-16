# Início

from funcoes import ler_notas, calcular_media, verificar_situacao, mostrar_resultado

def executar():
    print("\n***** Sistema de Controle de Notas *****")
    lista_media = []

    while True:
        print("\nEscolha a opção")
        print("1 - Entrada de notas do aluno")
        print("2 - Encerrar o programa")

        opcao = input("Opção: ")

        if opcao == "2":
            print(f"\nListagem das médias apuradas: {lista_media}")
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
        situacao = verificar_situacao(media_notas)

        # Apurando a listagem de médias dos alunos
        media = f"{media_notas:.2f}"
        lista_media.append(media)

        # Duncao exibir nome do aluno, media da nota e a situacao do aluno (Aprovado/Recuperação/Reprovado)
        mostrar_resultado(aluno,media_notas,situacao)

if __name__ == "__main__":
    executar()

# Fim