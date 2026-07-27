import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix item deletion bug (delete next[item.entryId || item.questionId])
old_delete_item_code = """                                                                    <button
                                                                        onClick={() => {
                                                                            if (window.confirm("Voulez-vous vraiment supprimer ce QCM de l'UE Ancrage Mémoriel ?")) {
                                                                                setAncrageData(prev => {
                                                                                    const next = { ...prev };
                                                                                    delete next[item.questionId];
                                                                                    return next;
                                                                                });
                                                                            }
                                                                        }}
                                                                        className="px-3 py-1.5 bg-red-950/80 hover:bg-red-900 border border-red-800/80 text-red-300 font-semibold rounded-xl text-xs flex items-center gap-1 transition-all cursor-pointer"
                                                                        title="Supprimer ce QCM de l'UE Ancrage"
                                                                    >
                                                                        🗑️ Supprimer de l'ancrage
                                                                    </button>"""

new_delete_item_code = """                                                                    <button
                                                                        onClick={() => {
                                                                            if (window.confirm("Voulez-vous vraiment supprimer ce QCM de votre UE Ancrage ?")) {
                                                                                setAncrageData(prev => {
                                                                                    const next = { ...prev };
                                                                                    const targetKey = item.entryId || item.questionId;
                                                                                    delete next[targetKey];
                                                                                    return next;
                                                                                });
                                                                            }
                                                                        }}
                                                                        className="px-3 py-1.5 bg-red-950/90 hover:bg-red-900 border border-red-800 text-red-300 font-bold rounded-xl text-xs flex items-center gap-1 transition-all cursor-pointer shadow-sm"
                                                                        title="Supprimer définitivement ce QCM de l'Ancrage"
                                                                    >
                                                                        🗑️ Supprimer
                                                                    </button>"""

html = html.replace(old_delete_item_code, new_delete_item_code)

# 2. Add Export & Import functions for PC & Mobile backup
old_state_helpers = """            // Active Ancrage Entry ID during quiz
            const [activeAncrageEntryId, setActiveAncrageEntryId] = useState(null);"""

new_backup_functions = """            // Active Ancrage Entry ID during quiz
            const [activeAncrageEntryId, setActiveAncrageEntryId] = useState(null);

            // Modal de Sauvegarde & Synchronisation PC ↔ Mobile
            const [showBackupModal, setShowBackupModal] = useState(false);
            const [importTextCode, setImportTextCode] = useState('');

            // Fonction d'exportation de la sauvegarde (PC & Mobile)
            const exportUserData = () => {
                const dataToExport = {
                    version: '2.0',
                    exportDate: new Date().toISOString(),
                    user,
                    ancrageData,
                    mistakes,
                    questions: questions.filter(q => q.id.startsWith('custom-')) // Sauvegarde des questions créées
                };
                const jsonStr = JSON.stringify(dataToExport, null, 2);
                
                // Téléchargement du fichier de sauvegarde
                const blob = new Blob([jsonStr], { type: 'application/json' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `med_prep_sauvegarde_${new Date().toISOString().split('T')[0]}.json`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            };

            // Copie rapide du code JSON de sauvegarde pour transfert par message / WhatsApp
            const copyBackupToClipboard = () => {
                const dataToExport = {
                    version: '2.0',
                    exportDate: new Date().toISOString(),
                    user,
                    ancrageData,
                    mistakes
                };
                const jsonStr = JSON.stringify(dataToExport);
                navigator.clipboard.writeText(jsonStr).then(() => {
                    alert("📋 Code de sauvegarde copié dans votre presse-papier ! Vous pouvez l'envoyer par message ou WhatsApp sur votre téléphone/PC pour le coller dans l'application.");
                }).catch(() => {
                    alert("Impossible de copier automatiquement. Utilisez le bouton 'Exporter Fichier JSON'.");
                });
            };

            // Importation du fichier de sauvegarde ou du code texte
            const importUserData = (jsonContent) => {
                try {
                    const parsed = JSON.parse(jsonContent);
                    if (parsed.ancrageData) {
                        setAncrageData(parsed.ancrageData);
                        localStorage.setItem('med_prep_ancrage_data_v1', JSON.stringify(parsed.ancrageData));
                    }
                    if (parsed.mistakes) setMistakes(parsed.mistakes);
                    if (parsed.user) setUser(parsed.user);
                    if (parsed.questions && Array.isArray(parsed.questions)) {
                        setQuestions(prev => {
                            const existingIds = prev.map(q => q.id);
                            const newCustoms = parsed.questions.filter(q => !existingIds.includes(q.id));
                            return [...prev, ...newCustoms];
                        });
                    }
                    alert("🎉 Sauvegarde restaurée avec succès ! Vos QCMs d'ancrage, vos erreurs et votre progression sont synchronisés !");
                    setShowBackupModal(false);
                    setImportTextCode('');
                } catch(e) {
                    alert("❌ Fichier ou code de sauvegarde invalide. Veuillez vérifier le format.");
                }
            };"""

