import random

def remover_produto(lista, id):
    i = 0
    while i < len(lista):
        if id in lista[i]:
            lista.pop(i)
        else:
            i += 1

def listar_produtos(lista_produtos):
    if lista_produtos:
        print("Produtos encontrados:")
        for i, produto in enumerate(lista_produtos, 1):
            print(f"Produto {i}:")
            print(f"  Nome: {produto[0]}")
            print(f"  Unidade: {produto[1]}")
            print(f"  Qtd: {produto[2]}")
            print(f"  Descrição: {produto[3]}")
            print(f"  ID: {produto[4]}")
    else:
        print("Não há produtos adicionados!")

def pesquisar_produtos(lista_produtos, vpesquisa):
    vpesquisa = vpesquisa.lower().strip() #strip remove espaços em branco no começo e no final
    resultados = []

    for produto in lista_produtos:
        nome_produto = produto[0].lower()  #lower deixa todas as string minusculas
        if vpesquisa in nome_produto:
            resultados.append(nome_produto)

    return resultados, len(resultados)


def gerar_id():
    return random.randint(100, 999)

def lista_de_compras():
    lista_produtos = []

    while True:
        print("\nBem vindo a Lista de Compras Simples!\n")

        listar_produtos(lista_produtos)

        print("\nMENU:")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Pesquisar produto")
        print("4 - sair\n")

        opcao = str(input("Selecione uma opção: "))

        if opcao == "4":
            print("Obrigado por utilizar a Lista de Compras!\n")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida! Tente novamente.")
            continue

        if opcao == "1":
            vnome = str(input("Digite o nome do produto:"))
            unidades = {
                "1": "Quilograma",
                "2": "Grama",
                "3": "Litro",
                "4": "Mililitro",
                "5": "Unidade",
                "6": "Metro",
                "7": "Centimetro"
            }
            opcao1 = str(input( "Escolha a unidade de medida:\n1-Quilograma\n2-Grama\n3-Litro\n4-Mililitro\n5-Unidade\n6-Metro\n7-Centimetro"))
            while True:
                if opcao1 not in unidades:
                    print("Opção inválida! Tente novamente.")
                    opcao1 = input(
                        "Escolha a unidade de medida:\n1-Quilograma\n2-Grama\n3-Litro\n4-Mililitro\n5-Unidade\n6-Metro\n7-Centimetro\nOpção: ")
                else:
                    vunidade = unidades[opcao1]  # Converte número para nome da unidade
                    break

            vquantidade = str(input("Digite a quantidade de produto:"))
            vdescricao = str(input("Digite a descrição do produto:"))
            numero_id = gerar_id()

            produto = [vnome, vunidade, vquantidade, vdescricao, numero_id]
            print("Produto adicionado com sucesso!")

            lista_produtos.append(produto)

        elif opcao == "2":

            id = int(input("Digite o ID do produto que você deseja remover:"))
            remover_produto(lista_produtos, id)
            print("Produto removido com sucesso!")

        else:
            vpesquisa = str(input("Digite o nome do produto que deseja:"))
            resultados, total = pesquisar_produtos(lista_produtos, vpesquisa)
            print("\nprodutos encontrados:",total)
            print(resultados)

lista_de_compras()



