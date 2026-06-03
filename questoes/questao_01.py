class CapsulaDoTempo():
    def __init__(self, autor, mensagem, ano_abertura, ano_atual):
        self.autor = autor
        self.mensagem = mensagem
        self.ano_abertura = ano_abertura
        self.ano_atual = ano_atual
    def pode_abrir(self):
        if self.ano_atual >= self.ano_abertura:
            return f"pode abrir"
        else:
            return f"Não pode abrir"
    def calcular_espera(self):
        if self.ano_atual >= self.ano_abertura:
            return 0
        else:
            return self.ano_atual - self.ano_abertura
    def classificar_espera(self):
        calculo = self.ano_atual - self.ano_abertura
        if calculo == 0:
            return f"pode abrir agora"
        elif calculo >= 1 and calculo <= 3:
            return f"espera curta"
        else:
            return f"espera longa"
    def exibir_resumo(self):
        print(f"autor {self.autor}, mensagem: {self.mensagem}, ano de abertura: {self.ano_abertura}, ano atual : {self.ano_atual}")
chama = CapsulaDoTempo("Julia", "arraso", 2008, 2026)
chama.pode_abrir()
print(chama.calcular_espera())
chama.classificar_espera()
chama.exibir_resumo()