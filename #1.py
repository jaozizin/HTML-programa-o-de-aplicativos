#1
class Caminhao:
    def __init__(self, marca, modelo, ano, cor):
        # Inicializa os atributos do caminhao
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def exibir_informacoes(self):
        # Exibe as informações do caminhao
        print(self)

    def alterar_cor(self, nova_cor):
        # Altera a cor do caminhao
        self.cor = nova_cor

    def __str__(self):
        # Retorna uma representação em string do caminhao
        return (f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Ano: {self.ano}\n"
                f"Cor: {self.cor}")

# Exemplo de uso da classe Caminhao
if __name__ == "__main__":
    # Criando uma instância da classe Caminhao
    meu_caminhao = Caminhao("Toyota", "Corolla", 2020, "Prata")

    # Exibindo as informações do caminhao
    meu_caminhao.exibir_informacoes()

    # Alterando a cor do caminhao
    meu_caminhao.alterar_cor("Azul")

    # Exibindo as informações do caminhao após a alteração da cor
    meu_caminhao.exibir_informacoes()
