import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Sidebar Nav Items to include UE Ancrage
old_sidebar_nav = """                            {[
                                { id: 'dashboard', label: 'Tableau de Bord' },
                                { id: 'subjects', label: 'Gestion des 8 UE' },
                                { id: 'bank', label: 'Banque de QCM (UE)' },
                                { id: 'pdf', label: 'Import PDF & IA' },
                                { id: 'mistakes', label: 'Coin Faute', badge: mistakes.length },
                                { id: 'stats', label: 'Statistiques' },
                            ].map(item => ("""

new_sidebar_nav = """                            {[
                                { id: 'dashboard', label: 'Tableau de Bord' },
                                { id: 'ancrage', label: '⚓ UE Ancrage Mémoriel', badge: ancrageDueCount > 0 ? `${ancrageDueCount} du jour` : ancrageActiveCount },
                                { id: 'subjects', label: 'Gestion des 8 UE' },
                                { id: 'bank', label: 'Banque de QCM (UE)' },
                                { id: 'pdf', label: 'Import PDF & IA' },
                                { id: 'mistakes', label: 'Coin Faute', badge: mistakes.length },
                                { id: 'stats', label: 'Statistiques' },
                            ].map(item => ("""

html = html.replace(old_sidebar_nav, new_sidebar_nav)

# 2. Add Header title for 'ancrage'
old_header_titles = """                                {currentView === 'dashboard' && 'Tableau de Bord'}
                                {currentView === 'subjects' && (selectedDetailedSubject ? selectedDetailedSubject.name : 'Les 8 Unités d’Enseignement')}"""

new_header_titles = """                                {currentView === 'dashboard' && 'Tableau de Bord'}
                                {currentView === 'ancrage' && '⚓ UE Ancrage Mémoriel — Boîte à Erreurs J1-J28'}
                                {currentView === 'subjects' && (selectedDetailedSubject ? selectedDetailedSubject.name : 'Les 8 Unités d’Enseignement')}"""

html = html.replace(old_header_titles, new_header_titles)

# 3. Add Dashboard UE Ancrage Hero Banner Card
old_dashboard_hero = """                                    <div className="bg-gradient-to-r from-red-950/40 to-blue-950/40 border border-red-500/20 rounded-3xl p-8 space-y-4">
                                        <h1 className="text-3xl font-black text-white">Maîtrisez les 8 Unités d'Enseignement</h1>
                                        <p className="text-slate-300 text-sm">Gérez vos banques de QCM par chapitre, lancez des séries ou testez-vous en mode mort subite.</p>
                                        <button onClick={() => startQuiz('training')} className="px-6 py-3 bg-gradient-to-r from-red-600 to-orange-500 text-white font-bold rounded-2xl shadow-lg">
                                            Lancer une session rapide
                                        </button>
                                    </div>"""

