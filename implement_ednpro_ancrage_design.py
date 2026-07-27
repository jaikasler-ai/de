import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire ancrage view block with the exact EDN Pro Ancrage UI & Design System!
old_ancrage_view_block = """                            {currentView === 'ancrage' && (
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
                                                <button onClick={() => startAncrageSession('due')} className="px-5 py-3 bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-bold rounded-2xl shadow-lg text-xs md:text-sm cursor-pointer">
                                                    ⚡ Révision du Jour ({ancrageDueCount})
                                                </button>
                                                <button onClick={() => startAncrageSession('all')} className="px-4 py-3 bg-slate-800 hover:bg-slate-700 text-purple-200 font-bold rounded-2xl border border-purple-500/30 text-xs md:text-sm cursor-pointer">
                                                    🎯 Réviser Tout ({ancrageActiveCount})
                                                </button>
                                                <button onClick={() => {
                                                    if (window.confirm("Êtes-vous sûr de vouloir supprimer TOUS les QCM de votre boîte d'ancrage mémoriel ?")) {
                                                        setAncrageData({});
                                                    }
                                                }} className="px-3.5 py-3 bg-red-950/60 hover:bg-red-900/80 text-red-300 font-bold rounded-2xl border border-red-800/80 text-xs md:text-sm cursor-pointer">
                                                    🗑️ Vider l'Ancrage
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
                                    </div>"""

