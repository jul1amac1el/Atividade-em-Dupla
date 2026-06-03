class TorneioDeDrones():
    def __init__(self, nome_torneio, provas, bateria):
        self.nome_torneio = nome_torneio
        self.provas = provas
        self.bateria = bateria
        self.pontos = 0
        self.provas_concluidas = []
    def listar_provas(self):
        for item in self.provas:
            print(f"Nome torneio: {item["nome"]}\nCusto: {item["custo"]}\npontuação: {item["pontuacao"]}")
    def tentar_prova(self, numero_prova):
        if numero_prova <= len(self.provas):
            if self.bateria >= self.provas[numero_prova]["custo"]:
                self.bateria -= self.provas[numero_prova]["custo"]
                self.pontos =+ self.provas[numero_prova]["pontuacao"]
                self.provas_concluidas.append(self.provas[numero_prova])
                self.provas.remove(self.provas[numero_prova])
            else:
                return "Bateria insuficiente."
        else:
            return "Número de prova inválido."
    def calcular_progresso(self):
        numtotal = len(self.provas_concluidas)
        return numtotal
    def verificar_situacao(self):
        if self.provas == 0 and self.bateria > 0:
            return "Torneio concluído"
        elif self.provas == 0 and self.bateria == 0:
            return "Torneio encerrado sem bateria"
        else:
            return "Torneio em andamento"
    def exibir_relatorio(self):
        print("---- RELATORIO ----")
        print(f"Nome do torneio: {self.nome_torneio}\nBateria restante: {self.bateria}\n"
              f"Pontos: {self.pontos}\n")
        for item in self.provas_concluidas:
            print(f"---- Provas Concluidas ----\nNome prova: {item["nome"]}\nCusto: {item["custo"]}\npontuação: {item["pontuacao"]}")
        print(f"Situação final: {self.verificar_situacao()}")

provas = [{
    "nome": "zigue-zague aéreo",
    "custo": 20,
    "pontuacao": 30
}]

provas_concluidas = []
t1 = TorneioDeDrones("Estrelar", provas, 100)
t1.listar_provas()
t1.tentar_prova(0)
t1.calcular_progresso()
t1.verificar_situacao()
t1.exibir_relatorio()