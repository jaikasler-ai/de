import React from 'react';
import { BarChart2, CheckCircle2, Target, Award, TrendingUp } from 'lucide-react';

export default function StatsView({ user, subjects, questions }) {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-xl font-bold text-white">Statistiques Globales</h3>
          <p className="text-xs text-slate-400 mt-0.5">Suivez vos performances sur les 8 Unités d'Enseignement.</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-2">
          <div className="flex items-center justify-between text-slate-400 text-xs font-semibold">
            <span>Taux de Réussite Global</span>
            <Target className="w-4 h-4 text-emerald-400" />
          </div>
          <p className="text-3xl font-black text-emerald-400">85%</p>
          <p className="text-[11px] text-slate-500">+4% par rapport à la semaine dernière</p>
        </div>

        <div className="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-2">
          <div className="flex items-center justify-between text-slate-400 text-xs font-semibold">
            <span>Questions Répondues</span>
            <CheckCircle2 className="w-4 h-4 text-blue-400" />
          </div>
          <p className="text-3xl font-black text-blue-400">412</p>
          <p className="text-[11px] text-slate-500">Sur un total de {questions.length * 100} QCM dispo</p>
        </div>

        <div className="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-2">
          <div className="flex items-center justify-between text-slate-400 text-xs font-semibold">
            <span>XP Médical Cumulé</span>
            <Award className="w-4 h-4 text-purple-400" />
          </div>
          <p className="text-3xl font-black text-purple-400">{user.xp} XP</p>
          <p className="text-[11px] text-slate-500">Niveau {user.level} atteint</p>
        </div>
      </div>

      {/* UE Performance list */}
      <div className="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-4">
        <h4 className="text-base font-bold text-white flex items-center gap-2">
          <TrendingUp className="w-4 h-4 text-red-500" />
          Performance par Unité d'Enseignement
        </h4>

        <div className="space-y-4">
          {subjects.map(s => (
            <div key={s.id} className="space-y-1.5">
              <div className="flex justify-between text-xs">
                <span className="font-semibold text-slate-200">{s.name} ({s.code})</span>
                <span className="font-bold text-slate-400">{s.progress}% de maîtrise</span>
              </div>
              <div className="w-full bg-slate-950 h-2.5 rounded-full overflow-hidden border border-slate-800">
                <div 
                  className={`h-full bg-gradient-to-r ${s.color}`} 
                  style={{ width: `${s.progress}%` }}
                ></div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