new_ednpro_ancrage_view = """                            {currentView === 'ancrage' && (
                                <div className="space-y-10 max-w-5xl mx-auto pb-16">
                                    {/* EDN PRO ANCRAGE HEADER */}
                                    <div className="text-center space-y-3 pt-4">
                                        <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-[#B88220]/20 border border-[#C58F28]/40 shadow-inner text-[#C58F28] text-3xl font-black mx-auto">
                                            🧠
                                        </div>
                                        <h1 className="text-4xl md:text-5xl font-black text-white tracking-tight font-serif">Ancrage</h1>
                                        <p className="text-slate-300 text-sm max-w-xl mx-auto leading-relaxed">
                                            Un rythme tenable chaque jour, calé sur ta courbe d'oubli — QCM, QROC et LiSA confondus.
                                        </p>
                                    </div>

                                    {/* EDN PRO HERO CARD - OBJECTIF DU JOUR */}
                                    <div className="bg-[#FAF7F0] text-slate-900 border border-[#E5DEC9] rounded-3xl p-8 md:p-10 shadow-2xl space-y-6 text-center relative overflow-hidden">
                                        <div className="space-y-2">
                                            <div className="text-xs font-bold text-[#8C7A5B] uppercase tracking-widest">
                                                OBJECTIF DU JOUR
                                            </div>
                                            <div className="text-6xl md:text-7xl font-black text-[#2C261E] font-serif tracking-tight">
                                                {ancrageDueCount}
                                            </div>
                                            <div className="text-sm font-semibold text-[#6E614B]">
                                                cartes à ancrer aujourd'hui
                                            </div>
                                        </div>

                                        {/* BARRE DE PROGRESSION EDN PRO */}
                                        <div className="max-w-md mx-auto space-y-1.5">
                                            <div className="w-full bg-[#E8DFC9] h-2.5 rounded-full overflow-hidden">
                                                <div 
                                                    className="bg-gradient-to-r from-[#C58F28] to-[#B88220] h-2.5 rounded-full transition-all duration-500"
                                                    style={{ width: `${ancrageActiveCount > 0 ? Math.min(100, (ancrageMasteredCount / ancrageActiveCount) * 100) : 0}%` }}
                                                ></div>
                                            </div>
                                            <div className="text-xs font-semibold text-[#8C7A5B]">
                                                {ancrageMasteredCount} / {ancrageActiveCount} validées
                                            </div>
                                        </div>

                                        {/* BADGES CATÉGORIES EDN PRO */}
                                        <div className="flex flex-wrap justify-center gap-2 pt-2">
                                            <span className="px-3.5 py-1.5 bg-[#EFEAD8] border border-[#DDD5C0] text-[#594F3C] text-xs font-bold rounded-full shadow-sm">
                                                UE 1 Biologie • {ancrageList.filter(i => {
                                                    const q = questions.find(item => item.id === i.questionId);
                                                    return q && q.subjectId === 'sub-1';
                                                }).length}
                                            </span>
                                            <span className="px-3.5 py-1.5 bg-[#EFEAD8] border border-[#DDD5C0] text-[#594F3C] text-xs font-bold rounded-full shadow-sm">
                                                UE 8 Biochimie • {ancrageList.filter(i => {
                                                    const q = questions.find(item => item.id === i.questionId);
                                                    return q && q.subjectId === 'sub-8';
                                                }).length}
                                            </span>
                                            <span className="px-3.5 py-1.5 bg-[#EFEAD8] border border-[#DDD5C0] text-[#594F3C] text-xs font-bold rounded-full shadow-sm">
                                                Anciens QCM • {ancrageList.filter(i => {
                                                    const q = questions.find(item => item.id === i.questionId);
                                                    return q && (q.year || q.tags?.includes('Annale'));
                                                }).length}
                                            </span>
                                            <span className="px-3.5 py-1.5 bg-[#EFEAD8] border border-[#DDD5C0] text-[#594F3C] text-xs font-bold rounded-full shadow-sm">
                                                Système Renforcé • {ancrageReinforcedCount}
                                            </span>
                                        </div>

                                        {/* BOUTON D'ACTION PRINCIPAL DORÉ EDN PRO */}
                                        <div className="pt-2">
                                            <button 
                                                onClick={() => startAncrageSession('due')} 
                                                className="w-full max-w-lg mx-auto py-4 px-8 bg-gradient-to-r from-[#C58F28] via-[#B88220] to-[#A37218] hover:from-[#B88220] hover:to-[#8F6312] text-white font-black rounded-2xl shadow-xl hover:shadow-2xl transition-all transform active:scale-98 flex items-center justify-center gap-3 text-base md:text-lg cursor-pointer"
                                            >
                                                <span>🧠 Lancer la révision ({ancrageDueCount})</span>
                                            </button>
                                        </div>
                                    </div>

                                    {/* SECTION RE-MESURES GPS & RAPPELS */}
                                    <div className="bg-[#FAF7F0] text-slate-900 border border-[#E5DEC9] rounded-3xl p-6 md:p-8 shadow-xl space-y-5">
                                        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-[#E5DEC9] pb-4">
                                            <div className="flex items-center gap-2">
                                                <span className="text-[#C58F28] text-xl">⚙️</span>
                                                <h3 className="text-lg font-black text-[#2C261E] font-serif">Re-mesures GPS</h3>
                                                <span className="px-2.5 py-0.5 bg-[#EFEAD8] text-[#594F3C] text-xs font-bold rounded-full">{Math.min(5, ancrageActiveCount)}</span>
                                            </div>

                                            <div className="flex items-center gap-1.5 text-xs font-bold">
                                                <button onClick={() => startAncrageSession('reinforced')} className="px-3 py-1 bg-[#EFEAD8] border border-[#DDD5C0] text-[#594F3C] rounded-lg hover:bg-[#E5DEC9] transition-all">
                                                    Mode Renforcé ({ancrageReinforcedCount})
                                                </button>
                                                <button onClick={() => startAncrageSession('all')} className="px-3 py-1 bg-[#C58F28] text-white rounded-lg hover:bg-[#B88220] transition-all">
                                                    Réviser Tout ({ancrageActiveCount})
                                                </button>
                                            </div>
                                        </div>

                                        <p className="text-xs md:text-sm text-[#6E614B] leading-relaxed">
                                            Des objectifs que tu as déjà croisés mais qui décrochent — on vérifie avec une question nouvelle sur le même objectif.
                                        </p>

                                        {/* LISTE DES ITEMS/QCM DE RE-MESURES */}
                                        <div className="space-y-2.5">
                                            {ancrageList.slice(0, 5).map((item, idx) => {
                                                const q = questions.find(qItem => qItem.id === item.questionId);
                                                if (!q) return null;
                                                return (
                                                    <div key={item.entryId} className="p-3.5 bg-white border border-[#E5DEC9] rounded-2xl flex items-center justify-between gap-4 shadow-sm hover:border-[#C58F28] transition-all">
                                                        <div className="flex items-center gap-3 flex-1 min-w-0">
                                                            <span className="w-7 h-7 rounded-full bg-[#EFEAD8] text-[#8C7A5B] font-bold text-xs flex items-center justify-center shrink-0">
                                                                {String.fromCharCode(65 + (idx % 4))}
                                                            </span>
                                                            <span className="text-xs md:text-sm font-medium text-[#2C261E] truncate">
                                                                {q.chapter} — {q.statement}
                                                            </span>
                                                        </div>
                                                        <div className="flex items-center gap-3 shrink-0">
                                                            <span className="text-[11px] font-bold text-[#8C7A5B] bg-[#F5F0E1] px-2.5 py-1 rounded-md">
                                                                {getAncrageStepLabel(item)}
                                                            </span>
                                                            <button 
                                                                onClick={() => {
                                                                    const testQ = { ...q, _ancrageEntryId: item.entryId };
                                                                    setQuizQuestions([testQ]);
                                                                    setCurrentQuizIndex(0); setQuizScore(0); setSelectedAnswers([]); setIsSubmitted(false); setQuizFinished(false); setQuizTimerSeconds(0); setUserAnswersHistory([]); setActiveQuizMode('ancrage');
                                                                }}
                                                                className="px-3 py-1 bg-[#C58F28] hover:bg-[#B88220] text-white font-bold rounded-lg text-xs transition-all shadow-sm"
                                                            >
                                                                Re-mesurer
                                                            </button>
                                                        </div>
                                                    </div>
                                                );
                                            })}
                                        </div>
                                    </div>"""

html = html.replace(old_ancrage_view_block, new_ednpro_ancrage_view)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully transformed Ancrage view into EDN Pro design system!")
