import re

new_chapters_js = """[
                    'Fiche n°1 - Techniques radiologiques, Ultrasons.pdf',
                    'Fiche n°2 - Produits de contraste ultrasonores.pdf',
                    'Fiche n°3 - La scintigraphie.pdf',
                    'Fiche n°4 - La tomographie par émission de positons.pdf',
                    'Fiche n°5 - Scanner.pdf',
                    'Fiche n°6 - IRM.pdf',
                    'Fiche n°7 - Radioprotection.pdf',
                    'Fiche n°8 - Rayons X et Radiographie.pdf',
                    'Fiche n°9 - Radiologie interventionnelle.pdf',
                    'Fiche n°10 - Influx Nerveux.pdf',
                    'Fiche n°11 - Explorations Fonctionnelles Respiratoires.pdf'
                ]"""

def replace_ue4_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = r"(id:\s*'sub-5',.*?chapters:\s*)\[[^\]]*\]"
    new_content = re.sub(pattern, r"\1" + new_chapters_js, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Replaced UE4 chapters in {filepath}")

replace_ue4_in_file('index.html')
replace_ue4_in_file('src/data/mockData.js')
