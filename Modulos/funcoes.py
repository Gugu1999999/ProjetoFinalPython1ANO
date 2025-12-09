import json
import random
from classes import *
from pathlib import Path
from time import sleep

def enunciado(texto):
    print("-" * 40)
    print(texto)
    print("-" * 40)
    sleep(0.5)

def menu3(Opc1, Opc2, Opc3):
    print("1.", Opc1)
    sleep(0.2)
    print("2.", Opc2)
    sleep(0.2)
    print("3.", Opc3)
    sleep(0.2)
    escolha = input("Escolha uma opção: ")
    return escolha
sleep(0.5)

def menu2(Opc1, Opc2):
    print("1.", Opc1)
    sleep(0.2)
    print("2.", Opc2)
    sleep(0.2)
    escolha = input("Escolha uma opção: ")
    return escolha
sleep(0.5)

import json

def cadastrar():
    nome = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()
    novo_jogador = jogador(nome, senha)
    with open("Data/jogadores.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    dados["jogadores"].append({
        "nome": novo_jogador.nome,
        "senha": novo_jogador.senha,
        "pontos": 0,
        "dinheiro": 0,
        "rank": "Iniciante"
    })
    with open("Data/jogadores.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        sleep(0.5)
    enunciado(f"Jogador {nome} cadastrado com sucesso!")

def login():
    while True:
        nome = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha: ").strip()
        jogador(nome, senha)
        with open("Data/jogadores.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
        for jogador_data in dados["jogadores"]:
            if jogador_data["nome"] == nome and jogador_data["senha"] == senha:
                enunciado(f"Bem-vindo de volta, {nome}!")
                jogador_atual = jogador(nome, senha)
                return jogador_atual
        enunciado("Nome de usuário ou senha incorretos. Tente novamente.")
        sleep(0.5)
            
def ranking():
    with open("Data/jogadores.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    jogadores_ordenados = sorted(dados["jogadores"], key=lambda x: x["pontos"], reverse=True)
    enunciado("Ranking dos Jogadores")
    sleep(0.5)
    for idx, jogador_data in enumerate(jogadores_ordenados, start=1):
        print(f" > {idx}. {jogador_data['nome']}", f"- Pontos: {jogador_data['pontos']}, Dinheiro: {jogador_data['dinheiro']}, Rank: {jogador_data['rank']}")
        sleep(0.5)
    print("-" * 40)

def voltar_menu():
    enunciado("Voltando ao menu principal...")

{'conteudo': [{'area': 'Matemática', 'perguntas': [{'pergunta': 'Qual a raiz quadrada de 9?', 'respostas': ['A: 2', 'B: 3', 'C: 4', 'D: 5'], 'correta': 'B'}, {'pergunta': 'Quanto é 5 + 5?', 'respostas': ['A: 8', 'B: 9', 'C: 10', 'D: 11'], 'correta': 'C'}]}, {'area': 'História', 'perguntas': [{'pergunta': 'Em que ano o Brasil foi descoberto?', 'respostas': ['A: 1492', 'B: 1500', 'C: 1600', 'D: 1822'], 'correta': 'B'}, {'pergunta': 'Quem proclamou a independência do Brasil?', 'respostas': ['A: Tiradentes', 'B: Getúlio Vargas', 'C: Dom Pedro I', 'D: Princesa Isabel'], 'correta': 'C'}]}]}

def Jogo():
    dinheiro = 0
    contPerg = 0
    while True:
        with open("Data/perguntas.json", "r", encoding="utf-8") as f:  # Essa parte do código é para selecionar uma pergunta
            dados = json.load(f)
        area = random.choice(dados["conteudo"])
        pergunta = random.choice(area["perguntas"])
        alternativas = pergunta["respostas"]
        correta = pergunta["correta"]
        print(f"Área: {area['area']}")                             #Agora é o jogo em si.
        print(pergunta["pergunta"])
        for alt in alternativas:
            sleep(0.2)
            print (alt)
        resposta = input("Escolha a alternativa correta (A, B, C, D): ").strip().upper()
        if resposta == correta:
            sleep(0.5)
            enunciado("Resposta correta!")
            dinheiro += 1000 
            contPerg += 1
        else:
            sleep(0.5)
            enunciado(f"Resposta incorreta! A resposta correta era {correta}.")
            dinheiro = dinheiro / 2
            contPerg += 1
        if contPerg == 5:
            jogador.saldo = dinheiro
            escolha = menu2("Voltar ao menu inicial", "Começar outra partidda")
            if escolha in "Ss" or escolha == 1:
                print (f"Você terminou a partida(s) com {jogador.saldo}")
                continue
            else:
                break
    enunciado(f"Fim da partida! Você agora está com {jogador.saldo}.")


    



    



   




    










        