html = html.replace(old_state_helpers, new_backup_functions)

# 3. Add Sync/Backup button in Top Navigation Bar
old_nav_actions = """                        <div className="flex items-center gap-3">
                            <div className="hidden md:flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-900 border border-slate-800 text-xs font-semibold text-slate-300">
                                <span>🔥 {user.streak} Jours d'affilée</span>
                            </div>"""

new_nav_actions = """                        <div className="flex items-center gap-3">
                            <button 
                                onClick={() => setShowBackupModal(true)} 
                                className="px-3 py-1.5 rounded-xl bg-purple-900/60 hover:bg-purple-800 text-purple-200 border border-purple-700/50 text-xs font-bold flex items-center gap-1.5 transition-all cursor-pointer"
                                title="Sauvegarder et synchroniser votre progression entre PC et Téléphone"
                            >
                                💾 Sync PC & Mobile
                            </button>
                            <div className="hidden md:flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-900 border border-slate-800 text-xs font-semibold text-slate-300">
                                <span>🔥 {user.streak} Jours d'affilée</span>
                            </div>"""

html = html.replace(old_nav_actions, new_nav_actions)

# 4. Add Clear & Backup buttons inside EDN Pro Hero Card
old_ednpro_hero_actions = """                                        {/* BOUTON D'ACTION PRINCIPAL DORÉ EDN PRO */}
                                        <div className="pt-2">
                                            <button 
                                                onClick={() => startAncrageSession('due')} 
                                                className="w-full max-w-lg mx-auto py-4 px-8 bg-gradient-to-r from-[#C58F28] via-[#B88220] to-[#A37218] hover:from-[#B88220] hover:to-[#8F6312] text-white font-black rounded-2xl shadow-xl hover:shadow-2xl transition-all transform active:scale-98 flex items-center justify-center gap-3 text-base md:text-lg cursor-pointer"
                                            >
                                                <span>🧠 Lancer la révision ({ancrageDueCount})</span>
                                            </button>
                                        </div>
                                    </div>"""

new_ednpro_hero_actions = """                                        {/* BOUTON D'ACTION PRINCIPAL DORÉ EDN PRO & ACTIONS COMPLÉMENTAIRES */}
                                        <div className="space-y-3 pt-2">
                                            <button 
                                                onClick={() => startAncrageSession('due')} 
                                                className="w-full max-w-lg mx-auto py-4 px-8 bg-gradient-to-r from-[#C58F28] via-[#B88220] to-[#A37218] hover:from-[#B88220] hover:to-[#8F6312] text-white font-black rounded-2xl shadow-xl hover:shadow-2xl transition-all transform active:scale-98 flex items-center justify-center gap-3 text-base md:text-lg cursor-pointer"
                                            >
                                                <span>🧠 Lancer la révision ({ancrageDueCount})</span>
                                            </button>

                                            <div className="flex flex-wrap justify-center gap-2 pt-1">
                                                <button 
                                                    onClick={() => setShowBackupModal(true)} 
                                                    className="px-3.5 py-2 bg-[#EFEAD8] hover:bg-[#E5DEC9] text-[#594F3C] font-bold rounded-xl text-xs border border-[#DDD5C0] cursor-pointer flex items-center gap-1 shadow-sm"
                                                >
                                                    📲 Sauvegarder PC ↔ Mobile
                                                </button>
                                                <button 
                                                    onClick={() => {
                                                        if (window.confirm("Voulez-vous supprimer les QCMs qui sont déjà Ancrés et Validés (🏆) ?")) {
                                                            setAncrageData(prev => {
                                                                const next = {};
                                                                Object.entries(prev).forEach(([key, val]) => {
                                                                    if (val.status !== 'mastered') next[key] = val;
                                                                });
                                                                return next;
                                                            });
                                                        }
                                                    }} 
                                                    className="px-3.5 py-2 bg-[#EFEAD8] hover:bg-[#E5DEC9] text-[#594F3C] font-bold rounded-xl text-xs border border-[#DDD5C0] cursor-pointer flex items-center gap-1 shadow-sm"
                                                >
                                                    🧹 Nettoyer les Ancrés (🏆)
                                                </button>
                                                <button 
                                                    onClick={() => {
                                                        if (window.confirm("Êtes-vous sûr de vouloir tout supprimer et vider intégralement votre boîte d'ancrage mémoriel ?")) {
                                                            setAncrageData({});
                                                        }
                                                    }} 
                                                    className="px-3.5 py-2 bg-red-100 hover:bg-red-200 text-red-800 font-bold rounded-xl text-xs border border-red-300 cursor-pointer flex items-center gap-1 shadow-sm"
                                                >
                                                    🗑️ Tout Vider
                                                </button>
                                            </div>
                                        </div>
                                    </div>"""

