class BombaCombustivel: #class
    def __init__(self, tipoCombustivel: str, valorLitro: float, quantidadeCombustivel: float): #função init, já foi identificado o que cada atributo é  como str, float
        """
        Inicializa a bomba de combustível.

        :param tipoCombustivel: O tipo de combustível (ex: Gasolina, Diesel).
        :param valorLitro: O valor do litro do combustível.
        :param quantidadeCombustivel: A quantidade de combustível presente na bomba.
        """
        self.tipoCombustivel = tipoCombustivel   #identificação da instancia ex: tipocombustivel
        self.valorLitro = valorLitro #indetificação da instancia ex: valorlitro
        self.quantidadeCombustivel = quantidadeCombustivel #identificação da instancia ex: quantidade combustivel

    def abastecerPorValor(self, valor_a_abastecer: float): #função abastecer por valor, adicionou atributo e já identificou o tipo dele, ex float
        """
        Abastece o veículo com um determinado valor em dinheiro.
        Mostra a quantidade de litros que foi colocada no veículo.
        Atualiza a quantidade de combustível na bomba.
        """
        if self.valorLitro <= 0:  #atributo lógico
            print("Erro: Valor do litro do combustível não configurado ou inválido.")
            return 0
        
        litros_abastecidos = valor_a_abastecer / self.valorLitro

        if litros_abastecidos > self.quantidadeCombustivel:
            litros_reais_abastecidos = self.quantidadeCombustivel
            valor_real_pago = litros_reais_abastecidos * self.valorLitro
            print(f"Não há combustível suficiente para R$ {valor_a_abastecer:.2f}.")
            print(f"Abastecendo o máximo possível: {litros_reais_abastecidos:.2f} litros de {self.tipoCombustivel}.")
            print(f"Valor cobrado: R$ {valor_real_pago:.2f}.")
            self.quantidadeCombustivel = 0
        else:
            self.quantidadeCombustivel -= litros_abastecidos
            print(f"Abastecidos: {litros_abastecidos:.2f} litros de {self.tipoCombustivel}.")
            print(f"Valor pago: R$ {valor_a_abastecer:.2f}.")
        
        print(f"Combustível restante na bomba: {self.quantidadeCombustivel:.2f} litros.")
        return litros_abastecidos if litros_abastecidos <= self.quantidadeCombustivel + (litros_abastecidos if litros_abastecidos > self.quantidadeCombustivel else 0) else self.quantidadeCombustivel + litros_abastecidos

    def abastecerPorLitro(self, litros_a_abastecer: float):
        """
        Abastece o veículo com uma determinada quantidade de litros.
        Mostra o valor a ser pago pelo cliente.
        Atualiza a quantidade de combustível na bomba.
        """
        if litros_a_abastecer <= 0:
            print("Erro: A quantidade de litros a abastecer deve ser positiva.")
            return 0

        valor_a_pagar = litros_a_abastecer * self.valorLitro

        if litros_a_abastecer > self.quantidadeCombustivel:
            litros_reais_abastecidos = self.quantidadeCombustivel
            valor_real_pago = litros_reais_abastecidos * self.valorLitro
            print(f"Não há {litros_a_abastecer:.2f} litros de combustível suficientes na bomba.")
            print(f"Abastecendo o máximo possível: {litros_reais_abastecidos:.2f} litros de {self.tipoCombustivel}.")
            print(f"Valor a pagar: R$ {valor_real_pago:.2f}.")
            self.quantidadeCombustivel = 0
        else:
            self.quantidadeCombustivel -= litros_a_abastecer
            print(f"Valor a pagar: R$ {valor_a_pagar:.2f} por {litros_a_abastecer:.2f} litros de {self.tipoCombustivel}.")
        
        print(f"Combustível restante na bomba: {self.quantidadeCombustivel:.2f} litros.")
        return valor_a_pagar if litros_a_abastecer <= self.quantidadeCombustivel + litros_a_abastecer else valor_real_pago

    def alterarValor(self, novo_valor_litro: float):
        """Altera o valor do litro do combustível."""
        if novo_valor_litro <= 0:
            print("Erro: O valor do litro deve ser positivo.")
            return
        self.valorLitro = novo_valor_litro
        print(f"Valor do litro de {self.tipoCombustivel} alterado para R$ {self.valorLitro:.2f}.")

    def alterarCombustivel(self, novo_tipo_combustivel: str):
        """Altera o tipo do combustível."""
        self.tipoCombustivel = novo_tipo_combustivel
        print(f"Tipo de combustível alterado para: {self.tipoCombustivel}.")

    def alterarQuantidadeCombustivel(self, nova_quantidade_combustivel: float):
        """Altera a quantidade de combustível restante na bomba."""
        if nova_quantidade_combustivel < 0:
            print("Erro: A quantidade de combustível não pode ser negativa.")
            return
        self.quantidadeCombustivel = nova_quantidade_combustivel
        print(f"Quantidade de {self.tipoCombustivel} na bomba alterada para: {self.quantidadeCombustivel:.2f} litros.")

    def exibir_status(self):
        """Exibe o status atual da bomba."""
        print("\n--- Status da Bomba ---")
        print(f"Tipo de Combustível: {self.tipoCombustivel}")
        print(f"Valor por Litro: R$ {self.valorLitro:.2f}")
        print(f"Quantidade na Bomba: {self.quantidadeCombustivel:.2f} litros")
        print("------------------------")

