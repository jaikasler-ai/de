import re

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = [
        (r"image:\s*\{\s*url:\s*'annale\.pdf',\s*page:\s*5,.*?\}", "image: { url: 'src/assets/annale/q7_enthalpie.png' }"),
        (r"image:\s*\{\s*url:\s*'annale\.pdf',\s*page:\s*7,.*?\}", "image: { url: 'src/assets/annale/q11_pgm.png' }"),
        (r"image:\s*\{\s*url:\s*'annale\.pdf',\s*page:\s*8,.*?\}", "image: { url: 'src/assets/annale/q12_nomenclature.png' }"),
        (r"image:\s*\{\s*url:\s*'annale\.pdf',\s*page:\s*9,.*?\}", "image: { url: 'src/assets/annale/q13_transcetolase.png' }"),
        (r"image:\s*\{\s*url:\s*'annale\.pdf',\s*page:\s*11,.*?\}", "image: { url: 'src/assets/annale/q17a_dandadan.png' }"),
        (r"image:\s*\{\s*url:\s*'annale\.pdf',\s*page:\s*12,.*?\}", "image: { url: 'src/assets/annale/q17b_berserk.png' }"),
        (r"image:\s*\{\s*url:\s*'annale\.pdf',\s*page:\s*13,.*?\}", "image: { url: 'src/assets/annale/q17c_lineweaver.png' }"),
        (r"image:\s*\{\s*url:\s*'annale\.pdf',\s*page:\s*16,.*?\}", "image: { url: 'src/assets/annale/q19a_hexokinase.png' }"),
        (r"image:\s*\{\s*url:\s*'annale\.pdf',\s*page:\s*18,.*?\}", "image: { url: 'src/assets/annale/q19c_hill.png' }"),
    ]

    for pat, rep in replacements:
        content = re.sub(pat, rep, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename}")

update_file("index.html")
update_file("src/data/mockData.js")
