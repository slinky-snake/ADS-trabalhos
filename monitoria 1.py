'''lista=['maçã','banana','laranja']# exe 2
print(f'preciso comprar {','.join(lista)}')#mostrar lista sem [ ]

a=str(input('qual o seu nome?'))#exe 3
b=int(input('qual o sua idade?'))
c=str(input('qual o sua qual sua altura?')).replace(',','.')
se_erro= float(c)
import datetime
ano_atual=datetime.datetime.now().year
print(f'olá, {a}\n você tem {b} anos e mede {c}cm\n você nasceu em {ano_atual-b}')

def caixa():#exe 4
    valor=int(input('digite o valor do saque:'))
    if valor % 2 != 0:
        print('saque inválido, pois o pedido deve conter quantia múltipla de 2R$')
        return
    notas=[100,50,20,10,5,2]
    quantia={}#dicionário vazio para armazenar o pedido
    for nota in notas:
        if valor >= nota:
         quantia[nota]= valor// nota
         valor %= nota
    print('notas entregues')
    for nota, quantia in quantia.items():
        if quantia > 0:
           print(f'{quantia}nota(s) de R${nota}')
caixa()

print('olá, sou um leitor de produtos')#exe 5
prod=int(input('diga a quantidade dos produtos:'))
produtos = 1
total1= 0
total2= 0
for prod in range(prod):
    preco=float(input(f'digite o preço do produto {produtos}:'))
    desc=int(input(f'digite o desconto sobre o mesmo:%'))
    result = preco - (preco * desc / 100)
    print(f'o valor deste produto é {result:.2f}')
    produtos += 1
    total1 += preco
    total2 += result

print(f'o valor total é {total2:.2f}')'''
