import React from 'react';
import { X, Save, CheckSquare } from 'lucide-react';

export default function QuestionModal({
  showQuestionModal,
  setShowQuestionModal,
  questionForm,
  setQuestionForm,
  saveQuestion,
  subjects,
  editingQuestion
}) {
  if (!showQuestionModal) return null;

  return (
    <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-800 p-6 rounded-3xl max-w-xl w-full max-h-[90vh] overflow-y-auto space-y-4 shadow-2xl animate-in zoom-in-95 duration-150">
        <div className="flex justify-between items-center pb-2 border-b border-slate-800">
          <h3 className="text-lg font-bold text-white">
            {editingQuestion ? 'Modifier le QCM' : 'Nouveau QCM'}
          </h3>
          <button 
            onClick={() => setShowQuestionModal(false)} 
            className="p-1 text-slate-400 hover:text-white rounded-lg transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <form onSubmit={saveQuestion} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-400 mb-1">
              Unité d'Enseignement (UE)
            </label>
            <select 
              value={questionForm.subjectId} 
              onChange={(e) => {
                const newSubId = e.target.value;
                const sub = subjects.find(s => s.id === newSubId);
                setQuestionForm({
                  ...questionForm, 
                  subjectId: newSubId, 
                  chapter: sub && sub.chapters.length > 0 ? sub.chapters[0] : ''
                });
              }} 
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-red-500"
            >
              {subjects.map(s => (
                <option key={s.id} value={s.id}>{s.code} - {s.name}</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-400 mb-1">
              Fiche / Chapitre associé
            </label>
            <select 
              value={questionForm.chapter} 
              onChange={(e) => setQuestionForm({...questionForm, chapter: e.target.value})} 
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-red-500"
            >
              {(subjects.find(s => s.id === questionForm.subjectId)?.chapters || []).map((chap, idx) => (
                <option key={idx} value={chap}>{chap}</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-400 mb-1">Énoncé de la question</label>
            <textarea 
              rows={3} 
              required 
              value={questionForm.statement} 
              onChange={(e) => setQuestionForm({...questionForm, statement: e.target.value})} 
              placeholder="Saisissez l'énoncé du QCM..."
              className="w-full bg-slate-950 border border-slate-800 rounded-xl p-3 text-sm text-white focus:outline-none focus:border-red-500"
            ></textarea>
          </div>

          <div className="space-y-2.5">
            <label className="block text-xs font-semibold text-slate-400">
              Propositions de réponses (Cochez la bonne réponse)
            </label>
            {questionForm.answers.map((ans, idx) => (
              <div key={idx} className="flex items-center gap-3">
                <input 
                  type="checkbox" 
                  checked={ans.correct} 
                  onChange={(e) => {
                    const newAns = [...questionForm.answers];
                    newAns[idx].correct = e.target.checked;
                    setQuestionForm({...questionForm, answers: newAns});
                  }} 
                  className="w-5 h-5 accent-red-600 rounded cursor-pointer" 
                />
                <span className="w-6 text-xs font-bold text-slate-400 text-center">
                  {String.fromCharCode(65 + idx)}
                </span>
                <input 
                  type="text" 
                  required 
                  placeholder={`Réponse ${String.fromCharCode(65 + idx)}`} 
                  value={ans.text} 
                  onChange={(e) => {
                    const newAns = [...questionForm.answers];
                    newAns[idx].text = e.target.value;
                    setQuestionForm({...questionForm, answers: newAns});
                  }} 
                  className="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-4 py-2 text-sm text-white focus:outline-none focus:border-red-500" 
                />
              </div>
            ))}
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-400 mb-1">Explication détaillée</label>
            <textarea 
              rows={2} 
              value={questionForm.explanation} 
              onChange={(e) => setQuestionForm({...questionForm, explanation: e.target.value})} 
              placeholder="Explication pédagogique de la bonne réponse..."
              className="w-full bg-slate-950 border border-slate-800 rounded-xl p-3 text-sm text-white focus:outline-none focus:border-red-500"
            ></textarea>
          </div>

          <div className="flex gap-3 pt-2">
            <button 
              type="button"
              onClick={() => setShowQuestionModal(false)}
              className="flex-1 py-3 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-semibold"
            >
              Annuler
            </button>
            <button 
              type="submit" 
              className="flex-1 py-3 bg-gradient-to-r from-red-600 to-orange-500 hover:from-red-500 hover:to-orange-400 text-white font-bold text-xs rounded-xl shadow-lg shadow-red-950/50 flex items-center justify-center gap-1.5"
            >
              <Save className="w-4 h-4" />
              {editingQuestion ? 'Mettre à jour' : 'Enregistrer'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
