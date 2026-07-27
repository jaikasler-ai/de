import React from 'react';
import { ArrowLeft, Flame, Heart, CheckCircle2, XCircle, Award, Trophy, RotateCcw } from 'lucide-react';

export default function QuizEngine({
  activeQuizMode,
  setActiveQuizMode,
  quizQuestions,
  currentQuizIndex,
  quizScore,
  selectedAnswer,
  quizFinished,
  userAnswersHistory,
  remainingHearts,
  handleAnswerSubmit,
  nextQuizQuestion
}) {
  if (quizQuestions.length === 0) {
    return (
      <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col items-center justify-center p-6 text-center">
        <h2 className="text-xl font-bold text-white mb-2">Aucune question disponible</h2>
        <p className="text-slate-400 text-sm mb-6">Il n'y a pas de questions dans cette sélection.</p>
        <button 
          onClick={() => setActiveQuizMode(null)} 
          className="px-6 py-3 bg-slate-800 hover:bg-slate-700 text-white font-bold rounded-xl text-xs"
        >
          Retour au Tableau de bord
        </button>
      </div>
    );
  }

  const currentQ = quizQuestions[currentQuizIndex];
  const progressPercent = ((currentQuizIndex + 1) / quizQuestions.length) * 100;

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      {/* Quiz Header */}
      <header className="border-b border-slate-800 bg-slate-900/80 backdrop-blur-xl px-6 py-4 flex items-center justify-between sticky top-0 z-50">
        <div className="flex items-center gap-4">
          <button 
            onClick={() => setActiveQuizMode(null)} 
            className="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold flex items-center gap-1.5 transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Quitter</span>
          </button>
          <div>
            <span className="text-[11px] uppercase tracking-widest text-red-500 font-extrabold flex items-center gap-1">
              {activeQuizMode === 'crashtest' ? (
                <>
                  <Flame className="w-3.5 h-3.5" /> Crash Test Mort Subite
                </>
              ) : activeQuizMode === 'mistakes' ? (
                <>⚡ Révision Coin Faute</>
              ) : (
                <>⚡ Annale Officielle 2024-2025</>
              )}
            </span>
            <h2 className="text-xs font-semibold text-slate-300">
              Question {currentQuizIndex + 1} sur {quizQuestions.length}
            </h2>
          </div>
        </div>

        <div className="flex items-center gap-4">
          <span className="text-sm font-black text-orange-400">Score : {quizScore}</span>
          {activeQuizMode === 'crashtest' && (
            <div className="bg-red-950/80 border border-red-800/80 px-3 py-1 rounded-full text-red-400 text-xs font-bold flex items-center gap-1.5 shadow-sm">
              <span className="flex gap-1">
                {Array.from({ length: Math.max(0, remainingHearts) }).map((_, i) => (
                  <Heart key={i} className="w-4 h-4 fill-red-500 text-red-500 animate-pulse" />
                ))}
              </span>
            </div>
          )}
        </div>
      </header>

      {/* Progress Line */}
      <div className="w-full bg-slate-900 h-1.5">
        <div 
          className="bg-gradient-to-r from-red-500 via-orange-500 to-amber-500 h-1.5 transition-all duration-300" 
          style={{ width: `${progressPercent}%` }}
        ></div>
      </div>

      <main className="flex-1 max-w-4xl w-full mx-auto p-6 md:p-8 flex flex-col justify-center">
        {!quizFinished && currentQ ? (
          <div className="space-y-6">
            <div className="flex justify-between items-center text-xs text-slate-400 font-medium border-b border-slate-900 pb-3">
              <span className="text-red-400 font-semibold">{currentQ.chapter}</span>
              <span className="bg-slate-900 px-3 py-1 rounded-full border border-slate-800">
                Année {currentQ.year} • {currentQ.difficulty}
              </span>
            </div>

            <h1 className="text-xl md:text-2xl font-bold text-white leading-snug whitespace-pre-line">
              {currentQ.statement}
            </h1>

            {/* Render Question Diagram/Graph if present */}
            {currentQ.imageSvg && (
              <div className="my-3">
                <div 
                  className="rounded-2xl overflow-hidden border border-slate-800 shadow-lg"
                  dangerouslySetInnerHTML={{ __html: currentQ.imageSvg }}
                />
              </div>
            )}

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
              {currentQ.answers.map((ans, idx) => {
                let btnStyle = "bg-slate-900/80 border-slate-800 hover:border-slate-700 text-slate-200 hover:bg-slate-800/80";
                if (selectedAnswer !== null) {
                  if (ans.correct) {
                    btnStyle = "bg-emerald-950/80 border-emerald-500 text-emerald-200 shadow-lg shadow-emerald-950/50";
                  } else if (selectedAnswer === idx) {
                    btnStyle = "bg-red-950/80 border-red-500 text-red-200 shadow-lg shadow-red-950/50";
                  } else {
                    btnStyle = "bg-slate-950/40 border-slate-900 text-slate-600 opacity-50";
                  }
                }

                return (
                  <button
                    key={ans.id || idx}
                    onClick={() => handleAnswerSubmit(idx)}
                    disabled={selectedAnswer !== null}
                    className={`p-4 md:p-5 rounded-2xl border text-left transition-all flex items-start gap-4 ${btnStyle}`}
                  >
                    <span className={`w-8 h-8 rounded-xl flex items-center justify-center font-bold text-sm shrink-0 ${
                      selectedAnswer !== null && ans.correct 
                        ? 'bg-emerald-500 text-white' 
                        : selectedAnswer === idx && !ans.correct
                        ? 'bg-red-500 text-white'
                        : 'bg-slate-800 text-slate-300'
                    }`}>
                      {String.fromCharCode(65 + idx)}
                    </span>
                    <span className="text-sm font-semibold pt-1 leading-normal">{ans.text}</span>
                  </button>
                );
              })}
            </div>

            {selectedAnswer !== null && (
              <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl space-y-4 mt-6 animate-in fade-in slide-in-from-bottom-3 duration-200">
                <div className="font-bold flex items-center gap-2">
                  {currentQ.answers[selectedAnswer].correct ? (
                    <span className="text-emerald-400 flex items-center gap-1.5 text-base">
                      <CheckCircle2 className="w-5 h-5 text-emerald-400" /> Bonne réponse !
                    </span>
                  ) : (
                    <span className="text-red-400 flex items-center gap-1.5 text-base">
                      <XCircle className="w-5 h-5 text-red-400" /> Mauvaise réponse. {activeQuizMode === 'crashtest' && remainingHearts <= 0 && '(Vies épuisées - Fin du test)'}
                    </span>
                  )}
                </div>
                {currentQ.explanation && (
                  <p className="text-sm text-slate-300 leading-relaxed bg-slate-950/80 p-4 rounded-xl border border-slate-800">
                    <strong className="text-white">Explication de la correction :</strong> {currentQ.explanation}
                  </p>
                )}
                <button 
                  onClick={nextQuizQuestion} 
                  className="w-full py-3.5 bg-gradient-to-r from-red-600 to-orange-500 hover:from-red-500 hover:to-orange-400 text-white font-bold rounded-xl transition-all shadow-lg shadow-red-950/50"
                >
                  {currentQuizIndex + 1 < quizQuestions.length && (activeQuizMode !== 'crashtest' || remainingHearts > 0) 
                    ? 'Question suivante →' 
                    : 'Voir le bilan et correction complète →'}
                </button>
              </div>
            )}
          </div>
        ) : (
          /* Bilan / Result Screen */
          <div className="bg-slate-900/90 border border-slate-800 p-8 rounded-3xl max-w-2xl mx-auto space-y-6 shadow-2xl backdrop-blur-xl">
            <div className="text-center space-y-3">
              <div className="w-16 h-16 bg-gradient-to-tr from-red-600 via-orange-500 to-amber-500 rounded-3xl mx-auto flex items-center justify-center text-white text-2xl shadow-xl shadow-red-500/20">
                <Trophy className="w-8 h-8 text-white" />
              </div>
              <h2 className="text-2xl font-black text-white">Session Terminée !</h2>
              <div className="text-orange-400 font-extrabold text-2xl">
                Score : {quizScore} / {quizQuestions.length}
              </div>
            </div>

            <div className="space-y-4 max-h-96 overflow-y-auto pr-2 scrollbar-thin">
              <h3 className="text-xs font-bold text-white uppercase tracking-wider">
                Correction détaillée ({userAnswersHistory.length} répondues)
              </h3>
              {userAnswersHistory.map((item, idx) => {
                const q = item.question;
                const isCorrect = item.isCorrect;
                return (
                  <div 
                    key={q.id || idx} 
                    className={`p-4 rounded-2xl border space-y-2.5 transition-all ${
                      isCorrect 
                        ? 'bg-emerald-950/20 border-emerald-500/30' 
                        : 'bg-red-950/20 border-red-500/30'
                    }`}
                  >
                    <div className="flex justify-between items-center text-xs font-bold text-white">
                      <span>Q{idx + 1} : {q.chapter}</span>
                      <span className={isCorrect ? 'text-emerald-400 flex items-center gap-1' : 'text-red-400 flex items-center gap-1'}>
                        {isCorrect ? <CheckCircle2 className="w-3.5 h-3.5" /> : <XCircle className="w-3.5 h-3.5" />}
                        {isCorrect ? 'Correct' : 'Incorrect'}
                      </span>
                    </div>
                    <p className="text-xs font-semibold text-slate-200 whitespace-pre-line">{q.statement}</p>
                    
                    {q.imageSvg && (
                      <div className="my-2">
                        <div 
                          className="rounded-xl overflow-hidden border border-slate-800"
                          dangerouslySetInnerHTML={{ __html: q.imageSvg }}
                        />
                      </div>
                    )}

                    <div className="space-y-1">
                      {q.answers.map(ans => (
                        <div 
                          key={ans.id} 
                          className={`text-xs p-2 rounded-xl flex items-center justify-between ${
                            ans.correct 
                              ? 'bg-emerald-900/40 border border-emerald-500/40 text-emerald-200 font-bold' 
                              : 'bg-slate-950/60 text-slate-400'
                          }`}
                        >
                          <span>{ans.id.toUpperCase()}. {ans.text}</span>
                          {ans.correct && <span className="text-[10px] text-emerald-400 font-bold">★ Bonne réponse</span>}
                        </div>
                      ))}
                    </div>
                    {q.explanation && (
                      <p className="text-[11px] text-slate-300 mt-1 bg-slate-950/60 p-2.5 rounded-xl">
                        <strong>Explication :</strong> {q.explanation}
                      </p>
                    )}
                  </div>
                );
              })}
            </div>

            <button 
              onClick={() => setActiveQuizMode(null)} 
              className="w-full py-3.5 bg-gradient-to-r from-red-600 to-orange-500 hover:from-red-500 hover:to-orange-400 text-white font-bold rounded-xl transition-all shadow-lg shadow-red-950/50"
            >
              Retour au Tableau de Bord
            </button>
          </div>
        )}
      </main>
    </div>
  );
}
