class GaleriaAlienigena():
    def __init__(self, nome_galeria, obras):
        self.nome_galeria = nome_galeria
        self.obras = obras
    def adicionar_item(self, nome, valor):
        if nome != "" and valor > 0:
            self.obras.append({
                "Nome": nome,
                "Valor": valor
            })
    def listar_itens(self):
        for item in self.obras:
            print(item)
    def calcular_total(self):
        soma = 0
        for item in self.obras:
            soma += item["Valor"]
        return soma
    def encontrar_item_mais_valioso(self):
        maiorvalor = 0
        maisvalioso = {}
        for item in self.obras:
            if item["Valor"] > maiorvalor:
                    maiorvalor = item["Valor"]
                    maisvalioso = item
        return maisvalioso
    def classificar_colecao(self):
        if self.calcular_total() < 500:
            return "Galeria comum"
        elif self.calcular_total() >= 500 and self.calcular_total <= 1500:
            return "Galeria rara"
        else:
            return "Galeria intergalática"
    def exibir_relatorio(self):
        print("---- RELATORIO ----")
        print(f"Nome da galeria: {self.nome_galeria}\nTotal de raridade: {self.calcular_total()}\n"
              f"Obra mais rara: {self.encontrar_item_mais_valioso()['Nome']}\nClassificação: {self.classificar_colecao()}")
        
obras = []

galeriaA = GaleriaAlienigena("Estrelaar", obras)
galeriaA.adicionar_item("Takis", 200)
galeriaA.listar_itens()
galeriaA.calcular_total()
galeriaA.encontrar_item_mais_valioso()
galeriaA.classificar_colecao()
galeriaA.exibir_relatorio()