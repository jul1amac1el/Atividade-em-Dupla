class PortalDimensional():
    def __init__(self, nome, destino, energia_necessaria, energia_disponivel):
        self. nome = nome
        self.destino = destino
        self.energia_necessaria = energia_necessaria
        self.energia_disponivel = energia_disponivel
    def pode_abrir(self):
        if self.energia_necessaria <= self.energia_disponivel:
            print("Pode abrir o Portal Dimensional")
        else:
            falta = self.calcular_falta_energia()
            print(f"Você não possui energia suficiente para abrir. Falta {falta} de energia.")
    def calcular_falta_energia(self):
        if self.energia_necessaria <= self.energia_disponivel:
            return 0
        else:
            return self.energia_necessaria - self.energia_disponivel
    def classificar_estabilidade(self):
        if self.energia_necessaria <= self.energia_disponivel:
            return "Portal estável."
        else:
            if (self.energia_necessaria - self.energia_disponivel) <= 20:
                return "Portal quase estável."
            if (self.energia_necessaria - self.energia_disponivel) > 20:
                return "Portal instável."
    def exibir_resumo(self):
        print("\n----- RESUMO ----")
        print(f"Nome portal: {self.nome}\nDestino: {self.destino}\nEnergia disponível: {self.energia_disponivel}"
              f"\nEnergia necessária: {self.energia_necessaria}\nSituação: {self.classificar_estabilidade()}")

portal1 = PortalDimensional("Estrelas", "Espaço", 1500, 1520)
portal1.pode_abrir()
portal1.calcular_falta_energia()
portal1.classificar_estabilidade()
portal1.exibir_resumo()