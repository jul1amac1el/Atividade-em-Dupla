class MochilaDeMissao():
    def __init__(self, agente, equipamentos, capacidade_maxima):
        self.agente = agente
        self.equipamentos = equipamentos
        self.capacidade_maxima = capacidade_maxima
    def adicionar_equipamento(self, equipamento):
        if equipamento != "" and len(self.equipamentos) < self.capacidade_maxima:
            self.equipamentos.append(equipamento)
    def listar_equipamentos(self):
        for item in self.equipamentos:
            print(item)
    def contar_equipamentos(self):
        total = len(self.equipamentos)
        return total
    def verificar_espaco(self):
        if len(self.equipamentos) < self.capacidade_maxima:
            return "A mochila ainda possui espaço."
        else:
            return "A mochila não possui mais espaço."
    def exibir_relatorio(self):
        print("---- RELATORIO ----")
        print(f"Nome: {self.agente}\nQuantidade de equipamentos: {self.contar_equipamentos()}\n"
              f"Capacidade Máxima: {self.capacidade_maxima}\nSituação da mochila: {self.verificar_espaco()}")
        
equipamentos = ["Luva", "Faca", "Chaves"]
mochilaA = MochilaDeMissao("Ste", equipamentos, 5)
mochilaA.adicionar_equipamento("Corrente")
mochilaA.listar_equipamentos()
mochilaA.contar_equipamentos()
mochilaA.verificar_espaco()
mochilaA.exibir_relatorio()