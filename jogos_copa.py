import json
import os
import time

# Início do programa -> Formatação inicial
print("--" * 20)
print("{:^40}".format("COPA DO MUNDO"))

times_file_name = "times_copa.json"
jogos_file_name = "jogos_copa.json"
times = list()
jogos = list()

def abrir_arquivo(file_name):
    if os.path.isfile(file_name):
        # Criação do arquivo times_copa.json
        with open(file_name, "r") as file:
            if len(file.readline()) > 0:
                # seek -> mover o cursor para o início do arquivo para poder carregar tudo ou salvar tudo a partir do inicio.
                file.seek(0)
                return json.load(file)

times = abrir_arquivo(times_file_name)
jogos = abrir_arquivo(jogos_file_name)


# Função 1 - Sair do programa
def sairPrograma():
    print("Você está saindo do programa...")
    time.sleep(1)
    quit()

# Salvar os times no arquivo times_copa.
def salvar_times_file():
    with open(times_file_name, "w") as times_file:
        json.dump(times, times_file)

# Salvar os jogos no arquivo jogos_copa.
def salvar_jogos_file():
    with open(jogos_file_name, "w") as jogos_file:
        json.dump(jogos, jogos_file)

def adicionar_grupo():
    add_grupo = False
    grupo = None
    # Validação -> Cada grupo pode ter apenas 4 times
    while not add_grupo:
        grupo = input("Insira o grupo do país: ").upper()
        # Manipulação de lista
        if len([time for time in times if time.get("Grupo") == grupo]) == 4:
            print("Este grupo já possui 4 seleções!\nEscolha outro grupo.")
        else:
            add_grupo = True
    return grupo

# Função 2 - para criar um time novo, uma nova equipe
def novo_time():
    salvar_times = False
    # Controle para continuar a cadastrar novos times
    while not salvar_times:
        pais = input("Insira o país da seleção: ")
        abreviacao = input("Insira a abreviação do país: ")
        grupo = adicionar_grupo()
        times.append({"id": len(times) + 1, "Pais": pais, "Abreviacao": abreviacao, "Grupo": grupo})

        if input("Cadastrar outra seleção(S/N): ").upper() != "S":
            salvar_times = True
    salvar_times_file()

def _pesquisar_time(nome_time):
    return [time for time in times if time.get("Pais") == nome_time][0]

def _pesquisar_time_por_codigo(time_id):
    return [time for time in times if time.get("id") == time_id][0]

def novo_jogo():
    salvar_jogos = False
    # Controle para continuar a cadastrar novos times
    while not salvar_jogos:
        time1 = input("Informe o primeiro time:  ")
        id_time1 = _pesquisar_time(time1).get("id") 
        time2 = input("Informe o segundo time:  ")
        id_time2 = _pesquisar_time(time2).get("id") 
        gols1 = input("Informe o número de gols obtidos no jogo pelo time 1:  ")
        gols2 = input("Informe o número de gols obtidos no jogo pelo time 2:  ")
        faltas1 = input("Informe o número de faltas marcadas no jogo pelo time 1:  ")
        faltas2 = input("Informe o número de faltas marcadas no jogo pelo time 2:  ")
        jogos.append({
            "time1": {"time": id_time1, "gols": gols1, "faltas": faltas1},
            "time2": {"time": id_time2, "gols": gols2, "faltas": faltas2},
            })
        if input("Cadastrar outra jogo(S/N): ").upper() != "S":
            salvar_jogos = True
    salvar_jogos_file()


# Função para listar os times existentes -> País - Abreviação - Grupo
def listarTimes(times):
    with open("times_copa.json", "r") as times_file:
        if len(times) == 0:
            print("Não há seleções cadastradas")
        for time in times:
            print(
                f"Seleção: {time.get('Pais')} - {time.get('Abreviacao')} - Grupo: {time.get('Grupo')}"
            )


# Função 8 - para listar os times existentes separando por GRUPOS
def listarGrupo():
    grupo = input("Grupo que deseja consultar: ").upper()
    # Manipulação de lista
    listarTimes([time for time in times if time.get("Grupo") == grupo])

#Função 9 - Pesquisar Jogo por país 
def pesquisajogo():

    quit()
    #como ler o arquivo .json?
    #como percorrer para "pesquisar"



#Função 10 - Apagar Jogo
def apagarArquivo():
    os.remove("times_copa.json")

def listar_jogos():
    for jogo in jogos:
        time1 = _pesquisar_time_por_codigo(jogo.get("time1").get("time"))
        time2 = _pesquisar_time_por_codigo(jogo.get("time2").get("time"))
        print(
            f'Grupo: {time1.get("Grupo")}, seleção: {time1.get("Pais")} - gols: {jogo.get("time1").get("gols")} - faltas: {jogo.get("time1").get("faltas")}\n'
            f'Grupo: {time2.get("Grupo")}, seleção: {time2.get("Pais")} - gols: {jogo.get("time2").get("gols")} - faltas: {jogo.get("time2").get("faltas")}'
            )


# MENU ->
opcao = 0
while opcao != 1:
    print("--" * 20)
    print("MENU:")
    opcao = int(
        input(
            f"[ 1 ] Sair do programa\n[ 2 ] Nova equipe\n[ 3 ] Listar times/equipes\n[ 4 ] Listar times/equipes por Grupo\n[ 5 ] Novo jogo\n[ 6 ] Número total de jogos armazenados no “banco” da Copa do Mundo\n[ 7 ] Número total de equipes no “banco” da Copa do Mundo.\n[ 8 ] Listar os jogos que constam no banco e suas respectivas equipes\n[ 9 ] Pesquisar por país\n[ 10 ] Apagar jogo\nInsira a sua opção: "
        )
    )
    print("--" * 20)

    # Caso o usuário digite 1, ele irá sair do programa
    if opcao == 1:
        sairPrograma()

    # Caso o usuário digite 2, ele poderá criar um ou mais times/equipes
    elif opcao == 2:
        novo_time()

    # Caso o usuário digite 3, ele irá visualizar os times/equipes cadastrados
    elif opcao == 3:
        listarTimes(times)

    # Caso o usuário digite 4, ele poderá escolher um grupo para visualizar os times/equipes contidos no mesmo
    elif opcao == 4:
        listarGrupo()

    # Caso o usuário digite 5, ele poderá criar um ou mais jogos
    elif opcao == 5:
        novo_jogo()

    # Caso o usuário digite 6, ele poderá visualizar o total de jogos cadastrados
    elif opcao == 6:
        break

    # Caso o usuário digite 7, ele poderá ver o número total de equipes cadastradas
    elif opcao == 7:
        break

    # Caso o usuário digite 8, ele poderá visualizar os jogos cadastrados com suas respectivas equipes
    elif opcao == 8:
        listar_jogos()

    # Caso o usuário digite 9, ele poderá fazer uma pesquisa por país
    elif opcao == 9:
        break

    # Caso o usuário digite 10, ele poderá apagar o jogo inteiro
    elif opcao == 10:
        print("Você está deletando o jogo...")
        apagarArquivo()
        print("Arquivo deletado!")
        print("Você está saindo do programa...")
        quit()

    # Caso o usuário digite uma opção diferente das propostas, ele terá que digitar novamente até colocar uma opção válida
    else:
        print("Opção inválida! Tente novamente.")
        time.sleep(1)