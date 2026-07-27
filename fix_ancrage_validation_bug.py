import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace handleMultiAnswerSubmit with robust, bug-free implementation
old_handle_submit = """            const handleMultiAnswerSubmit = () => {
                if (isSubmitted) return;
                setIsSubmitted(true);
                const currentQ = quizQuestions[currentQuizIndex];
                
                // Perfect match check (medical PASS/LAS scoring)
                const isCorrect = currentQ.answers.every((ans, idx) => ans.correct === selectedAnswers.includes(idx));

                setUserAnswersHistory(prev => [...prev, {
                    question: currentQ,
                    selectedAnswerIndices: selectedAnswers,
                    isCorrect
                }]);

                const todayMs = Date.now();
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
                    });
                    if (activeQuizMode === 'crashtest') {
                        setRemainingHearts(prev => {
                            const nextHearts = prev - 1;
                            if (nextHearts <= 0) {
                                setTimeout(() => {
                                    setQuizFinished(true);
                                }, 1200);
                            }
                            return nextHearts;
                        });
                    }
                }
            };"""

new_handle_submit = """            const handleMultiAnswerSubmit = () => {
                if (isSubmitted) return;
                setIsSubmitted(true);
                const currentQ = quizQuestions[currentQuizIndex];
                
                // Perfect match check (medical PASS/LAS scoring)
                const isCorrect = currentQ.answers.every((ans, idx) => ans.correct === selectedAnswers.includes(idx));

                setUserAnswersHistory(prev => [...prev, {
                    question: currentQ,
                    selectedAnswerIndices: selectedAnswers,
                    isCorrect
                }]);

                const todayMs = Date.now();
                const oneDayMs = 24 * 3600 * 1000;
                const questionId = currentQ.id;

                if (isCorrect) {
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
                            const intervals = existing.isReinforced ? REINFORCED_INTERVALS : STANDARD_INTERVALS;
                            const nextStep = existing.stepIndex + 1;

                            if (nextStep >= intervals.length) {
                                // Validation Ultime : Ancré et libéré !
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
                                const nextDelayDays = intervals[nextStep];
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
                                    stepIndex: 0, // Repart à J0 (Aujourd'hui)
                                    failureCount: newFailCount,
                                    isReinforced: isReinforced,
                                    nextReviewTimestamp: todayMs,
                                    lastReviewTimestamp: todayMs,
                                    status: 'active'
                                }
                            };
                        });
                    } else {
                        // En mode normal/crashtest -> Création d'une instance immédiate pour aujourd'hui !
                        addAncrageEntry(questionId);
                    }

                    if (activeQuizMode === 'crashtest') {
                        setRemainingHearts(prev => {
                            const nextHearts = prev - 1;
                            if (nextHearts <= 0) {
                                setTimeout(() => {
                                    setQuizFinished(true);
                                }, 1200);
                            }
                            return nextHearts;
                        });
                    }
                }
            };"""

html = html.replace(old_handle_submit, new_handle_submit)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully fixed validation bug in Ancrage mode!")
