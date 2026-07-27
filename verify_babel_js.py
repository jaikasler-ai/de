import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all curly apostrophes and check for syntax anomalies
content = content.replace("d'oubli", "d’oubli")
content = content.replace("d'ancrer", "d’ancrer")
content = content.replace("d'Ancrage", "d’Ancrage")
content = content.replace("d'ancrage", "d’ancrage")
content = content.replace("s'ajouteront", "s’ajouteront")
content = content.replace("s'entraîner", "s’entraîner")
content = content.replace("l'étape", "l’étape")
content = content.replace("l'échéance", "l’échéance")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced all raw single quotes in text with safe typographic apostrophes!")
