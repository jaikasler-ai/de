import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update addAncrageEntry & handleMultiAnswerSubmit so failed QCMs have nextReviewTimestamp = todayMs (due today!)
old_add_entry_func = """            const addAncrageEntry = (questionId) => {
                const todayMs = Date.now();
                const newEntryId = 'ancrage-' + todayMs + '-' + Math.random().toString(36).substr(2, 6);
                
                // Compter les doublons existants pour cette question
                const existingCount = Object.values(ancrageData).filter(item => item.questionId === questionId).length;

                setAncrageData(prev => ({
                    ...prev,
                    [newEntryId]: {
                        entryId: newEntryId,
                        questionId: questionId,
                        instanceNumber: existingCount + 1,
                        stepIndex: 0,
                        failureCount: 0,
                        isReinforced: false,
                        nextReviewTimestamp: todayMs, // À réviser immédiatement aujourd'hui !
                        lastReviewTimestamp: todayMs,
                        status: 'active',
                        addedDate: new Date().toISOString()
                    }
                }));
            };"""

new_add_entry_func = """            const addAncrageEntry = (questionId) => {
                const todayMs = Date.now();
                const newEntryId = 'ancrage-' + todayMs + '-' + Math.random().toString(36).substr(2, 6);
                
                const existingCount = Object.values(ancrageData).filter(item => item.questionId === questionId).length;

                setAncrageData(prev => ({
                    ...prev,
                    [newEntryId]: {
                        entryId: newEntryId,
                        questionId: questionId,
                        instanceNumber: existingCount + 1,
                        stepIndex: 0,
                        failureCount: 0,
                        isReinforced: false,
                        nextReviewTimestamp: todayMs, // Immédiatement disponible dans Révision du Jour !
                        lastReviewTimestamp: todayMs,
                        status: 'active',
                        addedDate: new Date().toISOString()
                    }
                }));
            };"""

html = html.replace(old_add_entry_func, new_add_entry_func)

# Fix handleMultiAnswerSubmit so that an error on any quiz makes nextReviewTimestamp = todayMs
old_submit_ancrage = """                    if (activeQuizMode === 'ancrage') {
                        const targetEntryId = currentQ._ancrageEntryId;
                        setAncrageData(prev => {
                            let entryKey = targetEntryId;
                            if (!entryKey) {
                                const found = Object.values(prev).find(e => e.questionId === questionId && e.status === 'active');
                                if (found) entryKey = found.entryId;
                            }
                            if (!entryKey || !prev[entryKey]) {
                                addAncrageEntry(questionId);
                                return prev;
                            }

                            const existing = prev[entryKey];
                            const newFailCount = existing.failureCount + 1;
                            const isReinforced = newFailCount >= 3;
                            return {
                                ...prev,
                                [entryKey]: {
                                    ...existing,
                                    stepIndex: 0, // Repart à J1
                                    failureCount: newFailCount,
                                    isReinforced: isReinforced,
                                    nextReviewTimestamp: todayMs + (1 * oneDayMs),
                                    lastReviewTimestamp: todayMs,
                                    status: 'active'
                                }
                            };
                        });
                    } else {
                        // En mode normal/crashtest, CHAQUE erreur crée une NOUVELLE instance (DOUBLON) dans la boîte d'ancrage !
                        addAncrageEntry(questionId);
                    }"""

new_submit_ancrage = """                    if (activeQuizMode === 'ancrage') {
                        const targetEntryId = currentQ._ancrageEntryId;
                        setAncrageData(prev => {
                            let entryKey = targetEntryId;
                            if (!entryKey) {
                                const found = Object.values(prev).find(e => e.questionId === questionId && e.status === 'active');
                                if (found) entryKey = found.entryId;
                            }
                            if (!entryKey || !prev[entryKey]) {
                                addAncrageEntry(questionId);
                                return prev;
                            }

                            const existing = prev[entryKey];
                            const newFailCount = existing.failureCount + 1;
                            const isReinforced = newFailCount >= 3;
                            return {
                                ...prev,
                                [entryKey]: {
                                    ...existing,
                                    stepIndex: 0, // Repart à J1
                                    failureCount: newFailCount,
                                    isReinforced: isReinforced,
                                    nextReviewTimestamp: todayMs, // Échec en ancrage -> Immédiatement dans la Révision du Jour !
                                    lastReviewTimestamp: todayMs,
                                    status: 'active'
                                }
                            };
                        });
                    } else {
                        // En mode normal/crashtest -> Création d'une instance immédiate pour aujourd'hui !
                        addAncrageEntry(questionId);
                    }"""

