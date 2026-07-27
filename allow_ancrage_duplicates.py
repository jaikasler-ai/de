import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Ancrage data structure and logic to support duplicate entries
old_ancrage_logic = """            // --- SYSTEME UE ANCRAGE MEMORIEL (Répétition Espacée J1-J28 & Renforcé J1-J24) ---
            const [ancrageData, setAncrageData] = useState(() => {
                try {
                    const saved = localStorage.getItem('med_prep_ancrage_data_v1');
                    return saved ? JSON.parse(saved) : {};
                } catch(e) {
                    return {};
                }
            });

            // Sauvegarde automatique dans localStorage
            React.useEffect(() => {
                try {
                    localStorage.setItem('med_prep_ancrage_data_v1', JSON.stringify(ancrageData));
                } catch(e) {
                    console.error("Erreur sauvegarde LocalStorage Ancrage:", e);
                }
            }, [ancrageData]);

            // Délais en jours
            const STANDARD_DELAYS = [1, 7, 14, 28]; // J1, J7, J14, J28
            const REINFORCED_DELAYS = [1, 3, 6, 12, 24]; // J1, J3, J6, J12, J24 (si >= 3 échecs)

            const getAncrageStepLabel = (item) => {
                if (!item) return 'J1';
                const sequence = item.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                const days = sequence[item.stepIndex] || sequence[sequence.length - 1];
                return `J${days}${item.isReinforced ? ' (Renforcé)' : ''}`;
            };

            const getAncrageNextStepLabel = (item) => {
                if (!item) return 'J1';
                const sequence = item.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                const nextIdx = item.stepIndex + 1;
                if (nextIdx >= sequence.length) return 'Validation finale & Libération 🏆';
                return `J${sequence[nextIdx]} (dans ${sequence[nextIdx]} jours)`;
            };

            // Statistiques globales d'ancrage
            const ancrageList = Object.values(ancrageData);
            const nowMs = Date.now();
            const ancrageDueCount = ancrageList.filter(item => item.status === 'active' && item.nextReviewTimestamp <= nowMs).length;
            const ancrageActiveCount = ancrageList.filter(item => item.status === 'active').length;
            const ancrageReinforcedCount = ancrageList.filter(item => item.status === 'active' && item.isReinforced).length;
            const ancrageMasteredCount = ancrageList.filter(item => item.status === 'mastered').length;

            const startAncrageSession = (filter = 'due') => {
                let activeIds = [];
                if (filter === 'due') {
                    activeIds = ancrageList
                        .filter(item => item.status === 'active' && item.nextReviewTimestamp <= nowMs)
                        .map(item => item.questionId);
                    if (activeIds.length === 0) {
                        // Si aucun QCM n'est arrivé à échéance aujourd'hui, proposer tous les QCM en ancrage
                        activeIds = ancrageList.filter(item => item.status === 'active').map(item => item.questionId);
                    }
                } else if (filter === 'reinforced') {
                    activeIds = ancrageList.filter(item => item.status === 'active' && item.isReinforced).map(item => item.questionId);
                } else {
                    activeIds = ancrageList.filter(item => item.status === 'active').map(item => item.questionId);
                }

                if (activeIds.length === 0) {
                    alert("Aucun QCM dans votre boîte d'ancrage mémoriel pour le moment ! Continuez à faire des séries de QCM pour alimenter votre boîte à erreurs.");
                    return;
                }

                let pool = questions.filter(q => activeIds.includes(q.id));
                if (pool.length === 0) {
                    alert("Les questions d'ancrage n'ont pas été trouvées dans la banque.");
                    return;
                }

                pool.sort(() => Math.random() - 0.5);
                setQuizQuestions(pool);
                setCurrentQuizIndex(0);
                setQuizScore(0);
                setSelectedAnswers([]);
                setIsSubmitted(false);
                setQuizFinished(false);
                setQuizTimerSeconds(0);
                setUserAnswersHistory([]);
                setActiveQuizMode('ancrage');
            };"""

