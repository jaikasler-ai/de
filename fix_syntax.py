for filename in ['index.html', 'src/data/mockData.js']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixed_content = content.replace("png' } },", "png' },")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f'Fixed {filename}')
