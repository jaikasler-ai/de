import React from 'react';
import { Play, BookOpen, Layers, Flame, ArrowRight } from 'lucide-react';

export default function DashboardView({ subjects, startQuiz, openUEConfig, setSelectedDetailedSubject, setCurrentView }) {
  return (
    <div className="space-y-8">
      {/* Banner */}
      <div className="relative overflow-hidden bg-gradient-to-r from-red-950/60 via-slate-900 to-blue-950/40 border border-red-500/20 rounded-3xl p-8 md:p-10 space-y-4 shadow-xl">
        <div className="absolute top-0 right-0 -mt-8 -mr-8 w-64 h-64 bg-red-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div className="relative z-10 max-w-2xl space-y-3">
          <span className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-500/10 border border-red-500/30 text-red-400 text-xs font-bold uppercase tracking-wider">
            <Flame className="w-3.5 h-3.5" /> Préparation Médicale Ultime
          </span>
          <h1 className="text-3xl md:text-4xl font-black text-white tracking-tight leading-tight">
            Maîtrisez les 8 Unités d'Enseignement
          </h1>
          <p className="text-slate-300 text-sm leading-relaxed">
            Gérez vos banques de QCM par chapitre, lancez des séries chronométrées ou testez vos limites en mode Crash Test mort subite.
          </p>
        </div>
        <div className="pt-2 relative z-10">
          <button 
            onClick={() => startQuiz('training')} 
            className="inline-flex items-center gap-2 px-6 py-3.5 bg-gradient-to-r from-red-600 to-orange-500 hover:from-red-500 hover:to-orange-400 text-white font-bold text-sm rounded-2xl shadow-lg shadow-red-600/30 transition-all hover:scale-[1.02] active:scale-[0.98]"
          >
            <Play className="w-4 h-4 fill-current" />
            Lancer une session rapide
          </button>
        </div>
      </div>

      {/* Grid of 8 UE */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <h3 className="text-lg font-bold text-white tracking-wide">
            Vos Unités d'Enseignement ({subjects.length})
          </h3>
          <button 
            onClick={() => { setSelectedDetailedSubject(null); setCurrentView('subjects'); }}
            className="text-xs text-red-400 hover:text-red-300 font-semibold flex items-center gap-1"
          >
            Voir tout <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {subjects.map(sub => (
            <div 
              key={sub.id} 
              className="bg-slate-900/60 hover:bg-slate-900/90 border border-slate-800 hover:border-slate-700 p-6 rounded-3xl space-y-4 flex flex-col justify-between transition-all group hover:shadow-xl hover:shadow-slate-950/50"
            >
              <div 
                className="space-y-3 cursor-pointer" 
                onClick={() => { setSelectedDetailedSubject(sub); setCurrentView('subjects'); }}
              >
                <div className="flex items-center justify-between">
                  <span className="text-3xl p-2.5 rounded-2xl bg-slate-950/60 border border-slate-800/80 inline-block group-hover:scale-110 transition-transform">
                    {sub.icon}
                  </span>
                  <span className="text-[11px] font-bold px-2.5 py-1 rounded-full bg-slate-800 text-slate-300">
                    {sub.code}
                  </span>
                </div>

                <div>
                  <h4 className="font-bold text-white text-base group-hover:text-red-400 transition-colors line-clamp-2">
                    {sub.name}
                  </h4>
                  <p className="text-xs text-slate-400 mt-1 flex items-center gap-2">
                    <Layers className="w-3.5 h-3.5 text-slate-500" />
                    <span>{sub.qcmCount} QCM • {sub.chapters.length} Fiches</span>
                  </p>
                </div>

                {/* Progress bar */}
                <div className="space-y-1 pt-1">
                  <div className="flex justify-between text-[11px] font-semibold text-slate-400">
                    <span>Progression</span>
                    <span className="text-red-400 font-bold">{sub.progress}%</span>
                  </div>
                  <div className="w-full bg-slate-950 h-2 rounded-full overflow-hidden border border-slate-800">
                    <div 
                      className={`h-full bg-gradient-to-r ${sub.color || 'from-red-500 to-orange-500'}`} 
                      style={{ width: `${sub.progress}%` }}
                    ></div>
                  </div>
                </div>
              </div>

              <div className="flex gap-2 pt-2 border-t border-slate-800/60">
                <button 
                  onClick={() => openUEConfig(sub)} 
                  className="flex-1 py-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 rounded-xl transition-colors flex items-center justify-center gap-1.5"
                >
                  <Play className="w-3 h-3 fill-current text-orange-400" />
                  Réviser
                </button>
                <button 
                  onClick={() => { setSelectedDetailedSubject(sub); setCurrentView('subjects'); }} 
                  className="px-3 py-2 bg-red-600/20 hover:bg-red-600/30 text-xs font-bold text-red-400 rounded-xl transition-colors flex items-center gap-1"
                >
                  <BookOpen className="w-3 h-3" />
                  Fiches
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
