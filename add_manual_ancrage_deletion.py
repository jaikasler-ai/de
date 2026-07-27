import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Ancrage Center Header Buttons
old_header_buttons = """                                            <div className="flex flex-wrap gap-2 shrink-0">
                                                <button onClick={() => startAncrageSession('due')} className="px-5 py-3 bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-bold rounded-2xl shadow-lg text-xs md:text-sm">
                                                    ⚡ Lancer Révision du Jour ({ancrageDueCount})
                                                </button>
                                                <button onClick={() => startAncrageSession('all')} className="px-4 py-3 bg-slate-800 hover:bg-slate-700 text-purple-200 font-bold rounded-2xl border border-purple-500/30 text-xs md:text-sm">
                                                    🎯 Réviser Tout ({ancrageActiveCount})
                                                </button>
                                            </div>"""

new_header_buttons = """                                            <div className="flex flex-wrap gap-2 shrink-0">
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
                                            </div>"""

html = html.replace(old_header_buttons, new_header_buttons)

# 2. Update Card-level Actions in Ancrage View
old_card_action = """                                                                    <button
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
                                                                    </button>"""

new_card_action = """                                                                    <button
                                                                        onClick={() => {
                                                                            setQuizQuestions([q]);
                                                                            setCurrentQuizIndex(0);
                                                                            setQuizScore(0);
                                                                            setSelectedAnswers([]);
                                                                            setIsSubmitted(false);
                                                                            setQuizFinished(false);
                                                                            setQuizTimerSeconds(0);
                                                                            setUserAnswersHistory([]);
                                                                            setActiveQuizMode('ancrage');
                                                                        }}
                                                                        className="px-3 py-1.5 bg-purple-900/60 hover:bg-purple-800 text-purple-200 font-semibold rounded-xl text-xs flex items-center gap-1 transition-all cursor-pointer border border-purple-700/50"
                                                                    >
                                                                        ⚡ Tester
                                                                    </button>
                                                                    <button
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

html = html.replace(old_card_action, new_card_action)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully added manual QCM deletion buttons in UE Ancrage!")
