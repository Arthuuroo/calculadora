#digitar 1 bom dia 
#digitar 2 boa tarde 
#digitar 3 boa

num_repeticao = 0
while num_repeticao < 5:


    digitar = int(input("Digite um numero de: ( 1 a 3): "))

    if digitar == 1:
     print("Bom dia!")


    elif digitar == 2:
     print("boa tarde.")  


    elif digitar == 3:
     print("Boa noite!")
 
    else:
     print("por favor escolher os numeros de 1 a 3")
    
    num_repeticao = num_repeticao + 1
    if num_repeticao == 5:
        print("voce exceeu a quantidade maxima de tentativa ({}), volte amanha". format(num_repeticao))
    
    else:
        print("voce tem mais 1 tentativa")