# Lista de tipos de combustível disponíveis
COMBUSTIVEIS_DISPONIVEIS = ["Etanol", "Gasolina", "Gasolina Aditivada", "Diesel", "Energia"]

def escolher_tipo_combustivel(mensagem_prompt: str) -> str:
    """Apresenta a lista de combustíveis e retorna a escolha do usuário."""
    print(mensagem_prompt)
    for i, tipo in enumerate(COMBUSTIVEIS_DISPONIVEIS):
        print(f"{i + 1}. {tipo}")
    
    while True:
        try:
            escolha = int(input("Digite o número correspondente ao tipo de combustível: "))
            if 1 <= escolha <= len(COMBUSTIVEIS_DISPONIVEIS):
                return COMBUSTIVEIS_DISPONIVEIS[escolha - 1]
            else:
                print("Opção inválida. Escolha um número da lista.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def main():
    print("Configuração Inicial da Bomba de Combustível")
    tipo_inicial = escolher_tipo_combustivel("Escolha o tipo de combustível inicial da bomba:")
    while True:
        try:
            valor_inicial_litro = float(input("Digite o valor inicial do litro: R$ "))
            if valor_inicial_litro <= 0:
                print("O valor do litro deve ser positivo.")
            else:
                break
        except ValueError:
            print("Valor inválido. Digite um número (ex: 5.50).")
    
    while True:
        try:
            qtd_inicial_bomba = float(input("Digite a quantidade inicial de combustível na bomba (litros): "))
            if qtd_inicial_bomba < 0:
                print("A quantidade de combustível não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Quantidade inválida. Digite um número (ex: 1000.0).")

    bomba = BombaCombustivel(tipo_inicial, valor_inicial_litro, qtd_inicial_bomba)

    while True:
        bomba.exibir_status()
        print("\nEscolha uma opção:")
        print("1. Abastecer por valor")
        print("2. Abastecer por litro")
        print("3. Alterar valor do litro")
        print("4. Alterar tipo de combustível")
        print("5. Alterar quantidade de combustível na bomba")
        print("6. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            try:
                valor = float(input("Digite o valor a ser abastecido: R$ "))
                if valor > 0: bomba.abastecerPorValor(valor)
                else: print("O valor a ser abastecido deve ser positivo.")
            except ValueError: print("Valor inválido.")
        elif opcao == '2':
            try:
                litros = float(input("Digite a quantidade de litros a ser abastecida: "))
                if litros > 0: bomba.abastecerPorLitro(litros)
                else: print("A quantidade de litros deve ser positiva.")
            except ValueError: print("Quantidade inválida.")
        elif opcao == '3':
            try:
                novo_valor = float(input("Digite o novo valor do litro: R$ "))
                bomba.alterarValor(novo_valor)
            except ValueError: print("Valor inválido.")
        elif opcao == '4':
            novo_tipo = escolher_tipo_combustivel("Escolha o novo tipo de combustível:")
            bomba.alterarCombustivel(novo_tipo)
        elif opcao == '5':
            try:
                nova_qtd = float(input("Digite a nova quantidade total de combustível na bomba (litros): "))
                bomba.alterarQuantidadeCombustivel(nova_qtd)
            except ValueError: print("Quantidade inválida.")
        elif opcao == '6':
            print("Encerrando o programa da bomba de combustível.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()