import json
import re

new_qcms = [
    {
        "id": "q-ue8-fiche5-12",
        "subjectId": "sub-8",
        "chapter": "Fiche n°5 - Immunonutrition _ Partie 2.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Dénutrition", "Acidose", "Bicarbonates", "pCO2"],
        "statement": "Un patient hospitalisé présente un IMC à 17, un pH plasmatique de 7.25, une pCO2 = 55 mmHg et une concentration de [Bicarbonates] = 24 mmol/L. On rappelle que les valeurs de référence sont : pCO2 = 35-45 mmHg et [Bicarbonates] = 22-26 mmol/L. Que pouvez-vous conclure sur ce patient ?",
        "answers": [
            {"id": "a", "text": "Ce patient est en état de dénutrition", "correct": True},
            {"id": "b", "text": "Ce patient a un état nutritionnel normal", "correct": False},
            {"id": "c", "text": "Ce patient présente une acidose respiratoire compensée", "correct": False},
            {"id": "d", "text": "Ce patient présente une acidose respiratoire non compensée", "correct": True},
            {"id": "e", "text": "Ce patient présente une alcalose respiratoire non compensée", "correct": False}
        ],
        "explanation": "A (Vrai) : L’IMC de ce patient est de 17, soit inférieur au seuil de 19.\nB (Faux) : cf. A.\nC (Faux) & D (Vrai) : Le patient présente une acidose respiratoire (pCO2 élevée à 55 mmHg vs norme 35-45) avec des bicarbonates normaux (24 mmol/L). Il n'y a donc pas de phénomène de compensation rénale.\nE (Faux) : Il s'agit bien d'une acidose et non d'une alcalose."
    },
    {
        "id": "q-ue8-fiche5-13",
        "subjectId": "sub-8",
        "chapter": "Fiche n°5 - Immunonutrition _ Partie 2.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Métalloenzymes", "MMP-1", "Zinc", "Cinétique"],
        "statement": "La métalloprotéase MMP-1 est une enzyme impliquée dans le processus de cicatrisation. Pour son bon fonctionnement, elle utilise l’ion zinc Zn2+. Cette enzyme est caractérisée par un KM = 0.56 mmol/L. Parmi ces propositions, lesquelles sont justes ?",
        "answers": [
            {"id": "a", "text": "Un état de dénutrition entraîne une augmentation du KM de la MMP-1", "correct": False},
            {"id": "b", "text": "Un état de dénutrition entraîne une diminution du KM de la MMP-1", "correct": False},
            {"id": "c", "text": "L’activité de la MMP-1 peut être compromise en cas de dénutrition", "correct": True},
            {"id": "d", "text": "L’ion Zn2+ est le cofacteur inorganique de l’enzyme MMP-1", "correct": True},
            {"id": "e", "text": "L’ion Zn2+ est faiblement lié à l’enzyme MMP-1", "correct": False}
        ],
        "explanation": "A & B (Fausse) : La dénutrition n’entraîne pas de modification intrinsèque de l’affinité des enzymes (KM) pour leurs substrats.\nC (Vrai) : La carence en minéraux (zinc) dans la dénutrition empêche le bon fonctionnement des métalloenzymes.\nD (Vrai) : Le zinc Zn2+ est un cofacteur inorganique essentiel.\nE (Faux) : Pour les métalloenzymes, le cofacteur métallique est fortement lié à la structure de l’enzyme."
    },
    {
        "id": "q-ue8-fiche5-14",
        "subjectId": "sub-8",
        "chapter": "Fiche n°5 - Immunonutrition _ Partie 2.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Évaluation nutritionnelle", "CMB", "Impédancemétrie", "NRI"],
        "statement": "Concernant les méthodes d’évaluation nutritionnelle, quelle(s) proposition(s) est (sont) juste(s) :",
        "answers": [
            {"id": "a", "text": "La circonférence musculaire brachiale (ou CMB) est un indicateur de l’état de nutrition protéique", "correct": True},
            {"id": "b", "text": "L’impédancemétrie permet de déterminer l’index de risque nutritionnel", "correct": False},
            {"id": "c", "text": "L’interrogatoire du patient fait partie intégrante de l’évaluation nutritionnelle", "correct": True},
            {"id": "d", "text": "Les différents compartiments tissulaires répondent de façon identique à des ondes haute fréquence", "correct": False},
            {"id": "e", "text": "L’index de risque nutritionnel (ou NRI) se base uniquement sur le taux d’albumine, le poids actuel du patient et son poids usuel", "correct": True}
        ],
        "explanation": "A (Vrai) : La CMB reflète la masse musculaire et la réserve protéique.\nB (Faux) : L’impédancemétrie permet d’évaluer les différents volumes et compartiments tissulaires (masse grasse / masse maigre).\nC (Vrai) : L’interrogatoire clinique est fondamental.\nD (Faux) : Les différents tissus offrent des résistances électriques distinctes aux ondes haute fréquence.\nE (Vrai) : Le score NRI calcule le risque à partir de l'albumine sérique et du rapport poids actuel/usuel."
    },
    {
        "id": "q-ue8-fiche5-15",
        "subjectId": "sub-8",
        "chapter": "Fiche n°5 - Immunonutrition _ Partie 2.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Métabolisme de base", "DER", "Dénutrition", "Composition corporelle"],
        "statement": "Concernant le métabolisme de base d’un organisme, quelle(s) proposition(s) est (sont) juste(s) :",
        "answers": [
            {"id": "a", "text": "Il faut déterminer le métabolisme de base d’un patient, ou DER, pour pouvoir le prendre en charge de manière optimale", "correct": True},
            {"id": "b", "text": "Le métabolisme de base d’un patient hospitalisé est déterminé uniquement en cas de dénutrition", "correct": False},
            {"id": "c", "text": "La composition corporelle d’un individu n’a aucune influence sur ses chances de survie en cas de dénutrition", "correct": False},
            {"id": "d", "text": "Les réserves énergétiques d’un organisme sont hétérogènes, mais utilisées de manière homogène", "correct": False},
            {"id": "e", "text": "Le métabolisme de base est uniquement dépendant de la taille et du poids du patient", "correct": False}
        ],
        "explanation": "A (Vrai) : La DER (dépense énergétique au repos) est essentielle pour adapter les apports.\nB (Faux) : En hospitalisation, la DER est systématiquement évaluée lors de la prise en charge globale.\nC (Faux) : La masse maigre/grasse initiale conditionne directement la résistance au jeûne.\nD (Faux) : Les réserves sont hétérogènes et mobilisées de manière séquentielle et hétérogène.\nE (Faux) : Le métabolisme de base dépend aussi du sexe et de l'âge."
    },
    {
        "id": "q-ue8-fiche5-16",
        "subjectId": "sub-8",
        "chapter": "Fiche n°5 - Immunonutrition _ Partie 2.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Cas clinique", "Jeûne", "Cétogenèse", "Adipokines"],
        "statement": "Vous êtes de garde aux urgences. On vous amène un patient très amaigri. Vous réalisez plusieurs examens afin de déterminer son état nutritionnel. Parmi ces propositions, lesquelles sont justes ?",
        "answers": [
            {"id": "a", "text": "La concentration en corps cétoniques du patient est élevée : son dernier repas remonte au moins à 16 h", "correct": True},
            {"id": "b", "text": "Le dosage de l’insuline et du glucagon révèle une balance insuline/glucagon faible, signe que le patient est dans un état nourri", "correct": False},
            {"id": "c", "text": "Vous constatez une diminution des pertes azotées chez le patient : son dernier repas était il y a moins de 3 jours", "correct": False},
            {"id": "d", "text": "La mesure du CMB du patient est en dessous de la moyenne, signe que son état nutritionnel protéique est impacté", "correct": True},
            {"id": "e", "text": "Le patient présente une concentration importante d’adipokines : son dernier repas remonte à 12 h", "correct": False}
        ],
        "explanation": "A (Vrai) : La cétogenèse prend le relais à la fin de la période post-absorptive (>16h).\nB (Faux) : Une balance insuline/glucagon faible reflète au contraire un état de jeûne.\nC (Faux) : L'épargne azotée (diminution de l'urée urinaire) n'apparaît qu'après 3 jours de jeûne prolongé.\nD (Vrai) : La diminution de la CMB marque l'atteinte protéique.\nE (Faux) : La sécrétion d'adipokines n'intervient que lors de la lipolyse prolongée (3-4 jours)."
    },
    {
        "id": "q-ue8-fiche5-17",
        "subjectId": "sub-8",
        "chapter": "Fiche n°5 - Immunonutrition _ Partie 2.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Inflammation", "Agression", "Dénutrition", "Immunothérapie"],
        "statement": "Concernant l’agression inflammatoire en cas de dénutrition, quelle(s) proposition(s) est (sont) juste(s) :",
        "answers": [
            {"id": "a", "text": "L’agression inflammatoire est nécessairement causée par l’état de dénutrition", "correct": False},
            {"id": "b", "text": "La présence ou l’absence d’une agression inflammatoire conditionne la prise en charge d’un patient dénutri", "correct": True},
            {"id": "c", "text": "L’agression inflammatoire peut être liée à la sécrétion d’adipokines, que l’on peut commencer à observer dès la période post-absorptive", "correct": False},
            {"id": "d", "text": "L’agression inflammatoire augmente les besoins nutritionnels de l’organisme, ce qui aggrave l’état de dénutrition", "correct": True},
            {"id": "e", "text": "L’utilisation d’un traitement d’immunothérapie est préconisée en cas d’agression inflammatoire", "correct": True}
        ],
        "explanation": "A (Faux) : L'agression inflammatoire peut dériver d'une infection ou d'un cancer indépendant.\nB (Vrai) : Elle détermine si la dénutrition est hypermétabolique ou non.\nC (Faux) : La sécrétion d'adipokines nécessite un jeûne prolongé (>3-4j).\nD (Vrai) : L'inflammation majore la dépense énergétique au repos.\nE (Vrai) : L'immunonutrition / immunothérapie aide à réguler la réponse inflammatoire."
    },
    {
        "id": "q-ue8-fiche5-18",
        "subjectId": "sub-8",
        "chapter": "Fiche n°5 - Immunonutrition _ Partie 2.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Complémentation", "Sonde entérale", "Sonde parentérale"],
        "statement": "Concernant la complémentation alimentaire et les différents modes d’administration, quelle(s) proposition(s) est (sont) juste(s) :",
        "answers": [
            {"id": "a", "text": "La complémentation alimentaire dépend de la dépense énergétique au repos (DER) du patient", "correct": True},
            {"id": "b", "text": "Un patient présentant des troubles de déglutition nécessite la mise en place d’une sonde entérale", "correct": True},
            {"id": "c", "text": "La sonde entérale est le mode d’administration assurant la complémentation la plus rapide", "correct": False},
            {"id": "d", "text": "Il est impossible d’utiliser plusieurs méthodes d’administration en parallèle", "correct": False},
            {"id": "e", "text": "Il est possible d’ajouter des composés immunomodulateurs à la complémentation alimentaire si le patient présente un état d’agression inflammatoire", "correct": True}
        ],
        "explanation": "A (Vrai) : Le calcul des besoins repose sur la DER.\nB (Vrai) : Indication classique des sondes entérales (voie digestive conservée).\nC (Faux) : La voie parentérale (intraveineuse directe) est la plus rapide.\nD (Faux) : On peut associer voie entérale et parentérale.\nE (Vrai) : Les immunomodulateurs (glutamine, arginine) sont indiqués en cas d'agression."
    },
    {
        "id": "q-ue8-fiche5-19",
        "subjectId": "sub-8",
        "chapter": "Fiche n°5 - Immunonutrition _ Partie 2.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Marqueurs cellulaires", "ROS", "Lymphocytes", "Inflammation"],
        "statement": "Parmi ces processus cellulaires, le(s)quel(s) peu(ven)t être mesuré(s) pour caractériser une agression inflammatoire ?",
        "answers": [
            {"id": "a", "text": "Sécrétion de cytokines anti-inflammatoires", "correct": False},
            {"id": "b", "text": "Production d’espèces réactives de l’oxygène", "correct": True},
            {"id": "c", "text": "Libération d’hormone de croissance", "correct": False},
            {"id": "d", "text": "Expression de marqueurs lymphocytaires", "correct": True},
            {"id": "e", "text": "Expression de facteurs de différenciation hépatique", "correct": False}
        ],
        "explanation": "A (Faux) : On mesure les cytokines pro-inflammatoires (IL-1, IL-6, TNF-alpha).\nB (Vrai) : Le stress oxydant et les ROS sont des marqueurs de l'agression.\nC (Faux) : Ce sont les hormones du stress (cortisol, catécholamines) qui augmentent.\nD (Vrai) : L'expression des marqueurs de surface lymphocytaires par cytométrie.\nE (Faux) : Non spécifique."
    },
    {
        "id": "q-ue8-fiche5-20",
        "subjectId": "sub-8",
        "chapter": "Fiche n°5 - Immunonutrition _ Partie 2.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Glutamine", "Immunomodulation", "Monoxyde d'azote", "Intestin"],
        "statement": "Concernant l’utilisation de la glutamine comme molécule ayant des propriétés immunomodulatrices, quelle(s) affirmation(s) est (sont) juste(s) ?",
        "answers": [
            {"id": "a", "text": "La glutamine favorise la production de cytokines anti-inflammatoires", "correct": True},
            {"id": "b", "text": "La glutamine peut servir de précurseur à la néoglucogenèse", "correct": True},
            {"id": "c", "text": "La glutamine inhibe la synthèse du NO", "correct": False},
            {"id": "d", "text": "La glutamine exerce des effets bénéfiques sur l’absorption intestinale", "correct": True},
            {"id": "e", "text": "La glutamine augmente les pertes azotées", "correct": False}
        ],
        "explanation": "A (Vrai) : Stimule la réponse anti-inflammatoire.\nB (Vrai) : C'est un acide aminé glucoformateur majeur.\nC (Faux) : Elle favorise la synthèse de NO (vasodilatation et action immunitaire).\nD (Vrai) : Substrat énergétique des entérocytes, favorise la croissance des villosités et l'immunité mucosale.\nE (Faux) : Elle réduit le catabolisme musculaire et diminue les pertes azotées."
    },
    {
        "id": "q-ue8-fiche5-21",
        "subjectId": "sub-8",
        "chapter": "Fiche n°5 - Immunonutrition _ Partie 2.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Cas clinique", "Hypermétabolisme", "Arginine", "Cytométrie"],
        "statement": "Un patient avec un IMC de 14.5 est admis pour un cancer colorectal. Il a une sonde entérale (apports = 1.5 x DER). Son état s’aggrave : perte de poids continue et hausse des marqueurs pro-inflammatoires. Concernant ce cas clinique, quelle(s) affirmation(s) est (sont) juste(s) ?",
        "answers": [
            {"id": "a", "text": "C’est une dénutrition par hypermétabolisme", "correct": True},
            {"id": "b", "text": "Il est possible de poser une sonde parentérale au patient, mais cela nécessite dans un premier temps de retirer la sonde entérale", "correct": False},
            {"id": "c", "text": "Afin d’adapter la complémentation nutritive, je demande au laboratoire de revérifier l’expression des marqueurs inflammatoires lymphocytaires par électrophorèse", "correct": False},
            {"id": "d", "text": "Le patient reçoit déjà la dose maximale d’apport protéique, soit 2 grammes par jour. Malgré le risque d’insuffisance rénale, je double temporairement cette dose afin d’observer une amélioration de son état nutritionnel", "correct": False},
            {"id": "e", "text": "Il est possible d’utiliser de l’arginine afin de moduler l’agression inflammatoire du patient", "correct": True}
        ],
        "explanation": "A (Vrai) : L'inflammation cancéreuse majore les besoins (hypermétabolisme).\nB (Faux) : On peut associer une sonde parentérale sans retirer la sonde entérale.\nC (Faux) : L'expression des marqueurs lymphocytaires s'évalue par cytométrie en flux (FACS).\nD (Faux) : Le seuil maximal d'apport est de 2 g/kg/jour. Au-delà, aucun bénéfice n'est observé.\nE (Vrai) : L'arginine est un acide aminé immunomodulateur recommandé."
    }
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', content, flags=re.DOTALL)
if match:
    existing_json = match.group(1)
    existing_json_clean = re.sub(r'[\r\n]+', ' ', existing_json)
    existing_data = json.loads(existing_json_clean)
    
    # Filter out any existing q-ue8-fiche5-12 to 21 to prevent duplicate addition
    new_ids = [q['id'] for q in new_qcms]
    existing_filtered = [q for q in existing_data if q['id'] not in new_ids]
    
    updated_data = existing_filtered + new_qcms
    
    formatted = json.dumps(updated_data, ensure_ascii=False, indent=4)
    
    js_code = 'const INITIAL_QUESTIONS = ' + formatted + ';'
    js_export = 'export const INITIAL_QUESTIONS = ' + formatted + ';'
    
    content = re.sub(r'const INITIAL_QUESTIONS = \[.*?\];', js_code, content, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as out:
        out.write(content)
        
    with open('src/data/mockData.js', 'r', encoding='utf-8') as f_mock:
        mock_content = f_mock.read()
    mock_content = re.sub(r'export const INITIAL_QUESTIONS = \[.*?\];', js_export, mock_content, flags=re.DOTALL)
    with open('src/data/mockData.js', 'w', encoding='utf-8') as out_mock:
        out_mock.write(mock_content)
        
    print(f'Successfully added 10 new QCMs (Q12 to Q21) to UE 8 Fiche n°5! Total questions in bank: {len(updated_data)}')
else:
    print('Failed to locate INITIAL_QUESTIONS array')
