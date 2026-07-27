import json
import re

new_ue8_fiche4_qcms = [
    {
        "id": "q-ue8-fiche4-1",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Dénutrition", "Malnutrition", "TD3"],
        "statement": "Question n°1 : Concernant la dénutrition, quelles propositions sont justes :",
        "answers": [
            { "id": "a", "text": "La dénutrition est une forme de malnutrition", "correct": True },
            { "id": "b", "text": "La dénutrition peut être causée par une diminution des besoins nutritionnels", "correct": False },
            { "id": "c", "text": "La dénutrition peut être causée par une malabsorption des nutriments", "correct": True },
            { "id": "d", "text": "La dénutrition se caractérise par des pertes tissulaires non délétères", "correct": False },
            { "id": "e", "text": "La dénutrition est nécessairement un phénomène involontaire", "correct": True }
        ],
        "explanation": "A, C, E VRAIS.\nB. FAUX : Cause par une augmentation (et non diminution) des besoins nutritionnels.\nD. FAUX : La perte tissulaire dans la dénutrition est délétère."
    },
    {
        "id": "q-ue8-fiche4-2",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Kwashiorkor", "Protéines", "TD3"],
        "statement": "Question n°2 : Concernant le syndrome de Kwashiorkor, quelle(s) proposition(s) est(sont) juste(s) :",
        "answers": [
            { "id": "a", "text": "Le syndrome de Kwashiorkor est une malnutrition chronique", "correct": True },
            { "id": "b", "text": "La synthèse des protéines viscérales est altérée : on dit que le syndrome de Kwashiorkor est compensé", "correct": False },
            { "id": "c", "text": "La présence d’œdème est spécifique du syndrome de Kwashiorkor", "correct": True },
            { "id": "d", "text": "Dans le syndrome de Kwashiorkor, le rapport protéine/calorie est augmenté", "correct": False },
            { "id": "e", "text": "La concentration plasmatique en albumine est une manière de différencier le marasme et le syndrome de Kwashiorkor sur le plan clinique", "correct": True }
        ],
        "explanation": "A, C, E VRAIS.\nB. FAUX : Le syndrome est dit DÉCOMPENSÉ car le foie n'arrive plus à compenser la carence en protéines (d'où dégradation viscérale et hypoalbuminémie).\nD. FAUX : Le rapport protéine/calorie est diminué."
    },
    {
        "id": "q-ue8-fiche4-3",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Kwashiorkor", "Clinique", "Ascite"],
        "statement": "Question n°3 : Un jeune patient de 4 ans atteint du syndrome de Kwashiorkor va être transféré dans votre service. Sur le plan clinique, vous vous attendez à :",
        "answers": [
            { "id": "a", "text": "observer une perturbation de sa synthèse protéique via un taux d’albumine sanguin faible : vous prévoyez une électrophorèse pour vérifier", "correct": True },
            { "id": "b", "text": "observer une accumulation de liquide dans la cavité péritonéale : vous planifiez une ponction pleurale", "correct": False },
            { "id": "c", "text": "observer une diminution du volume hépatique", "correct": False },
            { "id": "d", "text": "observer une situation d’acidose", "correct": True },
            { "id": "e", "text": "observer une perturbation de la cicatrisation du patient", "correct": True }
        ],
        "explanation": "A, D, E VRAIS.\nB. FAUX : Il faut prévoir une ponction d'ASCITE (pas pleurale).\nC. FAUX : Augmentation du volume hépatique liée à une sursollicitation du foie."
    },
    {
        "id": "q-ue8-fiche4-4",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Jeûne", "Réseres", "Chronique"],
        "statement": "Question n°4 : Plus un jeûne se prolonge, plus :",
        "answers": [
            { "id": "a", "text": "on se retrouve dans un état de dénutrition aiguë", "correct": False },
            { "id": "b", "text": "l’organisme va diminuer ses besoins nutritionnels", "correct": True },
            { "id": "c", "text": "l’organisme va utiliser en priorité ses réserves protéiques, puis ses réserves lipidiques", "correct": False },
            { "id": "d", "text": "l’état de dénutrition risque de devenir irréversible", "correct": True },
            { "id": "e", "text": "on risque de développer un tableau clinique proche de celui du syndrome de Kwashiorkor", "correct": True }
        ],
        "explanation": "B, D, E VRAIS.\nA. FAUX : On se trouve dans un état de dénutrition CHRONIQUE.\nC. FAUX : L'organisme utilise en priorité ses réserves lipidiques, puis en dernier lieu ses protéines."
    },
    {
        "id": "q-ue8-fiche4-5",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Métabolisme", "Néoglucogenèse", "Jeûne"],
        "statement": "Question n°5 : Concernant la mobilisation différentielle des voies métaboliques en période de jeûne, quelle(s) proposition(s) est(sont) juste(s) :",
        "answers": [
            { "id": "a", "text": "En parallèle de l’ATP, on génère également du glycogène et des triglycérides pendant la période post-prandiale", "correct": True },
            { "id": "b", "text": "C’est au cours de la période post-absorptive que glycogénolyse et néoglucogenèse se mettent en place", "correct": True },
            { "id": "c", "text": "En cas d’un jeûne long, la néoglucogenèse va principalement utiliser le pyruvate comme précurseur afin de générer de l’énergie pour les organes gluco-dépendant", "correct": False },
            { "id": "d", "text": "La genèse de corps cétonique devient un processus majoritaire 12h après le dernier repas", "correct": False },
            { "id": "e", "text": "La lipolyse permet de fournir des précurseurs pour la voie des pentoses phosphate", "correct": False }
        ],
        "explanation": "A, B VRAIS.\nC. FAUX : La néoglucogenèse utilise le glycérol (via lipolyse) puis les acides aminés.\nD. FAUX : C'est à partir de 3-4 jours de jeûne que la cétogenèse devient majoritaire.\nE. FAUX : La lipolyse fournit des précurseurs pour la cétogenèse et la néoglucogenèse."
    },
    {
        "id": "q-ue8-fiche4-6",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Post-absorptif", "Pertes Azotées"],
        "statement": "Question n°6 : Concernant la période post-absorptive, quelle(s) proposition(s) est(sont) fausse(s) :",
        "answers": [
            { "id": "a", "text": "Cette période commence 8h après le dernier repas, et dure environ 8h", "correct": True },
            { "id": "b", "text": "La glycogénolyse et la lipolyse sont les voies métaboliques majoritaires au cours de cette période", "correct": False },
            { "id": "c", "text": "La néoglucogenèse au cours de cette période s’effectue à partir de pyruvate et de lactate", "correct": True },
            { "id": "d", "text": "La glycogénolyse est régulée par des signaux hormonaux, tels que le glucagon", "correct": True },
            { "id": "e", "text": "On observe une diminution des pertes azotées au cours de cette période", "correct": False }
        ],
        "explanation": "A, C, D sont des propositions FAUSSES (donc les bonnes réponses demandées par la question) !\nB. VRAI : Glycogénolyse et néoglucogenèse sont majoritaires.\nE. VRAI : La diminution des pertes azotées s'observe au-delà de 3 jours de jeûne."
    },
    {
        "id": "q-ue8-fiche4-7",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Jeûne long", "Épargne Protéique"],
        "statement": "Question n°7 : Après 3-4 jours de jeûne, on observe :",
        "answers": [
            { "id": "a", "text": "une diminution de l’utilisation du glucose", "correct": True },
            { "id": "b", "text": "une épargne protéique", "correct": True },
            { "id": "c", "text": "une augmentation de la production d’urée", "correct": False },
            { "id": "d", "text": "une sécrétion d’adipokine", "correct": True },
            { "id": "e", "text": "une diminution des corps cétoniques", "correct": False }
        ],
        "explanation": "A, B, D VRAIS.\nC. FAUX : L'épargne protéique diminue la protéolyse, d'où une DIMINUTION de la production d'urée.\nE. FAUX : La production de corps cétoniques augmente."
    },
    {
        "id": "q-ue8-fiche4-8",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Jeûne terminal", "Urée"],
        "statement": "Question n°8 : Concernant la phase terminale d’un jeûne, quelle(s) proposition(s) est(sont) juste(s) :",
        "answers": [
            { "id": "a", "text": "Cela correspond à un jeûne de plus de 60 j", "correct": True },
            { "id": "b", "text": "A ce stade, la dénutrition est irréversible", "correct": True },
            { "id": "c", "text": "Les réserves lipidiques sont épuisées : la cétogenèse est donc diminuée", "correct": True },
            { "id": "d", "text": "La production d’urée est diminuée", "correct": False },
            { "id": "e", "text": "La néoglucogenèse ne peut plus fonctionner", "correct": False }
        ],
        "explanation": "A, B, C VRAIS.\nD. FAUX : La production d'urée augmente en raison du catabolisme protéique massif ultime.\nE. FAUX : La néoglucogenèse continue à utiliser les acides aminés."
    },
    {
        "id": "q-ue8-fiche4-9",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Insuline", "Glucagon", "Balance"],
        "statement": "Question n°9 : Concernant la balance insuline/glucagon, quelle(s) proposition(s) est(sont) juste(s) :",
        "answers": [
            { "id": "a", "text": "La balance insuline/glucagon augmente pendant le repas", "correct": True },
            { "id": "b", "text": "La balance insuline/glucagon diminue quand on s’éloigne du repas", "correct": True },
            { "id": "c", "text": "L’augmentation de la balance insuline/glucagon favorise la protéolyse des protéines exogènes (apportées par l’alimentation)", "correct": False },
            { "id": "d", "text": "L’augmentation de la balance insuline/glucagon favorise la glycogénolyse", "correct": False },
            { "id": "e", "text": "La diminution de la balance insuline/glucagon favorise la lipolyse", "correct": True }
        ],
        "explanation": "A, B, E VRAIS.\nC & D. FAUX : C'est la DIMINUTION de la balance insuline/glucagon qui favorise la protéolyse et la glycogénolyse."
    },
    {
        "id": "q-ue8-fiche4-10",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Hypermétabolisme", "Stress", "Cancer"],
        "statement": "Question n°10 : Concernant la dénutrition par hypermétabolisme, quelle(s) proposition(s) est(sont) juste(s) :",
        "answers": [
            { "id": "a", "text": "On parle de dénutrition par hypermétabolisme quand les besoins énergétiques sont supérieurs à la normale", "correct": True },
            { "id": "b", "text": "Certaines pathologies comme le cancer peuvent conduire à une dénutrition par hypermétabolisme", "correct": True },
            { "id": "c", "text": "Une situation d’hypermétabolisme constitue une situation de stress (agression) pour l’organisme", "correct": True },
            { "id": "d", "text": "Les priorités métaboliques sont modifiées en cas de dénutrition hypermétabolique", "correct": True },
            { "id": "e", "text": "Ce type de dénutrition n’est pas concerné par la spirale de la dénutrition", "correct": False }
        ],
        "explanation": "A, B, C, D VRAIS.\nE. FAUX : La spirale de la dénutrition concerne tous les types de dénutrition."
    },
    {
        "id": "q-ue8-fiche4-11",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Signes Cliniques", "Ostéopénie", "Immunité"],
        "statement": "Question n°11 : Lorsqu’un patient est dans une situation de dénutrition, il est possible d’observer :",
        "answers": [
            { "id": "a", "text": "une concentration d’immunoglobuline sanguine élevée", "correct": False },
            { "id": "b", "text": "une hypoxie", "correct": True },
            { "id": "c", "text": "un débit cardiaque augmenté", "correct": False },
            { "id": "d", "text": "une déminéralisation des os du patient (ostéopénie)", "correct": True },
            { "id": "e", "text": "une malabsorption des nutriments", "correct": True }
        ],
        "explanation": "B, D, E VRAIS.\nA. FAUX : Diminution des immunoglobulines.\nC. FAUX : Débit cardiaque diminué."
    },
    {
        "id": "q-ue8-fiche4-12",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Biochimie Métabolique", "Glycolyse", "Cétogenèse"],
        "statement": "12. Partie 4 : Biochimie métabolique (Question n°4.2) Afin de répondre au besoin de notre organisme, plusieurs molécules biochimiques peuvent être utilisées pour fournir de l’énergie à l’organisme et vont conditionner les priorités selon l’état nutritionnel :",
        "answers": [
            { "id": "a", "text": "La cétogenèse est une voie métabolique qui permet la dégradation des protéines, notamment lors d’un jeûne.", "correct": False },
            { "id": "b", "text": "La voie des pentoses phosphates est une voie métabolique alternative à la glycolyse qui permet de fournir divers produits utiles à la cellules et de lutter contre le stress oxydatif.", "correct": True },
            { "id": "c", "text": "La néoglucogenèse avec dégradation protéique permet de produire du glucose à partir de précurseurs non-glucidiques tels que les acides aminés en période de jeûne trop prolongé.", "correct": True },
            { "id": "d", "text": "La lipolyse est une voie métabolique qui permet la dégradation des lipides, notamment lors d’un jeûne.", "correct": True },
            { "id": "e", "text": "En période post-prandiale, juste après un repas, c’est la voie de la glycolyse qui va majoritairement apporter de l’énergie en utilisant le glucose.", "correct": True }
        ],
        "explanation": "B, C, D, E VRAIS.\nA. FAUX : La cétogenèse produit des corps cétoniques à partir des acides gras (la protéolyse dégrade les protéines)."
    },
    {
        "id": "q-ue8-fiche4-13",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Conséquences Dénutrition", "Vitamines", "Myocarde"],
        "statement": "13. Partie 4 : Biochimie métabolique (Question n°4.3) Les conséquences d’une dénutrition peuvent être multiples sur l’organisme humain, que pouvons-nous affirmer ?",
        "answers": [
            { "id": "a", "text": "L’état de dénutrition altère la réponse immunitaire globale du patient.", "correct": True },
            { "id": "b", "text": "Une dénutrition peut entrainer une carence en vitamines, qui sont des cofacteurs essentiels au bon fonctionnement enzymatique.", "correct": True },
            { "id": "c", "text": "La dénutrition peut affecter la force musculaire, augmenter sa fatigabilité et même impacter le myocarde et le débit cardiaque.", "correct": True },
            { "id": "d", "text": "La dénutrition n’a jamais aucun effet délétère sur notre système osseux.", "correct": False },
            { "id": "e", "text": "La dénutrition n’induit jamais d’interférence avec le métabolisme des médicaments.", "correct": False }
        ],
        "explanation": "A, B, C VRAIS.\nD. FAUX : Effets osseux marqués (ostéopénie).\nE. FAUX : Interférence avec le métabolisme des médicaments."
    },
    {
        "id": "q-ue8-fiche4-14",
        "subjectId": "sub-8",
        "chapter": "Fiche n°4 - Immunonutrition _ Partie 1.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Évaluation Nutritionnelle", "Albumine", "Nutrition Entérale"],
        "statement": "14. Partie 4 : Biochimie métabolique (Question n°4.4) Que pouvez-vous affirmer en ce qui concerne l ‘état nutritionnel d’un patient ?",
        "answers": [
            { "id": "a", "text": "Il est possible d’évaluer l’état nutritionnel d’un patient en dosant son albumine plasmatique.", "correct": True },
            { "id": "b", "text": "Le métabolisme de base peut être calculé par une équation qui tient compte du poids, de la taille, de l’âge et du sexe chez un individu adulte.", "correct": True },
            { "id": "c", "text": "La dépense énergétique de repos peut être calculée par une équation qui tient compte du poids, de la taille, de l’âge et du sexe chez un individu adulte.", "correct": True },
            { "id": "d", "text": "La nutrition parentérale est généralement moins lourde, moins risquée et moins coûteuse que la nutrition entérale.", "correct": False },
            { "id": "e", "text": "La nutrition entérale peut être administrée par différentes types de sondes (naso-gastriques/duodénales/jéjunales).", "correct": True }
        ],
        "explanation": "A, B, C, E VRAIS.\nD. FAUX : La nutrition entérale est moins lourde, moins risquée et moins coûteuse que la nutrition parentérale."
    }
]

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', html, flags=re.DOTALL)
if match:
    questions = json.loads(match.group(1))
    
    # Remove existing q-ue8-fiche4- if any
    filtered_q = [q for q in questions if not q.get('id', '').startswith('q-ue8-fiche4-')]
    
    final_questions = filtered_q + new_ue8_fiche4_qcms
    
    js_code = "const INITIAL_QUESTIONS = " + json.dumps(final_questions, ensure_ascii=False, indent=4) + ";"
    js_export = "export const INITIAL_QUESTIONS = " + json.dumps(final_questions, ensure_ascii=False, indent=4) + ";"

    html = re.sub(r'const INITIAL_QUESTIONS = \[.*?\];', js_code, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Successfully added 14 new UE 8 Fiche 4 questions to index.html!")

    with open('src/data/mockData.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = re.sub(r'export const INITIAL_QUESTIONS = \[.*?\];', js_export, js, flags=re.DOTALL)

    with open('src/data/mockData.js', 'w', encoding='utf-8') as f:
        f.write(js)

    print("Successfully added 14 new UE 8 Fiche 4 questions to mockData.js!")
