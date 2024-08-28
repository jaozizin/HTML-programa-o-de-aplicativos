#1
class Carro:
    def __init__(self, marca, modelo, ano, cor):
        # Inicializa os atributos do carro
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_informacoes(self):
        # Exibe as informações do carro
        print(self)

    def alterar_cor(self, nova_cor):
        # Altera a cor do carro
        self.cor = nova_cor

    def __str__(self):
        # Retorna uma representação em string do carro
        return (f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Ano: {self.ano}\n"
                f"Cor: {self.cor}")

# Exemplo de uso da classe Carro
if __name__ == "__main__":
    # Criando uma instância da classe Carro
    meu_carro = Carro("Toyota", "Corolla", 2020, "Prata")

    # Exibindo as informações do carro
    meu_carro.exibir_informacoes()

    # Alterando a cor do carro
    meu_carro.alterar_cor("Azul")

    # Exibindo as informações do carro após a alteração da cor
    meu_carro.exibir_informacoes()
