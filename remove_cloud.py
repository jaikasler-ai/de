import re

def strip_cloud():
    filepath = 'index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove CLOUD_SYNC_URL and cloudSyncStatus
    content = re.sub(r"const CLOUD_SYNC_URL = '.*?';\n", "", content)
    content = re.sub(r"const \[cloudSyncStatus, setCloudSyncStatus\] = useState\('idle'\); // 'syncing', 'synced', 'error'\n", "", content)

    # 2. Remove syncFromCloud callback and useEffect
    sync_from_regex = r"// Charge la sauvegarde Cloud globale.*?\}, \[\]\);\s*React\.useEffect\(\(\) => \{\s*syncFromCloud\(\);\s*\}, \[syncFromCloud\]\);"
    content = re.sub(sync_from_regex, "", content, flags=re.DOTALL)

    # 3. Remove auto-save useEffect
    auto_save_regex = r"// Sauvegarde automatique sur le Cloud.*?\}, \[ancrageData\]\);"
    content = re.sub(auto_save_regex, "", content, flags=re.DOTALL)

    # 4. Remove saveToCloud function
    save_to_cloud_regex = r"const saveToCloud = async \(dataToSave\) => \{.*?\};\n"
    content = re.sub(save_to_cloud_regex, "", content, flags=re.DOTALL)

    # 5. Remove the calls to saveToCloud(newAncrageData) and saveToCloud(newData) 
    # and saveToCloud(updatedAncrageData) and saveToCloud(newCoinFauteData)
    # Actually, we can just remove lines containing saveToCloud(
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if 'saveToCloud(' in line:
            continue
        new_lines.append(line)
    content = '\n'.join(new_lines)

    # 6. Remove the first Save Button (in Header/Dashboard)
    button_regex1 = r"<div className=\"flex items-center gap-4\">\s*<button onClick=\{\(\) => \{[^}]*fetch\(CLOUD_SYNC_URL[^}]*\}\s*className=\"flex items-center gap-2 hover:bg-slate-700 p-2 rounded cursor-pointer transition-colors\">\s*<div className=\{`w-2 h-2 rounded-full \$\{cloudSyncStatus === 'synced' \? 'bg-green-400' : cloudSyncStatus === 'syncing' \? 'bg-yellow-400 animate-pulse' : 'bg-red-400'\}`} />\s*<span className=\"hidden sm:inline text-sm font-medium\">\s*\{cloudSyncStatus === 'syncing' \? 'Sauvegarde en cours\.\.\.' : 'Save Data \(Sync PC/Tl\)'\}\s*</span>\s*</button>\s*</div>"
    
    # Let's replace this completely with nothing or just remove it.
    # Since the regex might not perfectly match the weird "Tl" character, let's use a simpler match.
    button_match1 = r"<div className=\"flex items-center gap-4\">\s*<button onClick=\{\(\) => \{.*?\}\s*className=\"flex items-center gap-2 hover:bg-slate-700 p-2 rounded cursor-pointer transition-colors\">\s*<div className=\{`w-2 h-2 rounded-full.*?</div>\s*<span className=\"hidden sm:inline text-sm font-medium\">\s*\{cloudSyncStatus.*?</span>\s*</button>\s*</div>"
    content = re.sub(button_match1, "", content, flags=re.DOTALL)

    # 7. Remove the second Save Button (in Quiz Header)
    button_match2 = r"<button\s*onClick=\{\(\) => \{\s*setCloudSyncStatus\('syncing'\);\s*fetch\(CLOUD_SYNC_URL.*?\s*className=\"px-3 py-1 bg-green-600/20 text-green-400 rounded hover:bg-green-600/30 text-sm font-medium transition-colors\"\s*>\s*☁️ Synchro Active\s*</button>"
    content = re.sub(button_match2, "", content, flags=re.DOTALL)
    
    button_match3 = r"<button\s*onClick=\{\(\) => \{[^}]*setCloudSyncStatus[^}]*alert\([^)]+\)[^}]*\}\s*className=\"px-3 py-1 bg-green-600/20 text-green-400 rounded hover:bg-green-600/30 text-sm font-medium transition-colors\"\s*>\s*<span className=\"hidden sm:inline\">\{cloudSyncStatus.*?</span>\s*<span className=\"sm:hidden\">☁️</span>\s*</button>"
    content = re.sub(button_match3, "", content, flags=re.DOTALL)
    
    # Fallback to remove ALL fetch(CLOUD_SYNC_URL) logic just in case
    # This ensures no cloud sync logic is left behind.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Cloud sync completely stripped.")

strip_cloud()
