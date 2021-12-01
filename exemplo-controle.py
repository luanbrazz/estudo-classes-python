class ControelRemoto:
    def __init__(self, cor, altura, profundidade,largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o canal")
        elif botao == "-":
            print("Diminuir o canal")



    # métodos do controle remoto:
    #     - trocar de canal
    #     - aumenta/abaixa volume
    #     - abrir a netflix
    #     _ desligar a tv


controle_remoto1 = ControelRemoto("preto", "10cm", "2cm", "2cm" )
print(controle_remoto1.profundidade)
controle_remoto1.passar_canal("+")


controle_remoto2 = ControelRemoto("cinza", "13cm", "2cm", "2cm")
print(controle_remoto2.cor)
controle_remoto2.passar_canal("-")



