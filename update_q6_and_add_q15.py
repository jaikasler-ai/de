import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', html, flags=re.DOTALL)
if match:
    questions = json.loads(match.group(1))
    
    # 1. Update Question 6
    for q in questions:
        if q.get('id') == 'q-ue8-fiche4-6':
            for ans in q['answers']:
                if ans['id'] == 'e':
                    ans['correct'] = True
                else:
                    ans['correct'] = False
            q['explanation'] = "E est la seule proposition FAUSSE (donc la seule bonne réponse à cocher) ! La diminution des pertes azotées (épargne azotée) s'observe lors du jeûne prolongé (après plusieurs jours). En période post-absorptive (jeûne court), la protéolyse et l'excrétion d'azote restent élevées pour la néoglucogenèse. A, B, C, D sont toutes vraies."

    # 2. Add QCM 13 (Marasme)
    q15_marasme = {
        "id": "q-ue8-fiche4-15",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Marasme", "Immunonutrition", "Dénutrition"],
        "statement": "QCM 13 : Biochimie de l’immunonutrition. Concernant les propositions suivantes indiquez celles qui sont justes :",
        "answers": [
            { "id": "a", "text": "La dénutrition protéino-énergétique résulte d’un déséquilibre entre les apports et les besoins de l’organisme.", "correct": True },
            { "id": "b", "text": "Le marasme est une pathologie psychiatrique.", "correct": False },
            { "id": "c", "text": "Le marasme est une malnutrition protéino-énergétique adaptative.", "correct": True },
            { "id": "d", "text": "Le marasme induit une fonte musculaire et une fonte du tissu adipeux, mais les patients ont une albuminémie préservée.", "correct": True },
            { "id": "e", "text": "Les patients atteints de marasme présentent de nombreux œdèmes.", "correct": False }
        ],
        "explanation": "A, C, D VRAIS.\nB. FAUX : Le marasme est une malnutrition protéino-énergétique adaptative liée à une carence d'apport globale.\nE. FAUX : Les œdèmes caractérisent le syndrome de Kwashiorkor (décompensé), alors que dans le marasme l'albuminémie reste préservée et il n'y a pas d'œdèmes."
    }

    # Avoid duplicate insertion
    if not any(q.get('id') == 'q-ue8-fiche4-15' for q in questions):
        questions.append(q15_marasme)

    formatted_json = json.dumps(questions, ensure_ascii=False, indent=4)
    
    js_code = 'const INITIAL_QUESTIONS = ' + formatted_json + ';'
    js_export = 'export const INITIAL_QUESTIONS = ' + formatted_json + ';'

    html = re.sub(r'const INITIAL_QUESTIONS = \[.*?\];', js_code, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Updated index.html Question 6 & added QCM 13 (Marasme)!")

    with open('src/data/mockData.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = re.sub(r'export const INITIAL_QUESTIONS = \[.*?\];', js_export, js, flags=re.DOTALL)

    with open('src/data/mockData.js', 'w', encoding='utf-8') as f:
        f.write(js)

    print("Updated mockData.js Question 6 & added QCM 13 (Marasme)!")