html = html.replace(old_submit_ancrage, new_submit_ancrage)

# 2. Add Tab state for filtering by Step J (All, Due Today, J1, J7, J14, J28, Reinforced, Mastered)
old_ancrage_filter_state = """            // Statistiques globales d'ancrage
            const ancrageList = Object.values(ancrageData);"""

new_ancrage_filter_state = """            const [ancrageTabFilter, setAncrageTabFilter] = useState('due'); // 'due', 'all', 'j1', 'j7', 'j14', 'j28', 'reinforced', 'mastered'

            // Statistiques globales d'ancrage
            const ancrageList = Object.values(ancrageData);"""

html = html.replace(old_ancrage_filter_state, new_ancrage_filter_state)

# 3. Update startAncrageSession to accept specific J step filtering (e.g. 'j1', 'j7', 'j14', 'j28')
old_start_session_fn = """            const startAncrageSession = (filter = 'due') => {
                let targetEntries = [];
                if (filter === 'due') {
                    // STRICTEMENT les QCM dont l'échéance est aujourd'hui ou dépassée
                    targetEntries = ancrageList.filter(item => item.status === 'active' && item.nextReviewTimestamp <= nowMs);
                    if (targetEntries.length === 0) {
                        alert("🎉 Aucun QCM à réviser aujourd'hui ! Vos prochaines révisions espacées (J1, J7, J14, J28) sont programmées pour les jours à venir.\\n\\nSi vous souhaitez quand même réviser par avance, utilisez le bouton '🎯 Réviser Tout'.");
                        return;
                    }
                } else if (filter === 'reinforced') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && item.isReinforced);
                    if (targetEntries.length === 0) {
                        alert("Aucun QCM en mode renforcé pour le moment.");
                        return;
                    }
                } else {
                    targetEntries = ancrageList.filter(item => item.status === 'active');
                    if (targetEntries.length === 0) {
                        alert("Votre boîte d'ancrage mémoriel est vide pour le moment.");
                        return;
                    }
                }"""

new_start_session_fn = """            const startAncrageSession = (filter = 'due') => {
                let targetEntries = [];
                if (filter === 'due') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && item.nextReviewTimestamp <= nowMs);
                    if (targetEntries.length === 0) {
                        alert("🎉 Aucun QCM à réviser aujourd'hui ! Vos fautes et vos rappels sont programmés pour les jours à venir.\\n\\nSi vous souhaitez vous entraîner par avance, sélectionnez un onglet de Palier (J1, J7, J14...) ou cliquez sur '🎯 Réviser Tout'.");
                        return;
                    }
                } else if (filter === 'reinforced') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && item.isReinforced);
                    if (targetEntries.length === 0) {
                        alert("Aucun QCM en mode renforcé (3+ échecs) pour le moment.");
                        return;
                    }
                } else if (filter === 'j1') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 0);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J1."); return; }
                } else if (filter === 'j7') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 1);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J7."); return; }
                } else if (filter === 'j14') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 2);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J14."); return; }
                } else if (filter === 'j28') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 3);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J28."); return; }
                } else {
                    targetEntries = ancrageList.filter(item => item.status === 'active');
                    if (targetEntries.length === 0) {
                        alert("Votre boîte d'ancrage mémoriel est vide pour le moment.");
                        return;
                    }
                }"""

html = html.replace(old_start_session_fn, new_start_session_fn)

