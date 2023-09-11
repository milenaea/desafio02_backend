# 1. Crie uma classe que modele o objeto "carro"
# 2. Um carro tem os seguintes atributos: ligado, cor, modelo,velocidade
# 3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,desacelera.
# 4. Crie uma instancia da classe carro.
#5. Faca o carro "andar" utilizando os metodos da sua classe.
#6. Faca o carro "parar" utilizando os metodos da sua classe





class carro : 
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0.0
        self.limite_velocidade= 180.0


    def liga(self):
        self.ligado = True

    def desliga(self):
        self.ligado = False
        self.velocidade = 0.0

    def acelera(self):
        if self.ligado == False:
            return
        
        if self.velocidade <self.limite_velocidade:
            self.velocidade == 10

    def desacelera(self):
        if self.ligado == False:
            return
        
        if self.velocidade >0:
            self.velocidade = self.velocidade -10
    def __str__(self):
        return f" carro {self.modelo} da cor {self.cor} esta {self.ligado}, com velocidade de {self.velocidade}"

carro = carro("Vermelho","Jeep")
print(carro)

carro.ligado()
print(carro)

for i in range (5):
    carro.acelera()

print(carro)

carro.desliga()
print(carro)