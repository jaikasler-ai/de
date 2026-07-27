import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract INITIAL_QUESTIONS
match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', html, flags=re.DOTALL)
if match:
    questions = json.loads(match.group(1))
    
    # Update chapter for all q-ue11-new- questions to Fiche n°1
    for q in questions:
        if q.get('id', '').startswith('q-ue11-new-'):
            q['chapter'] = 'Fiche n°1 - Introduction à la Biologie moléculaire.pdf'
            
    js_code = "const INITIAL_QUESTIONS = " + json.dumps(questions, ensure_ascii=False, indent=4) + ";"
    js_export = "export const INITIAL_QUESTIONS = " + json.dumps(questions, ensure_ascii=False, indent=4) + ";"

    html = re.sub(r'const INITIAL_QUESTIONS = \[.*?\];', js_code, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Updated index.html: all new UE1.1 questions are in Fiche n°1!")

    with open('src/data/mockData.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = re.sub(r'export const INITIAL_QUESTIONS = \[.*?\];', js_export, js, flags=re.DOTALL)

    with open('src/data/mockData.js', 'w', encoding='utf-8') as f:
        f.write(js)

    print("Updated mockData.js: all new UE1.1 questions are in Fiche n°1!")
