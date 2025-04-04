def escrever_arquivo(arquivo,texto):#isso cria função
    with open(arquivo,'w',encoding="utf-8")as arq:#isso põe o parametro write(criar) e comoo vai ser lido
        arq.write(texto)#abre para escrever
escrever_arquivo('arquivo_x.txt','a bagaça foi')#'aq se cria nome' e 'conteudo'
input('escreva')










def ler_retorno(arquivo_x):
    with open(arquivo_x,'r',encoding="utf-8")as arq:
        conteudo = arq.read()
    return conteudo
def escrever_arquivo(arquivo,texto):#exe(2)3 modificado
    with open(arquivo,'a',encoding="utf-8")as arq:
        arq.write(texto)
    

import csv
def criar_csv():
    dados = [
           {"nome": "paulo brito", "idade": "19", "cidade": "SC"},
           {"nome": "joão c.", "idade": "20", "cidade": "SP"},
           {"nome": "Ana Maria", "idade": "29", "cidade": "RJ"}
       ]
    with open("dados.csv","w",encoding="utf-8")as arquivo_csv:
        writer=csv.DictWriter(arquivo_csv,fieldnames=["nome","idade","cidade"])
        writer.writeheader()                  
        writer.writerows(dados)
criar_csv()


def ler_arquivo():
    with open('dados.csv','r',encoding='utf-8')as arquivo:
        conteudo=arquivo.read()
        print(conteudo)
ler_arquivo()        