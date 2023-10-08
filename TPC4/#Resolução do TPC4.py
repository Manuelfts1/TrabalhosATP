#Resolução do TPC4
print("Bem Vindo!")
menu_text ="""   (1) Criar Lista 
     (2) Ler Lista
     (3) Soma
     (4) Média
     (5) Maior
     (6) Menor
     (7) estaOrdenada por ordem crescente
     (8) estaOrdenada por ordem decrescente
     (9) Procura um elemento
     (0) Sair"""

print(menu_text)
atividade = int(input("O que deseja fazer?"))

def menu(atividade):
    print(menu_text)
    atividade = int(input("E agora?"))
    return(atividade)
    
    
if atividade == 0:
    print("Volte sempre!")

while atividade != 0:
    
    if atividade == 1:
        print("Criar lista:")
        lista = []
        u = 0
        while u < 4:
            import random
            lista.append(random.randint(1, 100))
            u = u + 1
        print(lista)
        menu(atividade)

    if atividade == 2:
        print("Ler lista:")
        lista = []
        y = 0
        while y < 4:
            lista.append(int(input("Escolha um número:")))
            y = y + 1
            print(lista)
            menu(atividade)

    if atividade == 3:
        print("Soma:")
        soma = 0
        for r in lista:
            soma = soma + r 
        print(soma)
        menu(atividade)
        
    if atividade == 4:
        print("Média:")
        soma = 0
        for r in lista:
            soma = soma + r 
        print(int(soma) / 4)
        menu(atividade)
        
    if atividade == 5:
        print("Maior:")
        for d in lista:
            maior = 0
            if maior < d: d = maior
        print(maior)
        menu(atividade)
        
    if atividade == 6:
        print("Menor:")
        for d in lista:
            menor = 100
            if menor > d: d = menor
        print(menor)
        menu(atividade)

    if atividade == 7:
        print("Ordem crescente?")
        z = 0
        for a in lista:
            if z < lista[a]: z = lista[a]
            if z == maior: 
                print("Sim!")
            else: print("Não!")
        menu(atividade)
            
                
    if atividade == 8:
        print("Ordem decrescente?")
        z = 100
        for a in lista:
            if z > lista[a]: z = lista[a]
            if z == menor: 
                print("Sim!")
            else: print("Não!")
        menu(atividade)
            
    if atividade == 9:
        print("Procura um elemento:")
        f = int(input("Introduza um número:"))
        for w in lista:
            if w == f:
                print(lista(w)) 
            else: print("-1")
        menu(atividade)
        
        
                        


        
