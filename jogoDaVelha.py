import requests
import sys
import os

def atualiza_tabuleiro(board,line,column,value):

    board[line][column] = value
    for linha in tabuleiro:
        for coluna in linha:
            print(coluna, end=" ")
        print(" ")
    return board

def limpa_terminal():

    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

url = "http://labcores.ppgi.ufrj.br/niv_python/ttt"
limpa_terminal()

while(True):

    parameters = {"start": "True"}
    req = requests.get(url, params=parameters)
    retorno = req.json()
    sessao = retorno["session"]
    jogador = retorno["player_num"]
    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    site = "2"

    if jogador == 2:
        cpu_move = retorno["cpu_move"]
        print("A primeira jogada foi do Site: ({},{})".format(cpu_move[0],cpu_move[1]))
        tabuleiro = atualiza_tabuleiro(tabuleiro, cpu_move[0], cpu_move[1], "1")
        site = "1"
    else:
        print("A primeira jogada será sua:")

    fim = False

    while(fim == False):

        lin = input("Informe a linha desejada para a sua jogada: ")

        if lin not in ["0", "1", "2"]:
            print("Entrada inválida.")
            continue

        col = input("Agora, informe a coluna desejada para a sua jogada: ")

        if col not in ["0", "1", "2"]:
            print("Entrada inválida.")
            continue

        if tabuleiro[int(lin)][int(col)] != " ":
            print("Posição já foi utilizada.")
            continue

        print("Sua jogada: ({},{})".format(lin,col))
        tabuleiro = atualiza_tabuleiro(tabuleiro,int(lin),int(col),str(jogador))
        parameters = {"session": str(sessao),"row": lin, "col": col}
        req = requests.get(url, params=parameters)
        retorno = req.json()

        try:
            fim = retorno["end"]
        except KeyError:
            print("A jogada do site: ({},{})".format(retorno["row"],retorno["col"]))
            tabuleiro = atualiza_tabuleiro(tabuleiro,int(retorno["row"]),int(retorno["col"]),site)

    if retorno["winner"] == jogador:
        print("Eu ganhei !!")
    elif retorno["winner"] == 0:
        print("Acabou empatado.")
    else:
        print("Eu perdi...")

    continuarJogando = None

    while(continuarJogando is None):

        continuarJogando = input("Deseja continuar, (S)im ou (N)ão?").upper()

        if continuarJogando not in ["S","N"]:
            print("Opção inválida.")
            continuarJogando = None
            continue
        elif continuarJogando == "N":
            limpa_terminal()
            print("Programa encerrado!!")
            sys.exit()
        limpa_terminal()
