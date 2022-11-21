import time

print('-=' * 20)
print('{:^40}'.format('COPA DO MUNDO'))
print('-=' * 20)

def novaEquipe(pais, abreviacao, grupo):
    while True:
        pais = input('Insira o país: ')
        abreviacao = input('Insira a abreviação do país: ')
        grupo = input('Insira o grupo do país: ')
        

def novoJogo(dadosEquipe, gols, faltas ):
    quit()

opcao = 0
while opcao != 8:
    print('--' * 20)
    opcao = int(input(f'MENU:\n[ 1 ] Sair do programa\n[ 2 ] Nova equipe\n[ 3 ] Novo jogo\n[ 4 ] Número total de jogos armazenados no “banco” da Copa do Mundo\n[ 5 ] Número total de equipes no “banco” da Copa do Mundo.\n[ 6 ] Listar os jogos que constam no banco e suas respectivas equipes\n[ 7 ] Pesquisar por país\n[ 8 ] Apagar jogo\nInsira a sua opção: '))
    print('--' * 20)

    if opcao == 1:
        time.sleep(1)
        print('Você está saindo do programa...')
        time.sleep(1)
        break

    elif opcao == 2:
        with open ("nova-equipe.txt", "a+") as arquivo:
            for linha in arquivo.readlines():
                print(linha)
        

    elif opcao == 3:
        break

    elif opcao == 4:
        break

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