#importar numpy
import numpy as np
# Dados dos Participantes
participantes  = [
    {"nome": "Alice", "localização": "Brasil", "curso": "administração", "interesse": "calculo"},
    {"nome": "Bob", "localização":  "Brasil", "curso": "economia", "interesse": "calculo"},
    {"nome": "Charlie", "localização": "Brasil", "curso": "administração", "interesse": "calculo"},
    {"nome": "Diana", "localização": "Canadá", "curso": "matemática", "interesse": "analise"}]
#caso seja necessário adcionar mais participantes
#usando sets para identiicar participantes únicos
regioes = set(participante["localização"] for participante in participantes)
#usando um dicionário para contar participantes por curso
cursos = {}
for p in participantes:
    curso = p["curso"]
    cursos.setdefault(curso, []).append(p["nome"])
#Usando o numpy para analisar os dados
#erro: cursos_de_interesses = np.array([interesse for participante in participantes for interesse  in participante["interesse"]]) 
interesses = np.array([p["interesse"] for p in participantes])
#interesses únicos
#interesses_unicos = np.unique(cursos_de_interesses, return_counts=True)
interesses_unicos, contagens = np.unique(interesses, return_counts=True)
interesse_mais_popular = interesses_unicos[np.argmax(contagens)]
#curso_mais_popular = interesses_unicos[np.argmax(contagem)  ]
# Exibindo os resultados
print("Regiões dos participantes:", regioes)
print("Cursos e participantes:", cursos)