import json
import re

exact_ue11_qcms = [
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
        "explanation": "D et E VRAIS. A. FAUX : Soit sous forme d’ARN soit sous forme d’ADN. B. FAUX : En 3 domaines (Eucaryotes, Archaebactéries, Eubactéries). C. FAUX : Les protistes sont des eucaryotes (ils ont un noyau). D. VRAI. E. VRAI."
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
        "explanation": "D et E VRAIS. A. FAUX : Pas de REG ni d’organites chez les procaryotes. B. FAUX : Pas d’organites chez les procaryotes. C. FAUX : Pas de noyau chez les procaryotes. D. VRAI. E. VRAI : Existent à l’état libre ou parasites."
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
            { "id": "c", "text": "Les virus sont les cellules vivantes les plus simple et sont classées parmi les procaryotes", "correct": False },
            { "id": "d", "text": "Chez les eucaryotes, il existe une compartimentation en ce qui concerne l’expression des gènes", "correct": True },
            { "id": "e", "text": "Les ribosomes sont présents chez les procaryotes et les eucaryotes", "correct": True }
        ],
        "explanation": "D et E VRAIS. A. FAUX : Ce sont les eucaryotes (10-100 μm). Procaryotes = 0,1 à 10 μm. B. FAUX : La paroi peut être absente. C. FAUX : Virus = acaryotes."
    },
    {
        "id": "q-ue11-new-4",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Moyen",
        "tags": ["Bactériophage", "Métazoaire", "Tænia"],
        "statement": "4. Parmi les propositions suivantes, indiquer la (les) bonne(s) réponse(s) :",
        "answers": [
            { "id": "a", "text": "Un bactériophage est une bactérie", "correct": False },
            { "id": "b", "text": "Un virus est un procaryote", "correct": False },
            { "id": "c", "text": "Un protozoaire est un organisme animal multicellulaire", "correct": False },
            { "id": "d", "text": "Un métazoaire possède des tissus et des organes", "correct": True },
            { "id": "e", "text": "Certains parasites comme le Tænia peuvent être plus grands qu’un être humain", "correct": True }
        ],
        "explanation": "D et E VRAIS. A. FAUX : Virus de bactérie. B. FAUX : Acaryote. C. FAUX : Eucaryote unicellulaire. D. VRAI : Métazoaire = pluricellulaire animal. E. VRAI : Jusqu’à 10 m."
    },
    {
        "id": "q-ue11-new-5",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2023,
        "difficulty": "Moyen",
        "tags": ["Cellules", "ADN-Z", "ADAR1"],
        "statement": "5. (Medisup) Parmi les propositions suivantes, cochez la ou les bonne(s) réponse(s) :",
        "answers": [
            { "id": "a", "text": "Tous les organismes vivants sont constitués d'au moins 1 cellule", "correct": True },
            { "id": "b", "text": "Les organismes pluricellulaires ou multicellulaires sont constitués de plusieurs cellules qui ont des fonctions précises", "correct": True },
            { "id": "c", "text": "L'ADN-Z comporte 12 pb par tour d'helice et des enzymes comme ADAR1 peuvent se lier sur des régions spécifiques", "correct": True },
            { "id": "d", "text": "Dans l'ADN-Z il y a des séquences riches en répétition GC ou GT", "correct": True },
            { "id": "e", "text": "Toutes les propositions sont exactes", "correct": False }
        ],
        "explanation": "A, B, C, D VRAIS. E. FAUX dans la grille Medisup."
    },
    {
        "id": "q-ue11-new-6",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2023,
        "difficulty": "Facile",
        "tags": ["Double Hélice", "Chargaff", "Liaisons H"],
        "statement": "6. (Medisup) Parmi les propositions suivantes, cochez la ou les bonne(s) réponse(s) :",
        "answers": [
            { "id": "a", "text": "L'ADN est une double hélice qui tourne vers la droite et dont les bases azotées sont liées par des liaisons hydrogènes", "correct": True },
            { "id": "b", "text": "Les 2 brins sont parallèles et sont complémentaires", "correct": False },
            { "id": "c", "text": "Il y a 2 liaisons hydrogène entre A et C", "correct": False },
            { "id": "d", "text": "Il y a 3 liaisons hydrogène entre G et T", "correct": False },
            { "id": "e", "text": "Selon la règle de Chargaff, A + G = T + C", "correct": True }
        ],
        "explanation": "A et E VRAIS. B. FAUX : Antiparallèles. C. FAUX : 2 liaisons H entre A-T. D. FAUX : 3 liaisons H entre G-C. E. VRAI : Purines A+G = Pyrimidines T+C."
    },
    {
        "id": "q-ue11-new-7",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2023,
        "difficulty": "Moyen",
        "tags": ["ADN-A", "Watson-Crick", "Désoxyribose"],
        "statement": "7. (Medisup) Parmi les propositions suivantes, cochez la ou les bonne(s) réponse(s) :",
        "answers": [
            { "id": "a", "text": "L'ADN-A comporte 11 pb par tour d'hélice", "correct": True },
            { "id": "b", "text": "L'ADN-A est le modèle stable décrit par Watson et Crick", "correct": False },
            { "id": "c", "text": "Le désoxyribose est le sucre présent dans l'ADN", "correct": True },
            { "id": "d", "text": "Le squelette sucre-phosphate est orienté dans le sens 5' vers 3'", "correct": True },
            { "id": "e", "text": "L'ADN-Z a un sens dextrogyre", "correct": False }
        ],
        "explanation": "A, C, D VRAIS. B. FAUX : C'est l'ADN-B. E. FAUX : L'ADN-Z est lévogyre."
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
        "explanation": "A, B, C, D VRAIS. E. FAUX : A, B, C et D décrivent les besoins fondamentaux d'une cellule."
    },
    {
        "id": "q-ue11-new-9",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Moyen",
        "tags": ["Phospholipides", "Liaisons Ester", "Membrane"],
        "statement": "9. Parmi les propositions suivantes laquelle (lesquelles) est (sont) correcte(s) ? Cochez-la ou les réponse(s) vraie(s)",
        "answers": [
            { "id": "a", "text": "Deux acides gras sont fixés au glycérol par des liaisons éthers", "correct": False },
            { "id": "b", "text": "Les molécules de phospholipides sont composées d’un groupe de tête hydrophile et de deux acides gras", "correct": True },
            { "id": "c", "text": "Les phospholipides sont situés au niveau de la membrane cellulaire", "correct": True },
            { "id": "d", "text": "Chaque cellule doit générer sa propre énergie et synthétiser ses propres macromolécules", "correct": True },
            { "id": "e", "text": "Aucune de ces propositions sont exactes", "correct": False }
        ],
        "explanation": "B, C, D VRAIS. A. FAUX : Liaisons ESTER (et non éthers)."
    },
    {
        "id": "q-ue11-new-10",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Facile",
        "tags": ["ARN", "Bases Azotées", "Uracile"],
        "statement": "10. Quelles sont les 4 bases azotées de l’ARN ?",
        "answers": [
            { "id": "a", "text": "Adénine", "correct": True },
            { "id": "b", "text": "Guanine", "correct": True },
            { "id": "c", "text": "Cytosine", "correct": True },
            { "id": "d", "text": "Thymine", "correct": False },
            { "id": "e", "text": "Uracile", "correct": True }
        ],
        "explanation": "A, B, C, E VRAIS. D. FAUX : Dans l’ARN, la thymine est remplacée par l’uracile."
    },
    {
        "id": "q-ue11-new-11",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Moyen",
        "tags": ["Ribonucléosides", "Ribonucléotides", "Squelette"],
        "statement": "11. Parmi les propositions suivantes, laquelle (lesquelles) est (sont) vraie(s) ? Cochez la (les) réponse(s) exacte(s).",
        "answers": [
            { "id": "a", "text": "Les ribonucléosides sont composés d’un sucre, d’un phosphate et d’une base.", "correct": False },
            { "id": "b", "text": "Les ribonucléosides triphosphate sont les substrats des ARN polymérases pour la synthèse des ARN.", "correct": False },
            { "id": "c", "text": "L’ADN est un double brin, ayant un squelette de sucre – phosphate lié à un ensemble de bases azotés.", "correct": True },
            { "id": "d", "text": "La cytidine, la thymidine, l’adénosine et la guanosine sont des ribonucléosides.", "correct": True },
            { "id": "e", "text": "Chaque ribonucléotide existe sous 3 formes : Ribonucléotide monophosphate, Ribonucléotide diphosphate et Ribonucléotide triphosphate.", "correct": True }
        ],
        "explanation": "C, D, E VRAIS. A. FAUX : Ribonucléosides = sucre + base (pas de phosphate). B. FAUX : Ribonucléotides triphosphate."
    },
    {
        "id": "q-ue11-new-12",
        "subjectId": "sub-1",
        "chapter": "Fiche n°1 - Introduction à la Biologie moléculaire.pdf",
        "year": 2024,
        "difficulty": "Difficile",
        "tags": ["Chargaff", "ADN-Z", "ADAR1"],
        "statement": "12. Parmi les propositions suivantes, quelle(s) est(sont) l’(les) affirmation(s) FAUSSE (S) ? Cochez-la(les) bonne(s) réponse(s).",
        "answers": [
            { "id": "a", "text": "Selon la règle de Chargaff, la quantité d’adénine doit être égale à la cytosine.", "correct": True },
            { "id": "b", "text": "Selon la règle de Chargaff, la quantité de thymine doit être égale à la guanine.", "correct": True },
            { "id": "c", "text": "L’ADN-A a un sens lévogyre en condition non-physiologie.", "correct": True },
            { "id": "d", "text": "L’ADN-H est favorisé par les conditions acides.", "correct": False },
            { "id": "e", "text": "L’enzyme ADAR-1 se lie spécifiquement à l’ADN-A.", "correct": True }
        ],
        "explanation": "A, B, C, E sont des réponses EXACTES (car ce sont des affirmations fausses). A. FAUX (Adénine = Thymine). B. FAUX (Guanine = Cytosine). C. FAUX (L'ADN-Z est lévogyre). D. VRAI (L'ADN-H est favorisé en milieu acide). E. FAUX (ADAR-1 se lie à l'ADN-Z)."
    }
]

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', html, flags=re.DOTALL)
if match:
    questions = json.loads(match.group(1))
    
    # Filter out old q-ue11-new-
    filtered_q = [q for q in questions if not q.get('id', '').startswith('q-ue11-new-')]
    
    # Combine
    final_questions = filtered_q + exact_ue11_qcms
    
    js_code = "const INITIAL_QUESTIONS = " + json.dumps(final_questions, ensure_ascii=False, indent=4) + ";"
    js_export = "export const INITIAL_QUESTIONS = " + json.dumps(final_questions, ensure_ascii=False, indent=4) + ";"

    html = re.sub(r'const INITIAL_QUESTIONS = \[.*?\];', js_code, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Successfully updated index.html with clean valid JSON!")

    with open('src/data/mockData.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = re.sub(r'export const INITIAL_QUESTIONS = \[.*?\];', js_export, js, flags=re.DOTALL)

    with open('src/data/mockData.js', 'w', encoding='utf-8') as f:
        f.write(js)

    print("Successfully updated mockData.js with clean valid JSON!")
