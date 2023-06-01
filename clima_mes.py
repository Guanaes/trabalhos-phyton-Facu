mes=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
tamanho=int(len(mes))
temp=(list(range(tamanho)))
temp_mair_med=[]
mes_temp_men_med=[]
mes_temp_mai_med=[]
med=float(0)
mair=float(0)
menr=float(0)
som=float(0)


def menu (lista):
    print ('''Escolha uma das opções:
              1) Cadastrar Temperaturas.
              2) Mostar temperaturas cadastradas.
              3)Resumo das informações.
              4)Sair do progama ''') 
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

while True:
    opção=menu(mes)
    print (temp)

    if opção == 1:
        i=int(0)
        c=int(0)
        while i != (len(mes)):
            c= input ('Informe a temperatura do mês {}: ' .format(mes[i]))
            temp[i]=c
            i+=1 
            if i == (len(mes)):
                print('Cadastro completo!\n')

    elif opção == 2:
        print('Segue a lista das temperaturas cadastradas e seus respectivos meses:\n')
        i=int(0)
        while i != (len(mes)):
            print ('A temperatura do mês {} foi {} ºC.' .format(mes[i],temp[i]))
            i+=1 
    
    elif opção == 3:
        i=0
        mair=temp[i]
        menr=temp[i]
        while i != (len(mes)):
            som=temp[i]
            med = med + int(som)
            i+=1
        
        mair=(max(temp))
        menr=min(min(temp))
        while i != (len(mes)):

            if temp[i] == mair:
                mes_temp_mai_med.append(mes[i]) 
            if temp[i] == menr:
                mes_temp_men_med.append(mes[i]) 
            if temp[i] > med:
                temp_mair_med.append(mes[i])

            i+=1
        print (''' A média do ano foi de {} ºC a mair temperatura registrada foi  {} ºC no(s) mês(es),
               já a menor temperatura registrada foi {} ºC no(s) mês(es) {}.
               os meses que apresentaram um valor de temperatura mair que a média foram''' .format(med/12,mair,','.join(mes_temp_mai_med),menr,','.join(mes_temp_men_med),','.join(temp_mair_med))) 