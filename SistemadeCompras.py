from os import system, name 
from time import sleep
from math import fsum
from math import ceil
from math import floor

produtos= [["Arroz", 3.75],["Feijão", 5.25],["Açucar", 2.35],["Macarrão", 1.75],["Bandeja30ovos", 15.90],["Bandeja15ovos", 10.90]]
carrinho1= []
fluxo=[]
save=[]

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def menu():
    print("Bem vindo ao supermercado! Insira a operação desejada: \n")
    print("1. Carrinho\n2. Remover produtos\n3. Relátorio de vendas\n4. Sair\n")
    x= int(input())
    if x== 1:
        sleep(0.5)
        clear()
        carrinho()
    elif x== 2:
        print(2)
    elif x== 3:
        print(3)
    elif x== 4:
        print(4)
    else:
        print("Por favor insira uma opção válida.")
        sleep(1.5)
        clear()
        menu()
    
def carrinho():
    print("Insira os códigos dos produtos a serem comprados:\n")
    print("0. Arroz\n1. Feijão\n2. Açúcar\n3. Macarrão\n4. Bandeja de 30 ovos\n5. Bandeja de 15 ovos\n6. Finalizar operação\n")
    while True:
        try:
            x= int(input())
        except:
            replaycar()
        if x== 6:
            sleep(0.5)
            clear()
            compra()
        try:
            print(produtos[x][0], end=" - ")
            print(produtos[x][1])
            carrinho1.append(produtos[x])
        except:
            replaycar()
                
def replaycar():
    print("Por favor, Insira um valor válido.")
    sleep(1)
    clear()
    print("Insira os códigos dos produtos a serem comprados:")
    print("0. Arroz\n1. Feijão\n2. Açúcar\n3. Macarrão\n4. Bandeja de 30 ovos\n5. Bandeja de 15 ovos\n")
    for i in carrinho1:
        print(i[0], end=" - ")
        print(i[1])
        
def valorf():
    y= len(carrinho1)-1
    for i in carrinho1:
        fluxo.append(carrinho1[y][1])
        y-=1
    return (fsum(fluxo))
    
def retorno():
    clear()
    print("Obrigado pela sua compra!")
    sleep(2)
    clear()
    menu()
    
def save():
    save.append(carrinho1)
    #mudar a forma de salvar pra uma mais eficiente,onde todas as informacões fiquem em uma lista só dentro do save.
    
def compra():
    print("Selecione o método de pagamento: \n")
    print("0. Dinheiro\n1. Cartão débito\n2. Cartão crédito\n3. Pix\n")
    x= int(input())
    y= valorf()
    if x== 0:
        sleep(0.5)
        clear()
        print(f"Valor a ser pago: {y}\n")
        print("Registre o valor pago:")
        z= float(input())
        if z> ceil(y):
            if z-y>=0.25:
                print("\nEntregue o troco para o cliente. \n")
                print("0. Finalizar\n1. Retornar\n")
                m= int(input())
                if m== 0:
                    fluxo.append(y)
                    retorno()
                elif m== 1:
                    sleep(0.5)
                    clear()
                    compra()
            elif z-y<0.25:
                fluxo.append(y)
                retorno()
        elif y<=z<=ceil(y):
            fluxo.append(y)
            retorno()
        elif z<y:
            if z>floor(y):
                fluxo.append(y)
                retorno()
            elif z<floor(y):
                print("Valor insuficiente, impossível finalizar a compra. \n")
                print("Por favor, chamar o gerente e cancelar a compra.")
                
def relatorio():
    x= len(save)-1
    y= 1
    print("Ultimas compras efetuadas:\n")
    for i in save:
        print(f"Compra {y}:")
        y+=1
        for j in save[x]:
            print()
    
menu()