new_dashboard_hero = """                                    <div className="bg-gradient-to-r from-red-950/40 to-blue-950/40 border border-red-500/20 rounded-3xl p-8 space-y-4">
                                        <h1 className="text-3xl font-black text-white">Maîtrisez les 8 Unités d'Enseignement</h1>
                                        <p className="text-slate-300 text-sm">Gérez vos banques de QCM par chapitre, lancez des séries ou testez-vous en mode mort subite.</p>
                                        <button onClick={() => startQuiz('training')} className="px-6 py-3 bg-gradient-to-r from-red-600 to-orange-500 text-white font-bold rounded-2xl shadow-lg">
                                            Lancer une session rapide
                                        </button>
                                    </div>

                                    {/* CARTE SPÉCIALE UE ANCRAGE MÉMORIEL */}
                                    <div className="bg-gradient-to-r from-purple-950/70 via-indigo-950/60 to-slate-900 border-2 border-purple-500/40 rounded-3xl p-8 shadow-2xl space-y-6 relative overflow-hidden">
                                        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 relative z-10">
                                            <div className="space-y-2 max-w-2xl">
                                                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/20 border border-purple-400/30 text-purple-300 text-xs font-bold uppercase tracking-wider">
                                                    <span>⚓ UE Spéciale — Répétition Espacée PASS/LAS</span>
                                                </div>
                                                <h2 className="text-2xl md:text-3xl font-black text-white">UE Ancrage Mémoriel (Boîte à Erreurs J1-J28)</h2>
                                                <p className="text-slate-300 text-sm leading-relaxed">
                                                    Chaque QCM raté entre automatiquement dans l'ancrage. Algorithme de révision espacée : <strong className="text-purple-300">J1 ➔ J7 ➔ J14 ➔ J28</strong> (ou <strong className="text-amber-300">Système Renforcé J1 ➔ J3 ➔ J6 ➔ J12 ➔ J24</strong> après 3 échecs). Conservé en mémoire permanente !
                                                </p>
                                            </div>

                                            <div className="flex flex-col sm:flex-row gap-3 w-full lg:w-auto shrink-0">
                                                <button onClick={() => startAncrageSession('due')} className="px-6 py-3.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-bold rounded-2xl shadow-lg flex items-center justify-center gap-2 cursor-pointer transition-all transform active:scale-95">
                                                    <span>🚀 Session du Jour ({ancrageDueCount})</span>
                                                </button>
                                                <button onClick={() => setCurrentView('ancrage')} className="px-5 py-3.5 bg-slate-800/90 hover:bg-slate-700 text-purple-200 font-bold rounded-2xl border border-purple-500/30 text-sm flex items-center justify-center gap-2 cursor-pointer transition-all">
                                                    <span>📊 Échéancier & Centre d'Ancrage</span>
                                                </button>
                                            </div>
                                        </div>

                                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 pt-2 border-t border-purple-900/40 relative z-10">
                                            <div className="bg-slate-900/80 border border-purple-900/50 p-4 rounded-2xl text-center space-y-1">
                                                <span className="text-2xl font-black text-purple-400">{ancrageDueCount}</span>
                                                <div className="text-xs text-slate-400 font-semibold uppercase">À Réviser Aujourd'hui</div>
                                            </div>
                                            <div className="bg-slate-900/80 border border-purple-900/50 p-4 rounded-2xl text-center space-y-1">
                                                <span className="text-2xl font-black text-indigo-300">{ancrageActiveCount}</span>
                                                <div className="text-xs text-slate-400 font-semibold uppercase">En Cycle d'Ancrage</div>
                                            </div>
                                            <div className="bg-slate-900/80 border border-amber-900/50 p-4 rounded-2xl text-center space-y-1">
                                                <span className="text-2xl font-black text-amber-400">{ancrageReinforcedCount}</span>
                                                <div className="text-xs text-slate-400 font-semibold uppercase">Renforcé (3+ échecs)</div>
                                            </div>
                                            <div className="bg-slate-900/80 border border-emerald-900/50 p-4 rounded-2xl text-center space-y-1">
                                                <span className="text-2xl font-black text-emerald-400">{ancrageMasteredCount}</span>
                                                <div className="text-xs text-slate-400 font-semibold uppercase">Ancrés & Libérés 🏆</div>
                                            </div>
                                        </div>
                                    </div>"""

html = html.replace(old_dashboard_hero, new_dashboard_hero)

# 4. Add Complete Ancrage Center View (`currentView === 'ancrage'`)
old_bank_view_marker = "{currentView === 'bank' && ("