new_ancrage_logic = """            // --- SYSTEME UE ANCRAGE MEMORIEL (Support Doublons, Répétition Espacée J1-J28 & Renforcé J1-J24) ---
            const [ancrageData, setAncrageData] = useState(() => {
                try {
                    const saved = localStorage.getItem('med_prep_ancrage_data_v1');
                    return saved ? JSON.parse(saved) : {};
                } catch(e) {
                    return {};
                }
            });

            // Active Ancrage Entry ID during quiz
            const [activeAncrageEntryId, setActiveAncrageEntryId] = useState(null);

            // Sauvegarde automatique dans localStorage
            React.useEffect(() => {
                try {
                    localStorage.setItem('med_prep_ancrage_data_v1', JSON.stringify(ancrageData));
                } catch(e) {
                    console.error("Erreur sauvegarde LocalStorage Ancrage:", e);
                }
            }, [ancrageData]);

            // Délais en jours
            const STANDARD_DELAYS = [1, 7, 14, 28]; // J1, J7, J14, J28
            const REINFORCED_DELAYS = [1, 3, 6, 12, 24]; // J1, J3, J6, J12, J24 (si >= 3 échecs)

            const getAncrageStepLabel = (item) => {
                if (!item) return 'J1';
                const sequence = item.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                const days = sequence[item.stepIndex] || sequence[sequence.length - 1];
                return `J${days}${item.isReinforced ? ' (Renforcé)' : ''}`;
            };

            const getAncrageNextStepLabel = (item) => {
                if (!item) return 'J1';
                const sequence = item.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                const nextIdx = item.stepIndex + 1;
                if (nextIdx >= sequence.length) return 'Validation finale & Libération 🏆';
                return `J${sequence[nextIdx]} (dans ${sequence[nextIdx]} jours)`;
            };

            // Statistiques globales d'ancrage
            const ancrageList = Object.values(ancrageData);
            const nowMs = Date.now();
            const ancrageDueCount = ancrageList.filter(item => item.status === 'active' && item.nextReviewTimestamp <= nowMs).length;
            const ancrageActiveCount = ancrageList.filter(item => item.status === 'active').length;
            const ancrageReinforcedCount = ancrageList.filter(item => item.status === 'active' && item.isReinforced).length;
            const ancrageMasteredCount = ancrageList.filter(item => item.status === 'mastered').length;

            // Fonction pour ajouter une instance / doublon de QCM en ancrage
            const addAncrageEntry = (questionId) => {
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
                        nextReviewTimestamp: todayMs + (1 * 24 * 3600 * 1000),
                        lastReviewTimestamp: todayMs,
                        status: 'active',
                        addedDate: new Date().toISOString()
                    }
                }));
            };

            const startAncrageSession = (filter = 'due') => {
                let targetEntries = [];
                if (filter === 'due') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && item.nextReviewTimestamp <= nowMs);
                    if (targetEntries.length === 0) {
                        targetEntries = ancrageList.filter(item => item.status === 'active');
                    }
                } else if (filter === 'reinforced') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && item.isReinforced);
                } else {
                    targetEntries = ancrageList.filter(item => item.status === 'active');
                }

                if (targetEntries.length === 0) {
                    alert("Aucun QCM dans votre boîte d'ancrage mémoriel pour le moment !");
                    return;
                }

                // Construire le pool de questions associées avec leur entryId respectif
                let pool = targetEntries.map(entry => {
                    const qObj = questions.find(q => q.id === entry.questionId);
                    if (!qObj) return null;
                    return {
                        ...qObj,
                        _ancrageEntryId: entry.entryId
                    };
                }).filter(Boolean);

                if (pool.length === 0) {
                    alert("Les questions d'ancrage n'ont pas été trouvées dans la banque.");
                    return;
                }

                pool.sort(() => Math.random() - 0.5);
                setQuizQuestions(pool);
                setCurrentQuizIndex(0);
                setQuizScore(0);
                setSelectedAnswers([]);
                setIsSubmitted(false);
                setQuizFinished(false);
                setQuizTimerSeconds(0);
                setUserAnswersHistory([]);
                setActiveQuizMode('ancrage');
            };"""

