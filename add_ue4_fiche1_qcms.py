import json
import re

ue4_fiche1_qcms = [
    {
        "id": "q-ue4-f1-1",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Ultrasons", "Propriétés", "Compression"],
        "statement": "QCM 1 : Concernant les ondes ultrasonores, laquelle (ou lesquelles) des propositions suivantes est (sont) exacte(s) ?",
        "answers": [
            {"id": "a", "text": "Elles se propagent mieux dans le vide que dans un milieu liquidien", "correct": False},
            {"id": "b", "text": "Il s’agit d’ondes de compression mécanique", "correct": True},
            {"id": "c", "text": "Elles entraînent un échauffement des milieux traversés", "correct": True},
            {"id": "d", "text": "Elles ont une fréquence comprise entre 0.02 et 20 KHz", "correct": False},
            {"id": "e", "text": "Elles sont émises à une fréquence audible", "correct": False}
        ],
        "explanation": "B, C (Vraies) : Les ultrasons sont des ondes mécaniques longitudinales de compression-décompression qui déposent de l'énergie thermique (échauffement).\nA (Faux) : Les ondes mécaniques nécessitent un milieu matériel et ne se propagent PAS dans le vide.\nD, E (Fausses) : Fréquence des ultrasons > 20 kHz (inaudibles pour l'oreille humaine)."
    },
    {
        "id": "q-ue4-f1-2",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Atténuation", "Absorption", "Diffusion", "Réflexion"],
        "statement": "QCM 2 : Quelles sont les causes de l’atténuation des ultrasons lorsqu’ils traversent les tissus biologiques ?",
        "answers": [
            {"id": "a", "text": "La diffraction", "correct": False},
            {"id": "b", "text": "La réflexion", "correct": True},
            {"id": "c", "text": "La diffusion", "correct": True},
            {"id": "d", "text": "L’absorption", "correct": True},
            {"id": "e", "text": "L’impédance acoustique", "correct": False}
        ],
        "explanation": "B, C, D (Vraies) : L'atténuation globale du faisceau ultrasonore résulte de la combinaison de l'absorption thermique, de la réflexion aux interfaces et de la diffusion par les petites structures."
    },
    {
        "id": "q-ue4-f1-3",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Doppler", "Flux sanguin", "Ondes ultrasonores"],
        "statement": "QCM 3 : Quel type d’onde ultrasonore est utilisé pour mesurer les vitesses de flux sanguin par effet Doppler ?",
        "answers": [
            {"id": "a", "text": "Onde stationnaire", "correct": False},
            {"id": "b", "text": "Onde longitudinale continue", "correct": True},
            {"id": "c", "text": "Onde transversale", "correct": False},
            {"id": "d", "text": "Onde impulsionnelle", "correct": True},
            {"id": "e", "text": "Onde circulaire", "correct": False}
        ],
        "explanation": "B, D (Vraies) : L'exploration Doppler vasculaire utilise des ondes longitudinales émanant soit en mode continu (Doppler continu), soit en séquences d'impulsions (Doppler pulsé)."
    },
    {
        "id": "q-ue4-f1-4",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Impédance acoustique", "Tissu osseux", "Milieux"],
        "statement": "QCM 4 : Parmi les matériaux suivants, lequel présente la plus grande impédance acoustique pour les ultrasons ?",
        "answers": [
            {"id": "a", "text": "L’air", "correct": False},
            {"id": "b", "text": "L’eau", "correct": False},
            {"id": "c", "text": "Le tissu osseux", "correct": True},
            {"id": "d", "text": "Le gel d’échographie", "correct": False},
            {"id": "e", "text": "Le tissu musculaire", "correct": False}
        ],
        "explanation": "C (Vrai) : L'impédance acoustique Z = rho * c. L'os possède une masse volumique et une célérité très élevées (Z_os ≈ 6x10^6 kg.m-2.s-1 vs eau/tissus mous ≈ 1.5x10^6 kg.m-2.s-1)."
    },
    {
        "id": "q-ue4-f1-5",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Fréquence", "Résolution", "Pénétration"],
        "statement": "QCM 5 : Lors d’une échographie, si la fréquence des ultrasons augmente, que se passe-t-il généralement ?",
        "answers": [
            {"id": "a", "text": "La résolution spatiale diminue", "correct": False},
            {"id": "b", "text": "L’atténuation des ultrasons augmente", "correct": True},
            {"id": "c", "text": "La profondeur de pénétration des ultrasons augmente", "correct": False},
            {"id": "d", "text": "La vitesse des ultrasons change", "correct": False},
            {"id": "e", "text": "L’échogénicité des tissus diminue", "correct": False}
        ],
        "explanation": "B (Vrai) : L'atténuation augmente directement avec la fréquence. En conséquence, la résolution spatiale augmente mais la profondeur de pénétration diminue."
    },
    {
        "id": "q-ue4-f1-6",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Impédance acoustique", "Calcul", "Célérité"],
        "statement": "QCM 6 : Si la vitesse du son dans un milieu est de 1500 m/s et sa densité est de 1000 kg/m3, quelle est son impédance acoustique ?",
        "answers": [
            {"id": "a", "text": "0.15 kg/m².s", "correct": False},
            {"id": "b", "text": "1.5 × 10³ kg/m².s", "correct": False},
            {"id": "c", "text": "1.5 × 10⁶ kg/m².s", "correct": True},
            {"id": "d", "text": "1.5 × 10⁹ kg/m².s", "correct": False},
            {"id": "e", "text": "1.5 × 10¹² kg/m².s", "correct": False}
        ],
        "explanation": "C (Vrai) : Z = rho * c = 1000 kg/m³ * 1500 m/s = 1 500 000 = 1.5 × 10⁶ kg.m⁻².s⁻¹."
    },
    {
        "id": "q-ue4-f1-7",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Échographie rénale", "Réflexion", "Calcul R"],
        "statement": "QCM 7 : Examen échographique du rein (Z_graisse = 1.35x10⁶, Z_rein = 1.62x10⁶, Z_calcul = 6x10⁶). Calculer les coefficients de réflexion R_gr (graisse-rein) et R_rc (rein-calcul) :",
        "answers": [
            {"id": "a", "text": "Rgr = 4 × 10⁻³", "correct": False},
            {"id": "b", "text": "Rgr = 8 × 10⁻³", "correct": True},
            {"id": "c", "text": "Rrc = 0.17", "correct": False},
            {"id": "d", "text": "Rrc = 0.33", "correct": True},
            {"id": "e", "text": "Rrc = 0.67", "correct": False}
        ],
        "explanation": "B, D (Vraies) :\nR_gr = [(1.62 - 1.35)/(1.62 + 1.35)]² = (0.27/2.97)² ≈ 0.00826 = 8 × 10⁻³.\nR_rc = [(6 - 1.62)/(6 + 1.62)]² = (4.38/7.62)² ≈ 0.33."
    },
    {
        "id": "q-ue4-f1-8",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Piézoélectricité", "Sonde", "Résolution"],
        "statement": "QCM 8 : Parmi les propositions suivantes concernant les sondes échographiques, lesquelles sont exactes ?",
        "answers": [
            {"id": "a", "text": "Les cristaux piézoélectriques sont le principal composant d’une sonde échographique générant des ondes ultrasonores", "correct": True},
            {"id": "b", "text": "L’acier inoxydable est souvent utilisé pour les cristaux piézoélectriques dans les sondes", "correct": False},
            {"id": "c", "text": "Les interfaces de couplage permettent d’adapter la fréquence d’émission aux tissus examinés", "correct": False},
            {"id": "d", "text": "Le gel utilisé lors de l’échographie permet la réduction du bruit ambiant", "correct": False},
            {"id": "e", "text": "Une fréquence élevée permet une résolution d’image améliorée en échographie", "correct": True}
        ],
        "explanation": "A, E (Vraies) : Les éléments piézoélectriques (ex: céramiques PZT) génèrent et reçoivent les ultrasons. Une fréquence élevée améliore la résolution spatiale.\nB (Faux) : Acier inoxydable non piézoélectrique.\nC, D (Fausses) : Le gel élimine l'air à l'interface peau/sonde."
    },
    {
        "id": "q-ue4-f1-9",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Échogénicité", "Kyste", "Mammographie"],
        "statement": "QCM 9 : Concernant l'interprétation des images échographiques, quelles propositions sont exactes ?",
        "answers": [
            {"id": "a", "text": "Un kyste simple à l’échographie apparaît hyperéchogène avec cône d’ombre", "correct": False},
            {"id": "b", "text": "Une interface très réfléchissante des ondes ultrasonores apparaît noire sur l’image échographique", "correct": False},
            {"id": "c", "text": "L’énergie ultrasonore est convertie en image", "correct": True},
            {"id": "d", "text": "Une échographie mammaire utilise généralement des ondes ultrasonores dans la gamme 5 à 7 MHz", "correct": True},
            {"id": "e", "text": "Une lésion hypoéchogène apparaît plus sombre lors d’une échographie car elle réfléchit moins les ondes ultrasonores", "correct": True}
        ],
        "explanation": "C, D, E (Vraies) : Les échos sont transformés en pixels lumineux. Les lésions hypoéchogènes renvoient peu d'échos (plus sombres).\nA (Faux) : Un kyste est anéchogène (noir) avec renforcement postérieur.\nB (Faux) : Interface très réfléchissante = blanche (hyperéchogène)."
    },
    {
        "id": "q-ue4-f1-10",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Doppler couleur", "Effet Doppler", "Globules rouges"],
        "statement": "QCM 10 : Concernant le Doppler et ses applications médicales, quelles propositions sont exactes ?",
        "answers": [
            {"id": "a", "text": "L’effet Doppler est un phénomène observé lorsque la fréquence d’une onde ultrasonore change en fonction de l’absorption", "correct": False},
            {"id": "b", "text": "Une échographie Doppler est principalement utilisée pour évaluer le flux sanguin", "correct": True},
            {"id": "c", "text": "Lors de l’utilisation d’un Doppler couleur, la couleur rouge indique que le flux se rapproche de la sonde", "correct": True},
            {"id": "d", "text": "La vitesse des globules rouges est proportionnelle au décalage de la fréquence entre les ondes émisses et les ondes réfléchies", "correct": True},
            {"id": "e", "text": "Le doppler pulsé consiste à envoyer des impulsions d’ultrasons dans une zone précise pour évaluer la vitesse du flux sanguin", "correct": True}
        ],
        "explanation": "B, C, D, E (Vraies) : L'effet Doppler mesure la vitesse d'éléments mobiles (globules rouges). En Doppler couleur, le rouge indique un flux allant vers la sonde (BART rule).\nA (Faux) : Le décalage de fréquence dépend du mouvement relatif de la cible."
    },
    {
        "id": "q-ue4-f1-11",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Ondes acoustiques", "Infrasons", "Propagation"],
        "statement": "Question 1 : Concernant les ondes acoustiques, quelles propositions sont exactes ?",
        "answers": [
            {"id": "a", "text": "Les ondes sonores sont des ondes longitudinales qui se propagent à des vitesses différentes dans les fluides gazeux ou liquides", "correct": True},
            {"id": "b", "text": "Les fréquences utilisées en échographie vont de 20 Hz à 20kHz", "correct": False},
            {"id": "c", "text": "Les ondes US ont uniquement des applications médicales telle que l'échographie", "correct": False},
            {"id": "d", "text": "Les infrasons sont des ondes de pression de fréquences inférieures à 20 Hz", "correct": True},
            {"id": "e", "text": "Aucune des propositions précédentes n'est exacte", "correct": False}
        ],
        "explanation": "A, D (Vraies) : Les ondes sonores sont mécaniques et longitudinales. Les infrasons ont une fréquence < 20 Hz.\nB (Faux) : Fréquences en échographie de 2 à 15 MHz.\nC (Faux) : Applications industrielles et militaires (sonar)."
    },
    {
        "id": "q-ue4-f1-12",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Célérité", "Atténuation", "Décibel"],
        "statement": "Question 2 : Concernant la propagation des ondes acoustiques dans les tissus :",
        "answers": [
            {"id": "a", "text": "Leur vitesse de propagation dépend de la densité du milieu de propagation", "correct": True},
            {"id": "b", "text": "Leur vitesse de propagation dans l'os est supérieure à leur vitesse de propagation dans la graisse", "correct": True},
            {"id": "c", "text": "Elles subissent une atténuation exponentielle dans les tissus traversés", "correct": True},
            {"id": "d", "text": "L'atténuation des US dans les tissus peut être quantifiée sur une échelle logarithmique en décibels", "correct": True},
            {"id": "e", "text": "L'atténuation des US dans les tissus est indépendante de la fréquence de l'onde utilisée", "correct": False}
        ],
        "explanation": "A, B, C, D (Vraies) : c_os ≈ 4000 m/s vs c_graisse ≈ 1450 m/s. Atténuation exponentielle en I = I0 * 10^(-alpha * f * x / 10).\nE (Faux) : L'atténuation augmente proportionnellement avec la fréquence."
    },
    {
        "id": "q-ue4-f1-13",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Calcul atténuation", "Intensité", "Décibel"],
        "statement": "Question 3 : Une onde US de fréquence 10 MHz d'intensité initiale I0 = 100 mW/m², traverse 1,5 cm d'un tissu dont le coefficient d'atténuation est de 0,2 dB/cm/MHz.",
        "answers": [
            {"id": "a", "text": "L'atténuation globale due aux tissus est de 0,3 dB", "correct": False},
            {"id": "b", "text": "L'atténuation globale due aux tissus est de 3 dB", "correct": True},
            {"id": "c", "text": "L'intensité transmise par le tissu est 50 mW/m²", "correct": True},
            {"id": "d", "text": "L'intensité a été atténuée d'un facteur 2", "correct": True},
            {"id": "e", "text": "L'intensité a diminué de 25%", "correct": False}
        ],
        "explanation": "B, C, D (Vraies) : Atténuation (dB) = 0.2 × 1.5 cm × 10 MHz = 3 dB.\nUne atténuation de 3 dB correspond à une division de l'intensité incidente par 2 (facteur 2), donc I_transmise = 100/2 = 50 mW/m²."
    },
    {
        "id": "q-ue4-f1-14",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Atténuation", "Impédance", "Réflexion"],
        "statement": "Question 4 : Concernant l'atténuation des ultrasons dans les tissus :",
        "answers": [
            {"id": "a", "text": "L'atténuation d'un faisceau US comprend uniquement les phénomènes d'absorption et de diffusion", "correct": False},
            {"id": "b", "text": "L'absorption des ondes US dans les tissus augmente avec la fréquence de ces ondes", "correct": True},
            {"id": "c", "text": "La diffusion des US dans les tissus augmente lorsque la viscosité augmente", "correct": False},
            {"id": "d", "text": "L'intensité réfléchie sur une interface dépend des impédances acoustiques de part et d'autre de l'interface", "correct": True},
            {"id": "e", "text": "L'intensité réfléchie en pourcentage R(%) est donnée par [(Z2 - Z1)/(Z2 + Z1)]²", "correct": True}
        ],
        "explanation": "B, D, E (Vraies) : L'atténuation englobe absorption, diffusion et réflexion. L'absorption croît avec la fréquence. R(%) = [(Z2 - Z1)/(Z2 + Z1)]²."
    },
    {
        "id": "q-ue4-f1-15",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Diffusion", "Longueur d'onde", "Impédance"],
        "statement": "Question 5 : Concernant la diffusion des ultrasons dans les milieux de propagation :",
        "answers": [
            {"id": "a", "text": "La diffusion des US consiste en la dispersion de l'énergie uniquement selon la direction de propagation", "correct": False},
            {"id": "b", "text": "La diffusion se produit sur des objets rencontrés par le faisceau de petites tailles par rapport à la longueur d'onde des US", "correct": True},
            {"id": "c", "text": "La diffusion contribue à la dégradation de la qualité des images échographiques", "correct": True},
            {"id": "d", "text": "L'impédance acoustique est le rapport de la masse volumique à la vitesse de propagation", "correct": False},
            {"id": "e", "text": "Aucune des propositions précédentes n'est exacte", "correct": False}
        ],
        "explanation": "B, C (Vraies) : La diffusion éparpille l'énergie dans toutes les directions sur de petites cibles (< lambda), créant du bruit spéculaire.\nD (Faux) : Z = rho * c (produit et non rapport)."
    },
    {
        "id": "q-ue4-f1-16",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Transducteur", "Céramique piézoélectrique", "Résonance"],
        "statement": "Question 6 : Concernant la production des ultrasons :",
        "answers": [
            {"id": "a", "text": "Un cristal piézoélectrique est un transducteur", "correct": True},
            {"id": "b", "text": "Les cristaux de quartz ont des propriétés piézoélectriques", "correct": True},
            {"id": "c", "text": "Une céramique piézoélectrique peut jouer à la fois le rôle d'émetteur et de récepteur", "correct": True},
            {"id": "d", "text": "La fréquence de résonance d'une lame piézoélectrique est d'autant plus grande que l'épaisseur de la lame est grande", "correct": False},
            {"id": "e", "text": "Le faisceau émis par un transducteur US se propage dans une seule direction sans divergence", "correct": False}
        ],
        "explanation": "A, B, C (Vraies) : Transducteur = conversion électromécanique réversible (effet direct et inverse).\nD (Faux) : f_résonance = c / (2 * épaisseur) -> plus l'épaisseur est faible, plus la fréquence est élevée."
    },
    {
        "id": "q-ue4-f1-17",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Modes échographiques", "Mode A", "Mode B", "Mode M"],
        "statement": "Question 7 : Concernant les modes de l'imagerie échographique :",
        "answers": [
            {"id": "a", "text": "On utilise généralement 3 modes différents en imagerie échographique (A, B, M)", "correct": True},
            {"id": "b", "text": "Le mode A est utilisé pour observer des interfaces statiques (pics d'amplitude)", "correct": True},
            {"id": "c", "text": "En mode B, la brillance d'un point de l'image augmente avec l'amplitude de l'écho", "correct": True},
            {"id": "d", "text": "Le mode M est la combinaison du mode A avec le temps", "correct": False},
            {"id": "e", "text": "Le mode M est pratique pour l'étude des structures statiques", "correct": False}
        ],
        "explanation": "A, B, C (Vraies) : Mode A (Amplitude), Mode B (Brillance 2D), Mode M (Mouvement 1D + Temps pour structures mobiles comme le cœur)."
    },
    {
        "id": "q-ue4-f1-18",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Échogénicité", "Calcul rénal", "Kyste", "Hémangiome"],
        "statement": "Question 8 : Concernant les images échographiques :",
        "answers": [
            {"id": "a", "text": "Plus l'amplitude de l'écho est grande et plus l'image est blanche", "correct": True},
            {"id": "b", "text": "Les interfaces liquidiennes sont généralement très échogènes", "correct": False},
            {"id": "c", "text": "Un calcul rénal est un objet hyperéchogène", "correct": True},
            {"id": "d", "text": "Les kystes sont des objets anéchogènes", "correct": True},
            {"id": "e", "text": "Les lacs vasculaires d'un hémangiome du foie correspondent à une multitude d'interfaces rencontrées par les US", "correct": True}
        ],
        "explanation": "A, C, D, E (Vraies) : Échos intenses = blanc (hyperéchogène). Kystes/liquides purement transmissifs = noirs (anéchogènes)."
    },
    {
        "id": "q-ue4-f1-19",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Résolution axiale", "Profondeur d'exploration", "Fréquence"],
        "statement": "Question 9 : Concernant les images échographiques et le choix de la fréquence :",
        "answers": [
            {"id": "a", "text": "La résolution axiale (en profondeur) augmente avec la fréquence de l'onde", "correct": True},
            {"id": "b", "text": "Plus la fréquence de l'onde est élevée et plus la profondeur de champ est grande", "correct": False},
            {"id": "c", "text": "En échographie il faut toujours trouver un compromis entre la profondeur d'exploration et la résolution", "correct": True},
            {"id": "d", "text": "Les fréquences les plus élevées sont utilisées pour l'échographie endocavitaire et superficielle", "correct": True},
            {"id": "e", "text": "L'échographie des seins nécessite les fréquences les plus faibles", "correct": False}
        ],
        "explanation": "A, C, D (Vraies) : Haute fréquence = excellente résolution mais forte atténuation (faible pénétration). Compromis obligatoire."
    },
    {
        "id": "q-ue4-f1-20",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Cas pratique", "Tumeur du foie", "Calcul dimension"],
        "statement": "Au cours d'une échographie d'une tumeur du foie, le délai séparant l'écho de la paroi antérieure de celui de la paroi postérieure est de 32 µs (célérité c = 1600 m/s). Question 10 : Quelle est la dimension de la tumeur selon cette ligne de tir ?",
        "answers": [
            {"id": "a", "text": "5,12 cm", "correct": False},
            {"id": "b", "text": "2,56 cm", "correct": True},
            {"id": "c", "text": "5,12 mm", "correct": False},
            {"id": "d", "text": "10,24 mm", "correct": False},
            {"id": "e", "text": "3,25 cm", "correct": False}
        ],
        "explanation": "B (Vrai) : Trajet aller-retour 2 * épaisseur = c * delta_t = 1600 m/s * 32×10⁻⁶ s = 0.0512 m = 5.12 cm -> épaisseur = 2.56 cm."
    },
    {
        "id": "q-ue4-f1-21",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Calcul intensité", "Tumeur du foie", "Rapport I_p/I_a"],
        "statement": "L'atténuation du tissu tumoral hépatique est de 1 dB/cm/MHz et la fréquence de la sonde est de 4 MHz. Question 11 : Calculer le rapport d'intensité Ip / Ia entre l'écho de la paroi postérieure et celui de la paroi antérieure :",
        "answers": [
            {"id": "a", "text": "10 000", "correct": False},
            {"id": "b", "text": "1 000", "correct": False},
            {"id": "c", "text": "100", "correct": True},
            {"id": "d", "text": "10", "correct": False},
            {"id": "e", "text": "1", "correct": False}
        ],
        "explanation": "C (Vrai) : Trajet aller-retour = 2 × 2.56 cm = 5.12 cm.\nAtténuation globale = 1 dB/cm/MHz × 5.12 cm × 4 MHz = 20.48 dB ≈ 20 dB.\nUne atténuation de 20 dB correspond à un facteur d'atténuation de 10² = 100."
    },
    {
        "id": "q-ue4-f1-22",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Effet Doppler", "Fréquence perçue", "Angle Doppler"],
        "statement": "Question 12 : Concernant l'effet Doppler :",
        "answers": [
            {"id": "a", "text": "L'effet Doppler traduit la variation de la fréquence émise par une source lorsque celle-ci est en mouvement", "correct": True},
            {"id": "b", "text": "La fréquence perçue par un observateur immobile lorsque la source s'éloigne de lui est inférieure à la fréquence réelle de la source", "correct": True},
            {"id": "c", "text": "Lorsque l'axe source-observateur fait un angle droit avec la direction de mouvement relatif source-observateur l'effet Doppler est à son maximum", "correct": False},
            {"id": "d", "text": "L'écart de fréquence de l'onde reçue après réflexion sur un objet en mouvement mesurée par effet Doppler est proportionnel à la fréquence émise par la sonde Doppler", "correct": True},
            {"id": "e", "text": "L'écart de fréquence de l'onde reçue après réflexion sur un objet en mouvement mesurée par effet Doppler est proportionnel à la vitesse de propagation des US", "correct": False}
        ],
        "explanation": "A, B, D (Vraies) : delta_f = 2 * f0 * v * cos(theta) / c.\nC (Faux) : Angle 90° -> cos(90°) = 0, effet Doppler nul.\nE (Faux) : Inversement proportionnel à c."
    },
    {
        "id": "q-ue4-f1-23",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Doppler couleur", "Innocuité", "Effets thermiques"],
        "statement": "Question 13 : Concernant le Doppler et la sécurité des ultrasons :",
        "answers": [
            {"id": "a", "text": "Le mode pulsé et le mode couleur peuvent être couplés avec l'imagerie TM", "correct": True},
            {"id": "b", "text": "Le mode couleur permet de savoir si les parties en mouvement s'éloignent ou se rapprochent de l'observateur", "correct": True},
            {"id": "c", "text": "La couleur rouge est donnée pour les parties qui s'éloignent de l'observateur", "correct": False},
            {"id": "d", "text": "Les effets secondaires thermiques des US sont fréquents pour des élévations de température < 1°C", "correct": False},
            {"id": "e", "text": "En imagerie US il est possible d'avoir autant d'examens que souhaité car leurs effets secondaires sont négligeables", "correct": True}
        ],
        "explanation": "A, B, E (Vraies) : L'imagerie US est non ionisante et sûre aux intensités diagnostiques (BART : Red = Toward).\nC (Faux) : Rouge = rapprochement de la sonde."
    },
    {
        "id": "q-ue4-f1-24",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Ultrasons vs Infrasons", "Échographie"],
        "statement": "Question 1 (Série 3) : Concernant la nature des sons et ultrasons :",
        "answers": [
            {"id": "a", "text": "L'échographie se base sur l'utilisation des infrasons", "correct": False},
            {"id": "b", "text": "Un son de f = 0,01 MHz est un ultrason", "correct": False},
            {"id": "c", "text": "Un son de f = 0,5 MHz peut être utilisé en échographie", "correct": False},
            {"id": "d", "text": "Un son nécessite un milieu matériel pour se propager", "correct": True},
            {"id": "e", "text": "Aucune réponse précédente n'est correcte", "correct": False}
        ],
        "explanation": "D (Vrai) : Les ondes mécaniques nécessitent un milieu élastique (air, eau, tissus).\nA (Faux) : Échographie = ultrasons.\nB (Faux) : 0,01 MHz = 10 kHz (domaine audible)."
    },
    {
        "id": "q-ue4-f1-25",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Paramètres acoustiques", "Amplitude"],
        "statement": "Question 2 (Série 3) : Concernant les caractéristiques d'une onde sonore :",
        "answers": [
            {"id": "a", "text": "La vitesse de propagation d'un son est déterminée par sa source", "correct": False},
            {"id": "b", "text": "La fréquence d'un son est déterminée par son milieu de propagation", "correct": False},
            {"id": "c", "text": "L'amplitude d'un son est déterminée par son milieu de propagation", "correct": True},
            {"id": "d", "text": "La longueur d'onde d'un son est indépendante du milieu de propagation", "correct": False},
            {"id": "e", "text": "Aucune réponse précédente n'est correcte", "correct": False}
        ],
        "explanation": "C (Vrai) : L'amplitude diminue au cours de la propagation selon l'atténuation du milieu.\nA, B (Fausses) : La vitesse dépend du milieu, la fréquence dépend de la source."
    },
    {
        "id": "q-ue4-f1-26",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Vitesse du son", "Élastance", "Milieux"],
        "statement": "Question 3 (Série 3) : Concernant la vitesse de propagation d'un son :",
        "answers": [
            {"id": "a", "text": "La vitesse de propagation augmente lorsque l'élasticité (incompressibilité) du milieu augmente", "correct": True},
            {"id": "b", "text": "La vitesse de propagation augmente lorsque la masse volumique augmente", "correct": False},
            {"id": "c", "text": "La vitesse du son dans l'eau est supérieure à celle dans l'air", "correct": True},
            {"id": "d", "text": "La vitesse du son dans les os est supérieure à celle dans les tissus mous", "correct": True},
            {"id": "e", "text": "Aucune réponse précédente n'est correcte", "correct": False}
        ],
        "explanation": "A, C, D (Vraies) : c = sqrt(E / rho). c_air ≈ 340 m/s, c_eau ≈ 1500 m/s, c_os ≈ 4000 m/s."
    },
    {
        "id": "q-ue4-f1-27",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Calcul I", "Atténuation", "W/m2"],
        "statement": "Question 4 (Série 3) : Un son d'intensité initiale I0 = 10⁻² W.m⁻² se propage (atténuation 20 dB/cm/MHz). Déterminer l'intensité finale au bout de 2 cm pour f = 1 MHz :",
        "answers": [
            {"id": "a", "text": "10⁻³ W.m⁻²", "correct": False},
            {"id": "b", "text": "10⁻¹ W.m⁻²", "correct": False},
            {"id": "c", "text": "10⁻⁶ W.m⁻²", "correct": True},
            {"id": "d", "text": "10² W.m⁻²", "correct": False},
            {"id": "e", "text": "10⁴ W.m⁻²", "correct": False}
        ],
        "explanation": "C (Vrai) : Atténuation (dB) = 20 × 2 cm × 1 MHz = 40 dB.\nUne baisse de 40 dB correspond à un facteur de 10⁻⁴.\nI = I0 × 10⁻⁴ = 10⁻² × 10⁻⁴ = 10⁻⁶ W.m⁻²."
    },
    {
        "id": "q-ue4-f1-28",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Calcul % atténuation", "Intensité"],
        "statement": "Question 5 (Série 3) : Un son d'intensité initiale I0 = 10⁻² W.m⁻² se propage. Son intensité finale est I = 2.10⁻³ W.m⁻². Déterminer le pourcentage d'atténuation :",
        "answers": [
            {"id": "a", "text": "20%", "correct": False},
            {"id": "b", "text": "50%", "correct": False},
            {"id": "c", "text": "70%", "correct": False},
            {"id": "d", "text": "99%", "correct": False},
            {"id": "e", "text": "Aucune réponse précédente n'est correcte (Le pourcentage vaut 80%)", "correct": True}
        ],
        "explanation": "E (Vrai) : Intensité transmise = (2.10⁻³ / 10⁻²) = 0,2 = 20%. Donc l'atténuation (perte) est de 100% - 20% = 80%. 80% ne figurant pas parmi A, B, C, D, la réponse est E."
    },
    {
        "id": "q-ue4-f1-29",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Atténuation", "Facteurs"],
        "statement": "Question 6 (Série 3) : Concernant les causes d'atténuation d'une onde ultrasonore :",
        "answers": [
            {"id": "a", "text": "L'atténuation ne dépend pas de la fréquence", "correct": False},
            {"id": "b", "text": "L'atténuation ne dépend que de l'absorption", "correct": False},
            {"id": "c", "text": "L'atténuation dépend de la diffusion et de la réflexion", "correct": True},
            {"id": "d", "text": "L'atténuation est indépendante des tissus traversés", "correct": False},
            {"id": "e", "text": "Aucune réponse précédente n'est correcte", "correct": False}
        ],
        "explanation": "C (Vrai) : L'atténuation est la somme des pertes par absorption, diffusion et réflexion aux interfaces."
    },
    {
        "id": "q-ue4-f1-30",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Absorption", "Interfaces", "Réflexion"],
        "statement": "Question 7 (Série 3) : Concernant les phénomènes d'interaction ultrasonore :",
        "answers": [
            {"id": "a", "text": "L'absorption augmente quand la fréquence de l'onde augmente", "correct": True},
            {"id": "b", "text": "L'énergie de l'absorption est convertie en énergie cinétique macroscopique", "correct": False},
            {"id": "c", "text": "L'absorption augmente quand la viscosité du milieu diminue", "correct": False},
            {"id": "d", "text": "La diffusion se produit lorsque les objets sont grands par rapport à la longueur d'onde", "correct": False},
            {"id": "e", "text": "La réflexion se produit à l'interface entre deux milieux", "correct": True}
        ],
        "explanation": "A, E (Vraies) : Absorption croissante avec la fréquence (dissipée en chaleur). La réflexion a lieu aux interfaces de rupture d'impédance."
    },
    {
        "id": "q-ue4-f1-31",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Production US", "Résonance", "Épaisseur céramique"],
        "statement": "Question 8 (Série 3) : Concernant la formation des ultrasons par transducteur :",
        "answers": [
            {"id": "a", "text": "Ils se basent sur l'effet de l'inversion des spins", "correct": False},
            {"id": "b", "text": "La fréquence de résonance dépend de l'épaisseur du cristal", "correct": True},
            {"id": "c", "text": "Plus l'épaisseur de la céramique est petite, plus la fréquence est grande", "correct": True},
            {"id": "d", "text": "Lors de l'acquisition du signal, la 2ᵉ impulsion est envoyée immédiatement après la première", "correct": False},
            {"id": "e", "text": "Lors de l'acquisition du signal, il n'y a qu'un écho", "correct": False}
        ],
        "explanation": "B, C (Vraies) : f = c / (2 * e). Plus l'épaisseur e est petite, plus f est grande."
    },
    {
        "id": "q-ue4-f1-32",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Modes A B M", "Imagerie"],
        "statement": "Question 9 (Série 3) : Concernant les modes d'affichage en échographie :",
        "answers": [
            {"id": "a", "text": "Le mode A est utilisé pour obtenir un pic proportionnel à l'amplitude", "correct": True},
            {"id": "b", "text": "Le mode B est utilisé pour obtenir une brillance proportionnelle à l'amplitude", "correct": True},
            {"id": "c", "text": "Le mode M est utilisé pour observer des mouvements en fonction du temps", "correct": True},
            {"id": "d", "text": "Le mode M est combiné avec le mode A", "correct": False},
            {"id": "e", "text": "Aucune proposition précédente n'est correcte", "correct": False}
        ],
        "explanation": "A, B, C (Vraies) : Mode A = Amplitude, Mode B = Brillance (carte de niveaux de gris 2D), Mode M = Mouvement (déroulement temporel 1D)."
    },
    {
        "id": "q-ue4-f1-33",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Interprétation écho", "Calculs", "Résolution"],
        "statement": "Question 10 (Série 3) : Concernant la formation des images et le choix de fréquence :",
        "answers": [
            {"id": "a", "text": "Un calcul apparaît en blanc car l'interface n'est pas réfléchissante", "correct": False},
            {"id": "b", "text": "Un kyste apparaît en blanc car il n'y a pas d'interface", "correct": False},
            {"id": "c", "text": "Plus la fréquence des ultrasons est élevée, plus la résolution en profondeur est grande", "correct": True},
            {"id": "d", "text": "Plus la fréquence est élevée, plus l'absorption par le milieu est élevée", "correct": True},
            {"id": "e", "text": "Plus on explore un tissu en profondeur, plus la fréquence des ultrasons doit être élevée", "correct": False}
        ],
        "explanation": "C, D (Vraies) : La haute fréquence améliore la résolution spatiale axiale mais majore l'absorption."
    },
    {
        "id": "q-ue4-f1-34",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Calcul écho foie", "Durée aller-retour", "dt"],
        "statement": "Question 11 (Série 3) : Échographie du foie (f = 3 MHz, c = 1500 m/s). Les ultrasons traversent Lp = 0,5 cm de peau, Lg = 1 cm de graisse et Lm = 1,5 cm de muscle avant d'atteindre le foie. Calculer le délai Δt émission-retour d'écho :",
        "answers": [
            {"id": "a", "text": "Δt = 400 µs", "correct": False},
            {"id": "b", "text": "Δt = 200 µs", "correct": False},
            {"id": "c", "text": "Δt = 40 µs", "correct": True},
            {"id": "d", "text": "Δt = 20 µs", "correct": False},
            {"id": "e", "text": "Δt = 4 µs", "correct": False}
        ],
        "explanation": "C (Vrai) : Distance totale aller d = 0.5 + 1.0 + 1.5 = 3.0 cm = 0.03 m.\nTrajet aller-retour = 2d = 0.06 m.\nΔt = 2d / c = 0.06 m / 1500 m/s = 4 × 10⁻⁵ s = 40 µs."
    },
    {
        "id": "q-ue4-f1-35",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Effet Doppler", "Rapprochement"],
        "statement": "Question 12 (Série 3) : Concernant l'effet Doppler :",
        "answers": [
            {"id": "a", "text": "Il a été découvert en 1492", "correct": False},
            {"id": "b", "text": "La fréquence perçue est indépendante du mouvement relatif entre l'émetteur et le récepteur", "correct": False},
            {"id": "c", "text": "Lorsqu'un récepteur se rapproche d'un émetteur, la fréquence perçue augmente", "correct": True},
            {"id": "d", "text": "Lorsqu'un récepteur s'éloigne d'un émetteur, la fréquence perçue augmente", "correct": False},
            {"id": "e", "text": "La fréquence de la source est indépendante de la vitesse du récepteur", "correct": True}
        ],
        "explanation": "C, E (Vraies) : Le rapprochement provoque un glissement vers les hautes fréquences (décalage vers le bleu)."
    },
    {
        "id": "q-ue4-f1-36",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Calcul vitesse GR", "Doppler", "15 cm/s"],
        "statement": "Question 13 (Série 3) : Examen Doppler avec f = 4,0 × 10⁴ Hz. Décalage Doppler mesuré Δf = 10 Hz (cérélité c = 1200 m/s). Quelle est la vitesse v du globule rouge ?",
        "answers": [
            {"id": "a", "text": "15 cm/s", "correct": True},
            {"id": "b", "text": "30 cm/s", "correct": False},
            {"id": "c", "text": "10 cm/s", "correct": False},
            {"id": "d", "text": "5 cm/s", "correct": False},
            {"id": "e", "text": "3 cm/s", "correct": False}
        ],
        "explanation": "A (Vrai) : Δf = (2 × f × v) / c => v = (c × Δf) / (2 × f) = (1200 × 10) / (2 × 4.0×10⁴) = 12000 / 80000 = 0.15 m/s = 15 cm/s."
    },
    {
        "id": "q-ue4-f1-37",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Doppler couleur", "Codage bleu", "Doppler pulsé"],
        "statement": "Question 14 (Série 3) : Concernant la technologie et les modes Doppler :",
        "answers": [
            {"id": "a", "text": "Dans le cadre du Doppler couleur, le codage bleu est utilisé pour les éléments qui s'éloignent du transducteur", "correct": True},
            {"id": "b", "text": "Le Doppler pulsé permet de sélectionner les zones de l'espace à étudier", "correct": True},
            {"id": "c", "text": "Le Doppler couleur se base sur l'effet Doppler des ondes lumineuses", "correct": False},
            {"id": "d", "text": "En Doppler couleur, lorsqu'un élément s'éloigne du transducteur, il apparaît en rouge", "correct": False},
            {"id": "e", "text": "Aucune réponse précédente n'est correcte", "correct": False}
        ],
        "explanation": "A, B (Vraies) : Règle BART (Blue Away, Red Toward). Le Doppler pulsé possède une fenêtre de tir réglable en profondeur."
    },
    {
        "id": "q-ue4-f1-38",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Effets secondaires US", "Cavitation"],
        "statement": "Question 15 (Série 3) : Concernant les effets secondaires des ultrasons :",
        "answers": [
            {"id": "a", "text": "Ils ont des effets significatifs si la température due à l'absorption augmente de 0,1 °C", "correct": False},
            {"id": "b", "text": "Ils peuvent provoquer une cavitation dans le cadre de haute pression acoustique", "correct": True},
            {"id": "c", "text": "Des effets in vivo néfastes sur le fœtus humain ont été démontrés aux doses diagnostiques", "correct": False},
            {"id": "d", "text": "Les ultrasons ne sont pas soumis au principe de justification appliqué aux rayons X", "correct": False},
            {"id": "e", "text": "Aucune réponse précédente n'est correcte", "correct": False}
        ],
        "explanation": "B (Vrai) : Les ultrasons de forte intensité génèrent des bulles de gaz pouvant imploser (cavitation)."
    },
    {
        "id": "q-ue4-f1-39",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Célérité", "Calcul c", "360 m/s"],
        "statement": "Une onde sonore a une fréquence de 15 kHz et une longueur d'onde de 2,4 cm. Quelle est la célérité de cette onde ?",
        "answers": [
            {"id": "a", "text": "0,16 m/s", "correct": False},
            {"id": "b", "text": "6,25 m/s", "correct": False},
            {"id": "c", "text": "360 m/s", "correct": True},
            {"id": "d", "text": "100 m/s", "correct": False},
            {"id": "e", "text": "1000 m/s", "correct": False}
        ],
        "explanation": "C (Vrai) : c = lambda × f = 2.4×10⁻² m × 15×10³ Hz = 360 m/s."
    },
    {
        "id": "q-ue4-f1-40",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Facile",
        "tags": ["Impédance eau", "Calcul Z", "1.5x106 SI"],
        "statement": "On donne rho_eau = 10³ kg.m⁻³. La vitesse des ondes sonores dans l'eau est de 1500 m.s⁻¹. Calculer l'impédance acoustique Z de l'eau :",
        "answers": [
            {"id": "a", "text": "Z = 1,5 × 10² SI", "correct": False},
            {"id": "b", "text": "Z = 1,5 × 10³ SI", "correct": False},
            {"id": "c", "text": "Z = 1,5 × 10⁴ SI", "correct": False},
            {"id": "d", "text": "Z = 1,5 × 10⁵ SI", "correct": False},
            {"id": "e", "text": "Z = 1,5 × 10⁶ SI", "correct": True}
        ],
        "explanation": "E (Vrai) : Z_eau = rho × c = 1000 kg/m³ × 1500 m/s = 1.5 × 10⁶ kg.m⁻².s⁻¹."
    },
    {
        "id": "q-ue4-f1-41",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Coefficients R et T", "R + T = 1"],
        "statement": "Une onde se propage d'un milieu Z1 vers Z2. Soit T le coefficient de transmission et R le coefficient de réflexion en intensité :",
        "answers": [
            {"id": "a", "text": "Si Z1 >> Z2, alors T ≈ 1", "correct": False},
            {"id": "b", "text": "Si Z1 << Z2, alors R ≈ 1", "correct": True},
            {"id": "c", "text": "Si Z1 ≈ Z2, alors R ≈ 1", "correct": False},
            {"id": "d", "text": "Si Z1 ≈ Z2, alors T ≈ 1", "correct": True},
            {"id": "e", "text": "Si Z1 >> Z2, R + T < 1", "correct": False}
        ],
        "explanation": "B, D (Vraies) : Si les impédances sont très différentes (Z1 << Z2 ou Z1 >> Z2), presque toute l'énergie est réfléchie (R ≈ 1). Si Z1 ≈ Z2, la transmission est maximale (T ≈ 1). On a toujours R + T = 1."
    },
    {
        "id": "q-ue4-f1-42",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Fraction transmise", "Calcul T", "64%"],
        "statement": "Une onde acoustique passe d'un milieu Z1 = 1000 SI vers un milieu Z2 = 4000 SI. Quelle est la fraction d'énergie incidente transmise T ?",
        "answers": [
            {"id": "a", "text": "36 %", "correct": False},
            {"id": "b", "text": "45 %", "correct": False},
            {"id": "c", "text": "52 %", "correct": False},
            {"id": "d", "text": "64 %", "correct": True},
            {"id": "e", "text": "72 %", "correct": False}
        ],
        "explanation": "D (Vrai) : T = 4*Z1*Z2 / (Z1 + Z2)² = 4 * 1000 * 4000 / (5000)² = 16 000 000 / 25 000 000 = 0.64 = 64%."
    },
    {
        "id": "q-ue4-f1-43",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Niveau sonore", "Niveau -20dB", "R=0.99"],
        "statement": "Lors d'un changement de milieu, le niveau sonore est diminué de 20 dB. Quelle est la valeur du coefficient de réflexion R ?",
        "answers": [
            {"id": "a", "text": "0,2", "correct": False},
            {"id": "b", "text": "0,1", "correct": False},
            {"id": "c", "text": "0,99", "correct": True},
            {"id": "d", "text": "0,5", "correct": False},
            {"id": "e", "text": "0,8", "correct": False}
        ],
        "explanation": "C (Vrai) : ΔL = -20 dB => T = 10^(-20/10) = 10⁻² = 0.01.\nComme R + T = 1, on a R = 1 - 0.01 = 0.99."
    },
    {
        "id": "q-ue4-f1-44",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Impédance poumon", "Calcul Zp", "1725 SI"],
        "statement": "Sur une échographie, le coefficient de réflexion à l'interface eau-poumon est R = 0,71 (Z_eau = 1.5×10⁶ SI). Déduire l'impédance Zp des tissus pulmonaires :",
        "answers": [
            {"id": "a", "text": "Zp = 17,25 SI", "correct": False},
            {"id": "b", "text": "Zp = 172,5 SI", "correct": False},
            {"id": "c", "text": "Zp = 1725 SI", "correct": True},
            {"id": "d", "text": "Zp = 17250 SI", "correct": False},
            {"id": "e", "text": "Zp = 172500 SI", "correct": False}
        ],
        "explanation": "C (Vrai) : sqrt(R) = sqrt(0.71) ≈ 0.84. (Z_eau - Zp)/(Z_eau + Zp) = 0.84 => Zp = Z_eau * (1 - 0.84)/(1 + 0.84) = 1.5×10⁶ × (0.16 / 1.84) ≈ 1725 SI."
    },
    {
        "id": "q-ue4-f1-45",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Écholocalisation", "Dauphin", "400 m"],
        "statement": "Sifflement d'un dauphin à f = 1 kHz (80 dB). Seuil de détection = 40 dB. Atténuation alpha = 1 dB.cm⁻¹.MHz⁻¹. Quelle est la distance maximale d d'écholocalisation ?",
        "answers": [
            {"id": "a", "text": "50 m", "correct": False},
            {"id": "b", "text": "200 m", "correct": False},
            {"id": "c", "text": "400 m", "correct": True},
            {"id": "d", "text": "800 m", "correct": False},
            {"id": "e", "text": "1600 m", "correct": False}
        ],
        "explanation": "C (Vrai) : Fréquence f = 0.001 MHz. Perte maximale autorisée = 80 - 40 = 40 dB.\nAtténuation aller-retour = alpha * f * 2d = 1 dB/cm/MHz * 10⁻³ MHz * 2d (en cm) = 40 dB.\n2d = 40 / 10⁻³ cm = 40 000 cm = 800 m => d = 400 m."
    },
    {
        "id": "q-ue4-f1-46",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Difficile",
        "tags": ["Nuisance sonore", "Aéroport", "125 dB"],
        "statement": "Un avion produit L = 92 dB à D = 2 km. À d = 100 m pour 5 avions identiques sur le tarmac, quel est le niveau sonore maximal Lmax au niveau du bâtiment ?",
        "answers": [
            {"id": "a", "text": "Lmax = 73 dB", "correct": False},
            {"id": "b", "text": "Lmax = 98 dB", "correct": False},
            {"id": "c", "text": "Lmax = 125 dB", "correct": True},
            {"id": "d", "text": "Lmax = 140 dB", "correct": False},
            {"id": "e", "text": "Lmax = 150 dB", "correct": False}
        ],
        "explanation": "C (Vrai) : Lmax = L + 10 log(5) + 20 log(D / d) = 92 + 10 log(5) + 20 log(2000 / 100) = 92 + 7 + 26 = 125 dB."
    },
    {
        "id": "q-ue4-f1-47",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Changement de milieu", "Fréquence", "Hauteur du son"],
        "statement": "Au passage de l'onde sonore dans le verre ou le PVC :",
        "answers": [
            {"id": "a", "text": "Le son transmis dans le PVC est plus grave que celui transmis dans le verre", "correct": False},
            {"id": "b", "text": "Le son transmis dans le PVC est à la même hauteur que celui transmis dans le verre", "correct": True},
            {"id": "c", "text": "Le son transmis dans le PVC est plus aigu que celui transmis dans le verre", "correct": False},
            {"id": "d", "text": "Les sons transmis dans le verre et le PVC ont des longueurs d'onde inférieures à celle de l'onde incidente", "correct": False},
            {"id": "e", "text": "Les sons transmis dans le verre et le PVC ont des longueurs d'onde supérieures à celle de l'onde incidente", "correct": True}
        ],
        "explanation": "B, E (Vraies) : La fréquence (hauteur du son) est invariante lors d'un changement de milieu. Comme c_verre et c_PVC > c_air, la longueur d'onde lambda = c / f augmente dans ces milieux."
    },
    {
        "id": "q-ue4-f1-48",
        "subjectId": "sub-5",
        "chapter": "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Calcul de fréquence", "c=1500", "5 MHz"],
        "statement": "L'exploration d'un organe utilise des ultrasons de longueur d'onde lambda = 0,3 mm dans un milieu où c = 1500 m/s. Quelle est la fréquence vibratoire f ?",
        "answers": [
            {"id": "a", "text": "8 MHz", "correct": False},
            {"id": "b", "text": "5 MHz", "correct": True},
            {"id": "c", "text": "2 MHz", "correct": False},
            {"id": "d", "text": "1 MHz", "correct": False},
            {"id": "e", "text": "0,5 MHz", "correct": False}
        ],
        "explanation": "B (Vrai) : f = c / lambda = 1500 m/s / (0.3 × 10⁻³ m) = 5 × 10⁶ Hz = 5 MHz."
    }
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const INITIAL_QUESTIONS = (\[.*?\]);', content, flags=re.DOTALL)
if match:
    existing_json = match.group(1)
    existing_json_clean = re.sub(r'[\r\n]+', ' ', existing_json)
    existing_data = json.loads(existing_json_clean)
    
    new_ids = [q['id'] for q in ue4_fiche1_qcms]
    existing_filtered = [q for q in existing_data if q['id'] not in new_ids]
    
    updated_data = existing_filtered + ue4_fiche1_qcms
    
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
        
    print(f'Successfully added {len(ue4_fiche1_qcms)} new QCMs to UE 4 Fiche n°1! Total questions in bank: {len(updated_data)}')
else:
    print('Failed to locate INITIAL_QUESTIONS array')
