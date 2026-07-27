import React from 'react';
import { Flame, Zap, Award, User } from 'lucide-react';

export default function Header({ currentView, selectedDetailedSubject, user }) {
  const getTitle = () => {
    switch(currentView) {
      case 'dashboard': return 'Tableau de Bord';
      case 'subjects': return selectedDetailedSubject ? selectedDetailedSubject.name : 'Les 8 Unités d’Enseignement';
      case 'bank': return 'Banque de QCM & Rangement par UE / Fiche';
      case 'pdf': return 'Import PDF & Extraction IA';
      case 'mistakes': return 'Coin Faute';
      case 'stats': return 'Statistiques';
      default: return 'Tableau de Bord';
    }
  };

  return (
    <header className="h-20 bg-slate-900/40 border-b border-slate-800 px-8 flex items-center justify-between sticky top-0 z-30 backdrop-blur-xl shrink-0">
      <div className="flex items-center gap-3 min-w-0">
        <h2 className="text-lg font-bold text-white uppercase tracking-wider truncate">
          {getTitle()}
        </h2>
      </div>

      <div className="flex items-center gap-3 shrink-0">
        <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-orange-950/40 border border-orange-500/30 text-orange-400 text-xs font-bold shadow-sm">
          <Flame className="w-4 h-4 text-orange-500 animate-pulse" />
          <span>Série {user.streak}j</span>
        </div>

        <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-900 border border-slate-800 text-blue-400 text-xs font-bold">
          <Zap className="w-4 h-4 text-blue-400" />
          <span>{user.xp} XP</span>
        </div>

        <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-purple-950/40 border border-purple-500/30 text-purple-300 text-xs font-bold">
          <Award className="w-4 h-4 text-purple-400" />
          <span>Niv. {user.level}</span>
        </div>
      </div>
    </header>
  );
}
