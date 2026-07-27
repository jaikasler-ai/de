import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', html, flags=re.DOTALL)
if match:
    questions = json.loads(match.group(1))
    
    for q in questions:
        if q.get('id') == 'q-ue11-new-11':
            for ans in q['answers']:
                if ans['id'] == 'd':
                    ans['correct'] = False
            
            q['explanation'] = "C et E VRAIS.\nA. FAUX : Les ribonucléosides = sucre + base (pas de phosphate).\nB. FAUX : Ce sont les ribonucléotides triphosphate qui sont substrats des ARN polymérases.\nC. VRAI.\nD. FAUX : La thymidine est un DÉSOXYRIBONUCLÉOSIDE (sucre désoxyribose dans l'ADN), pas un ribonucléoside.\nE. VRAI (NMP, NDP, NTP)."

    js_code = "const INITIAL_QUESTIONS = " + json.dumps(questions, ensure_ascii=False, indent=4) + ";"
    js_export = "export const INITIAL_QUESTIONS = " + json.dumps(questions, ensure_ascii=False, indent=4) + ";"

    html = re.sub(r'const INITIAL_QUESTIONS = \[.*?\];', js_code, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Updated Question 11 (item D set to False) in index.html!")

    with open('src/data/mockData.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = re.sub(r'export const INITIAL_QUESTIONS = \[.*?\];', js_export, js, flags=re.DOTALL)

    with open('src/data/mockData.js', 'w', encoding='utf-8') as f:
        f.write(js)

    print("Updated Question 11 in mockData.js!")
