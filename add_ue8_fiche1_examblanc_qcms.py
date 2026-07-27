import json
import re

new_qcms = [
    {
        "id": "q-ue8-fiche1-eb-1",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Biochimie analytique", "Examen Blanc", "Pr. DER VARTANIAN"],
        "statement": "En médecine, la biochimie analytique c’est la science qui consiste à analyser des échantillons humains afin d’explorer les réactions biochimiques qui permettent... : (indiquez les propositions justes)",
        "answers": [
            {"id": "a", "text": "de suivre l’état de santé d’un patient", "correct": True},
            {"id": "b", "text": "de dépister ou de diagnostiquer un patient", "correct": True},
            {"id": "c", "text": "d’aider à l’ajustement thérapeutique d’un patient", "correct": True},
            {"id": "d", "text": "d’aider à l’acharnement thérapeutique d’un patient", "correct": False},
            {"id": "e", "text": "de blâmer le patient", "correct": False}
        ],
        "explanation": "A, B, C (Vraies) : La biochimie analytique permet le suivi de santé, le dépistage/diagnostic et l'ajustement thérapeutique.\nD et E (Fausses) : Elle ne sert ni à l'acharnement thérapeutique ni à blâmer le patient."
    },
    {
        "id": "q-ue8-fiche1-eb-2",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Prélèvements", "Biochimie analytique", "Examen Blanc"],
        "statement": "Le plus souvent le matériel biologique utilisé en biochimie analytique peut être constitué par... : (indiquez les propositions justes)",
        "answers": [
            {"id": "a", "text": "des prélèvements urinaires", "correct": True},
            {"id": "b", "text": "des prélèvements radiographiques", "correct": False},
            {"id": "c", "text": "des prélèvements sanguins", "correct": True},
            {"id": "d", "text": "des prélèvements vestimentaires", "correct": False},
            {"id": "e", "text": "des prélèvements tissulaires", "correct": True}
        ],
        "explanation": "A, C, E (Vraies) : Le matériel biologique en biochimie se compose de liquides (sang, urine) ou de tissus.\nB (Faux) : Les clichés radiographiques relèvent de la biophysique/imagerie.\nD (Faux) : Non biologique."
    },
    {
        "id": "q-ue8-fiche1-eb-3",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Acide borique", "Conservation", "Urine", "Cytolyse"],
        "statement": "Concernant l'utilisation de l'acide borique dans les tubes de prélèvement, indiquez les propositions qui sont justes :",
        "answers": [
            {"id": "a", "text": "L’acide borique est souvent utilisé dans les tubes de prélèvements pour bloquer la faim bactérienne et induire la cytolyse", "correct": False},
            {"id": "b", "text": "L’acide borique est souvent utilisé dans les tubes de prélèvements pour bloquer la multiplication bactérienne et réduire la cytolyse", "correct": True},
            {"id": "c", "text": "L’acide borique permet d’améliorer le délai de transmission des échantillons humains au laboratoire", "correct": True},
            {"id": "d", "text": "L’acide borique n’est jamais utilisé en biochimie analytique", "correct": False},
            {"id": "e", "text": "L’acide borique et le borate de sodium ont les mêmes propriétés", "correct": True}
        ],
        "explanation": "B, C, E (Vraies) : L'acide borique bloque la prolifération bactérienne et réduit la cytolyse, ce qui prolonge le délai d'analyse. Il dérive du borate de sodium.\nA et D (Fausses) : L'acide borique est un agent conservateur très utilisé en analyse urinaire."
    },
    {
        "id": "q-ue8-fiche1-eb-4",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Urines", "Turbidité", "Verdoglobinurie", "Examen physique"],
        "statement": "Concernant l'analyse et l'aspect général des urines, indiquez les propositions qui sont justes :",
        "answers": [
            {"id": "a", "text": "L’aspect général des urines peut donner une première indication sur l’état de santé du patient", "correct": True},
            {"id": "b", "text": "L’urine humaine ne peut jamais se colorer en vert", "correct": False},
            {"id": "c", "text": "La turbidité de l’urine peut s’accompagner d’une forte concentration en leucocytes, en cristaux, en bactéries ou en mucus", "correct": True},
            {"id": "d", "text": "L’aspect trouble des urines est considéré comme normal", "correct": False},
            {"id": "e", "text": "L’aspect trouble des urines est considéré comme anormal", "correct": True}
        ],
        "explanation": "A, C, E (Vraies) : L'aspect trouble des urines est pathologique et s'accompagne d'éléments en suspension (leucocytes, cristaux, bactéries).\nB (Faux) : La verdoglobinurie (coloration verte) s'observe après certains médicaments (ex: propofol, bleu de méthylène).\nD (Faux) : L'urine normale est claire."
    },
    {
        "id": "q-ue8-fiche1-eb-5",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Prélèvements", "Ponction lombaire", "Lavage bronchoalvéolaire", "Biopsie"],
        "statement": "Concernant les différents prélèvements médicaux, indiquez les propositions qui sont justes :",
        "answers": [
            {"id": "a", "text": "Le lavage bronchoalvéolaire est indiqué pour la caractérisation de la santé des alvéoles pulmonaires d’un patient", "correct": True},
            {"id": "b", "text": "Une ponction pleurale est une ponction réalisée dans les glandes lacrymales de l’œil", "correct": False},
            {"id": "c", "text": "Une ponction de moelle osseuse peut s’avérer très douloureuse pour le patient", "correct": True},
            {"id": "d", "text": "Une ponction lombaire permet de récupérer du liquide céphalorachidien", "correct": True},
            {"id": "e", "text": "Les biopsies du système digestif ne sont jamais réalisées sous anesthésie", "correct": False}
        ],
        "explanation": "A, C, D (Vraies) : Le LBA explore les alvéoles, la myelogramme est douloureux, la PL prélève le LCR.\nB (Faux) : La ponction pleurale se fait dans la cavité pleurale (poumons).\nE (Faux) : Les biopsies digestives (endoscopie, coloscopie) nécessitent une anesthésie."
    },
    {
        "id": "q-ue8-fiche1-eb-6",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Biomarqueurs", "Spécificité", "Sensibilité", "Diagnostic"],
        "statement": "Concernant les biomarqueurs en biochimie analytique, indiquez les propositions qui sont justes :",
        "answers": [
            {"id": "a", "text": "Les biomarqueurs permettent d’évaluer un processus biologique physiologique ou pathologique", "correct": True},
            {"id": "b", "text": "La principale caractéristique d’un biomarqueur est d’être curatif", "correct": False},
            {"id": "c", "text": "La principale caractéristique d’un biomarqueur est d’être invasif", "correct": False},
            {"id": "d", "text": "Les biomarqueurs peuvent être des protéines ou des fragments d’ADN", "correct": True},
            {"id": "e", "text": "La valeur d’un biomarqueur résulte de sa spécificité et de sa sensibilité", "correct": True}
        ],
        "explanation": "A, D, E (Vraies) : Un biomarqueur évalue un processus biologique (protéine, ADN...) et se caractérise par sa sensibilité et spécificité.\nB et C (Fausses) : Un biomarqueur est un outil diagnostique/pronostique et non un traitement curatif."
    },
    {
        "id": "q-ue8-fiche1-eb-7",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Asepsie", "Prélèvements", "Laboratoire"],
        "statement": "Concernant la collecte et l'analyse d'échantillons biologiques, indiquez les propositions qui sont justes :",
        "answers": [
            {"id": "a", "text": "La collecte d’échantillons biologiques se fait dans des conditions d’asepsie", "correct": True},
            {"id": "b", "text": "Dès le prélèvement d’un échantillon, j’ai tout mon temps pour la transmission au laboratoire", "correct": False},
            {"id": "c", "text": "En clinique, les analyses biochimiques peuvent s’effectuer sur des liquides biologiques et des prélèvements tissulaires", "correct": True},
            {"id": "d", "text": "La biochimie analytique permet de suivre l’état de santé d’un patient", "correct": True},
            {"id": "e", "text": "La biochimie analytique est inefficace pour le suivi thérapeutique d’un patient", "correct": False}
        ],
        "explanation": "A, C, D (Vraies) : L'asepsie est indispensable lors des prélèvements d'échantillons tissulaires ou liquides.\nB (Faux) : La transmission au laboratoire doit respecter des délais stricts d'acheminement.\nE (Faux) : Elle est essentielle pour le suivi thérapeutique."
    },
    {
        "id": "q-ue8-fiche1-eb-8",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Sang", "Héparine", "EDTA", "Calcium", "Anticoagulants"],
        "statement": "Concernant les prélèvements sanguins, indiquez les propositions justes :",
        "answers": [
            {"id": "a", "text": "L’intégralité des tests sanguins se fait sur le sang total", "correct": False},
            {"id": "b", "text": "L’ordre des tubes de prélèvement sanguin n’a aucune importance", "correct": False},
            {"id": "c", "text": "L’héparine est un anticoagulant de choix pour le prélèvement du plasma", "correct": True},
            {"id": "d", "text": "La couleur des bouchons permet de s’y retrouver dans les anticoagulants utilisés", "correct": True},
            {"id": "e", "text": "L’EDTA peut être utilisé pour doser le calcium", "correct": False}
        ],
        "explanation": "C, D (Vraies) : L'héparine est l'anticoagulant de référence pour le plasma. Les bouchons colorés codifient les additifs.\nA (Faux) : Les tests utilisent sang total, plasma ou sérum selon la prescription.\nB (Faux) : L'ordre des tubes évite la contamination croisée.\nE (Faux) : L'EDTA est un chélateur puissant du calcium, ce qui fausse totalement son dosage."
    },
    {
        "id": "q-ue8-fiche1-eb-9",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Potentiométrie", "Cytométrie", "Chromatographie", "CCM"],
        "statement": "Concernant les méthodes d’évaluation et de dosage en biochimie, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "La potentiométrie permet le dosage ionique", "correct": True},
            {"id": "b", "text": "Le dosage immunologique est basé sur l’utilisation d’anticorps ou d’immunoglobulines", "correct": True},
            {"id": "c", "text": "Le dosage immunologique ne permet pas de visualiser les cellules cancéreuses", "correct": False},
            {"id": "d", "text": "La cytométrie en flux est une méthode de numération", "correct": True},
            {"id": "e", "text": "La chromatographie sur couche mince (CCM) est une méthode uniquement quantitative", "correct": False}
        ],
        "explanation": "A, B, D (Vraies) : Potentiométrie = électrodes spécifiques (ions). Immunologie = anticorps. Cytométrie = numération et caractérisation de cellules.\nC (Faux) : Les immuno-marquages spécifiques permettent de déceler les cellules tumorales.\nE (Faux) : La CCM est à la fois qualitative et quantitative."
    },
    {
        "id": "q-ue8-fiche1-eb-10",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Bandelettes urinaires", "Nitrites", "ECBU", "Oxydoréduction"],
        "statement": "Concernant les bandelettes urinaires, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "Les bandelettes urinaires sont basées sur l’utilisation d’indicateurs colorés", "correct": True},
            {"id": "b", "text": "Les bandelettes urinaires sont des tests lents", "correct": False},
            {"id": "c", "text": "Les bandelettes urinaires permettent de détecter la présence de bactéries dans les urines", "correct": True},
            {"id": "d", "text": "Les bandelettes urinaires permettent une analyse cytobactériologique des urines", "correct": False},
            {"id": "e", "text": "Les bandelettes urinaires mobilisent des réactions acido-basiques et d’oxydoréduction", "correct": True}
        ],
        "explanation": "A, C, E (Vraies) : Les bandelettes réactives reposent sur des réactions colorimétriques rapides. La présence de nitrites traduit une entérobactérie.\nB (Faux) : Ce sont des tests d'orientation très rapides (1-2 min).\nD (Faux) : L'analyse cytobactériologique formelle correspond au test d'ECBU."
    },
    {
        "id": "q-ue8-fiche1-eb-11",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["ECBU", "Cristaux", "Cylindres hyalins", "Urines"],
        "statement": "Concernant l’ECBU, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "L’ECBU permet l’observation cytobactériologique des urines", "correct": True},
            {"id": "b", "text": "Le type de cellules retrouvé dans les urines permet d’identifier la zone du système urinaire impactée", "correct": True},
            {"id": "c", "text": "L’observation de cristaux dans les urines est spécifique d’une urine alcaline", "correct": False},
            {"id": "d", "text": "L’observation de cristaux est comprise dans un ECBU", "correct": True},
            {"id": "e", "text": "Les cylindres hyalins sont liés à la précipitation des protéines quand l’urine est acide", "correct": True}
        ],
        "explanation": "A, B, D, E (Vraies) : L'ECBU associe numération cellulaire, cristallurie et bactériologie. Les cylindres hyalins précipitent en milieu acide.\nC (Faux) : Il existe des cristaux spécifiques des milieux acides (ex: acide urique, oxalate) et alcalins (ex: struvites)."
    },
    {
        "id": "q-ue8-fiche1-eb-12",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Acide fort", "Base faible", "Autoprotolyse"],
        "statement": "Concernant les réactions acido-basiques, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "Un acide fort AH est caractérisé par la réaction chimique équilibrée suivante AH + H2O <-> A- + H3O+", "correct": False},
            {"id": "b", "text": "La formule du pH d’une solution d’acide fort est pH = -log[AH]", "correct": True},
            {"id": "c", "text": "La force d’un acide est déterminée par sa capacité à capter des protons H+", "correct": False},
            {"id": "d", "text": "La réaction d’une base faible en solution n’est pas totale", "correct": True},
            {"id": "e", "text": "L’autoprotolyse de l’eau est négligeable quand le pH de la solution est pH = 6.8", "correct": False}
        ],
        "explanation": "B, D (Vraies) : pH = -log[AH] pour un acide fort. Une base faible a une réaction incomplète.\nA (Faux) : La réaction d'un acide fort est totale (flèche unique AH + H2O -> A- + H3O+).\nC (Faux) : Un acide cède des protons H+ (la base capte).\nE (Faux) : L'autoprotolyse de l'eau n'est pas négligeable dans la zone 6.5 < pH < 7.5."
    },
    {
        "id": "q-ue8-fiche1-eb-13",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Base forte", "Constante d'acidité", "KA", "KB"],
        "statement": "Concernant les réactions acido-basiques, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "À l’équilibre, pH = -log KA", "correct": True},
            {"id": "b", "text": "Une base forte B- est caractérisée par la réaction chimique suivante B- + H2O -> BH + OH-", "correct": True},
            {"id": "c", "text": "Les constantes d’acidité et de basicité d’un couple acide/base vérifient : KA * KB = [OH-] * [H3O+]", "correct": True},
            {"id": "d", "text": "Une base est dite faible si, en solution aqueuse, s’établit un équilibre où coexistent la base et son acide conjugué", "correct": True},
            {"id": "e", "text": "Un acide fort est caractérisé par une constante d’acidité KA faible", "correct": False}
        ],
        "explanation": "A, B, C, D (Vraies) : À l'équilibre pH = pKa. Pour une base forte, la réaction est totale. KA * KB = Ke = 10^-14.\nE (Faux) : Un acide fort possède un KA élevé et un pKA faible."
    },
    {
        "id": "q-ue8-fiche1-eb-15",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Diagramme de prédominance", "pKa", "Acide fort", "Base forte"],
        "statement": "Concernant les diagrammes de prédominance acido-basiques, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "Le diagramme de prédominance permet de visualiser l’équilibre entre les acides/bases et leurs formes conjuguées en fonction du pH", "correct": True},
            {"id": "b", "text": "Pour chaque couple acido-basique, on peut définir deux zones de prédominance et une zone où les deux espèces sont à l’équilibre", "correct": True},
            {"id": "c", "text": "Ce diagramme ne peut être utilisé que pour représenter les acides/bases forts", "correct": False},
            {"id": "d", "text": "Une base forte sera placée sur le diagramme aux valeurs de pH les plus élevées", "correct": True},
            {"id": "e", "text": "Un acide fort sera placé sur le diagramme aux valeurs de pH les plus élevées", "correct": False}
        ],
        "explanation": "A, B, D (Vraies) : Le diagramme montre la prédominance en fonction du pH. Une base forte prédomine aux pH les plus basiques (élevés).\nC (Faux) : Utilisé pour les acides/bases faibles et forts.\nE (Faux) : L'acide fort prédomine aux pH les plus acides (faibles)."
    },
    {
        "id": "q-ue8-fiche1-eb-17",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["pH sanguin", "Acidose", "Alcalose", "Systèmes régulateurs"],
        "statement": "Concernant l’équilibre acido-basique d’un organisme, quelle(s) proposition(s) est (sont) vraie(s) :",
        "answers": [
            {"id": "a", "text": "Le pH de l’organisme est finement régulé afin d’assurer le bon fonctionnement de l’organisme", "correct": True},
            {"id": "b", "text": "Un pH sanguin d’une valeur pH = 7.4 correspond à une situation d’acidose", "correct": False},
            {"id": "c", "text": "Dans l’organisme, la concentration d’H+ est physiologiquement très élevée", "correct": False},
            {"id": "d", "text": "L’organisme est plus assujetti à développer des acidoses, mais est plus efficace pour lutter contre l’alcalose", "correct": False},
            {"id": "e", "text": "Les systèmes respiratoire et rénal assurent l’excrétion des acides de l’organisme", "correct": True}
        ],
        "explanation": "A, E (Vraies) : Le pH physiologique (7.38-7.42) est régulé par les poumons et les reins.\nB (Faux) : pH 7.4 est la valeur physiologique normale.\nC (Faux) : [H+] est extrêmement faible (~40 nmol/L).\nD (Faux) : L'organisme produit beaucoup d'acides et est donc mieux armé pour lutter contre les acidoses."
    },
    {
        "id": "q-ue8-fiche1-eb-18",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Sources d'acides", "Acides volatiles", "Acides fixes"],
        "statement": "Concernant l’équilibre acido-basique d’un organisme, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "L’eau via son autoprotolyse et le dioxyde de carbone sont les principales sources d’H+ de l’organisme", "correct": True},
            {"id": "b", "text": "L’alimentation et le métabolisme oxydatif sont les principales sources d’acide de l’organisme", "correct": True},
            {"id": "c", "text": "On distingue deux grands types d’acides dans l’organisme : des volatiles et des fixes", "correct": True},
            {"id": "d", "text": "Les acides fixes produits par l’organisme sont non métabolisables", "correct": False},
            {"id": "e", "text": "L’ammoniac NH3 est la seule base de l’organisme capable de diminuer la concentration d’H+", "correct": False}
        ],
        "explanation": "A, B, C (Vraies) : Le CO2 (acide volatile) et l'alimentation produisent des H+. On distingue acides volatiles (éliminés par les poumons) et fixes.\nD (Faux) : Certains acides fixes sont métabolisables (ex: acide lactique).\nE (Faux) : Le système tampon fondamental repose sur l'ion bicarbonate (HCO3-)."
    },
    {
        "id": "q-ue8-fiche1-eb-19",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Gaz du sang", "Alcalose respiratoire", "Compensation rénale"],
        "statement": "Vous auscultez un patient présentant un pH plasmatique = 7.48, PaCO2 = 30 mmHg et [HCO3-] = 18 mmol/L (Valeurs de référence : PaCO2 = 35-45 mmHg, [HCO3-] = 22-26 mmol/L). Vous posez le diagnostic :",
        "answers": [
            {"id": "a", "text": "le patient présente une acidose métabolique qui est compensée par le système respiratoire", "correct": False},
            {"id": "b", "text": "le patient présente une acidose respiratoire non compensée", "correct": False},
            {"id": "c", "text": "le patient présente une alcalose respiratoire non compensée", "correct": False},
            {"id": "d", "text": "le patient présente une alcalose métabolique qui est compensée par le système respiratoire", "correct": False},
            {"id": "e", "text": "le patient présente une alcalose respiratoire qui est compensée par le système métabolique/rénal", "correct": True}
        ],
        "explanation": "E (Vrai) : pH = 7.48 (>7.42) indique une ALCALOSE. PaCO2 = 30 mmHg (<35) montre l'origine RESPIRATOIRE du trouble. [HCO3-] = 18 mmol/L (<22) démontre la COMPENSATION métabolique/rénale (élimination des bicarbonates pour faire baisser le pH)."
    },
    {
        "id": "q-ue8-fiche1-eb-20",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Diagnostic acido-basique", "PaCO2", "HCO3-"],
        "statement": "Concernant la prise en charge clinique d’un patient présentant un déséquilibre acido-basique, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "La mesure du pH plasmatique d’un patient suffit à identifier l’origine d’une acidose/alcalose", "correct": False},
            {"id": "b", "text": "Une acidose métabolique implique une diminution du pH sanguin et une augmentation de [HCO3-]", "correct": False},
            {"id": "c", "text": "Les alcaloses sont forcément d’origine métabolique", "correct": False},
            {"id": "d", "text": "Les mesures du pH, du taux de CO2 et de bicarbonate sont requises pour faire un diagnostic complet d’une acidose/alcalose", "correct": True},
            {"id": "e", "text": "L’acidose respiratoire est caractérisée par un excès de CO2", "correct": True}
        ],
        "explanation": "D, E (Vraies) : Le triptyque pH, PaCO2 et HCO3- est indispensable au diagnostic. L'acidose respiratoire s'accompagne d'hypercapnie (CO2 élevé).\nA (Faux) : Le pH seul ne précise pas le mécanisme ni la compensation.\nB (Faux) : L'acidose métabolique fait baisser les bicarbonates.\nC (Faux) : Les alcaloses peuvent être respiratoires (hyperventilation)."
    },
    {
        "id": "q-ue8-fiche1-eb-21",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Régulation acido-basique", "Poumons", "Reins", "Systèmes tampons"],
        "statement": "Concernant les régulations de l’équilibre acido-basique dans l’organisme, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "La ventilation, la fonction rénale et les systèmes tampons sont les systèmes que l’organisme utilise pour réguler l’équilibre acido-basique", "correct": True},
            {"id": "b", "text": "Les systèmes tampons sont exclusivement extracellulaires", "correct": False},
            {"id": "c", "text": "La régulation des équilibres acido-basiques va s’effectuer de manière séquentielle : d’abord les systèmes tampons, puis la fonction rénale, et en dernier lieu la ventilation", "correct": False},
            {"id": "d", "text": "Les systèmes tampons permettent une régulation rapide, mais sont néanmoins limités", "correct": True},
            {"id": "e", "text": "Le système respiratoire traite la grande majorité des perturbations acido-basiques que rencontre l’organisme", "correct": True}
        ],
        "explanation": "A, D, E (Vraies) : Les tampons réagissent immédiatement (secondes), la ventilation prend le relais (minutes, ~75% des perturbations), le rein agit en heures/jours.\nB (Faux) : Les tampons sont intra et extracellulaires (ex: hémoglobine, métaux, érythrocytes).\nC (Faux) : L'ordre chronologique est : 1. Tampons, 2. Ventilation, 3. Rein."
    },
    {
        "id": "q-ue8-fiche1-eb-22",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Henderson-Hasselbalch", "Système tampon ouvert", "Bicarbonates"],
        "statement": "Concernant les systèmes tampons dans l’organisme, quelle(s) proposition(s) est (sont) vraie(s) :",
        "answers": [
            {"id": "a", "text": "L’équation d’Henderson-Hasselbalch est utilisée pour déterminer le pH d’une solution tamponnée", "correct": True},
            {"id": "b", "text": "Les systèmes tampons peuvent être ouverts ou fermés", "correct": True},
            {"id": "c", "text": "Le système tampon de l’ion bicarbonate (HCO3-) est un système tampon intracellulaire ouvert", "correct": False},
            {"id": "d", "text": "Les systèmes tampons intracellulaires ont, contrairement aux systèmes tampons extracellulaires, une action immédiate", "correct": True},
            {"id": "e", "text": "Un système tampon est le mélange d’un acide faible et de sa base conjuguée", "correct": True}
        ],
        "explanation": "A, B, D, E (Vraies) : pH = pKa + log([A-]/[AH]). Les tampons sont ouverts ou fermés. Les tampons intracellulaires agissent immédiatement.\nC (Faux) : Le système des bicarbonates est le principal système tampon EXTRACELLULAIRE ouvert."
    },
    {
        "id": "q-ue8-fiche1-eb-1-1",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Biochimie analytique", "Définition", "Examens"],
        "statement": "En médecine la biochimie analytique est la science qui...",
        "answers": [
            {"id": "a", "text": "Consiste à analyser l’ensemble des voies métaboliques chez un patient", "correct": False},
            {"id": "b", "text": "Permet l’identification et le dosage des molécules constitutives chez le patient", "correct": True},
            {"id": "c", "text": "Interroge les liquides biologiques ou les prélèvements tissulaires d’un patient", "correct": True},
            {"id": "d", "text": "Permet de traiter un patient", "correct": False},
            {"id": "e", "text": "Permet de dépister une pathologie en corrélation avec le tableau clinique d’un patient", "correct": True}
        ],
        "explanation": "B, C, E (Vraies) : La biochimie analytique identifie et dose les molécules sur prélèvements liquides ou tissulaires pour dépister/diagnostiquer.\nA (Faux) : Trop restrictif.\nD (Faux) : C'est un outil d'exploration et non un traitement direct."
    },
    {
        "id": "q-ue8-fiche1-eb-1-2",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Échantillonnage", "Prélèvements invasifs", "Biopsie"],
        "statement": "Concernant les échantillonnages biologiques, indiquez les propositions justes :",
        "answers": [
            {"id": "a", "text": "Le prélèvement sanguin est considéré comme un prélèvement invasif", "correct": True},
            {"id": "b", "text": "La ponction lombaire est considérée comme un prélèvement invasif", "correct": True},
            {"id": "c", "text": "Le matériel de recueil utilisé en biochimie analytique est standard quel que soit le contexte du patient", "correct": False},
            {"id": "d", "text": "La biopsie d’un polype intestinal est considérée comme un prélèvement invasif", "correct": True},
            {"id": "e", "text": "La biopsie cérébrale est un examen classique et fréquent", "correct": False}
        ],
        "explanation": "A, B, D (Vraies) : Prélèvements sanguins, PL et biopsies sont qualifiés d'invasifs.\nC (Faux) : Le matériel s'adapte au contexte (pédiatrie, gériatrie, réanimation).\nE (Faux) : La biopsie cérébrale est un acte rare et exceptionnel."
    },
    {
        "id": "q-ue8-fiche1-eb-2-1",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Acides et bases", "Amphotère", "pKa"],
        "statement": "Concernant les acides et les bases, est-il vrai que :",
        "answers": [
            {"id": "a", "text": "Le terme « pH » signifie « power of hematocrit »", "correct": False},
            {"id": "b", "text": "Une espèce amphotère est un composé chimique qui peut se comporter comme une base ou comme un acide selon le contexte", "correct": True},
            {"id": "c", "text": "Une base est une espèce chimique capable de libérer un proton (H+)", "correct": False},
            {"id": "d", "text": "Dans un couple acido-basique en solution lorsque le pH est égal au pKa les concentrations en acide et en base sont égales", "correct": True},
            {"id": "e", "text": "Le pKa permet de déterminer la force d’un acide", "correct": True}
        ],
        "explanation": "B, D, E (Vraies) : Espèce amphotère = amphotère (ex: H2O, HCO3-). Quand pH = pKa, [AH] = [A-]. Le pKa mesure la force de dissociation.\nA (Faux) : pH = Potentiel Hydrogène.\nC (Faux) : Une base capte un proton H+ (l'acide libère H+)."
    },
    {
        "id": "q-ue8-fiche1-eb-2-2",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Équilibre acido-basique", "Ventilation", "Réabsorption HCO3-"],
        "statement": "Chez l’humain, que peut-on dire de l’équilibre acido-basique ?",
        "answers": [
            {"id": "a", "text": "L’être humain sain a plutôt tendance à tendre vers une alcalinité de son pH sanguin", "correct": False},
            {"id": "b", "text": "Le pH sanguin et les paramètres ventilatoires n’ont jamais aucun lien de causalité", "correct": False},
            {"id": "c", "text": "Les systèmes tampons extracellulaires peuvent constituer une réponse rapide contre l’acidose", "correct": True},
            {"id": "d", "text": "La ventilation permet d’éliminer le CO2 afin de limiter la formation de l’acide carbonique H2CO3", "correct": True},
            {"id": "e", "text": "Le système rénal est important dans le maintien de l’équilibre acido-basique car il réabsorbe les ions HCO3- dans l’urine et excrète les molécules NH4+", "correct": True}
        ],
        "explanation": "C, D, E (Vraies) : Les tampons extracellulaires agissent immédiatement. La ventilation élimine le CO2. Les reins réabsorbent HCO3- et excrètent les acides (NH4+).\nA (Faux) : L'organisme produit constamment des acides (tendance à l'acidité).\nB (Faux) : L'hyperventilation/hypoventilation module directement le pH."
    },
    {
        "id": "q-ue8-fiche1-eb-2-3",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Gaz du sang", "Acidose métabolique", "Hypoxémie"],
        "statement": "Gaz du sang patient adulte n°1 : pH = 7.10, PaCO2 = 40 mmHg, [HCO3-] = 10 mmol/L, PaO2 = 60 mmHg, SaO2 = 92% (Normes : pH 7.38-7.42, PaCO2 38-42, HCO3- 22-26, PaO2 80-100, SaO2 <94% = hypoxémie). Que peut-on dire ?",
        "answers": [
            {"id": "a", "text": "Le patient n°1 présente une hypoxémie légère et un trouble acido-basique", "correct": True},
            {"id": "b", "text": "Le patient n°1 présente un trouble de la concentration en HCO3-", "correct": True},
            {"id": "c", "text": "Le patient n°1 présente une acidose métabolique non compensée", "correct": True},
            {"id": "d", "text": "Le patient n°1 présente une acidose respiratoire non compensée", "correct": False},
            {"id": "e", "text": "Le patient n°1 ne présente pas de trouble de la PaCO2", "correct": True}
        ],
        "explanation": "A, B, C, E (Vraies) : SaO2 92% = hypoxémie légère. pH 7.10 = Acidose. [HCO3-] = 10 mmol/L (effondré) = d'origine MÉTABOLIQUE. PaCO2 = 40 mmHg (dans les normes 38-42), montrant qu'il n'y a pas encore eu de compensation respiratoire.\nD (Faux) : La PaCO2 est normale donc ce n'est pas une acidose respiratoire."
    },
    {
        "id": "q-ue8-fiche1-eb-2-4",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Gaz du sang", "Alcalose respiratoire", "Patient n°2"],
        "statement": "Gaz du sang patient adulte n°2 : pH = 7.80, PaCO2 = 25 mmHg, [HCO3-] = 24 mmol/L, PaO2 = 90 mmHg, SaO2 = 98% (Normes : pH 7.38-7.42, PaCO2 38-42, HCO3- 22-26, PaO2 80-100). Que peut-on dire ?",
        "answers": [
            {"id": "a", "text": "Le patient n° 2 présente une hypoxémie", "correct": False},
            {"id": "b", "text": "Le patient n° 2 présente un trouble acido-basique", "correct": True},
            {"id": "c", "text": "Le patient n° 2 présente une acidose métabolique non compensée", "correct": False},
            {"id": "d", "text": "Le patient n° 2 présente une alcalose métabolique non compensée", "correct": False},
            {"id": "e", "text": "Le patient n° 2 présente une alcalose respiratoire non compensée", "correct": True}
        ],
        "explanation": "B, E (Vraies) : pH 7.80 (>7.42) = ALCALOSE. PaCO2 = 25 mmHg (<38) = origine RESPIRATOIRE. [HCO3-] = 24 mmol/L (normal), montrant l'absence de compensation métabolique/rénale.\nA (Faux) : SaO2 98% est normale."
    }
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', content, flags=re.DOTALL)
if match:
    existing_json = match.group(1)
    existing_json_clean = re.sub(r'[\r\n]+', ' ', existing_json)
    existing_data = json.loads(existing_json_clean)
    
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
        
    print(f'Successfully added new Examen Blanc & TD QCMs to UE 8 Fiche n°1! Total questions in bank: {len(updated_data)}')
else:
    print('Failed to locate INITIAL_QUESTIONS array')