html = html.replace(old_ednpro_hero_actions, new_ednpro_hero_actions)

# 5. Add Modal for Backup / Sync PC & Phone before closing App component tag `</App>`
backup_modal_html = """
            {/* MODAL DE SAUVEGARDE & SYNCHRONISATION PC ↔ MOBILE */}
            {showBackupModal && (
                <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
                    <div className="bg-slate-900 border border-purple-500/30 rounded-3xl p-6 md:p-8 max-w-lg w-full space-y-6 shadow-2xl">
                        <div className="flex items-center justify-between border-b border-slate-800 pb-4">
                            <div className="flex items-center gap-2">
                                <span className="text-2xl">💾</span>
                                <h3 className="text-xl font-black text-white">Sauvegarde & Sync PC / Téléphone</h3>
                            </div>
                            <button onClick={() => setShowBackupModal(false)} className="w-8 h-8 rounded-full bg-slate-800 text-slate-400 hover:text-white font-bold flex items-center justify-center">✕</button>
                        </div>

                        <p className="text-slate-300 text-xs md:text-sm leading-relaxed">
                            Exportez votre progression (boîte d’ancrage, fautes, score) sous forme de fichier ou code texte pour l’ouvrir facilement sur votre téléphone ou PC.
                        </p>

                        <div className="space-y-3">
                            <div className="p-4 bg-slate-950 border border-slate-800 rounded-2xl space-y-3">
                                <h4 className="text-xs font-bold text-purple-400 uppercase tracking-wider">1. Exporter vos données (Depuis cet appareil)</h4>
                                <div className="flex flex-wrap gap-2">
                                    <button onClick={exportUserData} className="px-4 py-2.5 bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-bold rounded-xl text-xs shadow-md cursor-pointer flex items-center gap-1.5">
                                        📥 Exporter Fichier JSON
                                    </button>
                                    <button onClick={copyBackupToClipboard} className="px-4 py-2.5 bg-slate-800 hover:bg-slate-700 text-purple-200 font-bold rounded-xl text-xs border border-purple-500/30 cursor-pointer flex items-center gap-1.5">
                                        📋 Copier Code Texte
                                    </button>
                                </div>
                            </div>

                            <div className="p-4 bg-slate-950 border border-slate-800 rounded-2xl space-y-3">
                                <h4 className="text-xs font-bold text-purple-400 uppercase tracking-wider">2. Importer une sauvegarde (Sur cet appareil)</h4>
                                <div className="space-y-2">
                                    <input 
                                        type="file" 
                                        accept=".json"
                                        onChange={(e) => {
                                            const file = e.target.files[0];
                                            if (file) {
                                                const reader = new FileReader();
                                                reader.onload = (event) => importUserData(event.target.result);
                                                reader.readAsText(file);
                                            }
                                        }}
                                        className="text-xs text-slate-400 file:mr-3 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-bold file:bg-purple-600 file:text-white hover:file:bg-purple-500 cursor-pointer"
                                    />

                                    <div className="pt-2">
                                        <textarea 
                                            value={importTextCode}
                                            onChange={(e) => setImportTextCode(e.target.value)}
                                            placeholder="Ou collez ici le code texte de sauvegarde..."
                                            className="w-full h-20 p-3 bg-slate-900 border border-slate-700 rounded-xl text-xs text-slate-200 focus:outline-none focus:border-purple-500"
                                        ></textarea>
                                        {importTextCode.trim() && (
                                            <button onClick={() => importUserData(importTextCode)} className="mt-2 w-full py-2 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-xs cursor-pointer">
                                                ✅ Restaurer à partir du texte
                                            </button>
                                        )}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            )}
"""

# Insert modal right before the closing tag of App component
app_end_pattern = """            );
        }

        const container = document.getElementById('root');"""

html = html.replace(app_end_pattern, backup_modal_html + app_end_pattern)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully fixed item deletion bug & added PC/Mobile Backup & Sync modal!")
