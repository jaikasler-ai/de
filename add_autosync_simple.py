def update_autosync():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    target = "localStorage.setItem('med_prep_ancrage_data_v1', JSON.stringify(ancrageData));\n                } catch(e) {\n                    console.error(\"Erreur sauvegarde LocalStorage Ancrage:\", e);\n                }\n            }, [ancrageData]);"
    
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
                if (ancrageData && Object.keys(ancrageData).length > 0) {
                    fetch('/api/save', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(ancrageData)
                    }).catch(e => {});
                }
            }, [ancrageData]);"""

    if target in content:
        content = content.replace(target, target + "\n" + sync_code)
        with open('index.html', 'w', encoding='utf-8') as out:
            out.write(content)
        print("Successfully updated index.html with auto-sync!")
    else:
        print("Target string not found in index.html")

update_autosync()
