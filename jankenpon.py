#Importação de módulos.
import random
import time

#Declaração de variaveis, posteriormente aparece variavel 'resposta' pois precisa esetar dentro do while pra alterar valor. 
x=0
y=0
mylist = ['pedra','papel','tesoura']
emoji=['👊','✋','✌']

#Funções
def menu (lista):
    print ('Escolha uma das opções:')
    
    c = 1
    for item in mylist:
        print ('{}) {} {}' .format (c,emoji[c-1],item))
        c += 1
    print ('{}) Reiniciar a pontuação\n{}) Sair do Sistema\n' .format (c,c+1))
    resposta = lervar ('Sua escolha: ')
    print('\n')
    return resposta
    
def lervar (msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError,KeyboardInterrupt):
            print('Informe uma opção válida.\n')
            continue
        else:
            return n    

def susp (msg):
    print ('JAN')
    time.sleep (1)
    print ('KEN')
    time.sleep (1.5)
    print ('PON\n')
    time.sleep (2)  

    pos=mylist.index(escolha)
    print ('( ͡❛ ᴗ ͡❛){} VS {} ( ͡• ᴗ ͡•)\n' .format(emoji[resposta-1],emoji[pos]))
    print ('___________________________________')
    

#looping do jogo.
while True:
    escolha=random.choice(mylist)
    #print (escolha)
    resposta=menu(mylist) 

    if resposta == 1 and escolha == 'tesoura' or resposta == 2 and escolha == 'pedra' or resposta == 3 and escolha == 'papel':
        susp(resposta)
        x +=1
        print ('Você ganhou!\nSua opção foi {} e a escolha do programa foi {}.\n'  .format (mylist[resposta-1],escolha))
        print ('Seus pontos {} VS Pontuação do Programa {}.\n' .format(x,y))

    elif resposta == 1 and escolha == 'papel' or resposta == 2 and escolha == 'tesoura' or resposta == 3 and escolha == 'pedra':
         susp(resposta)
         y += 1    
         print ('Você perdeu!\nSua opção foi {} e a escolha do programa foi {}.\n' .format (mylist[resposta-1],escolha))
         print ('Seus pontos {} VS Pontuação do Programa {}.\n' .format(x,y))

    
    elif resposta == 1 and escolha == 'pedra' or resposta == 2 and escolha == 'papel' or resposta == 3 and escolha == 'tesoura':
        susp(resposta)
        print ('Empate!\nSua opção foi {} e a escolha do programa foi {}.\n' .format (mylist[resposta-1],escolha))
        print ('Seus pontos {} VS Pontuação do Programa. {}\n' .format(x,y))
        

    elif resposta == 4:
        print ('Pontuação zerada.\n')
        x=0
        y=0
    
    elif resposta == 5:
        print ('Obrigado por jogar!\nSaindo do programa.')
        break

    else:
        print('Informe uma opção válida!\n')
        