import json
import re

all_td1_qcms = [
    {
        "id": "q-ue8-f1-eb-1",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Biochimie analytique", "Examen Blanc", "Pr. DER VARTANIAN"],
        "statement": "Question n°1 (Examen Blanc – Pr. Audrey DER VARTANIAN) : En médecine, la biochimie analytique c’est la science qui consiste à analyser des échantillons humains afin d’explorer les réactions biochimiques qui permettent... : (indiquez les propositions justes)",
        "answers": [
            {"id": "a", "text": "de suivre l’état de santé d’un patient", "correct": True},
            {"id": "b", "text": "de dépister ou de diagnostiquer un patient", "correct": True},
            {"id": "c", "text": "d’aider à l’ajustement thérapeutique d’un patient", "correct": True},
            {"id": "d", "text": "d’aider à l’acharnement thérapeutique d’un patient", "correct": False},
            {"id": "e", "text": "de blâmer le patient", "correct": False}
        ],
        "explanation": "A, B, C (Vraies) : La biochimie analytique sert au suivi de santé, au dépistage/diagnostic et à l'ajustement thérapeutique.\nD, E (Fausses) : Elle n'a aucun but d'acharnement ni de blâme."
    },
    {
        "id": "q-ue8-f1-eb-2",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Prélèvements", "Examen Blanc", "Pr. DER VARTANIAN"],
        "statement": "Question n°2 (Examen Blanc – Pr. Audrey DER VARTANIAN) : Le plus souvent le matériel biologique utilisé en biochimie analytique peut être constitué par... : (indiquez les propositions justes)",
        "answers": [
            {"id": "a", "text": "des prélèvements urinaires", "correct": True},
            {"id": "b", "text": "des prélèvements radiographiques", "correct": False},
            {"id": "c", "text": "des prélèvements sanguins", "correct": True},
            {"id": "d", "text": "des prélèvements vestimentaires", "correct": False},
            {"id": "e", "text": "des prélèvements tissulaires", "correct": True}
        ],
        "explanation": "A, C, E (Vraies) : Liquides biologiques (sang, urine) et tissus prélevés.\nB (Faux) : La radiographie relève de la biophysique/imagerie.\nD (Faux) : Matériel non biologique."
    },
    {
        "id": "q-ue8-f1-eb-3",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Acide borique", "Conservation", "Cytolyse"],
        "statement": "Question n°3 (Examen Blanc – Pr. Audrey DER VARTANIAN) : Concernant les tubes de prélèvement et l'acide borique, indiquez les propositions qui sont justes :",
        "answers": [
            {"id": "a", "text": "L’acide borique est souvent utilisé dans les tubes de prélèvements pour bloquer la faim bactérienne et induire la cytolyse", "correct": False},
            {"id": "b", "text": "L’acide borique est souvent utilisé dans les tubes de prélèvements pour bloquer la multiplication bactérienne et réduire la cytolyse", "correct": True},
            {"id": "c", "text": "L’acide borique permet d’améliorer le délai de transmission des échantillons humains au laboratoire", "correct": True},
            {"id": "d", "text": "L’acide borique n’est jamais utilisé en biochimie analytique", "correct": False},
            {"id": "e", "text": "L’acide borique et le borate de sodium ont les mêmes propriétés", "correct": True}
        ],
        "explanation": "B, C, E (Vraies) : L'acide borique bloque la multiplication bactérienne, préserve les cellules de la cytolyse et améliore le délai de transmission. Il dérive du borate de sodium."
    },
    {
        "id": "q-ue8-f1-eb-4",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Urines", "Turbidité", "Verdoglobinurie"],
        "statement": "Question n°4 (Examen Blanc – Pr. Audrey DER VARTANIAN) : Concernant les urines, indiquez les propositions qui sont justes :",
        "answers": [
            {"id": "a", "text": "L’aspect général des urines peut donner une première indication sur l’état de santé du patient", "correct": True},
            {"id": "b", "text": "L’urine humaine ne peut jamais se colorer en vert", "correct": False},
            {"id": "c", "text": "La turbidité de l’urine peut s’accompagner d’une forte concentration en leucocytes, en cristaux, en bactéries ou en mucus", "correct": True},
            {"id": "d", "text": "L’aspect trouble des urines est considéré comme normal", "correct": False},
            {"id": "e", "text": "L’aspect trouble des urines est considéré comme anormal", "correct": True}
        ],
        "explanation": "A, C, E (Vraies) : L'aspect trouble des urines est anormal et traduit la présence de leucocytes, cristaux ou bactéries.\nB (Faux) : Verdoglobinurie (urines vertes) observable sous certains traitements."
    },
    {
        "id": "q-ue8-f1-eb-5",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Ponction lombaire", "LBA", "Biopsies"],
        "statement": "Question n°5 (Examen Blanc – Pr. Audrey DER VARTANIAN) : Concernant les actes de prélèvement médical, indiquez les propositions qui sont justes :",
        "answers": [
            {"id": "a", "text": "Le lavage bronchoalvéolaire est indiqué pour la caractérisation de la santé des alvéoles pulmonaires d’un patient", "correct": True},
            {"id": "b", "text": "Une ponction pleurale est une ponction réalisée dans les glandes lacrymales de l’œil", "correct": False},
            {"id": "c", "text": "Une ponction de moelle osseuse peut s’avérer très douloureuse pour le patient", "correct": True},
            {"id": "d", "text": "Une ponction lombaire permet de récupérer du liquide céphalorachidien", "correct": True},
            {"id": "e", "text": "Les biopsies du système digestif ne sont jamais réalisées sous anesthésie", "correct": False}
        ],
        "explanation": "A, C, D (Vraies) : Le LBA explore le poumon, le myelogramme est douloureux, la PL prélève le LCR.\nB (Faux) : Dans la cavité pleurale (poumons).\nE (Faux) : Endoscopie et coloscopie nécessitent une anesthésie."
    },
    {
        "id": "q-ue8-f1-eb-6",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Biomarqueurs", "Diagnostic", "Sensibilité"],
        "statement": "Question n°6 (Examen Blanc – Pr. Audrey DER VARTANIAN) : Concernant les biomarqueurs, indiquez les propositions qui sont justes :",
        "answers": [
            {"id": "a", "text": "Les biomarqueurs permettent d’évaluer un processus biologique physiologique ou pathologique", "correct": True},
            {"id": "b", "text": "La principale caractéristique d’un biomarqueur est d’être curatif", "correct": False},
            {"id": "c", "text": "La principale caractéristique d’un biomarqueur est d’être invasif", "correct": False},
            {"id": "d", "text": "Les biomarqueurs peuvent être des protéines ou des fragments d’ADN", "correct": True},
            {"id": "e", "text": "La valeur d’un biomarqueur résulte de sa spécificité et de sa sensibilité", "correct": True}
        ],
        "explanation": "A, D, E (Vraies) : Un biomarqueur caractérise un état physiologique ou pathologique avec sa sensibilité et spécificité.\nB, C (Fausses) : Outil diagnostique/pronostique et non curatif."
    },
    {
        "id": "q-ue8-f1-eb-7",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Asepsie", "Prélèvements", "Laboratoire"],
        "statement": "Question n°7 (TD1) : Concernant les prélèvements et la biochimie analytique, indiquez les propositions qui sont justes :",
        "answers": [
            {"id": "a", "text": "La collecte d’échantillons biologiques se fait dans des conditions d’asepsie", "correct": True},
            {"id": "b", "text": "Dès le prélèvement d’un échantillon, j’ai tout mon temps pour la transmission au laboratoire", "correct": False},
            {"id": "c", "text": "En clinique, les analyses biochimiques peuvent s’effectuer sur des liquides biologiques et des prélèvements tissulaires", "correct": True},
            {"id": "d", "text": "La biochimie analytique permet de suivre l’état de santé d’un patient", "correct": True},
            {"id": "e", "text": "La biochimie analytique est inefficace pour le suivi thérapeutique d’un patient", "correct": False}
        ],
        "explanation": "A, C, D (Vraies) : Conditions d'asepsie indispensables, transmission rapide requise.\nB (Faux) : Les délais de conservation sont stricts.\nE (Faux) : Essentielle pour le suivi thérapeutique."
    },
    {
        "id": "q-ue8-f1-eb-8",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Sang", "Héparine", "EDTA", "Calcium"],
        "statement": "Question n°8 (TD1) : Concernant les prélèvements sanguins, indiquez les propositions justes :",
        "answers": [
            {"id": "a", "text": "L’intégralité des tests sanguins se fait sur le sang total", "correct": False},
            {"id": "b", "text": "L’ordre des tubes de prélèvement sanguin n’a aucune importance", "correct": False},
            {"id": "c", "text": "L’héparine est un anticoagulant de choix pour le prélèvement du plasma", "correct": True},
            {"id": "d", "text": "La couleur des bouchons permet de s’y retrouver dans les anticoagulants utilisés", "correct": True},
            {"id": "e", "text": "L’EDTA peut être utilisé pour doser le calcium", "correct": False}
        ],
        "explanation": "C, D (Vraies) : L'héparine est l'anticoagulant de référence pour le plasma. La couleur codifie le tube.\nA (Faux) : Tests sur sang total, plasma ou sérum.\nB (Faux) : Ordre des tubes très strict.\nE (Faux) : L'EDTA est un chélateur du calcium (séquestre le Ca2+)."
    },
    {
        "id": "q-ue8-f1-eb-9",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Potentiométrie", "Cytométrie", "CCM"],
        "statement": "Question n°9 (TD1) : Concernant les méthodes d’évaluation en biochimie, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "La potentiométrie permet le dosage ionique", "correct": True},
            {"id": "b", "text": "Le dosage immunologique est basé sur l’utilisation d’anticorps ou d’immunoglobulines", "correct": True},
            {"id": "c", "text": "Le dosage immunologique ne permet pas de visualiser les cellules cancéreuses", "correct": False},
            {"id": "d", "text": "La cytométrie en flux est une méthode de numération", "correct": True},
            {"id": "e", "text": "La chromatographie sur couche mince (CCM) est une méthode uniquement quantitative", "correct": False}
        ],
        "explanation": "A, B, D (Vraies) : Potentiométrie = ions. Immuno-dosages = anticorps. Cytométrie = numération et analyse cellulaire.\nC (Faux) : Les immuno-marquages révèlent les cellules tumorales.\nE (Faux) : La CCM est quantitative et qualitative."
    },
    {
        "id": "q-ue8-f1-eb-10",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Bandelettes urinaires", "Nitrites", "ECBU"],
        "statement": "Question n°10 (TD1) : Concernant les bandelettes urinaires, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "Les bandelettes urinaires sont basées sur l’utilisation d’indicateurs colorés", "correct": True},
            {"id": "b", "text": "Les bandelettes urinaires sont des tests lents", "correct": False},
            {"id": "c", "text": "Les bandelettes urinaires permettent de détecter la présence de bactéries dans les urines", "correct": True},
            {"id": "d", "text": "Les bandelettes urinaires permettent une analyse cytobactériologique des urines", "correct": False},
            {"id": "e", "text": "Les bandelettes urinaires mobilisent des réactions acido-basiques et d’oxydoréduction", "correct": True}
        ],
        "explanation": "A, C, E (Vraies) : Tests rapides colorimétriques. Détectent les nitrites (entérobactéries).\nB (Faux) : Tests rapides (seconds).\nD (Faux) : L'analyse cytobactériologique formelle correspond à l'ECBU."
    },
    {
        "id": "q-ue8-f1-eb-11",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["ECBU", "Cristaux", "Cylindres hyalins"],
        "statement": "Question n°11 (TD1) : Concernant l’ECBU, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "L’ECBU permet l’observation cytobactériologique des urines", "correct": True},
            {"id": "b", "text": "Le type de cellules retrouvé dans les urines permet d’identifier la zone du système urinaire impactée", "correct": True},
            {"id": "c", "text": "L’observation de cristaux dans les urines est spécifique d’une urine alcaline", "correct": False},
            {"id": "d", "text": "L’observation de cristaux est comprise dans un ECBU", "correct": True},
            {"id": "e", "text": "Les cylindres hyalins sont liés à la précipitation des protéines quand l’urine est acide", "correct": True}
        ],
        "explanation": "A, B, D, E (Vraies) : Cytologie, numération, cristallurie et bactériologie. Cylindres hyalins précipitent en milieu acide.\nC (Faux) : Cristaux observés à pH acide (acide urique, oxalate) ET alcalin (struvites)."
    },
    {
        "id": "q-ue8-f1-eb-12",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Acide fort", "Base faible", "Autoprotolyse"],
        "statement": "Question n°12 (TD1) : Concernant les réactions acido-basiques, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "Un acide fort AH est caractérisé par la réaction chimique suivante AH + H2O <-> A- + H3O+", "correct": False},
            {"id": "b", "text": "La formule du pH d’une solution d’acide fort est pH = -log[AH]", "correct": True},
            {"id": "c", "text": "La force d’un acide est déterminée par sa capacité à capter des protons H+", "correct": False},
            {"id": "d", "text": "La réaction d’une base faible en solution n’est pas totale", "correct": True},
            {"id": "e", "text": "L’autoprotolyse de l’eau est négligeable quand le pH de la solution est pH = 6.8", "correct": False}
        ],
        "explanation": "B, D (Vraies) : pH = -log[AH] pour acide fort. Base faible = équilibre incomplet.\nA (Faux) : Réaction totale AH + H2O -> A- + H3O+.\nC (Faux) : L'acide cède des protons H+.\nE (Faux) : Non négligeable si 6.5 < pH < 7.5."
    },
    {
        "id": "q-ue8-f1-eb-13",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["KA", "KB", "Base forte"],
        "statement": "Question n°13 (TD1) : Concernant les réactions acido-basiques, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "À l’équilibre, pH = -log KA", "correct": True},
            {"id": "b", "text": "Une base forte B- est caractérisée par la réaction chimique suivante B- + H2O -> BH + OH-", "correct": True},
            {"id": "c", "text": "Les constantes d’acidité et de basicité d’un couple acide/base vérifient : KA * KB = [OH-] * [H3O+]", "correct": True},
            {"id": "d", "text": "Une base est dite faible si, en solution aqueuse, s’établit un équilibre où coexistent la base et son acide conjugué", "correct": True},
            {"id": "e", "text": "Un acide fort est caractérisé par une constante d’acidité KA faible", "correct": False}
        ],
        "explanation": "A, B, C, D (Vraies) : À l'équilibre pH = pKa. Réaction totale pour base forte. KA * KB = Ke = 10^-14.\nE (Faux) : Acide fort = KA fort et pKA faible."
    },
    {
        "id": "q-ue8-f1-eb-14",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Exercice TD", "Acide fluorhydrique", "HF", "pKa"],
        "statement": "Question n°14 (Résolution d’exercice type TD) : Soit une solution d’acide fluorhydrique HF ([HF] = 7.10^-3 mol/L, pH = 3.8, [F-] = 7.10^-6 mol/L). Quelles affirmations sont vraies ?",
        "answers": [
            {"id": "a", "text": "La demi-équation s'écrit HF + H2O <-> F- + H3O+ (acide faible, réaction pas totale)", "correct": True},
            {"id": "b", "text": "La constante d'acidité KA vaut KA = 10^-6.8", "correct": True},
            {"id": "c", "text": "À l'équilibre, le pH de la solution vaut pH = pKa = 6.8", "correct": True},
            {"id": "d", "text": "Dans ces conditions d'équilibre (pH = 6.8), l'autoprotolyse de l'eau n'est pas négligeable (6.5 < pH < 7.5)", "correct": True},
            {"id": "e", "text": "L'autoprotolyse de l'eau est parfaitement négligeable pour pH = 6.8", "correct": False}
        ],
        "explanation": "A, B, C, D (Vraies) : KA = [F-][H3O+]/[HF] = (7.10^-6 * 10^-3.8)/(7.10^-3) = 10^-6.8. À l'équilibre, pH = pKa = 6.8. Autoprotolyse non négligeable entre 6.5 et 7.5."
    },
    {
        "id": "q-ue8-f1-eb-15",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Diagramme de prédominance", "Base forte", "Acide fort"],
        "statement": "Question n°15 (TD1) : Concernant les diagrammes de prédominance, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "Le diagramme de prédominance permet de visualiser l’équilibre entre les acides/bases et leurs formes conjuguées en fonction du pH", "correct": True},
            {"id": "b", "text": "Pour chaque couple acido-basique, on peut définir deux zones de prédominance et une zone où les deux espèces sont à l’équilibre", "correct": True},
            {"id": "c", "text": "Ce diagramme ne peut être utilisé que pour représenter les acides/bases forts", "correct": False},
            {"id": "d", "text": "Une base forte sera placée sur le diagramme aux valeurs de pH les plus élevées", "correct": True},
            {"id": "e", "text": "Un acide fort sera placé sur le diagramme aux valeurs de pH les plus élevées", "correct": False}
        ],
        "explanation": "A, B, D (Vraies) : Visualise les formes prédominantes selon le pH. Base forte prédomine aux pH les plus basiques.\nC (Faux) : S'applique aussi aux acides/bases faibles.\nE (Faux) : Acide fort placé aux pH les plus bas."
    },
    {
        "id": "q-ue8-f1-eb-16",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Exercice TD", "Acide ascorbique", "Vitamine C", "Estomac"],
        "statement": "Question n°16 (Résolution d’exercice type TD) : L’acide ascorbique (Vitamine C) est un diacide (pKa1 = 4.1, pKa2 = 11.8). Un comprimé dissous à pH 4.25 avec [C6H8O6] = 2.10^-2 mol/L. À pH = 1 dans l'estomac, quelles affirmations sont vraies ?",
        "answers": [
            {"id": "a", "text": "Pour pH = 4.25, l'espèce prédominante est l'ion mono-anionique C6H7O6-", "correct": True},
            {"id": "b", "text": "Dans l'estomac (pH = 1), l'espèce diacide neutre C6H8O6 est prédominante (pH < pKa1)", "correct": True},
            {"id": "c", "text": "Pour un composé Actif-H2 (pKa1 = 1) dans l'estomac (pH = 1), pH = pKa1 donc [Actif-H2] = [Actif-H-]", "correct": True},
            {"id": "d", "text": "Actif-H2 a un pKa1 plus faible que la Vitamine C, c'est donc un acide plus fort", "correct": True},
            {"id": "e", "text": "L'espèce C6H6O6(2-) est la base la plus forte car elle présente le pKa le plus élevé (pKa2 = 11.8)", "correct": True}
        ],
        "explanation": "Toutes vraies (A, B, C, D, E) : À pH 4.25 (>4.1), C6H7O6- prédomine. À pH 1 (<4.1), C6H8O6 prédomine. Quand pH = pKa = 1, les concentrations acide et base conjuguée sont égales. Acide plus fort = pKa plus faible. Base plus forte = pKa plus élevé."
    },
    {
        "id": "q-ue8-f1-eb-17",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["pH sanguin", "Acidose", "Excrétion d'acides"],
        "statement": "Question n°17 (TD1) : Concernant l’équilibre acido-basique d’un organisme, quelle(s) proposition(s) est (sont) vraie(s) :",
        "answers": [
            {"id": "a", "text": "Le pH de l’organisme est finement régulé afin d’assurer le bon fonctionnement de l’organisme", "correct": True},
            {"id": "b", "text": "Un pH sanguin d’une valeur pH = 7.4 correspond à une situation d’acidose", "correct": False},
            {"id": "c", "text": "Dans l’organisme, la concentration d’H+ est physiologiquement très élevée", "correct": False},
            {"id": "d", "text": "L’organisme est plus assujetti à développer des acidoses, mais est plus efficace pour lutter contre l’alcalose", "correct": False},
            {"id": "e", "text": "Les systèmes respiratoire et rénal assurent l’excrétion des acides de l’organisme", "correct": True}
        ],
        "explanation": "A, E (Vraies) : pH finement régulé (7.38-7.42). Poumons et reins éliminent les acides.\nB (Faux) : pH 7.4 est la valeur normale.\nC (Faux) : [H+] très faible (~40 nmol/L).\nD (Faux) : L'organisme produit beaucoup d'acides et est donc mieux équipé pour lutter contre l'acidose."
    },
    {
        "id": "q-ue8-f1-eb-18",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Sources d'acides", "Acides volatiles", "Acides fixes"],
        "statement": "Question n°18 (TD1) : Concernant l’équilibre acido-basique d’un organisme, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "L’eau via son autoprotolyse et le dioxyde de carbone sont les principales sources d’H+ de l’organisme", "correct": True},
            {"id": "b", "text": "L’alimentation et le métabolisme oxydatif sont les principales sources d’acide de l’organisme", "correct": True},
            {"id": "c", "text": "On distingue deux grands types d’acides dans l’organisme : des volatiles et des fixes", "correct": True},
            {"id": "d", "text": "Les acides fixes produits par l’organisme sont non métabolisables", "correct": False},
            {"id": "e", "text": "L’ammoniac NH3 est la seule base de l’organisme capable de diminuer la concentration d’H+", "correct": False}
        ],
        "explanation": "A, B, C (Vraies) : Métabolisme oxydatif (CO2) et alimentation fournissent les H+. Acides volatiles (CO2) vs fixes.\nD (Faux) : Certains acides fixes sont métabolisables (ex: lactate).\nE (Faux) : L'ion bicarbonate HCO3- est la base majeure."
    },
    {
        "id": "q-ue8-f1-eb-19",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Gaz du sang", "Alcalose respiratoire", "Diagnostic"],
        "statement": "Question n°19 (TD1) : Vous auscultez un patient présentant pH = 7.48, PaCO2 = 30 mmHg et [HCO3-] = 18 mmol/L (Normes : PaCO2 = 35-45, HCO3- = 22-26). Vous posez le diagnostic :",
        "answers": [
            {"id": "a", "text": "le patient présente une acidose métabolique qui est compensée par le système respiratoire", "correct": False},
            {"id": "b", "text": "le patient présente une acidose respiratoire non compensée", "correct": False},
            {"id": "c", "text": "le patient présente une alcalose respiratoire non compensée", "correct": False},
            {"id": "d", "text": "le patient présente une alcalose métabolique qui est compensée par le système respiratoire", "correct": False},
            {"id": "e", "text": "le patient présente une alcalose respiratoire qui est compensée par le système métabolique/rénal", "correct": True}
        ],
        "explanation": "E (Vrai) : pH 7.48 (>7.42) = Alcalose. PaCO2 30 mmHg (<35) = origine respiratoire. HCO3- 18 mmol/L (<22) = compensation rénale (excrétion des bicarbonates)."
    },
    {
        "id": "q-ue8-f1-eb-20",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Diagnostic acido-basique", "PaCO2", "HCO3-"],
        "statement": "Question n°20 (TD1) : Concernant la prise en charge clinique d’un patient présentant un déséquilibre acido-basique, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "La mesure du pH plasmatique d’un patient suffit à identifier l’origine d’une acidose/alcalose", "correct": False},
            {"id": "b", "text": "Une acidose métabolique implique une diminution du pH sanguin et une augmentation de [HCO3-]", "correct": False},
            {"id": "c", "text": "Les alcaloses sont forcément d’origine métabolique", "correct": False},
            {"id": "d", "text": "Les mesures du pH, du taux de CO2 et de bicarbonate sont requises pour faire un diagnostic complet d’une acidose/alcalose", "correct": True},
            {"id": "e", "text": "L’acidose respiratoire est caractérisée par un excès de CO2", "correct": True}
        ],
        "explanation": "D, E (Vraies) : Diagnostic complet via pH, PaCO2 et HCO3-. Acidose respiratoire = rétention de CO2.\nA (Faux) : Le pH seul ne suffit pas.\nB (Faux) : Acidose métabolique = baisse de HCO3-.\nC (Faux) : Alcalose peut être respiratoire."
    },
    {
        "id": "q-ue8-f1-eb-21",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Tampons", "Ventilation", "Fonction rénale"],
        "statement": "Question n°21 (TD1) : Concernant les régulations de l’équilibre acido-basique dans l’organisme, indiquez les affirmations justes :",
        "answers": [
            {"id": "a", "text": "La ventilation, la fonction rénale et les systèmes tampons sont les systèmes que l’organisme utilise pour réguler l’équilibre acido-basique", "correct": True},
            {"id": "b", "text": "Les systèmes tampons sont extracellulaires", "correct": False},
            {"id": "c", "text": "La régulation des équilibres acido-basiques va s’effectuer de manière séquentielle : d’abord les systèmes tampons, puis la fonction rénale, et en dernier lieu la ventilation", "correct": False},
            {"id": "d", "text": "Les systèmes tampons permettent une régulation rapide, mais sont néanmoins limités", "correct": True},
            {"id": "e", "text": "Le système respiratoire traite la grande majorité des perturbations acido-basiques que rencontre l’organisme", "correct": True}
        ],
        "explanation": "A, D, E (Vraies) : Tampons (rapides mais saturables), poumons (~75% des régulations), reins. Chronologie : 1. Tampons, 2. Ventilation, 3. Reins.\nB (Faux) : Tampons intra et extracellulaires.\nC (Faux) : Le rein intervient en dernier."
    },
    {
        "id": "q-ue8-f1-eb-22",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Henderson-Hasselbalch", "Bicarbonates", "Tampons ouverts"],
        "statement": "Question n°22 (TD1) : Concernant les systèmes tampons dans l’organisme, quelle(s) proposition(s) est (sont) vraie(s) :",
        "answers": [
            {"id": "a", "text": "L’équation d’Henderson-Hasselbalch est utilisée pour déterminer le pH d’une solution tamponnée", "correct": True},
            {"id": "b", "text": "Les systèmes tampons peuvent être ouverts ou fermés", "correct": True},
            {"id": "c", "text": "Le système tampon de l’ion bicarbonate (HCO3-) est un système tampon intracellulaire ouvert", "correct": False},
            {"id": "d", "text": "Les systèmes tampons intracellulaires ont, contrairement aux systèmes tampons extracellulaires, une action immédiate", "correct": True},
            {"id": "e", "text": "Un système tampon est le mélange d’un acide faible et de sa base conjuguée", "correct": True}
        ],
        "explanation": "A, B, D, E (Vraies) : Équation d'Henderson-Hasselbalch. Tampons intracellulaires immédiats.\nC (Faux) : Le système bicarbonate est le principal système tampon EXTRACELLULAIRE ouvert."
    },
    {
        "id": "q-ue8-f1-eb-23",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Exercice TD", "Bicarbonate", "Injection Actif-H2", "Calcul pH"],
        "statement": "Question n°23 (Résolution d’exercice type TD) : Tampon sanguin H2CO3/HCO3- (pH initial 7.4, Ka = 4.3x10^-7, Ctotale = 0.5x10^-2 mol/L). On injecte un acide fort Actif-H2 (4.0x10^-3 mol/L). Quelles sont les affirmations vraies ?",
        "answers": [
            {"id": "a", "text": "Dans le sang (pH 7.4), l'autoprotolyse de l'eau n'est pas négligeable (6.5 < pH < 7.5)", "correct": True},
            {"id": "b", "text": "Avant injection : [H2CO3] = 0.4x10^-3 mol/L et [HCO3-] = 4.6x10^-3 mol/L", "correct": True},
            {"id": "c", "text": "La réaction Actif-H2 + HCO3- -> Actif-H- + H2CO3 a une constante d'équilibre Ke = 2.3x10^6 (réaction totale)", "correct": True},
            {"id": "d", "text": "Après injection de 4.0x10^-3 mol/L d'Actif-H2, les concentrations finales deviennent [HCO3-] = 0.6x10^-3 mol/L et [H2CO3] = 4.4x10^-3 mol/L", "correct": True},
            {"id": "e", "text": "Après injection, le nouveau pH s'effondre à pH = 5.5, ce qui correspond à une acidose sévère", "correct": True}
        ],
        "explanation": "Toutes vraies (A, B, C, D, E) : Autoprotolyse non négligeable à pH 7.4. [H2CO3] = Ctot / (1 + Ka/10^-7.4) = 0.4 mM et [HCO3-] = 4.6 mM. Réaction totale (Ke > 1000). Tableau d'avancement : [HCO3-]final = 4.6-4.0 = 0.6 mM, [H2CO3]final = 0.4+4.0 = 4.4 mM. Nouveau pH = pKa + log(0.6/4.4) = 6.36 - 0.86 = 5.5 (Acidose)."
    },
    {
        "id": "q-ue8-f1-eb-annales",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Annales", "Biochimie analytique", "Prélèvements"],
        "statement": "Annales Partie 1 (Biochimie analytique & Échantillonnage) : Quelles affirmations sont vraies ?",
        "answers": [
            {"id": "a", "text": "La biochimie analytique permet l’identification et le dosage des molécules constitutives chez le patient (Q1.1 - B)", "correct": True},
            {"id": "b", "text": "La biochimie analytique interroge les liquides biologiques ou les prélèvements tissulaires d’un patient (Q1.1 - C)", "correct": True},
            {"id": "c", "text": "La biochimie analytique permet de dépister une pathologie en corrélation avec le tableau clinique (Q1.1 - E)", "correct": True},
            {"id": "d", "text": "Le prélèvement sanguin, la ponction lombaire et la biopsie intestinale sont des prélèvements invasifs (Q1.2 - A, B, D)", "correct": True},
            {"id": "e", "text": "La biopsie cérébrale est un examen classique et fréquent en routine médicale (Q1.2 - E)", "correct": False}
        ],
        "explanation": "A, B, C, D (Vraies) : Q1.1 (B, C, E) & Q1.2 (A, B, D).\nE (Faux) : La biopsie cérébrale est un examen rare et exceptionnel."
    },
    {
        "id": "q-ue8-f1-eb-gazdesang",
        "subjectId": "sub-8",
        "chapter": "Fiche n°1 - Biochimie analytique en médecine.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Annales", "Gaz du sang", "Acidose métabolique", "Alcalose respiratoire"],
        "statement": "Annales Partie 2 (Cas cliniques Gaz du Sang Patients n°1 et n°2) : Quelles affirmations sont vraies ?",
        "answers": [
            {"id": "a", "text": "Patient 1 (pH 7.10, PaCO2 40, HCO3- 10, SaO2 92%) : hypoxémie légère et trouble de la concentration en HCO3- (Q2.3 - A, B)", "correct": True},
            {"id": "b", "text": "Patient 1 présente une acidose métabolique non compensée avec PaCO2 normale (Q2.3 - C, E)", "correct": True},
            {"id": "c", "text": "Patient 2 (pH 7.80, PaCO2 25, HCO3- 24, SaO2 98%) : présente un trouble acido-basique (Q2.4 - B)", "correct": True},
            {"id": "d", "text": "Patient 2 présente une alcalose respiratoire non compensée avec bicarbonates normaux (Q2.4 - E)", "correct": True},
            {"id": "e", "text": "Patient 2 présente une hypoxémie sévère avec SaO2 à 98%", "correct": False}
        ],
        "explanation": "A, B, C, D (Vraies) : Q2.3 (A, B, C, E) & Q2.4 (B, E).\nE (Faux) : SaO2 = 98% est parfaitement normale."
    }
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', content, flags=re.DOTALL)
if match:
    existing_json = match.group(1)
    existing_json_clean = re.sub(r'[\r\n]+', ' ', existing_json)
    existing_data = json.loads(existing_json_clean)
    
    # Filter out existing to avoid any duplicates
    new_ids = [q['id'] for q in all_td1_qcms]
    existing_filtered = [q for q in existing_data if q['id'] not in new_ids]
    
    updated_data = existing_filtered + all_td1_qcms
    
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
        
    print(f'Successfully updated all TD1 & Examen Blanc QCMs in UE 8 Fiche n°1! Total questions in bank: {len(updated_data)}')
else:
    print('Failed to locate INITIAL_QUESTIONS array')
