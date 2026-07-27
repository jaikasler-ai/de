with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix unescaped single quotes inside JS single-quoted strings
content = content.replace("'J0 (Aujourd'hui)'", '"J0 (Aujourd\'hui)"')
content = content.replace("'Aujourd'hui'", '"Aujourd\'hui"')
content = content.replace("Aujourd'hui", "Aujourd’hui") # Use right single quotation mark / apostrophe to avoid any JS string breaks

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed apostrophes in index.html!")
