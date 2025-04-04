'''n=int(input('dia um numero:'))#5
if n%2==0:
    print('este número é par')
else:
    print('este número é ímpar')'''

'''n=int(input('me diga um número entre 1  10:'))#6
if 1<= n <=10:
  print('este número está entre 1 e 10')
else:
  print('este número está incorreto')'''

'''u=str(input('me diga o usuário:\n>>>'))#6
s=int(input('me diga a senha:\n>>>'))
count=0
while True:
    if u == 'alunos' and s == 1122:
        print('acesso permitido')
        break
    else:
        print('login incorreto!tente novamente')
        count+=1'''

import calculadora# exe 8
v=str(input('selecione uma operação:\n soma=1 \nsubtração=2 \n multiplicação=3 \n divisão=4\n'))
cont=0
while True:
  if v == '1':
    a=float(input('digite numero 1:'))
    b=float(input('diga número 2:'))
    c=calculadora.soma(a,b)
    print(c)
    break
  elif v == '2':
    a=float(input('digite numero 1:'))
    b=float(input('diga número 2:'))
    c=calculadora.subtracao(a,b)
    print(c)
    break
  elif v == '3':
    a=float(input('digite numero 1:'))
    b=float(input('diga número 2:'))
    c=calculadora.multiplicacao(a,b)
    print(c)
    break
  elif v == '4':
    a=float(input('digite numero 1:'))
    b=float(input('diga número 2:'))
    c=calculadora.divisao(a,b)
    print(c)
    break
  else:
    print('erro')
    cont +=1

