import React from 'react';
import { AlertTriangle, Play, CheckCircle, XCircle } from 'lucide-react';

export default function MistakesView({ mistakes, questions, startQuiz }) {
  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <div>
          <h3 className="text-xl font-bold text-white flex items-center gap-2">
            <AlertTriangle className="w-5 h-5 text-red-500" />
            Coin Faute ({mistakes.length})
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">
            Vos erreurs passées sont enregistrées ici pour vous permettre de réviser vos points faibles.
          </p>
        </div>

        {mistakes.length > 0 && (
          <button 
            onClick={() => startQuiz('mistakes')}
            className="px-4 py-2.5 bg-gradient-to-r from-red-600 to-orange-500 hover:from-red-500 hover:to-orange-400 text-white font-bold rounded-xl text-xs transition-all flex items-center gap-2 shadow-lg shadow-red-950/50"
          >
            <Play className="w-3.5 h-3.5 fill-current" />
            Réviser mes fautes
          </button>
        )}
      </div>

      {mistakes.length === 0 ? (
        <div className="text-center py-16 bg-slate-900/40 border border-slate-800 rounded-3xl space-y-3">
          <div className="w-12 h-12 bg-emerald-950/60 border border-emerald-500/30 rounded-2xl mx-auto flex items-center justify-center text-emerald-400">
            <CheckCircle className="w-6 h-6" />
          </div>
          <h4 className="text-base font-bold text-white">Aucune faute enregistrée !</h4>
          <p className="text-slate-400 text-xs max-w-sm mx-auto">
            Bravo ! Vos erreurs lors des sessions d'entraînement apparaîtront ici automatiquement.
          </p>
        </div>
      ) : (
        <div className="space-y-4">
          {mistakes.map(m => {
            const q = questions.find(item => item.id === m.questionId);
            if (!q) return null;
            return (
              <div key={m.id} className="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-3">
                <div className="flex justify-between items-center text-xs">
                  <span className="font-semibold text-slate-400">{q.chapter}</span>
                  <span className="text-red-400 font-bold bg-red-950/40 px-2 py-0.5 rounded-md border border-red-500/30">
                    Erreur le {m.date}
                  </span>
                </div>
                <h4 className="font-bold text-white text-base leading-relaxed">{q.statement}</h4>
                {q.explanation && (
                  <p className="text-xs text-slate-300 bg-slate-950 p-3 rounded-xl border border-slate-800">
                    <strong className="text-orange-400">Explication :</strong> {q.explanation}
                  </p>
                )}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
