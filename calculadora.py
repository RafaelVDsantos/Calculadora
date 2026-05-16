class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("O divisor não pode ser zero.")
        return a / b
    
    def potenciacao(self, base, expoente):
        return base ** expoente