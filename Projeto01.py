import time 

print('\033[4mCadastramento de Curriculo Eletrônico')
time.sleep(0.5)
print('Desde de já agradecemos pelo seu contato\033[m')
time.sleep (1)
nome = str(input('Qual é seu nome: '))
time.sleep(0.5)
idade = int(input(f'Ótimo {nome}, agora qual é sua idade: '))
idade = ' '
if idade <'18':
    print('Infelizmente voce não pode continuar')
    exit()
    if idade >='18':
        print(f'Va,ps continuar {nome}')
time.sleep (1)
email = str(input('Digite seu email para contatos futuros: '))
print(''' 
    1 - TI
    2 - Mecânica
    3 - Eletrica''') 
time.sleep (1) 
area = int(input('Qual a area desejada:')) #Escolha da área. 
if area == 1: #Áreas de TI
    print(f'''Então {nome}, você solicitou as vagas na area de Tecnologia.
    As especificas são:
    1 - Engenherio de Software 
    2 - Cientista de Dados
    3 - Analistas de Sistema
    4 - Programador FullStack 
    ''')
    areati = int(input('Qual das vagas você deseja: '))
    if areati == 1:
        print(f'{nome} sua vaga foi cadastrada em Engenharia de Software.')    
    elif areati == 2:
        print(f'{nome} sua vaga foi cadastrada em Cientista de Dados.')
    elif areati == 3 :
        print(f'{nome} sua vaga foi cadastrada em Analista de Sistema.')
    

if area == 2: #Áreas de Mecânica
    print(f'''Então {nome}, você socilitou as vagas na área de Mecânica:
    1 - Torneiro
    
    ''')

if area == 3: #Áreas de Eletrica 
    print(f'''Então {nome}, você solicitou as vagas na area de Eletrica
    
    
    ''')