import re
import json

new_ue4_chapters = [
    "Fiche n°1 - Techniques radiologiques, Ultrasons.pdf",
    "Fiche n°2 - Produits de contraste ultrasonores.pdf",
    "Fiche n°3 - La scintigraphie.pdf",
    "Fiche n°4 - La tomographie par émission de positons.pdf",
    "Fiche n°5 - Scanner.pdf",
    "Fiche n°6 - IRM.pdf",
    "Fiche n°7 - Radioprotection.pdf",
    "Fiche n°8 - Rayons X et Radiographie.pdf",
    "Fiche n°9 - Radiologie interventionnelle.pdf",
    "Fiche n°10 - Influx Nerveux.pdf",
    "Fiche n°11 - Explorations Fonctionnelles Respiratoires.pdf"
]

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Locate sub-5 inside INITIAL_SUBJECTS
    # We replace chapters for sub-5 with the new_ue4_chapters list
    pattern = r"(\{\s*id:\s*'sub-5',\s*name:\s*'UE 4 - Biophysique'.*?chapters:\s*\[).*?(\]\s*\})"
    
    formatted_chapters = json.dumps(new_ue4_chapters, ensure_ascii=False, indent=20)
    # adjust formatting
    formatted_chapters_str = json.dumps(new_ue4_chapters, ensure_ascii=False)
    
    # Let's cleanly replace sub-5 object
    def replace_sub5(m):
        prefix = m.group(1)
        suffix = m.group(2)
        ch_str = "[\n" + ",\n".join([f"                    '{c}'" for c in new_ue4_chapters]) + "\n                ]"
        return f"{{ \n                id: 'sub-5', \n                name: 'UE 4 - Biophysique', \n                code: 'UE4', \n                icon: '⚛️', \n                color: 'from-indigo-500 to-purple-600', \n                progress: 70, \n                qcmCount: 175, \n                chapters: {ch_str}\n            }}"

    new_content = re.sub(
        r"\{\s*id:\s*'sub-5'.*?chapters:\s*\[.*?\]\s*\}",
        replace_sub5,
        content,
        flags=re.DOTALL
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filename} successfully!")

update_file('index.html')
update_file('src/data/mockData.js')
