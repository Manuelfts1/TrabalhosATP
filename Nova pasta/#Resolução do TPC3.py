#Resolução do TPC3 
## Adivinha o Número.

game = int(input("""Vamos jogar ao Adivinha o número!
                 Se quiser escolher o número digite 1.
                 Caso queira que o computador escolha digite 2."""))
if game == 2:
    #O computador pensa no número.
    print("Estou a pensar num número entre 0 e 100.")
    import random
    a = random.randint(0, 100)

    tentativas = 0
    n = int(input("Que número acha que é?"))
    while a != n:
        if n < a:
         print("É maior!")
        
        if n > a:
            print("É menor!")
        n = int(input("Tem outro palpite?"))
        tentativas = tentativas + 1
    
    if a == n:
        print("Acertou! Conseguiu fazê-lo em " + str(tentativas) + " tentativas.")

if game == 1:  
    #O computador adivinha o número.
    print("Pense num número entre 0 e 100.")
    
    import random
    a = random.randint(0, 100)
    
    print("Acho que é " + str(a) + " .")
    right = (input("Acertei?"))
    tentativas = 0
    while right != "acertou":
        b = 1
        if right == "maior":
            b = random.randint(a, 100)
            right = (input(str(b) + "; E agora?"))
            
        if right == "menor":
            b = random.randint(0, a) 
            right = (input(str(b) + "; E agora?"))        
        a = b
        tentativas = tentativas + 1
    if right == "acertou":
        print("Em apenas " + str(tentativas) + " tentativas!") 


