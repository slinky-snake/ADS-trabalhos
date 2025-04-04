tentativas = 3#1exe
for i in range(3):
    log=str(input('digite o usuário:'))
    sen=str(input('digite sua senha'))
    if log == 'admin' and sen == 'senha123':
        print('bem vindo, usuário "admin" logado')
        break
    elif log != 'admin' or sen != 'senha123':#2
        print('usuário e/ou senha incorretos')
        tentativas -= 1
    if tentativas == 0:
        print('usuário bloqueado')
        break

soma=0#2exe
while True:
  v=int(input('me diga números inteiros e positivos(0 para stop):'))
  if v == 0:
      break
  soma += v
print(f' resultado é:{soma}')


for i in range (1,6):#3exe
  soma= 1 * i
  print(f'{1}x{i}={soma}')

print('olá, eu digo números primos')#4exe
v=int(input('diga um número inteiro positivo'))
for i in range(1):
    if v//v==1 and v//1==v and not v%2==0 or v==2:
      print('primo')
      break
    else:
      print('não primo')#5


v = int(input('me diga um número de loop, começarei um princípio de fibonacci:'))
a,b=0,1
count=0
while count < v:
    print(a, end=',')
    a,b=b,a+b
    count+=1
