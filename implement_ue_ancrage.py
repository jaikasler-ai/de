import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Ancrage state and handlers inside App component
old_state_marker = "const [selectedDetailedSubject, setSelectedDetailedSubject] = useState(null);"

new_state_and_handlers = """const [selectedDetailedSubject, setSelectedDetailedSubject] = useState(null);

            // --- SYSTEME UE ANCRAGE MEMORIEL (Répétition Espacée J1-J28 & Renforcé J1-J24) ---
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

html = html.replace(old_state_marker, new_state_and_handlers)

# 2. Update handleMultiAnswerSubmit to update ancrageData on wrong/correct answers!
old_submit_handler = """                if (isCorrect) {
                    setQuizScore(prev => prev + 1);
                } else {
                    if (!mistakes.some(m => m.questionId === currentQ.id)) {
                        setMistakes(prev => [...prev, { id: 'm-' + Date.now(), questionId: currentQ.id, date: new Date().toISOString().split('T')[0], userChoice: selectedAnswers, correctChoices: currentQ.answers.map((a, i) => a.correct ? i : null).filter(x => x !== null) }]);
                    }"""

new_submit_handler = """                const todayMs = Date.now();
                const oneDayMs = 24 * 3600 * 1000;
                const questionId = currentQ.id;

                if (isCorrect) {
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
                    });"""

html = html.replace(old_submit_handler, new_submit_handler)

# 3. Add Ancrage Header Info inside Active Quiz View
old_quiz_mode_title = "{activeQuizMode === 'crashtest' ? `🔥 Crash Test (Vies : ${remainingHearts})` : '⚡ Série QCM Entraînement'}"
new_quiz_mode_title = "{activeQuizMode === 'crashtest' ? `🔥 Crash Test (Vies : ${remainingHearts})` : activeQuizMode === 'ancrage' ? '⚓ Session UE Ancrage Mémoriel (Répétition Espacée)' : '⚡ Série QCM Entraînement'}"

html = html.replace(old_quiz_mode_title, new_quiz_mode_title)

# 4. Add Ancrage Step Banner under statement in active quiz
old_statement_render = """<h1 className="text-xl md:text-2xl font-bold text-white">{currentQ.statement}</h1>"""

new_statement_render = """{activeQuizMode === 'ancrage' && ancrageData[currentQ.id] && (
                                        <div className="bg-purple-950/80 border border-purple-800/80 p-3.5 rounded-2xl flex flex-wrap items-center justify-between gap-3 text-xs shadow-md">
                                            <div className="flex items-center gap-2">
                                                <span className="bg-purple-600 text-white font-black px-2.5 py-1 rounded-lg">⚓ {getAncrageStepLabel(ancrageData[currentQ.id])}</span>
                                                <span className="text-purple-200 font-medium">
                                                    {ancrageData[currentQ.id].isReinforced ? '🚨 Mode Renforcé (J1 - J24)' : 'Standard (J1 - J28)'}
                                                </span>
                                            </div>
                                            <div className="text-purple-300 font-semibold">
                                                Si réussi ➔ {getAncrageNextStepLabel(ancrageData[currentQ.id])}
                                            </div>
                                        </div>
                                    )}
                                    <h1 className="text-xl md:text-2xl font-bold text-white">{currentQ.statement}</h1>"""

html = html.replace(old_statement_render, new_statement_render)

# 5. Add UE Ancrage Card on Dashboard and Navigation link!
# Let's inspect where navigation & dashboard cards are located in index.html!

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully injected state & algorithm for UE Ancrage!")
