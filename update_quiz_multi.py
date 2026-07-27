import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update State variables in App component
old_state = "const [selectedAnswer, setSelectedAnswer] = useState(null);"
new_state = "const [selectedAnswers, setSelectedAnswers] = useState([]);\n            const [isSubmitted, setIsSubmitted] = useState(false);"

html = html.replace(old_state, new_state)

# 2. Reset state in quiz launch functions
html = html.replace("setSelectedAnswer(null);", "setSelectedAnswers([]); setIsSubmitted(false);")

# 3. Replace handleAnswerSubmit with multi-choice toggle and submit
old_submit_handler = """            const handleAnswerSubmit = (ansIndex) => {
                if (selectedAnswer !== null) return;
                setSelectedAnswer(ansIndex);
                const currentQ = quizQuestions[currentQuizIndex];
                const isCorrect = currentQ.answers[ansIndex].correct;

                setUserAnswersHistory(prev => [...prev, {
                    question: currentQ,
                    selectedAnswerIndex: ansIndex,
                    isCorrect
                }]);

                if (isCorrect) {
                    setQuizScore(prev => prev + 1);
                } else {
                    if (!mistakes.some(m => m.questionId === currentQ.id)) {
                        setMistakes(prev => [...prev, { id: 'm-' + Date.now(), questionId: currentQ.id, date: new Date().toISOString().split('T')[0], userChoice: ansIndex, correctChoice: currentQ.answers.findIndex(a => a.correct) }]);
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

new_submit_handler = """            const toggleAnswerChoice = (ansIndex) => {
                if (isSubmitted) return;
                setSelectedAnswers(prev => 
                    prev.includes(ansIndex) ? prev.filter(i => i !== ansIndex) : [...prev, ansIndex]
                );
            };

            const handleMultiAnswerSubmit = () => {
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

                if (isCorrect) {
                    setQuizScore(prev => prev + 1);
                } else {
                    if (!mistakes.some(m => m.questionId === currentQ.id)) {
                        setMistakes(prev => [...prev, { id: 'm-' + Date.now(), questionId: currentQ.id, date: new Date().toISOString().split('T')[0], userChoice: selectedAnswers, correctChoices: currentQ.answers.map((a, i) => a.correct ? i : null).filter(x => x !== null) }]);
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

html = html.replace(old_submit_handler, new_submit_handler)

# 4. Update answer rendering UI
old_answers_ui = """                                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                        {currentQ.answers.map((ans, idx) => {
                                            let btnStyle = "bg-slate-900 border-slate-800 hover:border-slate-700 text-slate-200";
                                            if (selectedAnswer !== null) {
                                                if (ans.correct) btnStyle = "bg-emerald-950 border-emerald-500 text-emerald-200";
                                                else if (selectedAnswer === idx) btnStyle = "bg-red-950 border-red-500 text-red-200";
                                                else btnStyle = "bg-slate-900/40 border-slate-900 text-slate-600 opacity-50";
                                            }

                                            return (
                                                <button
                                                    key={ans.id || idx}
                                                    onClick={() => handleAnswerSubmit(idx)}
                                                    disabled={selectedAnswer !== null}
                                                    className={`p-4 rounded-2xl border text-left transition-all flex items-start gap-4 ${btnStyle}`}
                                                >
                                                    <span className="w-8 h-8 rounded-xl bg-slate-800 flex items-center justify-center font-bold text-sm text-slate-300">
                                                        {String.fromCharCode(65 + idx)}
                                                    </span>
                                                    <span className="text-sm font-medium pt-1">{ans.text}</span>
                                                </button>
                                            );
                                        })}
                                    </div>

                                    {selectedAnswer !== null && (
                                        <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl space-y-4 mt-6">
                                            <div className="font-semibold">
                                                {currentQ.answers[selectedAnswer].correct ? (
                                                    <span className="text-emerald-400">✓ Bonne réponse !</span>
                                                ) : (
                                                    <span className="text-red-400">✕ Mauvaise réponse. {activeQuizMode === 'crashtest' && remainingHearts <= 0 && '(Game Over)'}</span>
                                                )}
                                            </div>
                                            <p className="text-sm text-slate-300"><strong>Explication :</strong> {currentQ.explanation}</p>
                                            <button onClick={nextQuizQuestion} className="w-full py-3 bg-gradient-to-r from-red-600 to-orange-500 text-white font-semibold rounded-xl">
                                                {currentQuizIndex + 1 < quizQuestions.length && (activeQuizMode !== 'crashtest' || remainingHearts > 0) ? 'Question suivante →' : 'Voir le bilan et correction complète →'}
                                            </button>
                                        </div>
                                    )}"""

new_answers_ui = """                                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                        {currentQ.answers.map((ans, idx) => {
                                            const isChecked = selectedAnswers.includes(idx);
                                            let btnStyle = isChecked 
                                                ? "bg-red-950/40 border-red-500 text-white font-semibold shadow-lg ring-1 ring-red-500/50" 
                                                : "bg-slate-900 border-slate-800 hover:border-slate-700 text-slate-200";

                                            let badgeContent = String.fromCharCode(65 + idx);
                                            let statusText = null;

                                            if (isSubmitted) {
                                                if (ans.correct && isChecked) {
                                                    btnStyle = "bg-emerald-950/80 border-emerald-500 text-emerald-100 font-semibold";
                                                    badgeContent = "✓";
                                                    statusText = <span className="text-xs bg-emerald-900/80 text-emerald-300 px-2 py-0.5 rounded font-bold">VRAI (Bien coché)</span>;
                                                } else if (ans.correct && !isChecked) {
                                                    btnStyle = "bg-amber-950/60 border-amber-500 text-amber-100 font-semibold ring-1 ring-amber-500/50";
                                                    badgeContent = "!";
                                                    statusText = <span className="text-xs bg-amber-900/80 text-amber-300 px-2 py-0.5 rounded font-bold">VRAI (Oublié)</span>;
                                                } else if (!ans.correct && isChecked) {
                                                    btnStyle = "bg-red-950/90 border-red-500 text-red-100 font-semibold";
                                                    badgeContent = "✕";
                                                    statusText = <span className="text-xs bg-red-900/80 text-red-300 px-2 py-0.5 rounded font-bold">FAUX (Coché à tort)</span>;
                                                } else {
                                                    btnStyle = "bg-slate-900/40 border-slate-900 text-slate-500 opacity-60";
                                                    statusText = <span className="text-xs text-slate-500 font-medium">FAUX (Bien évité)</span>;
                                                }
                                            }

                                            return (
                                                <button
                                                    key={ans.id || idx}
                                                    onClick={() => toggleAnswerChoice(idx)}
                                                    disabled={isSubmitted}
                                                    className={`p-4 rounded-2xl border text-left transition-all flex items-start gap-4 ${btnStyle}`}
                                                >
                                                    <div className={`w-8 h-8 rounded-xl flex items-center justify-center font-bold text-sm shrink-0 ${isChecked ? 'bg-red-600 text-white' : 'bg-slate-800 text-slate-300'}`}>
                                                        {isChecked && !isSubmitted ? '✓' : badgeContent}
                                                    </div>
                                                    <div className="flex-1">
                                                        <div className="flex items-center justify-between gap-2 mb-1">
                                                            <span className="text-sm font-medium">{ans.text}</span>
                                                            {statusText}
                                                        </div>
                                                    </div>
                                                </button>
                                            );
                                        })}
                                    </div>

                                    {!isSubmitted ? (
                                        <div className="mt-6 flex justify-end">
                                            <button
                                                onClick={handleMultiAnswerSubmit}
                                                className="w-full md:w-auto px-8 py-3.5 bg-gradient-to-r from-red-600 to-orange-500 hover:from-red-500 hover:to-orange-400 text-white font-bold rounded-xl shadow-lg transition-all transform active:scale-95 flex items-center justify-center gap-2"
                                            >
                                                <span>Valider mes réponses ({selectedAnswers.length} propositon{selectedAnswers.length > 1 ? 's' : ''} choisie{selectedAnswers.length > 1 ? 's' : ''})</span>
                                                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M5 13l4 4L19 7" /></svg>
                                            </button>
                                        </div>
                                    ) : (
                                        <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl space-y-4 mt-6">
                                            <div className="font-semibold text-lg">
                                                {currentQ.answers.every((ans, idx) => ans.correct === selectedAnswers.includes(idx)) ? (
                                                    <span className="text-emerald-400 flex items-center gap-2">✓ Tout est juste ! Réponse parfaite (+1 pt)</span>
                                                ) : (
                                                    <span className="text-red-400 flex items-center gap-2">✕ Réponses incorrectes ou incomplètes. {activeQuizMode === 'crashtest' && remainingHearts <= 0 && '(Game Over)'}</span>
                                                )}
                                            </div>
                                            <p className="text-sm text-slate-300"><strong>Explication :</strong> {currentQ.explanation}</p>
                                            <button onClick={nextQuizQuestion} className="w-full py-3.5 bg-gradient-to-r from-red-600 to-orange-500 text-white font-semibold rounded-xl text-center">
                                                {currentQuizIndex + 1 < quizQuestions.length && (activeQuizMode !== 'crashtest' || remainingHearts > 0) ? 'Question suivante →' : 'Voir le bilan et correction complète →'}
                                            </button>
                                        </div>
                                    )}"""

html = html.replace(old_answers_ui, new_answers_ui)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully updated index.html to Multi-Choice QCM!")
