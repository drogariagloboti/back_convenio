from datetime import datetime, timedelta, date
import re

def data_atual():

    data_atual = date.today() #pega a data atual

    return data_atual

def hora_agora():

    data_e_hora_atuais = datetime.now() #pega data e hora atual

    hora_agora = data_e_hora_atuais.strftime('%H:%M:%S') #remove a data deixando horas em horas:minutos:segundos

    return hora_agora

def hora_anterior():

    data_e_hora_anterior = datetime.now() - timedelta(hours=1) #pega data e hora atual e subtrai uma hora

    hora_anterior = data_e_hora_anterior.strftime('%H:%M:%S') #remove a data da subtração deixando horas em horas:minutos:segundos

    return hora_anterior

def get_ano():

    data_atual = str(date.today()) #pega a data atual
    ano = data_atual[:4]

    return ano

def get_mes():

    data_atual = str(date.today()) #pega a data atual
    mes = data_atual[5:7]

    return mes

def get_dia():

    data_atual = str(date.today()) #pega a data atual
    dia = data_atual[8:]

    return dia

def get_periodo(inicio,fim):

    # Data final
    d2 = datetime.strptime(fim, '%Y-%m-%d')

    # Data inicial
    d1 = datetime.strptime(inicio, '%Y-%m-%d')

    # Realizamos o calculo da quantidade de dias
    quantidade_dias = abs((d2 - d1).days)

    i = 0
    periodo = []
    while(i < quantidade_dias):
        data_comp = d1 + timedelta(days=i)
        data_ajust = data_comp.strftime('%Y-%m-%d')
        periodo.append(data_ajust)
        i = i + 1
    periodo.append(fim)

    return periodo

def dia_anterior():
    dia = date.today()

    ontem = dia - timedelta(days=1)

    return ontem

def data_hora_agora():

    data_atual = str(date.today())

    data_e_hora_atuais = datetime.now() #pega data e hora atual

    hora_agora = str(data_e_hora_atuais.strftime('%H:%M:%S')) #remove a data deixando horas em horas:minutos:segundos

    return str(data_atual + ' ' + hora_agora)