# 4. Add Tab Navigation in Ancrage Center view to filter and launch QCMs by Step J!
old_ancrage_table_header = """                                    {/* TABLEAU DES QCMS EN ANCRAGE */}
                                    <div className="space-y-4">
                                        <h3 className="text-lg font-bold text-white uppercase tracking-wider flex items-center justify-between">
                                            <span>QCMs actuellement dans votre Boîte d'Ancrage ({ancrageList.length})</span>
                                            <span className="text-xs text-purple-400 font-normal">Sauvegarde locale active (Persistant)</span>
                                        </h3>"""

new_ancrage_table_header = """                                    {/* TABLEAU DES QCMS EN ANCRAGE AVEC ONGLET PAR PALIER J */}
                                    <div className="space-y-4">
                                        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                                            <h3 className="text-lg font-bold text-white uppercase tracking-wider">
                                                Boîte d'Ancrage ({ancrageList.length})
                                            </h3>

                                            {/* ONGLET DE FILTRAGE PAR PALIER J */}
                                            <div className="flex gap-1.5 overflow-x-auto pb-2 w-full md:w-auto">
                                                {[
                                                    { id: 'due', label: `⚡ Du Jour (${ancrageDueCount})` },
                                                    { id: 'all', label: `Tout (${ancrageActiveCount})` },
                                                    { id: 'j1', label: `J1 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===0).length})` },
                                                    { id: 'j7', label: `J7 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===1).length})` },
                                                    { id: 'j14', label: `J14 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===2).length})` },
                                                    { id: 'j28', label: `J28 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===3).length})` },
                                                    { id: 'reinforced', label: `🚨 Renforcé (${ancrageReinforcedCount})` },
                                                    { id: 'mastered', label: `🏆 Ancrés (${ancrageMasteredCount})` }
                                                ].map(tab => (
                                                    <button
                                                        key={tab.id}
                                                        onClick={() => setAncrageTabFilter(tab.id)}
                                                        className={`px-3 py-1.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all cursor-pointer ${
                                                            ancrageTabFilter === tab.id
                                                                ? 'bg-purple-600 text-white shadow-md'
                                                                : 'bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800'
                                                        }`}
                                                    >
                                                        {tab.label}
                                                    </button>
                                                ))}
                                            </div>
                                        </div>

                                        {ancrageTabFilter !== 'all' && ancrageTabFilter !== 'mastered' && (
                                            <div className="flex justify-end">
                                                <button
                                                    onClick={() => startAncrageSession(ancrageTabFilter)}
                                                    className="px-4 py-2 bg-gradient-to-r from-purple-600 to-indigo-600 text-white text-xs font-bold rounded-xl shadow-md cursor-pointer flex items-center gap-1.5"
                                                >
                                                    <span>🚀 Lancer la session pour cet onglet ({ancrageTabFilter.toUpperCase()})</span>
                                                </button>
                                            </div>
                                        )}"""

html = html.replace(old_ancrage_table_header, new_ancrage_table_header)

# 5. Filter displayed list by ancrageTabFilter
old_list_map = """{ancrageList.map((item) => {"""
new_list_map = """{ancrageList.filter(item => {
                                                    if (ancrageTabFilter === 'due') return item.status === 'active' && item.nextReviewTimestamp <= nowMs;
                                                    if (ancrageTabFilter === 'j1') return item.status === 'active' && !item.isReinforced && item.stepIndex === 0;
                                                    if (ancrageTabFilter === 'j7') return item.status === 'active' && !item.isReinforced && item.stepIndex === 1;
                                                    if (ancrageTabFilter === 'j14') return item.status === 'active' && !item.isReinforced && item.stepIndex === 2;
                                                    if (ancrageTabFilter === 'j28') return item.status === 'active' && !item.isReinforced && item.stepIndex === 3;
                                                    if (ancrageTabFilter === 'reinforced') return item.status === 'active' && item.isReinforced;
                                                    if (ancrageTabFilter === 'mastered') return item.status === 'mastered';
                                                    return item.status === 'active';
                                                }).map((item) => {"""

html = html.replace(old_list_map, new_list_map)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully updated today's mistake availability & J step filter tabs!")
