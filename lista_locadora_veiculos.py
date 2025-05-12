class Veiculo:
    """
    Classe base para representar um veículo.
    """
    def __init__(self, marca: str, modelo: str):
        """
        Construtor da classe Veiculo.

        :param marca: A marca do veículo.
        :param modelo: O modelo do veículo.
        """
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        """
        Exibe as informações básicas do veículo.
        """
        print(f"{self.marca} {self.modelo}")

class Carro(Veiculo):
    """
    Representa um carro, herdando de Veiculo.
    """
    def __init__(self, marca: str, modelo: str, quantidade_de_portas: int):
        """
        Construtor da classe Carro.

        :param marca: A marca do carro.
        :param modelo: O modelo do carro.
        :param quantidade_de_portas: A quantidade de portas do carro.
        """
        super().__init__(marca, modelo) # Chama o construtor da classe pai (Veiculo)
        self.quantidade_de_portas = quantidade_de_portas

    def exibir_informacoes(self): # Sobrescrevendo o método da classe pai
        """
        Exibe as informações do carro, incluindo a quantidade de portas.
        """
        print(f"{self.marca} {self.modelo}, Portas: {self.quantidade_de_portas}")

class Moto(Veiculo):
    """
    Representa uma moto, herdando de Veiculo.
    """
    def __init__(self, marca: str, modelo: str, cilindradas: int):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def exibir_informacoes(self): # Sobrescrevendo o método da classe pai
        print(f"{self.marca} {self.modelo}, Cilindradas: {self.cilindradas}cc")

# Teste das classes
if __name__ == "__main__":
    meu_carro = Carro("Volkswagen", "Gol", 4)
    minha_moto = Moto("Honda", "CB 500", 500)

    print("Informações do Carro:")
    meu_carro.exibir_informacoes()

    print("\nInformações da Moto:")
    minha_moto.exibir_informacoes()

    # Testando um veículo genérico (se desejado)
    # veiculo_generico = Veiculo("Marca Genérica", "Modelo X")
    # print("\nInformações do Veículo Genérico:")
    # veiculo_generico.exibir_informacoes()