ancrage_center_view = """{currentView === 'ancrage' && (
                                <div className="space-y-8">
                                    <div className="bg-gradient-to-r from-purple-950/80 via-indigo-950/80 to-slate-950 border border-purple-500/30 rounded-3xl p-8 space-y-6 shadow-xl">
                                        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                                            <div>
                                                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/20 border border-purple-400/30 text-purple-300 text-xs font-bold uppercase tracking-wider mb-2">
                                                    ⚓ Algorithme Spacé PASS/LAS
                                                </div>
                                                <h2 className="text-2xl md:text-3xl font-black text-white">Centre d'Ancrage Mémoriel & Boîte à Erreurs</h2>
                                                <p className="text-slate-300 text-xs md:text-sm mt-1 max-w-2xl leading-relaxed">
                                                    Toutes vos erreurs y sont conservées sans limite de temps (même lors de futures mises à jour). Système progressif : <strong>J1 ➔ J7 ➔ J14 ➔ J28 ➔ Suppression/Ancré 🏆</strong>. En cas de 3 échecs en ancrage, bascule automatique en <strong>Système Renforcé : J1 ➔ J3 ➔ J6 ➔ J12 ➔ J24</strong>.
                                                </p>
                                            </div>
                                            <div className="flex flex-wrap gap-2 shrink-0">
                                                <button onClick={() => startAncrageSession('due')} className="px-5 py-3 bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-bold rounded-2xl shadow-lg text-xs md:text-sm">
                                                    ⚡ Lancer Révision du Jour ({ancrageDueCount})
                                                </button>
                                                <button onClick={() => startAncrageSession('all')} className="px-4 py-3 bg-slate-800 hover:bg-slate-700 text-purple-200 font-bold rounded-2xl border border-purple-500/30 text-xs md:text-sm">
                                                    🎯 Réviser Tout ({ancrageActiveCount})
                                                </button>
                                            </div>
                                        </div>

                                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 pt-4 border-t border-purple-900/40">
                                            <div className="p-4 bg-slate-900/80 rounded-2xl border border-purple-900/50">
                                                <div className="text-xs text-slate-400 font-bold uppercase">Session du jour</div>
                                                <div className="text-2xl font-black text-purple-400 mt-1">{ancrageDueCount} QCMs</div>
                                            </div>
                                            <div className="p-4 bg-slate-900/80 rounded-2xl border border-indigo-900/50">
                                                <div className="text-xs text-slate-400 font-bold uppercase">En cours d'ancrage</div>
                                                <div className="text-2xl font-black text-indigo-300 mt-1">{ancrageActiveCount} QCMs</div>
                                            </div>
                                            <div className="p-4 bg-slate-900/80 rounded-2xl border border-amber-900/50">
                                                <div className="text-xs text-slate-400 font-bold uppercase">Système Renforcé</div>
                                                <div className="text-2xl font-black text-amber-400 mt-1">{ancrageReinforcedCount} QCMs</div>
                                            </div>
                                            <div className="p-4 bg-slate-900/80 rounded-2xl border border-emerald-900/50">
                                                <div className="text-xs text-slate-400 font-bold uppercase">Ancrés & Validé</div>
                                                <div className="text-2xl font-black text-emerald-400 mt-1">{ancrageMasteredCount} QCMs</div>
                                            </div>
                                        </div>
                                    </div>

                                    {/* TABLEAU DES QCMS EN ANCRAGE */}
                                    <div className="space-y-4">
                                        <h3 className="text-lg font-bold text-white uppercase tracking-wider flex items-center justify-between">
                                            <span>QCMs actuellement dans votre Boîte d'Ancrage ({ancrageList.length})</span>
                                            <span className="text-xs text-purple-400 font-normal">Sauvegarde locale active (Persistant)</span>
                                        </h3>

                                        {ancrageList.length === 0 ? (
                                            <div className="bg-slate-900/60 border border-slate-800 p-12 rounded-3xl text-center space-y-4">
                                                <div className="w-16 h-16 bg-purple-950/60 border border-purple-800 rounded-3xl mx-auto flex items-center justify-center text-purple-400 text-3xl">⚓</div>
                                                <h4 className="text-xl font-bold text-white">Votre Boîte à Erreurs est vide !</h4>
                                                <p className="text-slate-400 text-sm max-w-md mx-auto">
                                                    Lorsque vous faites des erreurs lors de vos séries ou Crash Tests, les QCM s'ajouteront automatiquement ici pour être ancrés selon l'algorithme de répétition espacée.
                                                </p>
                                                <button onClick={() => setCurrentView('dashboard')} className="px-6 py-2.5 bg-gradient-to-r from-red-600 to-orange-500 text-white font-bold rounded-xl text-xs">
                                                    Faire des QCM pour s'entraîner
                                                </button>
                                            </div>
                                        ) : (
                                            <div className="space-y-4">
                                                {ancrageList.map((item) => {
                                                    const q = questions.find(qItem => qItem.id === item.questionId);
                                                    if (!q) return null;
                                                    const targetSub = subjects.find(s => s.id === q.subjectId);
                                                    const isDue = item.status === 'active' && item.nextReviewTimestamp <= nowMs;
                                                    const sequence = item.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                                                    const daysLeft = Math.max(0, Math.ceil((item.nextReviewTimestamp - nowMs) / (24 * 3600 * 1000)));

                                                    return (
                                                        <div key={item.questionId} className={`p-6 rounded-3xl border-2 transition-all space-y-4 ${
                                                            item.status === 'mastered'
                                                                ? 'bg-emerald-950/20 border-emerald-500/40 opacity-80'
                                                                : isDue
                                                                    ? 'bg-purple-950/40 border-purple-500/80 shadow-lg shadow-purple-900/20'
                                                                    : 'bg-slate-900/60 border-slate-800'
                                                        }`}>
                                                            <div className="flex flex-wrap items-center justify-between gap-3">
                                                                <div className="flex items-center gap-2 flex-wrap">
                                                                    <span className="px-3 py-1 bg-purple-600 text-white font-bold text-xs rounded-xl shadow-sm">
                                                                        ⚓ {getAncrageStepLabel(item)}
                                                                    </span>
                                                                    {item.isReinforced && (
                                                                        <span className="px-3 py-1 bg-amber-500/20 border border-amber-400/40 text-amber-300 font-bold text-xs rounded-xl">
                                                                            🚨 Système Renforcé (J1 - J24)
                                                                        </span>
                                                                    )}
                                                                    <span className="text-xs text-slate-400 font-semibold">
                                                                        {targetSub ? targetSub.name : 'UE'} • {q.chapter}
                                                                    </span>
                                                                </div>

                                                                <div className="flex items-center gap-3">
                                                                    {item.status === 'mastered' ? (
                                                                        <span className="text-xs bg-emerald-600 text-white px-3 py-1 rounded-full font-bold shadow-sm">
                                                                            🏆 Ancré et Validé !
                                                                        </span>
                                                                    ) : isDue ? (
                                                                        <span className="text-xs bg-purple-600 text-white px-3 py-1 rounded-full font-bold shadow-sm animate-pulse">
                                                                            ⚡ À réviser aujourd'hui !
                                                                        </span>
                                                                    ) : (
                                                                        <span className="text-xs bg-slate-800 text-slate-300 px-3 py-1 rounded-full font-semibold border border-slate-700">
                                                                            📅 Prochain rappel dans {daysLeft} jour{daysLeft > 1 ? 's' : ''}
                                                                        </span>
                                                                    )}

                                                                    <button
                                                                        onClick={() => {
                                                                            setAncrageData(prev => {
                                                                                const next = { ...prev };
                                                                                delete next[item.questionId];
                                                                                return next;
                                                                            });
                                                                        }}
                                                                        className="text-xs text-red-400 hover:text-red-300 font-semibold px-2 py-1"
                                                                        title="Retirer cet ancrage"
                                                                    >
                                                                        Retirer
                                                                    </button>
                                                                </div>
                                                            </div>

                                                            <h4 className="text-base font-bold text-white leading-relaxed">{q.statement}</h4>

                                                            <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
                                                                {q.answers.map(ans => (
                                                                    <div key={ans.id} className={`p-2.5 rounded-xl border ${ans.correct ? 'bg-emerald-950/30 border-emerald-500/30 text-emerald-200 font-semibold' : 'bg-slate-950 border-slate-900 text-slate-400'}`}>
                                                                        {ans.id.toUpperCase()}. {ans.text}
                                                                    </div>
                                                                ))}
                                                            </div>

                                                            <div className="flex flex-wrap items-center justify-between gap-3 text-xs pt-2 border-t border-slate-800/60 text-slate-400">
                                                                <span>Échecs cumulés en ancrage : <strong>{item.failureCount}</strong></span>
                                                                <span>Dernière révision : <strong>{new Date(item.lastReviewTimestamp).toLocaleDateString('fr-FR')}</strong></span>
                                                            </div>
                                                        </div>
                                                    );
                                                })}
                                            </div>
                                        )}
                                    </div>
                                </div>
                            )}

                            {currentView === 'bank' && ("""

html = html.replace(old_bank_view_marker, ancrage_center_view)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully injected full UE Ancrage Dashboard Card, Navigation & Center View!")
