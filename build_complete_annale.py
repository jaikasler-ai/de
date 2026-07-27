import json

complete_questions = [
    {
        "id": "q-1",
        "subjectId": "sub-1",
        "chapter": "Fiche n°4 - Réplication de l’ADN et PCR.pdf",
        "year": 2026,
        "difficulty": "Difficile",
        "tags": ["ADN", "Polymérase", "Réplication"],
        "statement": "Quelle enzyme est responsable de la levée des super-tours de l’ADN pendant la réplication ?",
        "answers": [
            { "id": "a", "text": "L’ADN polymérase alpha", "correct": False },
            { "id": "b", "text": "La topoisomérase (ou gyrase)", "correct": True },
            { "id": "c", "text": "L’hélicase", "correct": False },
            { "id": "d", "text": "La ligase", "correct": False }
        ],
        "explanation": "Les topoisomérases modifient le degré de super-enroulement de l’ADN en coupant et en resoudant les brins."
    },
    {
        "id": "q-2",
        "subjectId": "sub-3",
        "chapter": "Immunité innée",
        "year": 2025,
        "difficulty": "Moyen",
        "tags": ["Macrophage", "Phagocytose"],
        "statement": "Quel récepteur membranaire reconnaît les motifs moléculaires associés aux pathogènes (PAMPs) ?",
        "answers": [
            { "id": "a", "text": "Les Toll-like Receptors (TLR)", "correct": True },
            { "id": "b", "text": "Les récepteurs aux lymphocytes T (TCR)", "correct": False },
            { "id": "c", "text": "Les anticorps circulants", "correct": False },
            { "id": "d", "text": "Les récepteurs CD4", "correct": False }
        ],
        "explanation": "Les TLR font partie des PRR (Pattern Recognition Receptors) de l’immunité innée."
    },
    {
        "id": "q-3",
        "subjectId": "sub-8",
        "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2026,
        "difficulty": "Moyen",
        "tags": ["Enzymes", "Biochimie"],
        "statement": "Quel est l’effet d’un catalyseur enzymatique sur l’énergie d’activation d’une réaction ?",
        "answers": [
            { "id": "a", "text": "Il augmente l’énergie d’activation", "correct": False },
            { "id": "b", "text": "Il diminue l’énergie d’activation", "correct": True },
            { "id": "c", "text": "Il n’a aucun effet sur l’énergie d’activation", "correct": False },
            { "id": "d", "text": "Il supprime totalement l’énergie libre de Gibbs", "correct": False }
        ],
        "explanation": "Les enzymes accélèrent les réactions chimiques en abaissant l’énergie d’activation nécessaire."
    },
    {
        "id": "q-annale-1", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Facile", "tags": ["Enzymes", "Structure"],
        "statement": "Concernant les propositions suivantes indiquez celles qui sont justes : (Question n°1)",
        "answers": [
            { "id": "a", "text": "Les enzymes sont des glucides.", "correct": False },
            { "id": "b", "text": "Les enzymes sont des protéines.", "correct": True },
            { "id": "c", "text": "Les enzymes présentent toutes une structure primaire, secondaire, tertiaire et quaternaire.", "correct": False },
            { "id": "d", "text": "Les enzymes présentent toutes une structure primaire, secondaire et tertiaire mais certaines enzymes ne sont pas concernées par la structure quaternaire.", "correct": True },
            { "id": "e", "text": "Les enzymes catalysent des réactions chimiques.", "correct": True }
        ], "explanation": "B, D, E vrais. Les enzymes sont de nature protéique (sauf ribozymes), et n'ont pas toutes une structure quaternaire."
    },
    {
        "id": "q-annale-2", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Holoenzyme", "Cofacteur"],
        "statement": "Concernant les propositions suivantes indiquez celles qui sont justes : (Question n°2)",
        "answers": [
            { "id": "a", "text": "L’apoenzyme est la partie protéique inactive de l’enzyme.", "correct": True },
            { "id": "b", "text": "L’holoenzyme est la partie protéique active de l’enzyme.", "correct": False },
            { "id": "c", "text": "Les cofacteurs sont des composés chimiques non protéique nécessaire à l’activité de la protéine.", "correct": True },
            { "id": "d", "text": "L’apoenzyme est la partie éthylique de l’enzyme.", "correct": False },
            { "id": "e", "text": "L’holoenzyme est une sous unité sans le site catalytique de l’enzyme.", "correct": False }
        ], "explanation": "A, C vrais. L'holoenzyme correspond à la forme active de l'enzyme (apoenzyme + cofacteur)."
    },
    {
        "id": "q-annale-3", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Thermodynamique", "Réactifs"],
        "statement": "Concernant les propositions suivantes indiquez celles qui sont justes : (Question n°3)",
        "answers": [
            { "id": "a", "text": "A la fin d’une réaction chimique, les réactifs sont transformés en substrat.", "correct": False },
            { "id": "b", "text": "A la fin d’une réaction chimique, les réactifs sont transformés en produits.", "correct": True },
            { "id": "c", "text": "Afin qu'une réaction chimique puisse se dérouler, les molécules de réactifs doivent entrer en collision", "correct": True },
            { "id": "d", "text": "L’énergie d’activation est l’énergie nécessaire pour initier le réarrangement des forces d'attraction entre les atomes des réactifs.", "correct": True },
            { "id": "e", "text": "L’énergie d’activation ne peut pas être représenté par un graphique.", "correct": False }
        ], "explanation": "B, C, D vrais. Les réactifs se transforment en produits, nécessitant collision et énergie d'activation."
    },
    {
        "id": "q-annale-4", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Facile", "tags": ["Catalyseur"],
        "statement": "Concernant les propositions suivantes indiquez celles qui sont justes : (Question n°4)",
        "answers": [
            { "id": "a", "text": "Un catalyseur chimique est une espèce qui augmente la vitesse d’une réaction chimique.", "correct": True },
            { "id": "b", "text": "Un catalyseur chimique est modifié à la fin d’une réaction chimique.", "correct": False },
            { "id": "c", "text": "Un catalyseur chimique n’est pas modifié à la fin d’une réaction chimique.", "correct": True },
            { "id": "d", "text": "Un catalyseur chimique n’a aucun impact sur une réaction chimique.", "correct": False },
            { "id": "e", "text": "Une enzyme est un catalyseur chimique.", "correct": True }
        ], "explanation": "A, C, E vrais. Un catalyseur augmente la vitesse sans être modifié en fin de réaction."
    },
    {
        "id": "q-annale-5", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Facile", "tags": ["Spécificité"],
        "statement": "Concernant les propositions suivantes indiquez celles qui sont justes : (Question n°5)",
        "answers": [
            { "id": "a", "text": "Les enzymes sont spécifiques de la réaction qu’elles catalysent.", "correct": True },
            { "id": "b", "text": "Les enzymes ne sont pas spécifiques de la réaction qu’elles catalysent.", "correct": False },
            { "id": "c", "text": "Les enzymes sont spécifiques d’un substrat donné.", "correct": True },
            { "id": "d", "text": "Les enzymes ne sont pas spécifiques d’un substrat donné.", "correct": False },
            { "id": "e", "text": "Le nom de l’enzyme indique souvent la nature du substrat que lequel elle agit.", "correct": True }
        ], "explanation": "A, C, E vrais. Les enzymes ont une double spécificité de réaction et de substrat."
    },
    {
        "id": "q-annale-6", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Cinétique", "Allostérie"],
        "statement": "Concernant les propositions suivantes indiquez celles qui sont justes : (Question n°6)",
        "answers": [
            { "id": "a", "text": "La cinétique enzymatique c’est l’évolution de la vitesse de catalyse de l’enzyme pour une réaction donnée, au cours du temps.", "correct": True },
            { "id": "b", "text": "Les enzymes de type « Michaeliennes » sont des enzymes simples.", "correct": True },
            { "id": "c", "text": "Les enzymes de type « Michaeliennes » sont des enzymes qui possèdent plusieurs sites actifs par molécule.", "correct": False },
            { "id": "d", "text": "Les enzymes de type « allostériques » sont des enzymes qui ne possèdent jamais plusieurs sites actifs par molécule.", "correct": False },
            { "id": "e", "text": "La cinétique des enzymes Michaeliennes peuvent être d’ordre 1 ou d’ordre 0.", "correct": True }
        ], "explanation": "A, B, E vrais. Les enzymes allostériques possèdent généralement plusieurs sites actifs avec coopérativité."
    },
    {
        "id": "q-annale-7", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Enthalpie", "Graphique"],
        "image": { "url": "src/assets/annale/q7_enthalpie.png" },
        "statement": "Sur cette représentation graphique du niveau d’enthalpie en fonction de la progression d’une réaction chimique, dites si les propositions suivantes sont vraies ou fausses : (Question n°7)",
        "answers": [
            { "id": "a", "text": "La flèche 1 représente l’énergie d’activation", "correct": True },
            { "id": "b", "text": "La flèche 2 représente l’énergie d’activation", "correct": False },
            { "id": "c", "text": "Cette réaction est une réaction exothermique", "correct": True },
            { "id": "d", "text": "La transformation du substrat en produit a libéré de l’énergie", "correct": True },
            { "id": "e", "text": "La présence d’une enzyme réduirait l’énergie représentée par la flèche 2 (la flèche réduirait de taille)", "correct": False }
        ], "explanation": "A, C, D vrais. La flèche 1 est l'énergie d'activation. La flèche 2 (ΔH) est négative, donc exothermique."
    },
    {
        "id": "q-annale-8", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Enthalpie", "Thermodynamique"],
        "statement": "Concernant les réactions endo- et exothermiques, dites si les propositions suivantes sont vraies ou fausses : (Question n°8)",
        "answers": [
            { "id": "a", "text": "La variation d’enthalpie correspond à l’énergie absorbée ou dégagée lors d’une réaction chimique", "correct": True },
            { "id": "b", "text": "Une réaction endothermique dans un sens, sera nécessairement exothermique dans l’autre sens", "correct": True },
            { "id": "c", "text": "Si une réaction chimique est caractérisée par une enthalpie de réactif HR = 25 KJ.mol-1 et une enthalpie de produit HP = -15 KJ.mol-1, alors la réaction chimique est endothermique", "correct": False },
            { "id": "d", "text": "Si une réaction chimique est caractérisée par une enthalpie de réactif HR = 25 KJ.mol-1 et une enthalpie de produit HP = -15 KJ.mol-1, alors la réaction chimique est exothermique", "correct": True },
            { "id": "e", "text": "La variation de l’enthalpie ΔH influence le caractère spontané ou non spontané d’une réaction", "correct": True }
        ], "explanation": "A, B, D, E vrais. ΔH = HP - HR = -15 - 25 = -40 kJ/mol < 0, donc réaction exothermique."
    },
    {
        "id": "q-annale-9", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Endergonique", "Exergonique"],
        "statement": "Concernant les réactions endergoniques et exergoniques, quelle(s) proposition(s) est(sont) vraie(s) : (Question n°9)",
        "answers": [
            { "id": "a", "text": "Une réaction à l’équilibre se caractérise par une variation d’enthalpie ΔH =0", "correct": False },
            { "id": "b", "text": "Une réaction exergonique est non spontanée", "correct": False },
            { "id": "c", "text": "Une réaction endergonique est spontanée", "correct": False },
            { "id": "d", "text": "Une enzyme n’influence pas la valeur d’enthalpie libre de Gibbs ΔG d’une réaction", "correct": True },
            { "id": "e", "text": "Théoriquement, une réaction chimique endergonique serait forcément endothermique si elle était réalisé à une température de T=0 Kelvin", "correct": True }
        ], "explanation": "D, E vrais. À l'équilibre ΔG = 0 (pas ΔH). L'enzyme n'influence pas le ΔG."
    },
    {
        "id": "q-annale-10", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Gibbs", "Enthalpie Libre"],
        "statement": "Dans des conditions physiologiques, on utilise la formule de Gibbs suivante : ΔG’= ΔG’0 +RT ln(Kω), où ΔG’ correspond à la variation d’enthalpie libre du système, ΔG’0 la variation de l’enthalpie libre standard, R la constante de gaz parfait, T la température et Kω la constante de Gibbs. Parmi ces propositions, quelle(s) est(sont) celle(s) qui est(sont) juste(s) : (Question n°10)",
        "answers": [
            { "id": "a", "text": "La constante de Gibbs Kω est équivalente à la constante d’équilibre de la réaction chimique", "correct": True },
            { "id": "b", "text": "L’enthalpie libre standard ΔG’0 correspond à l’enthalpie libre que l’on détermine dans des conditions in vitro", "correct": True },
            { "id": "c", "text": "La valeur de ΔG’0 permet de dire si la réaction chimique est endo/exothermique", "correct": False },
            { "id": "d", "text": "La valeur d’enthalpie libre du système ΔG’ permet de dire si la réaction chimique est ender/exergonique", "correct": False },
            { "id": "e", "text": "Une réaction chimique réversible aura une valeur d’enthalpie libre standard ΔG’0 proche de 0", "correct": True }
        ], "explanation": "A, B, E vrais. ΔG'0 permet de définir ender/exergonique (pas endo/exothermique). ΔG' est mesuré in vivo."
    },
    {
        "id": "q-annale-11a", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["PGM", "Thermodynamique"],
        "image": { "url": "src/assets/annale/q11_pgm.png" },
        "statement": "La phosphoglucomutase (PGM) est une isomérase permettant l’interconversion du glucose-1-phosphate (G1P) en glucose-6-phosphate (G6P). On mesure expérimentalement l’enthalpie ΔG’0 = -7.6 kJ.mol-1 de cette réaction. Dire si les affirmations suivantes sont vraies ou fausses : (Question n°11-A)",
        "answers": [
            { "id": "a", "text": "Avec les données à votre disposition, on peut dire que la réaction est endothermique", "correct": False },
            { "id": "b", "text": "Avec les données à votre disposition, on peut dire que la réaction est exothermique", "correct": False },
            { "id": "c", "text": "Avec les données à votre disposition, on peut dire que la réaction est réversible", "correct": False },
            { "id": "d", "text": "Avec les données à votre disposition, on peut dire que la réaction est exergonique", "correct": True },
            { "id": "e", "text": "Sans la PGM, la valeur de l’enthalpie ΔG’0 serait plus petite", "correct": False }
        ], "explanation": "D vrai. ΔG'0 = -7.6 < 0 donc la réaction est exergonique."
    },
    {
        "id": "q-annale-11b", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["PGM", "Calculs"],
        "statement": "Pour la réaction catalysée par la PGM, on détermine que la concentration cellulaire de [G1P] = 2.0.10-4 mol.L-1 et [G6P]= 5.0.10-1 mol.L-1. Dans ces conditions, quelle(s) proposition(s) est(sont) juste(s). (ΔG’= ΔG’0 +RT ln(Kω) et RT = 2.6 KJ.mol-1 et ΔG’0= -7.6 kJ.mol-1 ) (Question n°11-B)",
        "answers": [
            { "id": "a", "text": "Avec les données à votre disposition, on peut dire que la réaction est endothermique", "correct": True },
            { "id": "b", "text": "Avec les données à votre disposition, on peut dire que la réaction est exothermique", "correct": False },
            { "id": "c", "text": "Avec les données à votre disposition, on peut dire que la réaction chimique produit de l’énergie", "correct": False },
            { "id": "d", "text": "Avec les données à votre disposition, on peut dire que la réaction chimique absorbe de l’énergie", "correct": True },
            { "id": "e", "text": "Avec les données à votre disposition, on peut dire que la réaction est en faveur de la formation de produit", "correct": True }
        ], "explanation": "A, D, E vrais. ΔG' = -7.6 + 2.6 ln(5e-1 / 2e-4) = 12.74 kJ.mol-1 > 0, donc la réaction absorbe de l'énergie (endothermique) et Kω = 2500 favorise la formation de produit."
    },
    {
        "id": "q-annale-12", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Facile", "tags": ["Nomenclature", "EC"],
        "image": { "url": "src/assets/annale/q12_nomenclature.png" },
        "statement": "Concernant la nomenclature et les différentes classes d’enzyme, quelle(s) proposition(s) est(sont) vraie(s) : (Question n°12)",
        "answers": [
            { "id": "a", "text": "Les hydrolases et les lyases catalysent des coupures de liaison chimique", "correct": True },
            { "id": "b", "text": "Une enzyme de nomenclature EC.2.7.3.2 est une oxydoréductase", "correct": False },
            { "id": "c", "text": "La classe 7 correspond au enzyme de type translocase", "correct": True },
            { "id": "d", "text": "Les isomérases ont une nomenclature qui commence par EC.5, et elles catalysent la formation de liaison covalente entre deux molécules", "correct": False },
            { "id": "e", "text": "Le deuxième numéro de la nomenclature (EC.X.X.X.X) définit le mécanisme d’action de l’enzyme", "correct": True }
        ], "explanation": "A, C, E vrais. EC.2 est transférase. Les isomérases catalysent l'isomérisation, pas la formation de liaisons entre 2 molécules."
    },
    {
        "id": "q-annale-13", "subjectId": "sub-8", "chapter": "Fiche n°2 - Caractères généraux des enzymes.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Nomenclature", "Transcétolase"],
        "image": { "url": "src/assets/annale/q13_transcetolase.png" },
        "statement": "La transcétolase est une enzyme de nomenclature EC.2.2.1.1 impliquée dans la voie des pentoses-phosphate. Son activité nécessite du thiamine pyrophosphate (TPP), molécule dérivée de la vitamine B1. Parmi les propositions suivantes, quelles sont les affirmations justes: (Question n°13)",
        "answers": [
            { "id": "a", "text": "La transcétolase est une translocase", "correct": False },
            { "id": "b", "text": "La transcétolase est une transférase", "correct": True },
            { "id": "c", "text": "X-5-P, E-4-P et TPP sont les substrats de la réaction", "correct": False },
            { "id": "d", "text": "La transcétolase n’utilise pas de cofacteur", "correct": False },
            { "id": "e", "text": "TPP est un groupement prosthétique", "correct": True }
        ], "explanation": "B, E vrais. EC.2 indique transférase. TPP est un cofacteur/groupement prosthétique dérivé de la vitamine B1."
    },
    {
        "id": "q-annale-14", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Michaelienne", "Km"],
        "statement": "Concernant les enzymes michaelienne et leur cinétique, quel(s) item(s) est(sont) exacte(s) : (Question n°14)",
        "answers": [
            { "id": "a", "text": "La formation du complexe ES est stabilisée par des liaisons de faible énergie", "correct": True },
            { "id": "b", "text": "La constante catalytique KCAT correspond à la constante d’équilibre de la réaction ES <-> E+P", "correct": False },
            { "id": "c", "text": "La constante de Michaëlis KM est inversement proportionnelle à l’affinité de l’enzyme pour son substrat", "correct": True },
            { "id": "d", "text": "La vitesse de la réaction chimique est dépendante de la concentration en substrat quand la vitesse Vmax est atteinte", "correct": False },
            { "id": "e", "text": "La vitesse de la réaction chimique correspond à la vitesse d’apparition du produit", "correct": True }
        ], "explanation": "A, C, E vrais. Kcat est une fréquence de conversion. A Vmax, la vitesse est d'ordre 0 (indépendante du substrat)."
    },
    {
        "id": "q-annale-15", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Michaelis-Menten", "Vmax"],
        "statement": "Concernant l’équation de Michaelis-Menten, quelle(s) affirmation(s) est(sont) fausse(s) : (Question n°15)",
        "answers": [
            { "id": "a", "text": "L’état quasi-stationnaire est défini par une vitesse d’association et de dissociation du complexe ES équivalente", "correct": False },
            { "id": "b", "text": "La vitesse initiale de la réaction se détermine par la relation suivante V0=KCAT.[E0]", "correct": True },
            { "id": "c", "text": "La vitesse initiale de la réaction se détermine par la relation suivante V0= (Vmax.[S]) / (KM + [S])", "correct": False },
            { "id": "d", "text": "On doit se placer dans des concentrations saturantes de substrat pour vérifier l’équation de Michaelis-Menten", "correct": True },
            { "id": "e", "text": "La Vmax est atteinte quand l’enzyme est complètement saturée par son substrat", "correct": False }
        ], "explanation": "B, D sont fausses. V0 = Kcat.[ES] (la formule avec E0 donne Vmax). Pour vérifier l'équation, on se place en excès de substrat (pas uniquement saturantes)."
    },
    {
        "id": "q-annale-16", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Inhibiteurs", "Compétitif"],
        "statement": "Concernant les inhibiteurs et leurs effets sur la cinétique enzymatique, quelle(s) affirmation(s) est(sont) vrai(s) : (Question n°16)",
        "answers": [
            { "id": "a", "text": "Un inhibiteur compétitif modifie uniquement la Vmax", "correct": False },
            { "id": "b", "text": "Un inhibiteur incompétitif modifie uniquement le KM", "correct": False },
            { "id": "c", "text": "Seuls les inhibiteurs incompétitifs et non compétitifs peuvent se fixer sur le complexe ES", "correct": True },
            { "id": "d", "text": "Seuls les inhibiteurs incompétitifs et non compétitifs modifient la Vmax de la réaction", "correct": True },
            { "id": "e", "text": "Un inhibiteur non compétitif peut se fixer sur l’enzyme libre, mais sur un site distinct du site catalytique", "correct": True }
        ], "explanation": "C, D, E vrais. Le compétitif modifie KM. L'incompétitif modifie KM et Vmax. Le non-compétitif modifie Vmax."
    },
    {
        "id": "q-annale-17a", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Dandadan", "Kcat"],
        "image": { "url": "src/assets/annale/q17a_dandadan.png" },
        "statement": "Dans votre laboratoire de recherche, vous étudiez une enzyme de procaryote encore jamais décrite, nommée «Dandadan ». Vous savez que l’enzyme a pour substrat le pyruvate, et vous décidez de mesurer ces propriétés catalytique, avec une concentration totale d’enzyme [Dandadan0] =5,0.10-1 mmol.L-1. Vous obtenez la courbe ci-dessous. Parmi ces différentes affirmations, lesquelles sont justes : (Question n°17-A)",
        "answers": [
            { "id": "a", "text": "Une mole d’enzyme «Dandadan » va catalyser 60 fois la réaction en une minute", "correct": False },
            { "id": "b", "text": "Une mole d’enzyme «Dandadan » va catalyser 120 fois la réaction en une minute", "correct": True },
            { "id": "c", "text": "Pour une concentration [Pyruvate] = 0.2 mmol.L-1, la vitesse de la réaction est de V0 =15 mmol.L-1.min-1", "correct": False },
            { "id": "d", "text": "A cette vitesse de réaction (V0 =15 mmol.L-1.min-1), la concentration de complexe ES est de [ES] = 1,5.10-1 mmol.L-1", "correct": False },
            { "id": "e", "text": "A cette vitesse de réaction (V0 =15 mmol.L-1.min-1), la concentration en enzyme libre est de [E] = 3.75.10-1 mmol.L-1", "correct": True }
        ], "explanation": "B, E vrais. Kcat = Vmax/[E0] = 60 / 0.5 = 120 min-1. Pour V0=15, [ES] = 15/120 = 0.125. Donc [E] = 0.5 - 0.125 = 0.375 mmol.L-1."
    },
    {
        "id": "q-annale-17b", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Berserk", "Inhibition"],
        "image": { "url": "src/assets/annale/q17b_berserk.png" },
        "statement": "Chez les procaryotes, il a été rapporté qu’une molécule appelée « Berserk » interagissait avec l’enzyme « Dandadan ». Vous décidez de caractériser l’effet de cette molécule sur la cinétique catalytique de l’enzyme. Vous obtenez la courbe cinétique ci-dessous (courbe bleue). Que pouvez-vous conclure sur le caractère de la molécule « Berserk ». (Question n°17-B)",
        "answers": [
            { "id": "a", "text": "« Berserk » est un inhibiteur compétitif", "correct": False },
            { "id": "b", "text": "« Berserk » est un inhibiteur non compétitif", "correct": True },
            { "id": "c", "text": "« Berserk » est un inhibiteur incompétitif", "correct": False },
            { "id": "d", "text": "« Berserk » interagit uniquement avec le complexe ES", "correct": False },
            { "id": "e", "text": "« Berserk » interagit uniquement avec l’enzyme libre", "correct": False }
        ], "explanation": "B vrai. La Vmax diminue sans modifier le Km, c'est le profil typique d'un inhibiteur non compétitif."
    },
    {
        "id": "q-annale-17c", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Lineweaver-Burk", "Evangelion"],
        "image": { "url": "src/assets/annale/q17c_lineweaver.png" },
        "statement": "Une autre équipe de recherche travaille également sur l’enzyme « Dandadan ». Elle a identifié un autre effecteur, « Evangelion », qui semble agir comme un inhibiteur de « Dandadan ». Vous décidez de collaborer avec cette équipe, et d’envoyer un échantillon de votre inhibiteur. Vous recevez par mail les résultats d’analyses, mais la courbe est mal annotée. Que pouvez-vous conclure ? (Question n°17-C)",
        "answers": [
            { "id": "a", "text": "Le point « A » correspond à -1/KM", "correct": True },
            { "id": "b", "text": "La pente jaune « Modulateur 1 » a le profil d’un inhibiteur non compétitif : il s’agit de l’inhibiteur « Berserk »", "correct": True },
            { "id": "c", "text": "La pente violette « Modulateur 2 » a le profil d’un inhibiteur incompétitif : il s’agit de l’inhibiteur « Berserk »", "correct": False },
            { "id": "d", "text": "L’inhibiteur « Evangelion » peut se fixer uniquement sur le complexe ES", "correct": True },
            { "id": "e", "text": "L’inhibiteur « Evangelion » peut se fixer sur le site catalytique de l’enzyme", "correct": False }
        ], "explanation": "A, B, D vrais. La droite violette (parallèle) correspond à un inhibiteur incompétitif (Evangelion) qui se fixe uniquement sur le complexe ES."
    },
    {
        "id": "q-annale-17d", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Inhibition", "Stœchiométrie"],
        "image": { "url": "src/assets/annale/q17d_inhibiteurs.png" },
        "statement": "Vous décidez d’évaluer plus précisément l’action de ces inhibiteurs, en mesurant l’activité catalytique de l’enzyme Dandadan en fonction de concentrations croissantes d’inhibiteurs. Vous vous placez dans des conditions de concentration de substrat où Vi = Vmax , avec [Dandadan] =3.5 mmol.L-1 . Vous obtenez les deux courbes suivantes. Que pouvez-vous en conclure ? (Question n°17-D)",
        "answers": [
            { "id": "a", "text": "En présence des inhibiteurs, on observe un arrêt de l’activité catalytique dans les deux cas", "correct": True },
            { "id": "b", "text": "Il faut une molécule de « Berserk » pour inhiber une molécule d’enzyme « Dandadan »", "correct": True },
            { "id": "c", "text": "Il faut trois molécules de « Evangelion » pour inhiber une molécule d’enzyme « Dandadan »", "correct": False },
            { "id": "d", "text": "Avec ces données, il est possible de conclure que « Berserk » a une plus grande affinité pour l’enzyme que l’inhibiteur « Evangelion »", "correct": False },
            { "id": "e", "text": "Avec ces données, on peut dire que les inhibitions de « Berserk » et de « Evangelion » sont réversibles", "correct": False }
        ], "explanation": "A, B vrais. Ratio [Berserk]/[Enzyme] = 3.5/3.5 = 1 pour arrêt total. Pour Evangelion 6.0/3.5 = 1.7 (moins de 2 molécules)."
    },
    {
        "id": "q-annale-17e", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Réversibilité", "Liaisons"],
        "image": { "url": "src/assets/annale/q17e_reversible.png" },
        "statement": "Finalement, vous décidez d’évaluer le caractère réversible/irréversible de l’inhibition de « Berserk » et « Evangelion ». Pour ce faire, vous purifiez l’enzyme ayant été en contact avec ces inhibiteurs et tentez d’observer s’il y a un retour de l’activité catalytique après avoir incubé l’enzyme avec une concentration de substrat où Vi = Vmax. Que pouvez-vous en conclure ? (Question n°17-E)",
        "answers": [
            { "id": "a", "text": "L’inhibition de « Berserk » est réversible", "correct": True },
            { "id": "b", "text": "L’inhibition de « Berserk » est irréversible", "correct": False },
            { "id": "c", "text": "L’inhibition de « Evangelion » est réversible", "correct": False },
            { "id": "d", "text": "La liaison de « Berserk » avec l’enzyme est une liaison non covalente", "correct": True },
            { "id": "e", "text": "La liaison de « Evangelion » avec l’enzyme est une liaison covalente", "correct": True }
        ], "explanation": "A, D, E vrais. Retour de l'activité pour Berserk = réversible (liaison non covalente). Pas de retour pour Evangelion = irréversible (liaison covalente)."
    },
    {
        "id": "q-annale-18", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Allostérie", "Conformation"],
        "statement": "Concernant les enzymes allostériques, quelle(s) proposition(s) est(sont) juste(s) ? (Question n°18)",
        "answers": [
            { "id": "a", "text": "Les enzymes allostériques ne peuvent jamais se comporter comme les enzymes michaeliennes", "correct": False },
            { "id": "b", "text": "La constante K0.5 est l’équivalent du KM pour les enzymes michaeliennes", "correct": True },
            { "id": "c", "text": "Une enzyme allostérique avec ses sous-unités en conformation tendue T a une grande affinité pour son substrat", "correct": False },
            { "id": "d", "text": "L’effet homotrope ne concerne que le substrat d’une enzyme allostérique", "correct": False },
            { "id": "e", "text": "Un activateur allostérique a un effet hétérotope positif et va faciliter le passage de la conformation R à T", "correct": False }
        ], "explanation": "B vrai. K0.5 est l'équivalent du Km. C'est la conformation relâchée R qui a une forte affinité pour le substrat."
    },
    {
        "id": "q-annale-19a", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Hexokinase", "ATP"],
        "image": { "url": "src/assets/annale/q19a_hexokinase.png" },
        "statement": "L’hexokinase est une enzyme allostérique catalysant la phosphorylation du glucose en glucose-6-phosphate. Vous décidez d’étudier la cinétique enzymatique de cette enzyme en présence d’ATP. Vous obtenez la courbe suivante. Parmi les propositions suivantes, quelles sont celles qui sont justes ? (Question n°19-A)",
        "answers": [
            { "id": "a", "text": "L’ATP est un activateur allostérique", "correct": True },
            { "id": "b", "text": "L’ATP augmente le K0.5, il augmente donc l’affinité de l’enzyme pour son substrat", "correct": False },
            { "id": "c", "text": "L’ATP exerce un effet hétérotrope positif", "correct": True },
            { "id": "d", "text": "L’ATP exerce un effet homotrope positif", "correct": False },
            { "id": "e", "text": "Le K0.5 de l’hexokinase est de K0.5 = 0.3 mmol.L-1 : cela représente la quantité de substrat nécessaire pour que la vitesse de la réaction soit équivalente à la moitié de la vitesse maximale", "correct": True }
        ], "explanation": "A, C, E vrais. L'ATP déplace la sigmoïde vers la gauche (diminue K0.5), augmentant l'affinité pour le substrat (effet hétérotrope positif)."
    },
    {
        "id": "q-annale-19b", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Moyen", "tags": ["Glucose-6-phosphate", "Inhibition"],
        "image": { "url": "src/assets/annale/q19b_g6p.png" },
        "statement": "Pour certaines enzymes, les réactifs/produits peuvent exercer un rôle de modulateurs allostériques. Vous décidez de tester cette hypothèse pour l’hexokinase, en étudiant la cinétique enzymatique en présence de Glucose-6-phosphate. Vous obtenez la courbe suivante. Parmi les propositions suivantes, quelles sont celles qui sont justes ? (Question n°19-B)",
        "answers": [
            { "id": "a", "text": "Le glucose-6-phosphate est un activateur allostérique", "correct": False },
            { "id": "b", "text": "Le glucose-6-phosphate est un inhibiteur allostérique", "correct": True },
            { "id": "c", "text": "Le glucose-6-phosphate est un inhibiteur allostérique incompétitif", "correct": False },
            { "id": "d", "text": "Le glucose-6-phosphate interagit avec le site catalytique de l’enzyme", "correct": False },
            { "id": "e", "text": "Le glucose-6-phosphate exerce un effet homotrope négatif", "correct": False }
        ], "explanation": "B vrai. Le G6P augmente le K0.5 de l'enzyme (inhibiteur allostérique à effet hétérotrope négatif)."
    },
    {
        "id": "q-annale-19c", "subjectId": "sub-8", "chapter": "Fiche n°3 - Cinétique enzymatique.pdf",
        "year": 2025, "difficulty": "Difficile", "tags": ["Hill", "Coopérativité"],
        "image": { "url": "src/assets/annale/q19c_hill.png" },
        "statement": "Finalement, vous décidez d’identifier précisément les mécanismes de coopérativité de l’ATP et du glucose-6-phosphate. Vous obtenez les représentations de Hill suivantes. (Les coordonnées de 4 points notés A,B,C et D sont indiquées sur le graphique) Parmi les propositions, quelles sont celles qui sont justes ? (Question n°19-C)",
        "answers": [
            { "id": "a", "text": "L’ATP est un activateur allostérique coopératif", "correct": True },
            { "id": "b", "text": "La fixation de l’ATP sur son site allostérique favorise la fixation de l’ATP sur les autres sites allostériques du même type", "correct": True },
            { "id": "c", "text": "Le glucose-6-phosphate est un inhibiteur allostérique compétitif et anti-coopératif", "correct": False },
            { "id": "d", "text": "Le glucose-6-phosphate est un inhibiteur allostérique compétitif et coopératif", "correct": False },
            { "id": "e", "text": "La fixation du glucose-6-phosphate sur son site allostérique n’a aucun effet sur la fixation du glucose-6-phosphate sur les autres sites allostériques du même type", "correct": True }
        ], "explanation": "A, B, E vrais. Pente m=1.5 > 1 pour l'ATP (coopératif). Pente m'=1 pour le G6P (pas d'effet coopératif)."
    }
]

import re

# Formatted JS string for INITIAL_QUESTIONS
js_code = "const INITIAL_QUESTIONS = " + json.dumps(complete_questions, ensure_ascii=False, indent=4) + ";"
js_export = "export const INITIAL_QUESTIONS = " + json.dumps(complete_questions, ensure_ascii=False, indent=4) + ";"

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'const INITIAL_QUESTIONS = \[.*?\];', js_code, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with all 24 questions!")

# 2. Update mockData.js
with open('src/data/mockData.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = re.sub(r'export const INITIAL_QUESTIONS = \[.*?\];', js_export, js, flags=re.DOTALL)

with open('src/data/mockData.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated mockData.js with all 24 questions!")
