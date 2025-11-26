import json

with open("perguntas.json", "r", encoding="utf-8") as perguntas:
    conteudo = json.load(perguntas)
    print (conteudo)
