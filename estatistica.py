# Autor: Wander dos Santos Vasconcellos
#Data: 11/02/2019
#Alterações:
#13/02/2019 - Inserção do intervalo de idade para o cálculo da probabilidade de viver de um passageiro.
#
import csv
import sys
import os

def read_csv(filePath):

    table = list()
    with open(filePath) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            table.append(row)
    return table

def is_float(idad):

    try:
        float(idad)
        return True
    except ValueError:
        return False

def calcula_probabilidade_de_viver(idade, sexo, classe, passageiros):

    if is_float(idade):
        totalPassageirosVivos = len([passgVivos for passgVivos in passageiros if is_float(passgVivos["Age"]) and float(passgVivos["Age"]) >= (float(idade)-1) and float(passgVivos["Age"]) <= (float(idade)+1) and passgVivos["Sex"] == sexo and passgVivos["Pclass"] == classe and passgVivos["Survived"] == "1"])
        totalPassageiros = len([passgVivos for passgVivos in passageiros if is_float(passgVivos["Age"]) and float(passgVivos["Age"]) >= (float(idade)-1) and float(passgVivos["Age"]) <= (float(idade)+1) and passgVivos["Sex"] == sexo and passgVivos["Pclass"] == classe])
    else:
        totalPassageirosVivos = len([passgVivos for passgVivos in passageiros if passgVivos["Age"] == idade and passgVivos["Sex"] == sexo and passgVivos["Pclass"] == classe and passgVivos["Survived"] == "1"])
        totalPassageiros = len([passgVivos for passgVivos in passageiros if passgVivos["Age"] == idade and passgVivos["Sex"] == sexo and passgVivos["Pclass"] == classe])

    return totalPassageirosVivos / totalPassageiros

def exibe_probabilidade(passg, passageiros):

    probabilidadeDeVida = calcula_probabilidade_de_viver(passg["Age"], passg["Sex"], passg["Pclass"], passageiros)
    print("A probabilidade de sobreviver do(a) passageiro(a) {} era de: {:3.2%}".format(passg["Name"], probabilidadeDeVida))

titanic_tbl = read_csv("D:/Setor/Python_Fonts/titanic/train.csv")
id = ''
passageiro = []
probabilidadeDeVida = 0.0

while (id == ''):
    
    id = input("Informe o id do passageiro, ou 'T' para calcular a probabilidade de sobrevivência de todos, ou 'S' para Sair: ").upper()

    if id == 'S':
        print("Programa encerrado!!")
        sys.exit()
    elif id == 'T':
        for passenger in titanic_tbl:
            exibe_probabilidade(passenger, titanic_tbl)
  
        print("Total de passageiros: ", len(titanic_tbl))
        sys.exit()
 
    passageiro = [passg for passg in titanic_tbl if passg["PassengerId"] == id]

    if len(passageiro) == 0:
        id = ''
        print("Id não encontrado!!")
        os.system("pause")
    elif len(passageiro) > 1:
        id = ''
        print("Existem várias ocorrências com este Id!!")
        os.system("pause")
    else:
        id = ''
        traveler = passageiro[0]
        exibe_probabilidade(traveler, titanic_tbl)
