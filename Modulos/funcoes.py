import json
import random
from classes import *

with open("perguntas.json", "r", encoding="utf-8") as f:
    conteudo = json.load(f)
def pergunta_aleatoria():
    area = random.choice(conteudo["conteudo"])
    pergunta = random.choice(area["perguntas"])
    print(f"Área: {area['area']}")
    print(f"Pergunta: {pergunta['pergunta']}")
    for resposta in pergunta["respostas"]:
        print(resposta)
    return pergunta["correta"]
    correta = pergunta_aleatoria()

def enunciado(texto):
    print("-" * 40)
    print(texto)
    print("-" * 40)

def menu():
    print("1. Entrar na competição")
    print("2. Ver Ranking")
    print("3. Sair do jogo")
    escolha = input("Escolha uma opção: ")
    return escolha

def cadastrar():
    Usuario = input("Digite seu nome de usuário: ")
    jog = jogador(Usuario, 0, 0)
    




        

