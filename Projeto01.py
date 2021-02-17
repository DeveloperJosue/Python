import time 
print('Curriculo')
time.sleep (1)
nome = str(input('Qual é seu nome: '))
idade = int(input(f'Ótimo {nome}, agora qual é sua idade: '))
if idade == 18: 
   print('Vamos continuar !')
else:
    print('Infelizmente voce não pode continuar')
time.sleep (1)
while True: 
    email = ''
    email = str(input('Digite seu email: '))
    while email not in '@gmail.com':
        email = str(input('Digite seu email: '))
    if email == '@gmail.com':
        break 
print(''' 
    1 - TI
    2 - Mecânica
    3 - Eletrica''') 
time.sleep (1) 
area = int(input('Qual a area desejada:'))
if area == 1:
    print(f'''Então {nome}, você solicitou as vagas na area de Tecnologia.
    As especificas são:
    1 - Engenherio de Software 
    2 - Cientista de Dados
    3 - Analistas de Sistema
    4 - Programador FullStack 
    ''')
    areati = int(input('Qual das vagas você deseja: '))
    if areati == 1:
        print(f'{nome} sua vaga foi cadastrada em Engenharia de Software')
        
    if areati == 2:
        print(f'{nome} sua vaga foi cadastrada em Cientista de Dados')

if area == 2:
    print(f'''Então {nome}, você socilitou as vagas na área de Mecânica:
    1 - Torneiro
    
    ''')

if area == 3:
    print(f'''Então {nome}, você solicitou as vagas na area de Eletrica
    
    
    ''')