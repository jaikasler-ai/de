import json
import re

new_ue11_questions = [
    {
        "id": "q-ue11-new-1",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Moyen",
        "tags": ["Virus", "Eucaryotes", "Procaryotes", "Griffith"],
        "statement": "1. Parmi les propositions suivantes, laquelle (lesquelles) est (sont) exacte(s) ?",
        "answers": [
            { "id": "a", "text": "Les virus contiennent leurs informations génétiques sous forme d’ADN", "correct": False },
            { "id": "b", "text": "Les êtres vivants sont divisés en 3 royaumes : Eucaryotes, Archaebactéries, Eubactéries", "correct": False },
            { "id": "c", "text": "Les protistes ne possèdent pas de noyau", "correct": False },
            { "id": "d", "text": "Toutes les enzymes sont des protéines utilisées comme catalyseurs.", "correct": True },
            { "id": "e", "text": "L’expérience de Griffith, en 1928, prouve que l’information génétique est portée par l’ADN", "correct": True }
        ],
        "explanation": "D et E vrais. A: Soit sous forme d’ARN soit d’ADN. B: En 3 domaines. C: Les protistes sont des eucaryotes (ont un noyau)."
    },
    {
        "id": "q-ue11-new-2",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Moyen",
        "tags": ["Organites", "Procaryotes", "Protozoaires"],
        "statement": "2. Concernant les propositions suivantes, indiquer celle(s) qui est (sont) exacte(s) :",
        "answers": [
            { "id": "a", "text": "Les cellules eucaryotes et procaryotes contiennent un réticulum endoplasmique granuleux", "correct": False },
            { "id": "b", "text": "Les cellules eucaryotes et procaryotes contiennent des peroxysomes", "correct": False },
            { "id": "c", "text": "Les cellules eucaryotes et procaryotes contiennent un noyau délimité par une enveloppe nucléaire", "correct": False },
            { "id": "d", "text": "Les procaryotes ne contiennent pas de mitochondries", "correct": True },
            { "id": "e", "text": "Les protozoaires sont des eucaryotes", "correct": True }
        ],
        "explanation": "D et E vrais. Pas d'organites ni de noyau délimité chez les procaryotes. Les protozoaires sont des eucaryotes."
    },
    {
        "id": "q-ue11-new-3",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Difficile",
        "tags": ["Taille", "Bactéries", "Ribosomes"],
        "statement": "3. Parmi les propositions suivantes concernant les différences entre procaryotes et eucaryotes, laquelle (lesquelles) est (sont) vraie(s) ?",
        "answers": [
            { "id": "a", "text": "Les procaryotes ont une taille comprise entre 10 et 100 μm", "correct": False },
            { "id": "b", "text": "Les cellules bactériennes sont toujours entourées d’une membrane cellulaire et d’une paroi cellulaire", "correct": False },
            { "id": "c", "text": "Les virus sont les cellules vivantes les plus simples et sont classées parmi les procaryotes", "correct": False },
            { "id": "d", "text": "Chez les eucaryotes, il existe une compartimentation en ce qui concerne l’expression des gènes", "correct": True },
            { "id": "e", "text": "Les ribosomes sont présents chez les procaryotes et les eucaryotes", "correct": True }
        ],
        "explanation": "D et E vrais. Procaryotes = 0,1 à 10 μm. La paroi peut être absente. Les virus sont des acaryotes."
    },
    {
        "id": "q-ue11-new-4",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Moyen",
        "tags": ["Bactériophage", "Métazoaire", "Parasite"],
        "statement": "4. Parmi les propositions suivantes, indiquer la (les) bonne(s) réponse(s) :",
        "answers": [
            { "id": "a", "text": "Un bactériophage est une bactérie", "correct": False },
            { "id": "b", "text": "Un virus est un procaryote", "correct": False },
            { "id": "c", "text": "Un protozoaire est un organisme animal multicellulaire", "correct": False },
            { "id": "d", "text": "Un métazoaire possède des tissus et des organes", "correct": True },
            { "id": "e", "text": "Certains parasites comme le Tænia peuvent être plus grands qu’un être humain", "correct": True }
        ],
        "explanation": "D et E vrais. Bactériophage = virus de bactérie. Protozoaire = unicellulaire. Métazoaire = pluricellulaire animal."
    },
    {
        "id": "q-ue11-new-5",
        "subjectId": "sub-1",
        "chapter": "Fiche n°2 - Organisation de l’ADN.pdf",
        "year": 2023,
        "difficulty": "Moyen",
        "tags": ["Cellules", "ADN-Z", "ADAR1"],
        "statement": "5. Parmi les propositions suivantes, cochez la ou les bonne(s) réponse(s) :",
        "answers": [
            { "id": "a", "text": "Tous les organismes vivants sont constitués d'au moins 1 cellule", "correct": True },
            { "id": "b", "text": "Les organismes pluricellulaires ou multicellulaires sont constitués de plusieurs cellules qui ont des fonctions précises", "correct": True },
            { "id": "c", "text": "L'ADN-Z comporte 12 pb par tour d'hélice et des enzymes comme ADAR1 peuvent se lier sur des régions spécifiques", "correct": True },
            { "id": "d", "text": "Dans l'ADN-Z il y a des séquences riches en répétition GC ou GT", "correct": True },
            { "id": "e", "text": "Toutes les propositions sont exactes", "correct": False }
        ],
        "explanation": "A, B, C, D vrais. E faux (les propositions A à D sont exactes)."
    },
    {
        "id": "q-ue11-new-6",
        "subjectId": "sub-1",
        "chapter": "Fiche n°2 - Organisation de l’ADN.pdf",
        "year": 2023,
        "difficulty": "Facile",
        "tags": ["Hélice ADN", "Chargaff", "Liaisons Hydrogène"],
        "statement": "6. Parmi les propositions suivantes, cochez la ou les bonne(s) réponse(s) :",
        "answers": [
            { "id": "a", "text": "L'ADN est une double hélice qui tourne vers la droite et dont les bases azotées sont liées par des liaisons hydrogènes", "correct": True },
            { "id": "b", "text": "Les 2 brins sont parallèles et sont complémentaires", "correct": False },
            { "id": "c", "text": "Il y a 2 liaisons hydrogène entre A et C", "correct": False },
            { "id": "d", "text": "Il y a 3 liaisons hydrogène entre G et T", "correct": False },
            { "id": "e", "text": "Selon la règle de Chargaff, A + G = T + C", "correct": True }
        ],
        "explanation": "A et E vrais. B: Brins antiparallèles. C: 2 liaisons H entre A et T. D: 3 liaisons H entre G et C."
    },
    {
        "id": "q-ue11-new-7",
        "subjectId": "sub-1",
        "chapter": "Fiche n°2 - Organisation de l’ADN.pdf",
        "year": 2023,
        "difficulty": "Moyen",
        "tags": ["ADN-A", "Watson-Crick", "Nucléosides"],
        "statement": "7. Parmi les propositions suivantes, cochez la ou les bonne(s) réponse(s) :",
        "answers": [
            { "id": "a", "text": "L'ADN-A comporte 11 pb par tour d'hélice", "correct": True },
            { "id": "b", "text": "L'ADN-A est le modèle stable décrit par Watson et Crick", "correct": False },
            { "id": "c", "text": "Le désoxyribose est le sucre présent dans l'ADN", "correct": True },
            { "id": "d", "text": "Le squelette sucre-phosphate est orienté dans le sens 5' vers 3'", "correct": True },
            { "id": "e", "text": "L'ADN-Z a un sens dextrogyre", "correct": False }
        ],
        "explanation": "A, C, D vrais. B: Le modèle Watson-Crick est l'ADN-B. E: L'ADN-Z est lévogyre."
    },
    {
        "id": "q-ue11-new-8",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Facile",
        "tags": ["Besoins cellulaires", "Énergie", "Reproduction"],
        "statement": "8. Concernant les besoins d’une cellule laquelle (lesquelles) de ces/cette proposition est (sont) correcte(s) ? Cochez-la ou les réponse(s) vraie(s)",
        "answers": [
            { "id": "a", "text": "Mécanisme de production d'énergie", "correct": True },
            { "id": "b", "text": "Une adaptation à l’environnement.", "correct": True },
            { "id": "c", "text": "La capacité de se reproduire.", "correct": True },
            { "id": "d", "text": "Doit reconnaitre le soi-même du reste (plus simple pour les êtres unicellulaires).", "correct": True },
            { "id": "e", "text": "Aucune de ces propositions sont exactes", "correct": False }
        ],
        "explanation": "A, B, C, D vrais. La cellule a besoin de produire de l'énergie, de s'adapter, de se reproduire et de distinguer le soi du non-soi."
    },
    {
        "id": "q-ue11-new-9",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Moyen",
        "tags": ["Phospholipides", "Liaison Ester", "Membrane"],
        "statement": "9. Parmi les propositions suivantes laquelle (lesquelles) est (sont) correcte(s) ? Cochez-la ou les réponse(s) vraie(s)",
        "answers": [
            { "id": "a", "text": "Deux acides gras sont fixés au glycérol par des liaisons éthers", "correct": False },
            { "id": "b", "text": "Les molécules de phospholipides sont composées d’un groupe de tête hydrophile et de deux acides gras", "correct": True },
            { "id": "c", "text": "Les phospholipides sont situés au niveau de la membrane cellulaire", "correct": True },
            { "id": "d", "text": "Chaque cellule doit générer sa propre énergie et synthétiser ses propres macromolécules", "correct": True },
            { "id": "e", "text": "Aucune de ces propositions sont exactes", "correct": False }
        ],
        "explanation": "B, C, D vrais. A faux : les deux acides gras sont fixés au glycérol par des liaisons ester."
    },
    {
        "id": "q-ue11-new-10",
        "subjectId": "sub-1",
        "chapter": "Fiche n°2 - Organisation de l’ADN.pdf",
        "year": 2024,
        "difficulty": "Facile",
        "tags": ["ARN", "Bases azotées", "Uracile"],
        "statement": "10. Quelles sont les 4 bases azotées de l’ARN ?",
        "answers": [
            { "id": "a", "text": "Adénine", "correct": True },
            { "id": "b", "text": "Guanine", "correct": True },
            { "id": "c", "text": "Cytosine", "correct": True },
            { "id": "d", "text": "Thymine", "correct": False },
            { "id": "e", "text": "Uracile", "correct": True }
        ],
        "explanation": "A, B, C, E vrais. D faux : dans l'ARN, la thymine est remplacée par l'uracile."
    },
    {
        "id": "q-ue11-new-11",
        "subjectId": "sub-1",
        "chapter": "Fiche n°2 - Organisation de l’ADN.pdf",
        "year": 2024,
        "difficulty": "Moyen",
        "tags": ["Nucléosides", "Nucléotides", "Squelette"],
        "statement": "11. Parmi les propositions suivantes, laquelle (lesquelles) est (sont) vraie(s) ? Cochez la (les) réponse(s) exacte(s).",
        "answers": [
            { "id": "a", "text": "Les ribonucléosides sont composés d’un sucre, d’un phosphate et d’une base.", "correct": False },
            { "id": "b", "text": "Les ribonucléosides triphosphate sont les substrats des ARN polymérases pour la synthèse des ARN.", "correct": False },
            { "id": "c", "text": "L’ADN est un double brin, ayant un squelette de sucre – phosphate lié à un ensemble de bases azotés.", "correct": True },
            { "id": "d", "text": "La cytidine, la thymidine, l’adénosine et la guanosine sont des ribonucléosides.", "correct": True },
            { "id": "e", "text": "Chaque ribonucléotide existe sous 3 formes : Ribonucléotide monophosphate, Ribonucléotide diphosphate et Ribonucléotide triphosphate.", "correct": True }
        ],
        "explanation": "C, D, E vrais. A: Les ribonucléosides = sucre + base (pas de phosphate). B: Ce sont les ribonucléotides triphosphate."
    },
    {
        "id": "q-ue11-new-12",
        "subjectId": "sub-1",
        "chapter": "Fiche n°2 - Organisation de l’ADN.pdf",
        "year": 2024,
        "difficulty": "Difficile",
        "tags": ["Chargaff", "ADN-Z", "ADAR1"],
        "statement": "12. Parmi les propositions suivantes, quelle(s) est(sont) l’(les) affirmation(s) fausse (s) ? Cochez-la(les) bonne(s) réponse(s).",
        "answers": [
            { "id": "a", "text": "Selon la règle de Chargaff, la quantité d’adénine doit être égale à la cytosine.", "correct": True },
            { "id": "b", "text": "Selon la règle de Chargaff, la quantité de thymine doit être égale à la guanine.", "correct": True },
            { "id": "c", "text": "L’ADN-A a un sens lévogyre en condition non-physiologie.", "correct": True },
            { "id": "d", "text": "L’ADN-H est favorisé par les conditions acides.", "correct": False },
            { "id": "e", "text": "L’enzyme ADAR-1 se lie spécifiquement à l’ADN-A.", "correct": True }
        ],
        "explanation": "A, B, C, E sont des affirmations fausses (donc les bonnes réponses demandées). D est une affirmation vraie."
    }
]

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract existing INITIAL_QUESTIONS array using regex
match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', html, flags=re.DOTALL)
if match:
    existing_q = json.loads(match.group(1))
    updated_q = existing_q + new_ue11_questions
    
    js_code = "const INITIAL_QUESTIONS = " + json.dumps(updated_q, ensure_ascii=False, indent=4) + ";"
    js_export = "export const INITIAL_QUESTIONS = " + json.dumps(updated_q, ensure_ascii=False, indent=4) + ";"

    html = re.sub(r'const INITIAL_QUESTIONS = \[.*?\];', js_code, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Updated index.html with 12 new UE1.1 questions!")

    # Update mockData.js
    with open('src/data/mockData.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = re.sub(r'export const INITIAL_QUESTIONS = \[.*?\];', js_export, js, flags=re.DOTALL)

    with open('src/data/mockData.js', 'w', encoding='utf-8') as f:
        f.write(js)

    print("Updated mockData.js with 12 new UE1.1 questions!")
