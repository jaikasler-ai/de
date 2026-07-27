import re

def update_autosync_in_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    sync_code = """
            // Sync automatique en arrière-plan avec le serveur (PC <-> Téléphone)
            React.useEffect(() => {
                fetch('/api/load')
                    .then(res => res.json())
                    .then(data => {
                        if (data && Object.keys(data).length > 0) {
                            setAncrageData(prev => {
                                const merged = { ...prev, ...data };
                                try {
                                    localStorage.setItem('med_prep_ancrage_data_v1', JSON.stringify(merged));
                                } catch(e) {}
                                return merged;
                            });
                        }
                    })
                    .catch(e => console.log("Mode hors-ligne"));
            }, []);

            React.useEffect(() => {
                if (Object.keys(ancrageData).length > 0) {
                    fetch('/api/save', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(ancrageData)
                    }).catch(e => {});
                }
            }, [ancrageData]);
"""
    
    target_pattern = r"(localStorage\.setItem\('med_prep_ancrage_data_v1',\s*JSON\.stringify\(ancrageData\)\);\s*\}\s*catch\(e\)\s*\{\s*console\.error\(\"Erreur sauvegarde LocalStorage Ancrage:\",\s*e\);\s*\}\s*\},?\s*\[ancrageData\]\);"
    
    if re.search(target_pattern, content):
        new_content = re.sub(target_pattern, r"\g<0>\n" + sync_code, content, count=1)
        with open('index.html', 'w', encoding='utf-8') as out:
            out.write(new_content)
        print("Successfully added auto-sync to index.html!")
    else:
        print("Could not locate target pattern in index.html")

update_autosync_in_index()
