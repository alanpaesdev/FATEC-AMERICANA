class Produto:
    def __init__(self, nome, preco, quantidade_estoque, descricao):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.descricao = descricao

    def exibir_informacoes(self):
        print(f"\nProduto: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade_estoque} unidades")

    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque. Estoque atual: {self.quantidade_estoque} unidades.")

    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade_estoque:
            print(f"Erro: Não há estoque suficiente para remover {quantidade} unidades.")
        else:
            self.quantidade_estoque -= quantidade
            print(f"{quantidade} unidades removidas. Estoque atual: {self.quantidade_estoque} unidades.")

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"O preço do produto {self.nome} foi atualizado para R${self.preco:.2f}.")


# Função principal para cadastrar e gerenciar produtos
def gerenciar_produtos():
    produtos = []

    # Cadastrando 2 produtos
    for i in range(2):
        print(f"\nCadastro do produto {i+1}:")
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade_estoque = int(input("Digite a quantidade em estoque: "))
        descricao = input("Digite a descrição do produto: ")

        produto = Produto(nome, preco, quantidade_estoque, descricao)
        produtos.append(produto)

    while True:
        print("\nProdutos disponíveis:")
        for idx, prod in enumerate(produtos):
            print(f"{idx + 1}. {prod.nome}")

        print(f"{len(produtos) + 1}. Sair")

        escolha_produto = int(input("Escolha o produto que deseja gerenciar: "))

        if escolha_produto == len(produtos) + 1:
            print("\nSaindo do sistema. Até a próxima!")
            break
        elif 1 <= escolha_produto <= len(produtos):
            produto_selecionado = produtos[escolha_produto - 1]

            while True:
                print(f"\nGerenciando o produto: {produto_selecionado.nome}")
                print("1. Exibir informações do produto")
                print("2. Alterar o preço")
                print("3. Adicionar ao estoque")
                print("4. Remover do estoque")
                print("5. Voltar para a lista de produtos")

                opcao = int(input("Escolha uma opção: "))

                if opcao == 1:
                    produto_selecionado.exibir_informacoes()
                elif opcao == 2:
                    novo_preco = float(input("Digite o novo preço: "))
                    produto_selecionado.alterar_preco(novo_preco)
                elif opcao == 3:
                    quantidade = int(input("Digite a quantidade a ser adicionada ao estoque: "))
                    produto_selecionado.adicionar_estoque(quantidade)
                elif opcao == 4:
                    quantidade = int(input("Digite a quantidade a ser removida do estoque: "))
                    produto_selecionado.remover_estoque(quantidade)
                elif opcao == 5:
                    print("\nVoltando para a lista de produtos...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")


gerenciar_produtos()
