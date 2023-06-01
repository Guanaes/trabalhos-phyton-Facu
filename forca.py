import random
mylist = ['salvador','palmas','brasilia','viamao', 'vitoria']
opção=int(0)
tent=int(0)


def menu (lista):
    print ('''Escolha uma das opções:
              1) Jogar Forcar
              2) Sair do progama''') 
    opção = lervar ('Sua escolha: ')
    print('\n')
    return opção

def lervar (msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError,KeyboardInterrupt):
            print('Informe uma opção válida.\n')
            continue
        else:
            return n 

def forca (erro):
    if erro == 0:
        print (''' |-----| 
 |     
 |
 |
 |''')
    if erro == 1:
        print (''' |-----| 
 |     O     
 |
 |
 |''')
    if erro == 2:
        print (''' |-----| 
 |     O     
 |     |
 |
 |''')    
    if erro == 3:
        print (''' |-----| 
 |     O     
 |    /|
 |
 |''')
    if erro == 4:
        print (''' |-----| 
 |     O     
 |    /|\\
 |
 |''')    
    if erro == 5:
        print (''' |-----| 
 |     O     
 |    /|\\
 |    /
 |''') 
    if erro == 6:
        print (''' |-----| 
 |     O     
 |    /|\\
 |    / \\
 |''')          

while True:
    opção=menu(mylist)
    erro=int(0)
    pos=int(0)
    
    
    if opção == 1:
        escolha=random.choice(mylist)
        segredo=list(escolha)
        tamanho=int(len(escolha))
        i=int(0)
        j=int(0)
        bur=(list(range(tamanho)))
        lerro=['_','_','_','_','_','_']
        gg=True

        while i != (len(segredo)):
            bur[i] = "_"
            i+=1 

        while erro != 6 and gg == True:          
            print(forca(erro),''.join(bur))
            print('-'*42)
            print('Lista de erros:{}\n'.format("".join(lerro)))
            tenta = str(input ('Escolha uma letra: '))
            
            if tenta in segredo:
                i=0
                while i != (len(bur)):
                    if tenta == segredo [i]:
                        bur[i]=tenta
                        i+=1
                    else:
                        i+=1        

            elif tenta in lerro:
                    print('Voce já tentou essa letra!\n')
            
            else:
                lerro[j]=tenta
                j+=1
                erro +=1 
                print('Essa letra está errada, você tem {} tentativas restantes\n' .format(6-erro))
            if erro == 6:
                print ('Você perdeu! A palavra correta é {}\n' .format(escolha.capitalize)) 

            if bur == segredo:
                print('Parabens você ganhou!')
                gg = False

                     
            
    elif opção == 2:
        print ('Obrigado por jogar!\nSaindo do programa.')
        break

    
            
            
