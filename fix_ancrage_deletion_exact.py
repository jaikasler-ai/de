import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the delete button handler in ancrageList.map
old_delete_btn = """                                                                    <button
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

new_delete_btn = """                                                                    <button
                                                                        onClick={() => {
                                                                            if (window.confirm("Voulez-vous vraiment supprimer ce QCM de votre boîte d'ancrage ?")) {
                                                                                setAncrageData(prev => {
                                                                                    const next = { ...prev };
                                                                                    if (item.entryId) delete next[item.entryId];
                                                                                    if (item.questionId && next[item.questionId]) delete next[item.questionId];
                                                                                    return next;
                                                                                });
                                                                            }
                                                                        }}
                                                                        className="px-3 py-1.5 bg-red-950/90 hover:bg-red-900 border border-red-800 text-red-300 font-bold rounded-xl text-xs flex items-center gap-1 transition-all cursor-pointer shadow-sm"
                                                                        title="Supprimer définitivement ce QCM de l'ancrage"
                                                                    >
                                                                        🗑️ Supprimer
                                                                    </button>"""

html = html.replace(old_delete_btn, new_delete_btn)

# Also add a deletion button in the Re-mesures GPS items
old_remesure_item = """                                                        <div className="flex items-center gap-3 shrink-0">
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
                                                        </div>"""

new_remesure_item = """                                                        <div className="flex items-center gap-2 shrink-0">
                                                            <span className="text-[11px] font-bold text-[#8C7A5B] bg-[#F5F0E1] px-2 py-1 rounded-md">
                                                                {getAncrageStepLabel(item)}
                                                            </span>
                                                            <button 
                                                                onClick={() => {
                                                                    const testQ = { ...q, _ancrageEntryId: item.entryId };
                                                                    setQuizQuestions([testQ]);
                                                                    setCurrentQuizIndex(0); setQuizScore(0); setSelectedAnswers([]); setIsSubmitted(false); setQuizFinished(false); setQuizTimerSeconds(0); setUserAnswersHistory([]); setActiveQuizMode('ancrage');
                                                                }}
                                                                className="px-2.5 py-1 bg-[#C58F28] hover:bg-[#B88220] text-white font-bold rounded-lg text-xs transition-all shadow-sm"
                                                            >
                                                                Re-mesurer
                                                            </button>
                                                            <button 
                                                                onClick={() => {
                                                                    if (window.confirm("Supprimer ce QCM de l'ancrage ?")) {
                                                                        setAncrageData(prev => {
                                                                            const next = { ...prev };
                                                                            if (item.entryId) delete next[item.entryId];
                                                                            if (item.questionId && next[item.questionId]) delete next[item.questionId];
                                                                            return next;
                                                                        });
                                                                    }
                                                                }}
                                                                className="px-2 py-1 bg-red-950/80 hover:bg-red-900 border border-red-800 text-red-300 font-bold rounded-lg text-xs transition-all shadow-sm"
                                                                title="Supprimer de l'ancrage"
                                                            >
                                                                🗑️
                                                            </button>
                                                        </div>"""

html = html.replace(old_remesure_item, new_remesure_item)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully updated exact deletion handler for ancrage items!")
