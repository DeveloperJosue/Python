import time 

print('\033[34mCadastramento de Curriculo Eletrônico')
time.sleep(0.5)
print('Desde de já agradecemos pelo seu contato\033[m')
time.sleep (1)
nome = str(input('Qual é seu nome: '))
time.sleep(0.5)

idade = int(input(f'Ótimo {nome}, agora qual é sua idade: '))
if idade <= 17:   #Idade
    print(f'''Infelizmente {nome} voce não pode continuar. 
    Pois nossas vagas são destinadas há pessoas maiores de 18 anos.
    Muito Obrigado pelo contato. ''')
    exit()

if idade >= 18:
    print(f'Vamos continuar {nome}')
time.sleep (1)
email = str(input('''Digite seu email.
Obs: Precisa ser um email valido! Pois entraremos em contato atravez dele!!
Email: '''))
time.sleep(1)
print(''' 
    1 - TI
    2 - Mecânica
    3 - Eletrica''') 
time.sleep (1) 
area = int(input('Qual a area desejada:')) #Escolha da área. 
time.sleep(1)

if area == 1:   #Áreas de TI
    print(f'''Então {nome}, você solicitou as vagas na area de Tecnologia.
    As especificas são:
    1 - Engenherio de Software 
    2 - Cientista de Dados
    3 - Analistas de Sistema
    4 - Programador FullStack ''')

    time.sleep(1)
    areati = int(input('Qual das vagas você deseja: '))
    if areati == '1':
        print(f'{nome} sua vaga foi cadastrada em Engenharia de Software.')    # 1
    elif areati == '2':
        print(f'{nome} sua vaga foi cadastrada em Cientista de Dados.')        # 2
    elif areati == '3':
        print(f'{nome} sua vaga foi cadastrada em Analista de Sistema.')       # 3
    elif areati == '4':
        print(f'{nome} sua vaga foi cadastrada em Programador FullStack')      # 4
    
if area == 2:   #Áreas de Mecânica 
    print(f'''Então {nome}, você socilitou as vagas na área de Mecânica:
    1 - Torneiro
    2 - Mecânico de Manutenção
    3 - Soldador ''')
    
    time.sleep(1)
    areamec = int(input('Qual das vagas você deseja: '))                       
    if areamec == '1':
        print(f'{nome} sua vaga foi cadastrada em Torneiro. ')                 # 1
    elif areamec == '2':
        print(f'{nome} sua vaga foi cadastrada em Mecânico de Manutenção. ')   # 2
    elif areamec == '3':
        print(f'{nome} sua vaga foi cadastrada em Soldador. ')                 # 3

if area == 3:   #Áreas de Eletrica   
    print(f'''Então {nome}, você solicitou as vagas na area de Eletrica:
    1 - Eletricista Industrial
    2 - Eletricista Predial
    3 - Eletroeletrônica ''')

    time.sleep(1)
    areaele = int(input('Qual das vagas você deseja:'))
    if areaele == '1':
        print(f'{nome} sua vaga foi cadastrada em Eletricista Industrial.')    # 1
    elif areaele == '2':
        print(f'{nome} sua vaga foi cadastrada em Eletricista Predial')        # 2
    elif areaele == '3':
        print(f'{nome} sua vaga foi cadastrada em Eletroeletrônica')           # 3

time.sleep(1)
print(f'''Agradeçemos pelo seu interrese por nossa Empresa {nome}.
Logo entraremos em contato pelo email {email}.
Obrigado!! ''')