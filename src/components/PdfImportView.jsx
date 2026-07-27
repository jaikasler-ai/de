import React from 'react';
import { FileUp, Sparkles, CheckCircle2, FileText, Loader2 } from 'lucide-react';

export default function PdfImportView({ simulateAIExtraction, isExtractingAI }) {
  return (
    <div className="max-w-2xl mx-auto py-10 space-y-6">
      <div className="bg-slate-900/60 border border-slate-800 p-8 md:p-10 rounded-3xl space-y-6 text-center shadow-xl relative overflow-hidden">
        <div className="w-16 h-16 rounded-3xl bg-gradient-to-tr from-red-600 via-orange-500 to-indigo-600 mx-auto flex items-center justify-center text-white shadow-lg shadow-red-500/20">
          <FileUp className="w-8 h-8 text-white" />
        </div>

        <div className="space-y-2 max-w-md mx-auto">
          <h3 className="text-2xl font-bold text-white">Import PDF & Extraction IA</h3>
          <p className="text-slate-400 text-sm">
            Glissez-déposez une fiche de cours PDF pour analyser le texte et générer automatiquement vos QCM classés par UE.
          </p>
        </div>

        {/* Dropzone mock */}
        <div className="border-2 border-dashed border-slate-700 hover:border-red-500/50 bg-slate-950/60 rounded-2xl p-8 space-y-3 cursor-pointer transition-all">
          <FileText className="w-10 h-10 text-slate-500 mx-auto" />
          <div className="text-xs text-slate-300 font-semibold">
            Déposez vos fichiers PDF ici ou <span className="text-red-400 hover:underline">Parcourir</span>
          </div>
          <p className="text-[11px] text-slate-500">PDF, Fiches de révision médicales (max 50Mo)</p>
        </div>

        <button 
          onClick={simulateAIExtraction} 
          disabled={isExtractingAI} 
          className="w-full py-4 bg-gradient-to-r from-red-600 via-orange-500 to-amber-500 hover:from-red-500 hover:to-amber-400 disabled:opacity-50 text-white font-bold text-sm rounded-2xl shadow-lg shadow-red-950/50 transition-all flex items-center justify-center gap-2"
        >
          {isExtractingAI ? (
            <>
              <Loader2 className="w-5 h-5 animate-spin" />
              <span>Extraction IA en cours des fiches de cours...</span>
            </>
          ) : (
            <>
              <Sparkles className="w-5 h-5" />
              <span>Lancer l’Extraction IA des QCM</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
}
