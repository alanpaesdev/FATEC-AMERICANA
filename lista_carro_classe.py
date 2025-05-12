class Carro:
    """
    Representa um carro com consumo de combustível e nível de combustível no tanque.
    """

    def __init__(self, consumo_km_por_litro: float):
        """
        Construtor da classe Carro.

        :param consumo_km_por_litro: O consumo do carro em quilômetros por litro.
        """
        self.consumo_combustivel = consumo_km_por_litro
        self.nivel_combustivel = 0  # Nível de combustível inicial é 0

    def andar(self, distancia_km: float):
        """
        Simula o ato de dirigir o veículo por uma certa distância.
        Reduz o nível de combustível no tanque.

        :param distancia_km: A distância em quilômetros que o carro tentará andar.
        """
        if self.consumo_combustivel <= 0:
            print("Consumo de combustível inválido. O carro não pode se mover.")
            return

        combustivel_necessario = distancia_km / self.consumo_combustivel

        if combustivel_necessario <= self.nivel_combustivel:
            self.nivel_combustivel -= combustivel_necessario
            print(f"O carro andou {distancia_km:.2f} km.")
        else:
            distancia_possivel = self.nivel_combustivel * self.consumo_combustivel
            self.nivel_combustivel = 0
            if distancia_possivel > 0:
                print(f"Combustível insuficiente para andar {distancia_km:.2f} km.")
                print(f"O carro andou {distancia_possivel:.2f} km e ficou sem combustível.")
            else:
                print("O carro está sem combustível e não pode andar.")

    def obterGasolina(self) -> float:
        """
        Retorna o nível atual de combustível no tanque.
        """
        return self.nivel_combustivel

    def adicionarGasolina(self, quantidade_litros: float):
        """
        Adiciona combustível ao tanque do carro.

        :param quantidade_litros: A quantidade de litros de combustível a ser adicionada.
        """
        if quantidade_litros > 0:
            self.nivel_combustivel += quantidade_litros
            print(f"{quantidade_litros:.2f} litros de combustível adicionados.")
        else:
            print("A quantidade de combustível a adicionar deve ser positiva.")

# Exemplo de uso:
if __name__ == "__main__":
    meuFusca = Carro(15)          # 15 quilômetros por litro de combustível.
    meuFusca.adicionarGasolina(20) # abastece com 20 litros de combustível.
    meuFusca.andar(100)           # anda 100 quilômetros.
    print(f"Combustível restante no tanque: {meuFusca.obterGasolina():.2f} litros.")

    print("\n--- Tentando andar mais ---")
    meuFusca.andar(200) # Tenta andar mais 200 km
    print(f"Combustível restante no tanque após tentar andar 200km: {meuFusca.obterGasolina():.2f} litros.")

    print("\n--- Abastecendo novamente ---")
    meuFusca.adicionarGasolina(10)
    meuFusca.andar(50)
    print(f"Combustível restante no tanque: {meuFusca.obterGasolina():.2f} litros.")