html = html.replace(old_ancrage_logic, new_ancrage_logic)

# Replace handleMultiAnswerSubmit logic for handling ancrage entries by _ancrageEntryId
old_submit_ancrage_handling = """                if (isCorrect) {
                    setQuizScore(prev => prev + 1);

                    // Si on est en mode Ancrage et qu'on réussit :
                    if (activeQuizMode === 'ancrage') {
                        setAncrageData(prev => {
                            const existing = prev[questionId];
                            if (!existing) return prev;
                            const sequence = existing.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                            const nextStep = existing.stepIndex + 1;

                            if (nextStep >= sequence.length) {
                                // Mastered & Ancré définitif !
                                return {
                                    ...prev,
                                    [questionId]: {
                                        ...existing,
                                        stepIndex: nextStep,
                                        status: 'mastered',
                                        lastReviewTimestamp: todayMs
                                    }
                                };
                            } else {
                                const nextDelayDays = sequence[nextStep];
                                return {
                                    ...prev,
                                    [questionId]: {
                                        ...existing,
                                        stepIndex: nextStep,
                                        nextReviewTimestamp: todayMs + (nextDelayDays * oneDayMs),
                                        lastReviewTimestamp: todayMs,
                                        status: 'active'
                                    }
                                };
                            }
                        });
                    }
                } else {
                    // Erreur commise -> Entrée ou Réinitialisation dans l'UE Ancrage Mémoriel !
                    if (!mistakes.some(m => m.questionId === currentQ.id)) {
                        setMistakes(prev => [...prev, { id: 'm-' + Date.now(), questionId: currentQ.id, date: new Date().toISOString().split('T')[0], userChoice: selectedAnswers, correctChoices: currentQ.answers.map((a, i) => a.correct ? i : null).filter(x => x !== null) }]);
                    }

                    setAncrageData(prev => {
                        const existing = prev[questionId];
                        if (!existing) {
                            // Première erreur : Entrée dans l'Ancrage au niveau J1
                            return {
                                ...prev,
                                [questionId]: {
                                    questionId,
                                    stepIndex: 0,
                                    failureCount: 0,
                                    isReinforced: false,
                                    nextReviewTimestamp: todayMs + (1 * oneDayMs),
                                    lastReviewTimestamp: todayMs,
                                    status: 'active',
                                    addedDate: new Date().toISOString()
                                }
                            };
                        } else {
                            // Erreur répétée en Ancrage
                            const newFailCount = existing.failureCount + 1;
                            const isReinforced = newFailCount >= 3;
                            return {
                                ...prev,
                                [questionId]: {
                                    ...existing,
                                    stepIndex: 0, // Repart à J1
                                    failureCount: newFailCount,
                                    isReinforced: isReinforced, // Bascule en mode renforcé J1 J3 J6 J12 J24 si >= 3 échecs
                                    nextReviewTimestamp: todayMs + (1 * oneDayMs),
                                    lastReviewTimestamp: todayMs,
                                    status: 'active'
                                }
                            };
                        }
                    });
                }"""

