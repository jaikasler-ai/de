import React from 'react';
import { X, Flame, Zap, Heart, Play } from 'lucide-react';

export default function UEConfigModal({
  showUEConfigModal,
  setShowUEConfigModal,
  selectedSubjectForQuiz,
  selectedChapterForQuiz,
  quizLaunchMode,
  setQuizLaunchMode,
  crashTestHearts,
  setCrashTestHearts,
  launchConfiguredQuiz
}) {
  if (!showUEConfigModal || !selectedSubjectForQuiz) return null;

  return (
    <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-800 p-6 rounded-3xl max-w-md w-full space-y-6 shadow-2xl animate-in zoom-in-95 duration-150">
        <div className="flex justify-between items-start">
          <div>
            <h3 className="text-base font-bold text-white">{selectedSubjectForQuiz.name}</h3>
            <p className="text-xs text-red-400 font-semibold mt-0.5">
              {selectedChapterForQuiz ? `Fiche : ${selectedChapterForQuiz}` : selectedSubjectForQuiz.code}
            </p>
          </div>
          <button 
            onClick={() => setShowUEConfigModal(false)} 
            className="p-1 text-slate-400 hover:text-white rounded-lg transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-400 mb-2">Mode de révision</label>
            <div className="grid grid-cols-2 gap-3">
              <button 
                onClick={() => setQuizLaunchMode('training')} 
                className={`p-3 rounded-2xl border text-xs font-bold transition-all flex items-center justify-center gap-1.5 ${
                  quizLaunchMode === 'training' 
                    ? 'bg-red-600 border-red-500 text-white shadow-md shadow-red-950/50' 
                    : 'bg-slate-950 border-slate-800 text-slate-300 hover:bg-slate-800'
                }`}
              >
                <Zap className="w-3.5 h-3.5" />
                Série QCM
              </button>

              <button 
                onClick={() => setQuizLaunchMode('crashtest')} 
                className={`p-3 rounded-2xl border text-xs font-bold transition-all flex items-center justify-center gap-1.5 ${
                  quizLaunchMode === 'crashtest' 
                    ? 'bg-gradient-to-r from-red-600 to-orange-600 border-orange-500 text-white shadow-md shadow-orange-950/50' 
                    : 'bg-slate-950 border-slate-800 text-slate-300 hover:bg-slate-800'
                }`}
              >
                <Flame className="w-3.5 h-3.5 text-orange-200 fill-current" />
                Crash Test
              </button>
            </div>
          </div>

          {quizLaunchMode === 'crashtest' && (
            <div className="space-y-2">
              <label className="block text-xs font-semibold text-slate-400">Nombre de cœurs (Vies)</label>
              <div className="grid grid-cols-3 gap-3">
                {[1, 3, 5].map(hearts => (
                  <button 
                    key={hearts} 
                    onClick={() => setCrashTestHearts(hearts)} 
                    className={`py-2 rounded-xl border text-xs font-bold transition-all flex items-center justify-center gap-1 ${
                      crashTestHearts === hearts 
                        ? 'bg-red-950 border-red-500 text-red-300 shadow-md shadow-red-950/50' 
                        : 'bg-slate-950 border-slate-800 text-slate-400 hover:bg-slate-800'
                    }`}
                  >
                    <Heart className="w-3 h-3 fill-red-500 text-red-500" />
                    <span>({hearts})</span>
                  </button>
                ))}
              </div>
              <p className="text-[11px] text-slate-500 leading-normal">
                Mort subite : chaque erreur retire un cœur. À 0 vie, le test s'arrête avec le bilan complet.
              </p>
            </div>
          )}
        </div>

        <div className="flex gap-3 pt-2">
          <button 
            onClick={() => setShowUEConfigModal(false)} 
            className="flex-1 py-3 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-semibold transition-colors"
          >
            Annuler
          </button>
          <button 
            onClick={launchConfiguredQuiz} 
            className="flex-1 py-3 bg-gradient-to-r from-red-600 to-orange-500 hover:from-red-500 hover:to-orange-400 text-white rounded-xl text-xs font-bold transition-all shadow-lg shadow-red-950/50 flex items-center justify-center gap-1.5"
          >
            <Play className="w-3.5 h-3.5 fill-current" />
            Lancer
          </button>
        </div>
      </div>
    </div>
  );
}
