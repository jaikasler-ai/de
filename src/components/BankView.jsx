import React from 'react';
import { Plus, Search, Trash2, Copy, Filter, CheckCircle, BookOpen, Layers, Image as ImageIcon } from 'lucide-react';

export default function BankView({
  questions,
  subjects,
  selectedBankSubject,
  setSelectedBankSubject,
  searchQuery,
  setSearchQuery,
  setEditingQuestion,
  setShowQuestionModal,
  changeQuestionSubject,
  changeQuestionChapter,
  deleteQuestion,
  duplicateQuestion
}) {
  const filteredQuestions = questions.filter(q => {
    const matchesSubject = selectedBankSubject === 'all' || q.subjectId === selectedBankSubject;
    const matchesSearch = !searchQuery || 
      q.statement.toLowerCase().includes(searchQuery.toLowerCase()) || 
      q.chapter.toLowerCase().includes(searchQuery.toLowerCase()) ||
      (q.tags && q.tags.some(t => t.toLowerCase().includes(searchQuery.toLowerCase())));
    return matchesSubject && matchesSearch;
  });

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <div>
          <h3 className="text-xl font-bold text-white">Banque de QCM & Rangement par UE / Fiche</h3>
          <p className="text-xs text-slate-400 mt-0.5">
            {filteredQuestions.length} QCM au total dans l'annale officielle.
          </p>
        </div>

        <button 
          onClick={() => { setEditingQuestion(null); setShowQuestionModal(true); }} 
          className="inline-flex items-center gap-2 px-4 py-2.5 bg-gradient-to-r from-red-600 to-orange-500 hover:from-red-500 hover:to-orange-400 text-white font-bold rounded-xl text-sm transition-all shadow-lg shadow-red-950/50"
        >
          <Plus className="w-4 h-4" />
          Créer un QCM
        </button>
      </div>

      {/* Filter Tabs for 8 UE */}
      <div className="flex gap-2 overflow-x-auto pb-2 scrollbar-none">
        <button 
          onClick={() => setSelectedBankSubject('all')} 
          className={`px-4 py-2 rounded-2xl text-xs font-bold transition-all shrink-0 ${
            selectedBankSubject === 'all' 
              ? 'bg-red-600 text-white shadow-md shadow-red-950/50' 
              : 'bg-slate-900 border border-slate-800 text-slate-300 hover:bg-slate-800'
          }`}
        >
          Toutes les UE
        </button>

        {subjects.map(s => (
          <button 
            key={s.id} 
            onClick={() => setSelectedBankSubject(s.id)} 
            className={`px-4 py-2 rounded-2xl text-xs font-semibold whitespace-nowrap transition-all shrink-0 flex items-center gap-1.5 ${
              selectedBankSubject === s.id 
                ? 'bg-red-600 text-white shadow-md shadow-red-950/50 font-bold' 
                : 'bg-slate-900 border border-slate-800 text-slate-300 hover:bg-slate-800'
            }`}
          >
            <span>{s.icon}</span>
            <span>{s.code}</span>
          </button>
        ))}
      </div>

      {/* Search Input */}
      <div className="relative">
        <Search className="w-4 h-4 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2" />
        <input 
          type="text" 
          placeholder="Rechercher par mot-clé, énoncé, tag ou fiche PDF..." 
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="w-full bg-slate-900/80 border border-slate-800 rounded-2xl pl-11 pr-4 py-3 text-sm text-white placeholder:text-slate-500 focus:outline-none focus:border-red-500 transition-colors"
        />
        {searchQuery && (
          <button 
            onClick={() => setSearchQuery('')}
            className="absolute right-4 top-1/2 -translate-y-1/2 text-xs text-slate-400 hover:text-white bg-slate-800 px-2 py-0.5 rounded-md"
          >
            Effacer
          </button>
        )}
      </div>

      {/* List of Questions */}
      <div className="space-y-6">
        {filteredQuestions.length === 0 ? (
          <div className="text-center py-16 bg-slate-900/30 border border-slate-800/60 rounded-3xl space-y-3">
            <p className="text-slate-400 text-sm">Aucun QCM ne correspond à vos critères de recherche.</p>
            <button 
              onClick={() => { setSelectedBankSubject('all'); setSearchQuery(''); }}
              className="text-xs text-red-400 hover:underline font-semibold"
            >
              Réinitialiser les filtres
            </button>
          </div>
        ) : (
          filteredQuestions.map(q => {
            const currentSub = subjects.find(s => s.id === q.subjectId) || subjects[0];
            return (
              <div 
                key={q.id} 
                className="bg-slate-900/60 border border-slate-800 hover:border-slate-700 p-6 rounded-3xl space-y-4 transition-all"
              >
                <div className="flex justify-between items-center flex-wrap gap-3">
                  <div className="flex items-center gap-2 flex-wrap">
                    {/* UE Selector */}
                    <div className="flex items-center gap-1.5 bg-slate-950 border border-slate-800 rounded-xl px-3 py-1.5">
                      <span className="text-xs text-slate-400 font-medium">UE :</span>
                      <select 
                        value={q.subjectId} 
                        onChange={(e) => changeQuestionSubject(q.id, e.target.value)} 
                        className="bg-transparent text-xs text-red-400 font-bold focus:outline-none cursor-pointer"
                      >
                        {subjects.map(s => (
                          <option key={s.id} value={s.id} className="bg-slate-900 text-slate-100">
                            {s.code} - {s.name}
                          </option>
                        ))}
                      </select>
                    </div>

                    {/* Fiche / Chapitre Selector */}
                    <div className="flex items-center gap-1.5 bg-slate-950 border border-slate-800 rounded-xl px-3 py-1.5">
                      <span className="text-xs text-slate-400 font-medium">Fiche :</span>
                      <select 
                        value={q.chapter} 
                        onChange={(e) => changeQuestionChapter(q.id, e.target.value)} 
                        className="bg-transparent text-xs text-orange-400 font-bold focus:outline-none max-w-xs truncate cursor-pointer"
                      >
                        {currentSub.chapters.map((chap, idx) => (
                          <option key={idx} value={chap} className="bg-slate-900 text-slate-100">
                            {chap}
                          </option>
                        ))}
                      </select>
                    </div>

                    <span className="text-xs bg-slate-800 text-slate-400 px-2.5 py-1 rounded-xl">
                      Année {q.year}
                    </span>
                    <span className="text-xs bg-slate-800 text-slate-400 px-2.5 py-1 rounded-xl">
                      {q.difficulty}
                    </span>

                    {q.imageSvg && (
                      <span className="text-xs bg-indigo-950 border border-indigo-500/30 text-indigo-400 px-2.5 py-1 rounded-xl font-bold flex items-center gap-1">
                        <ImageIcon className="w-3 h-3" /> Graphique / Schéma
                      </span>
                    )}
                  </div>

                  <div className="flex items-center gap-2">
                    <button 
                      onClick={() => duplicateQuestion(q)}
                      className="p-1.5 text-slate-400 hover:text-white hover:bg-slate-800 rounded-lg text-xs flex items-center gap-1 transition-colors"
                      title="Dupliquer le QCM"
                    >
                      <Copy className="w-3.5 h-3.5" />
                    </button>

                    <button 
                      onClick={() => deleteQuestion(q.id)} 
                      className="p-1.5 text-red-400 hover:text-red-300 hover:bg-red-950/40 rounded-lg text-xs flex items-center gap-1 transition-colors"
                      title="Supprimer"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>

                <h4 className="text-base font-bold text-white leading-relaxed whitespace-pre-line">
                  {q.statement}
                </h4>

                {/* Render SVG Diagram if question has image */}
                {q.imageSvg && (
                  <div className="py-2">
                    <div 
                      className="rounded-2xl overflow-hidden border border-slate-800 shadow-md"
                      dangerouslySetInnerHTML={{ __html: q.imageSvg }}
                    />
                  </div>
                )}

                <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5">
                  {q.answers.map(a => (
                    <div 
                      key={a.id} 
                      className={`p-3.5 rounded-xl text-xs font-medium flex items-start gap-2.5 ${
                        a.correct 
                          ? 'bg-emerald-950/40 border border-emerald-500/40 text-emerald-200' 
                          : 'bg-slate-950/80 border border-slate-800/80 text-slate-400'
                      }`}
                    >
                      <span className={`w-5 h-5 rounded-md flex items-center justify-center font-bold text-[11px] shrink-0 ${
                        a.correct ? 'bg-emerald-500/20 text-emerald-300' : 'bg-slate-800 text-slate-500'
                      }`}>
                        {a.id.toUpperCase()}
                      </span>
                      <span className="pt-0.5">{a.text}</span>
                    </div>
                  ))}
                </div>

                {q.explanation && (
                  <p className="text-xs text-slate-300 bg-slate-950/60 p-3.5 rounded-xl border border-slate-800/60 leading-relaxed">
                    <strong className="text-slate-100">Explication de la correction :</strong> {q.explanation}
                  </p>
                )}
              </div>
            );
          })
        )}
      </div>
    </div>
  );
}