new_submit_ancrage_handling = """                if (isCorrect) {
                    setQuizScore(prev => prev + 1);

                    if (activeQuizMode === 'ancrage') {
                        const targetEntryId = currentQ._ancrageEntryId;
                        setAncrageData(prev => {
                            let entryKey = targetEntryId;
                            if (!entryKey) {
                                const found = Object.values(prev).find(e => e.questionId === questionId && e.status === 'active');
                                if (found) entryKey = found.entryId;
                            }
                            if (!entryKey || !prev[entryKey]) return prev;

                            const existing = prev[entryKey];
                            const sequence = existing.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                            const nextStep = existing.stepIndex + 1;

                            if (nextStep >= sequence.length) {
                                return {
                                    ...prev,
                                    [entryKey]: {
                                        ...existing,
                                        stepIndex: nextStep,
                                        status: 'mastered',
                                        lastReviewTimestamp: todayMs
                                    }
                                };
                            } else {
                                const nextDelayDays = sequence[nextStep];
                                return {
                                    ...prev,
                                    [entryKey]: {
                                        ...existing,
                                        stepIndex: nextStep,
                                        nextReviewTimestamp: todayMs + (nextDelayDays * oneDayMs),
                                        lastReviewTimestamp: todayMs,
                                        status: 'active'
                                    }
                                };
                            }
                        });
                    }
                } else {
                    if (!mistakes.some(m => m.questionId === currentQ.id)) {
                        setMistakes(prev => [...prev, { id: 'm-' + Date.now(), questionId: currentQ.id, date: new Date().toISOString().split('T')[0], userChoice: selectedAnswers, correctChoices: currentQ.answers.map((a, i) => a.correct ? i : null).filter(x => x !== null) }]);
                    }

                    if (activeQuizMode === 'ancrage') {
                        const targetEntryId = currentQ._ancrageEntryId;
                        setAncrageData(prev => {
                            let entryKey = targetEntryId;
                            if (!entryKey) {
                                const found = Object.values(prev).find(e => e.questionId === questionId && e.status === 'active');
                                if (found) entryKey = found.entryId;
                            }
                            if (!entryKey || !prev[entryKey]) {
                                // Si pas encore d'instance, en créer une
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
                    }
                }"""

html = html.replace(old_submit_ancrage_handling, new_submit_ancrage_handling)

# Add "➕ Dupliquer l'ancrage" button on each QCM card in Ancrage View
old_card_buttons = """                                                                    <button
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
                                                                    </button>"""

new_card_buttons = """                                                                    <button
                                                                        onClick={() => {
                                                                            addAncrageEntry(q.id);
                                                                            alert("Une nouvelle instance (doublon) de ce QCM a été ajoutée dans votre UE Ancrage !");
                                                                        }}
                                                                        className="px-3 py-1.5 bg-indigo-900/60 hover:bg-indigo-800 text-indigo-200 font-semibold rounded-xl text-xs flex items-center gap-1 transition-all cursor-pointer border border-indigo-700/50"
                                                                        title="Ajouter une instance supplémentaire de ce QCM (Doublon)"
                                                                    >
                                                                        ➕ Dupliquer
                                                                    </button>
                                                                    <button
                                                                        onClick={() => {
                                                                            const testQ = { ...q, _ancrageEntryId: item.entryId };
                                                                            setQuizQuestions([testQ]);
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
                                                                    </button>"""

html = html.replace(old_card_buttons, new_card_buttons)

# Add Instance / Doublon label on Ancrage card display
old_instance_display = """                                                                    <span className="px-3 py-1 bg-purple-600 text-white font-bold text-xs rounded-xl shadow-sm">
                                                                        ⚓ {getAncrageStepLabel(item)}
                                                                    </span>"""

new_instance_display = """                                                                    <span className="px-3 py-1 bg-purple-600 text-white font-bold text-xs rounded-xl shadow-sm">
                                                                        ⚓ {getAncrageStepLabel(item)}
                                                                    </span>
                                                                    {item.instanceNumber && item.instanceNumber > 1 && (
                                                                        <span className="px-2.5 py-1 bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 font-bold text-xs rounded-xl">
                                                                            🏷️ Doublon #{item.instanceNumber}
                                                                        </span>
                                                                    )}"""

html = html.replace(old_instance_display, new_instance_display)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully updated UE Ancrage to support duplicate QCM instances!")
