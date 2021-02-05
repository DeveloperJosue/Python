import time 
print('Curriculo')
time.sleep (1)
nome = str(input('Qual é seu nome: '))
idade = int(input(f'Ótimo {nome}, agora qual é sua idade: '))
While True 
if idade < 18: 
    print('Infelizmente voce não pode continuar')
    exit 
else: 
    print('Vamos continuar !')
time.sleep (1)
print(''' 
    1 - TI
    2 - Mecânica
    3 - Eletrica
    4 - Logistica''') 
time.sleep (1) 
area = int(input('Qual a area desejada:'))
#if area = 1:
 #   print(f'''Então {nome}, você solicitou as vagas na area de Tecnologia.
 #   As especificas são:
 #   1 - Engenherio de Software 
 #   2 - Cientista de Dados
 #   3 - Analistas de Sistema
 #   4 - Programador FullStack 
 #   ''')
areati = int(input('Qual das vagas você deseja: '))