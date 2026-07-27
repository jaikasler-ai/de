import React from 'react';
import { Stethoscope, Lock, Mail, ArrowRight } from 'lucide-react';

export default function LoginView({ setIsAuthenticated }) {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex items-center justify-center p-4 relative overflow-hidden">
      {/* Background glow effects */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-red-600/10 rounded-full blur-3xl pointer-events-none"></div>
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-orange-600/10 rounded-full blur-3xl pointer-events-none"></div>

      <div className="w-full max-w-md bg-slate-900/90 border border-slate-800 p-8 md:p-10 rounded-3xl shadow-2xl relative z-10 space-y-6 backdrop-blur-xl">
        <div className="text-center space-y-2">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-tr from-red-600 via-orange-500 to-amber-500 shadow-xl shadow-red-500/20 text-white mb-2">
            <Stethoscope className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-2xl font-black text-white tracking-tight">
            MED-PREP <span className="text-red-500">PRO</span>
          </h1>
          <p className="text-slate-400 text-xs">Plateforme SaaS de préparation aux 8 UE médicales</p>
        </div>

        <form 
          onSubmit={(e) => { 
            e.preventDefault(); 
            setIsAuthenticated(true); 
          }} 
          className="space-y-4"
        >
          <div>
            <label className="block text-xs font-semibold text-slate-400 mb-1.5">
              Email professionnel
            </label>
            <div className="relative">
              <Mail className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
              <input 
                type="email" 
                required 
                defaultValue="alexis.m@med-prep.io" 
                className="w-full bg-slate-950 border border-slate-800 rounded-xl pl-10 pr-4 py-3 text-sm text-white focus:outline-none focus:border-red-500 transition-colors" 
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-400 mb-1.5">
              Mot de passe
            </label>
            <div className="relative">
              <Lock className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
              <input 
                type="password" 
                required 
                defaultValue="password123" 
                className="w-full bg-slate-950 border border-slate-800 rounded-xl pl-10 pr-4 py-3 text-sm text-white focus:outline-none focus:border-red-500 transition-colors" 
              />
            </div>
          </div>

          <button 
            type="submit" 
            className="w-full py-3.5 bg-gradient-to-r from-red-600 via-orange-500 to-amber-500 hover:from-red-500 hover:to-amber-400 text-white font-bold text-sm rounded-xl shadow-lg shadow-red-950/50 transition-all flex items-center justify-center gap-2"
          >
            <span>Connexion à l'Espace Médical</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </form>
      </div>
    </div>
  );
}
