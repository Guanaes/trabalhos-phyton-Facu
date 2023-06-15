matriz=[['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]  
sit=bool(True)


def resetar(reset):
    linhas = len(reset)
    colunas = len(reset[0])

    for i in range(linhas):
        for j in range(colunas):
            reset[i][j]='-'

 
def jgv(jogo):
    linhas = len(jogo)
    colunas = len(jogo[0])

    for i in range(linhas):
        for j in range(colunas):
            print ('|',jogo[i][j], end='|' )
        
        print('')


def vithori(part):
    linhas = len(part)
    colunas = len(part[0])
    vitx=0
    vito=0
    

    for i in range(linhas):
        for j in range(colunas):
            if part[i][j] == 'X':
                vitx = vitx + 1
            if vitx == 3:
                print('Jogador X venceu pela horizontal!\n')
                jgv(part)
                resetar(matriz)
                print('')
                menu()
        vitx=0

    for i in range(linhas):
        for j in range(colunas):
            if part[i][j] == 'O':
                    vito = vito + 1
            if vito == 3:
                print('Jogador O venceu pela horizontal!\n')
                jgv(part)
                resetar(matriz)
                print('')
                menu()
        vito=0


def vitvert(part):
    linhas = len(part)
    colunas = len(part[0])
    vitx=0
    vito=0
    

    for j in range(linhas):
        for i in range(colunas):
            if part[i][j] == 'X':
                vitx = vitx + 1
            if vitx == 3:
                print('Jogador X venceu pela vertical!\n')
                jgv(part)
                resetar(matriz)
                print('')
                menu()
        vitx=0

    for j in range(linhas):
        for i in range(colunas):
            if part[i][j] == 'O':
                    vito = vito + 1
            if vito == 3:
                print('Jogador O venceu pela vertical!\n')
                jgv(part)
                resetar(matriz)
                print('')
                menu()
        vito=0    
                

def vitdig1(part):
    linhas = len(part)
    colunas = len(part[0])
    vitx=0
    vito=0
    
    #Verifica diagonal simples para 'X'
    for i in range(linhas):
        for j in range(colunas):
            if  i == j and part[i][j] == 'X':
                vitx = vitx + 1
    
    if vitx == 3:
        print('Jogador X venceu pela diagonal!\n')
        jgv(part)
        resetar(matriz)
        print('')
        menu()


    #Verifica diagonal simples para 'O'
    for i in range(linhas):
        for j in range(colunas):
            if i == j and part[i][j] == 'O':
                    vito = vito + 1
    
    if vito == 3:
        print('Jogador O venceu pela diagonal!\n')
        jgv(part)
        resetar(matriz)
        print('')
        menu()
    

def vitdig2(part):
    vitx=0
    vito=0
    linhas = len(part)
    colunas = len(part[0])


    for i in range(linhas):
        for j in range(colunas):
            if part[i][j] == 'X' and i + j == colunas -1:
                vitx = vitx + 1

    if vitx == 3:
        print('Jogador X venceu pela diagonal 2!\n')
        jgv(part)
        resetar(matriz)
        print('')
        menu()



    for i in range(linhas):
        for j in range(colunas):
            if part[i][j] == 'X' and i + j == colunas -1:
                vito = vito + 1
            
        
    if vito == 3:
        print('Jogador O venceu pela diagonal 2!\n')
        jgv(part)
        resetar(matriz)
        print('')
        menu()


def empate(part):
    linhas = len(part)
    colunas = len(part[0])
    c=int(0)

    for i in range(linhas):
        for j in range(colunas):
            if part [i][j] != '-':
                c = c + 1

    if c == 9:
        print ( 'Empate! Deu velha!\n')
        resetar(matriz)
        menu()


def jogo(sit):
    cont=0
    while  sit == True:

        turno=int(cont%2)
        cont=int(cont+1)

        jgv (matriz)

        if turno ==  0:
            print('Turno do jogador X!')
            
        elif turno == 1:
            print('Turno do jogador O!')
            


        x=int(input('Informe a linha que deseja: '))
        
        y=int(input('Informe a coluna que deseja: '))
            
        

        if turno ==  0:
            print('X joga na linha {} e na coluna {}\n' .format(x,y))
            matriz[x][y]='X'
        elif turno == 1:
            print('O joga na linha {} e na coluna {}' .format(x,y))
            matriz[x][y]='O'    
        
        print('_'*42)
        print('')

        vithori(matriz)
        vitvert(matriz)
        vitdig1(matriz)
        vitdig2(matriz)
        empate(matriz)


def menu ():
    while True:
        print('Escolha uma das opções:\n1)Jogar jogo da velha\n2)Sair')
        resposta = int(input('Sua escolha: '))

        if resposta == 1:
            jogo(sit)

        if  resposta == 2 :
            break    

menu()