class calculadora:
    def __init__(self):
       pass
    def soma(self, a, b):
        self.soma = a + b
        return self.soma
    def sub(self, a, b):
        self.sub = a + b
        return self.sub
    def mult(self, a, b):
        self.mult = a * b
        return self.mult
    def div(self, a, b):
        self.div = a / b
        return self.div
class usuario:
    def perguntar(self):
      print("sou uma calculadora\n>>>")
      operacao=input('digite soma para somar\nsub para subtrair\nmult para multiplicação\nou \ndiv para divisor:\n>>>').strip().lower()
      a=float(input('digite o número 1:'))
      b=float   (input("digit o número 2:"))
      calc=calculadora()#abrevia e cria uma espécie de self
      if operacao=='soma':
        print(f'a soma é:{calc.soma(a,b)}')
      elif operacao =='sub':
        print(f'a subtração é:{calc.sub(a,b)}')
      elif operacao =='mult':
        print(f'a subtração é:{calc.mult(a, b)}')
      elif operacao =='div':
        print(f'a divisão é:{calc.div(a, b)}')
      else:
        print('inválido')
inicio=usuario()
inicio.perguntar()