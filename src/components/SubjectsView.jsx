import React from 'react';
import { ArrowLeft, Play, Flame, BookOpen, Layers, CheckCircle2 } from 'lucide-react';

export default function SubjectsView({ 
  subjects, 
  selectedDetailedSubject, 
  setSelectedDetailedSubject, 
  openUEConfig, 
  setSelectedSubjectForQuiz, 
  setSelectedChapterForQuiz, 
  setQuizLaunchMode, 
  setShowUEConfigModal,
  setSelectedBankSubject,
  setSearchQuery,
  setCurrentView
}) {

  // List of all UEs view
  if (!selectedDetailedSubject) {
    return (
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-xl font-bold text-white">Les 8 Unités d'Enseignement</h3>
            <p className="text-xs text-slate-400 mt-0.5">Accédez aux fiches de cours officielles et lancez vos séries par UE.</p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {subjects.map(sub => (
            <div 
              key={sub.id} 
              className="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-4 hover:border-slate-700 transition-all flex flex-col justify-between"
            >
              <div 
                className="flex items-center justify-between cursor-pointer group" 
                onClick={() => setSelectedDetailedSubject(sub)}
              >
                <div className="flex items-center gap-4">
                  <span className="text-3xl p-3 bg-slate-950 rounded-2xl border border-slate-800 group-hover:scale-105 transition-transform">
                    {sub.icon}
                  </span>
                  <div>
                    <h4 className="font-bold text-white text-lg group-hover:text-red-400 transition-colors">
                      {sub.name}
                    </h4>
                    <div className="flex items-center gap-2 mt-1">
                      <span className="text-xs font-bold text-red-400 bg-red-950/40 border border-red-500/30 px-2 py-0.5 rounded-md">
                        {sub.code}
                      </span>
                      <span className="text-xs text-slate-400">
                        • {sub.chapters.length} Chapitres / Fiches
                      </span>
                    </div>
                  </div>
                </div>
              </div>

              {/* Progress */}
              <div className="space-y-1.5 pt-2">
                <div className="flex justify-between text-xs text-slate-400">
                  <span>Maîtrise du programme</span>
                  <span className="font-bold text-white">{sub.progress}%</span>
                </div>
                <div className="w-full bg-slate-950 h-2 rounded-full overflow-hidden border border-slate-800">
                  <div 
                    className={`h-full bg-gradient-to-r ${sub.color}`} 
                    style={{ width: `${sub.progress}%` }}
                  ></div>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-3 pt-2">
                <button 
                  onClick={() => { 
                    setSelectedSubjectForQuiz(sub); 
                    setQuizLaunchMode('training'); 
                    openUEConfig(sub); 
                  }} 
                  className="py-2.5 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 rounded-xl transition-colors flex items-center justify-center gap-1.5"
                >
                  <Play className="w-3.5 h-3.5 fill-current text-slate-300" />
                  Série QCM
                </button>

                <button 
                  onClick={() => { 
                    setSelectedSubjectForQuiz(sub); 
                    setQuizLaunchMode('crashtest'); 
                    openUEConfig(sub); 
                  }} 
                  className="py-2.5 bg-gradient-to-r from-red-600 to-orange-600 hover:from-red-500 hover:to-orange-500 text-xs font-bold text-white rounded-xl transition-all shadow-md shadow-red-950/50 flex items-center justify-center gap-1.5"
                >
                  <Flame className="w-3.5 h-3.5 text-orange-200 fill-current" />
                  Crash Test
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  // Detailed UE breakdown with chapters/fiches
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between flex-wrap gap-4">
        <button 
          onClick={() => setSelectedDetailedSubject(null)} 
          className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-xs font-bold rounded-xl text-slate-300 transition-colors flex items-center gap-2"
        >
          <ArrowLeft className="w-4 h-4" /> Retour aux 8 UE
        </button>

        <div className="flex gap-2">
          <button 
            onClick={() => { 
              setSelectedSubjectForQuiz(selectedDetailedSubject); 
              setQuizLaunchMode('training'); 
              openUEConfig(selectedDetailedSubject); 
            }} 
            className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-xs font-bold rounded-xl text-slate-200 transition-colors flex items-center gap-1.5"
          >
            <Play className="w-3.5 h-3.5 fill-current text-slate-300" />
            Série QCM Globale
          </button>

          <button 
            onClick={() => { 
              setSelectedSubjectForQuiz(selectedDetailedSubject); 
              setQuizLaunchMode('crashtest'); 
              openUEConfig(selectedDetailedSubject); 
            }} 
            className="px-4 py-2 bg-gradient-to-r from-red-600 to-orange-600 hover:from-red-500 hover:to-orange-500 text-xs font-bold rounded-xl text-white transition-all flex items-center gap-1.5 shadow-lg shadow-red-950/40"
          >
            <Flame className="w-3.5 h-3.5 fill-current" />
            Crash Test Global
          </button>
        </div>
      </div>

      <div className="bg-slate-900/60 border border-slate-800 p-6 md:p-8 rounded-3xl space-y-6">
        <div className="flex items-center gap-4">
          <span className="text-4xl p-4 bg-slate-950 rounded-2xl border border-slate-800">
            {selectedDetailedSubject.icon}
          </span>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold text-red-400 bg-red-950/40 border border-red-500/30 px-2 py-0.5 rounded-md">
                {selectedDetailedSubject.code}
              </span>
              <h3 className="text-2xl font-black text-white">{selectedDetailedSubject.name}</h3>
            </div>
            <p className="text-xs text-slate-400 mt-1">
              Liste officielle des fiches de cours. Lancez directement un QCM ou un Crash Test ciblé par fiche !
            </p>
          </div>
        </div>

        <div className="space-y-3 pt-2">
          {selectedDetailedSubject.chapters.map((chap, idx) => (
            <div 
              key={idx} 
              className="p-4 bg-slate-950/80 border border-slate-800/80 hover:border-slate-700 rounded-2xl flex flex-col md:flex-row items-start md:items-center justify-between gap-4 transition-all"
            >
              <div className="flex items-center gap-3 min-w-0">
                <span className="w-8 h-8 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-center text-xs font-bold text-red-400 shrink-0">
                  {idx + 1}
                </span>
                <span className="text-sm font-semibold text-slate-200 truncate">
                  {chap}
                </span>
              </div>

              <div className="flex items-center gap-2 self-end md:self-auto shrink-0">
                <button 
                  onClick={() => { 
                    setSelectedBankSubject(selectedDetailedSubject.id); 
                    setSearchQuery(chap); 
                    setCurrentView('bank'); 
                  }} 
                  className="px-3 py-1.5 bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 rounded-xl transition-colors"
                >
                  QCM associés
                </button>

                <button 
                  onClick={() => openUEConfig(selectedDetailedSubject, chap)} 
                  className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 rounded-xl transition-colors flex items-center gap-1"
                >
                  <Play className="w-3 h-3 fill-current text-slate-300" />
                  QCM Fiche
                </button>

                <button 
                  onClick={() => { 
                    setSelectedSubjectForQuiz(selectedDetailedSubject); 
                    setSelectedChapterForQuiz(chap); 
                    setQuizLaunchMode('crashtest'); 
                    setShowUEConfigModal(true); 
                  }} 
                  className="px-3 py-1.5 bg-gradient-to-r from-red-600 to-orange-600 hover:from-red-500 hover:to-orange-500 text-xs font-bold text-white rounded-xl transition-all flex items-center gap-1 shadow-md shadow-red-950/40"
                >
                  <Flame className="w-3 h-3 fill-current" />
                  Crash Test Fiche
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
