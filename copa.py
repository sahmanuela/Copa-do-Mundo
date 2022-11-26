import time
import json
import os

print('--' * 20)
print('{:^40}'.format('COPA DO MUNDO'))

if os.path.exists('times.json'):
    times_file = open('times.json', 'r+')  
    if len(times_file.readline()) > 0:
        times_file.seek(0)
        times = json.load(times_file)
    else:
        times = list()  
else:
    times_file = open('times.json', 'w')  
    times = list()


def salvar_times_file():
    times_file.truncate(0)
    times_file.seek(0)
    times_file.write(json.dumps(times))  


def novoTime():
    salvar_times = False
    while not salvar_times:
        pais = input('Insira o país da seleção: ')
        abreviacao = input('Insira a abreviação do país: ')
        add_grupo = False
        grupo = None
        while not add_grupo:
            grupo = input('Insira o grupo do país: ').upper()
            if len([time for time in times if time.get('Grupo') == grupo]) == 4:
                print('Este grupo já possui 4 seleções!\nEscolha outro grupo.')
            else: 
                add_grupo = True
        times.append({'Pais': pais, 'Abreviacao': abreviacao ,'Grupo': grupo})
        
        if input('Cadastrar outra seleção(S/N): ').upper() != 'S':
            salvar_times = True
    salvar_times_file()

def listarTimes(times):
  if len(times) == 0:
    print("Não há seleções cadastradas")
  for time in times:
    print(f"Seleção: {time.get('Pais')} - {time.get('Abreviacao')} - Grupo: {time.get('Grupo')}")

def listarGrupo():
  grupo = input('Grupo que deseja consultar: ').upper() 
  listarTimes([time for time in times if time.get('Grupo') == grupo])

opcao = 0
while opcao != 1:
    print('--' * 20)
    print('MENU:')
    time.sleep(1)
    opcao = int(input(f'[ 1 ] Sair do programa\n[ 2 ] Nova equipe\n[ 3 ] Novo jogo\n[ 4 ] Número total de jogos armazenados no “banco” da Copa do Mundo\n[ 5 ] Número total de equipes no “banco” da Copa do Mundo.\n[ 6 ] Listar os jogos que constam no banco e suas respectivas equipes\n[ 7 ] Pesquisar por país\n[ 8 ] Apagar jogo\nInsira a sua opção: '))
    print('--' * 20)

    if opcao == 1:
        time.sleep(1)
        print('Você está saindo do programa...')
        time.sleep(1)
        break

    elif opcao == 2:
        novoTime()
    
    elif opcao == 3:
        listarTimes(times)

    elif opcao == 4:
        listarGrupo()

    elif opcao == 5:
        break
    
    elif opcao == 6:
        break
    
    elif opcao == 7:
        break

    elif opcao == 8:
        break

    else:
        time.sleep(1)
        print('Opção inválida! Tente novamente.')
        time.sleep(1)