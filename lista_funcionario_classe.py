class Funcionario:
    """
    Representa um funcionário com nome e salário.
    """

    def __init__(self, nome: str, salario: float):
        """
        Construtor da classe Funcionario.

        :param nome: O nome do funcionário (string).
        :param salario: O salário do funcionário (float).
        """
        self.nome = nome
        self.salario = salario

    def get_nome(self) -> str:
        """
        Retorna o nome do funcionário.
        """
        return self.nome

    def get_salario(self) -> float:
        """
        Retorna o salário do funcionário.
        """
        return self.salario

# Pequeno programa para testar a classe Funcionario
if __name__ == "__main__":
    # Criando uma instância da classe Funcionario
    funcionario1 = Funcionario("Carlos Alberto", 3500.50)

    # Usando os métodos para obter nome e salário
    print(f"Nome do Funcionário: {funcionario1.get_nome()}")
    print(f"Salário do Funcionário: R$ {funcionario1.get_salario():.2f}")

    funcionario2 = Funcionario("Ana Paula", 5270.00)
    print(f"\nNome do Funcionário: {funcionario2.get_nome()}")
    print(f"Salário do Funcionário: R$ {funcionario2.get_salario():.2f}")