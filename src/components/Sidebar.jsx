import React from 'react';
import { 
  LayoutDashboard, 
  BookOpen, 
  Database, 
  FileUp, 
  AlertTriangle, 
  BarChart2, 
  Sparkles,
  Stethoscope
} from 'lucide-react';

export default function Sidebar({ currentView, setCurrentView, setSelectedDetailedSubject, mistakeCount }) {
  const navItems = [
    { id: 'dashboard', label: 'Tableau de Bord', icon: LayoutDashboard },
    { id: 'subjects', label: 'Gestion des 8 UE', icon: BookOpen },
    { id: 'bank', label: 'Banque de QCM (UE)', icon: Database },
    { id: 'pdf', label: 'Import PDF & IA', icon: FileUp, badgeText: 'AI' },
    { id: 'mistakes', label: 'Coin Faute', icon: AlertTriangle, badge: mistakeCount },
    { id: 'stats', label: 'Statistiques', icon: BarChart2 },
  ];

  return (
    <aside className="w-72 bg-slate-900/60 border-r border-slate-800 flex flex-col sticky top-0 h-screen hidden lg:flex backdrop-blur-xl shrink-0">
      <div className="p-6 flex items-center gap-3 border-b border-slate-800">
        <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-red-600 via-orange-500 to-amber-500 flex items-center justify-center font-black text-white shadow-lg shadow-red-500/20">
          <Stethoscope className="w-5 h-5 text-white" />
        </div>
        <div>
          <h1 className="font-extrabold text-white text-base tracking-tight flex items-center gap-1.5">
            MED-PREP <span className="px-1.5 py-0.5 rounded bg-red-600/30 text-red-400 text-xs font-bold border border-red-500/30">PRO</span>
          </h1>
          <p className="text-[11px] text-slate-400 font-medium">8 Unités d'Enseignement</p>
        </div>
      </div>

      <nav className="flex-1 p-4 space-y-1.5 overflow-y-auto">
        {navItems.map(item => {
          const Icon = item.icon;
          const isActive = currentView === item.id;
          return (
            <button
              key={item.id}
              onClick={() => { 
                setCurrentView(item.id); 
                setSelectedDetailedSubject(null); 
              }}
              className={`w-full flex items-center justify-between px-4 py-3 rounded-2xl text-sm font-semibold transition-all duration-200 ${
                isActive 
                  ? 'bg-gradient-to-r from-red-600/20 to-orange-500/10 border border-red-500/30 text-white shadow-md shadow-red-950/40' 
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/50 border border-transparent'
              }`}
            >
              <div className="flex items-center gap-3">
                <Icon className={`w-4 h-4 transition-colors ${isActive ? 'text-red-400' : 'text-slate-400'}`} />
                <span>{item.label}</span>
              </div>
              {item.badge > 0 && (
                <span className="px-2 py-0.5 bg-red-500/20 text-red-400 text-xs rounded-full font-bold border border-red-500/30">
                  {item.badge}
                </span>
              )}
              {item.badgeText && (
                <span className="px-2 py-0.5 bg-indigo-500/20 text-indigo-400 text-[10px] rounded-full font-extrabold border border-indigo-500/30 flex items-center gap-1">
                  <Sparkles className="w-2.5 h-2.5" />
                  {item.badgeText}
                </span>
              )}
            </button>
          );
        })}
      </nav>

      {/* User profile footer info */}
      <div className="p-4 border-t border-slate-800 m-4 rounded-2xl bg-slate-950/60 border-slate-800">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-slate-700 to-slate-800 flex items-center justify-center font-bold text-xs text-white border border-slate-700">
            AM
          </div>
          <div className="min-w-0 flex-1">
            <h4 className="text-xs font-bold text-white truncate">Dr. Alexis Martin</h4>
            <p className="text-[10px] text-slate-400 truncate">alexis.m@med-prep.io</p>
          </div>
        </div>
      </div>
    </aside>
  );
}
