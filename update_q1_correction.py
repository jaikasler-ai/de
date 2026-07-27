import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', html, flags=re.DOTALL)
if match:
    questions = json.loads(match.group(1))
    
    for q in questions:
        if q.get('id') == 'q-ue11-new-1':
            # Update item A text and item B correct
            for ans in q['answers']:
                if ans['id'] == 'a':
                    ans['text'] = "Les virus contiennent uniquement leurs informations génétiques sous forme d’ADN"
                    ans['correct'] = False
                elif ans['id'] == 'b':
                    ans['correct'] = True
            
            q['explanation'] = "B, D, E VRAIS. A. FAUX : Soit sous forme d'ARN soit sous forme d'ADN (pas uniquement ADN). B. VRAI (selon l'énoncé du cours). C. FAUX : Les protistes sont des eucaryotes (ils ont un noyau). D. VRAI. E. VRAI."

    js_code = "const INITIAL_QUESTIONS = " + json.dumps(questions, ensure_ascii=False, indent=4) + ";"
    js_export = "export const INITIAL_QUESTIONS = " + json.dumps(questions, ensure_ascii=False, indent=4) + ";"

    html = re.sub(r'const INITIAL_QUESTIONS = \[.*?\];', js_code, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Updated index.html Question 1 successfully!")

    with open('src/data/mockData.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = re.sub(r'export const INITIAL_QUESTIONS = \[.*?\];', js_export, js, flags=re.DOTALL)

    with open('src/data/mockData.js', 'w', encoding='utf-8') as f:
        f.write(js)

    print("Updated mockData.js Question 1 successfully!")
