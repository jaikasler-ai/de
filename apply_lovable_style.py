import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the answers UI block in index.html with the new vertical stack white-card design with strikethrough correction
old_ui_block = """                                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                        {currentQ.answers.map((ans, idx) => {
                                            const isChecked = selectedAnswers.includes(idx);
                                            let btnStyle = isChecked 
                                                ? "bg-red-950/40 border-red-500 text-white font-semibold shadow-lg ring-1 ring-red-500/50" 
                                                : "bg-slate-900 border-slate-800 hover:border-slate-700 text-slate-200";

                                            let badgeContent = String.fromCharCode(65 + idx);
                                            let statusText = null;

                                            if (isSubmitted) {
                                                if (ans.correct && isChecked) {
                                                    btnStyle = "bg-emerald-950/80 border-emerald-500 text-emerald-100 font-semibold";
                                                    badgeContent = "✓";
                                                    statusText = <span className="text-xs bg-emerald-900/80 text-emerald-300 px-2 py-0.5 rounded font-bold">VRAI (Bien coché)</span>;
                                                } else if (ans.correct && !isChecked) {
                                                    btnStyle = "bg-amber-950/60 border-amber-500 text-amber-100 font-semibold ring-1 ring-amber-500/50";
                                                    badgeContent = "!";
                                                    statusText = <span className="text-xs bg-amber-900/80 text-amber-300 px-2 py-0.5 rounded font-bold">VRAI (Oublié)</span>;
                                                } else if (!ans.correct && isChecked) {
                                                    btnStyle = "bg-red-950/90 border-red-500 text-red-100 font-semibold";
                                                    badgeContent = "✕";
                                                    statusText = <span className="text-xs bg-red-900/80 text-red-300 px-2 py-0.5 rounded font-bold">FAUX (Coché à tort)</span>;
                                                } else {
                                                    btnStyle = "bg-slate-900/40 border-slate-900 text-slate-500 opacity-60";
                                                    statusText = <span className="text-xs text-slate-500 font-medium">FAUX (Bien évité)</span>;
                                                }
                                            }

                                            return (
                                                <button
                                                    key={ans.id || idx}
                                                    onClick={() => toggleAnswerChoice(idx)}
                                                    disabled={isSubmitted}
                                                    className={`p-4 rounded-2xl border text-left transition-all flex items-start gap-4 ${btnStyle}`}
                                                >
                                                    <div className={`w-8 h-8 rounded-xl flex items-center justify-center font-bold text-sm shrink-0 ${isChecked ? 'bg-red-600 text-white' : 'bg-slate-800 text-slate-300'}`}>
                                                        {isChecked && !isSubmitted ? '✓' : badgeContent}
                                                    </div>
                                                    <div className="flex-1">
                                                        <div className="flex items-center justify-between gap-2 mb-1">
                                                            <span className="text-sm font-medium">{ans.text}</span>
                                                            {statusText}
                                                        </div>
                                                    </div>
                                                </button>
                                            );
                                        })}
                                    </div>"""

new_ui_block = """                                    <div className="flex flex-col gap-3.5 w-full">
                                        {currentQ.answers.map((ans, idx) => {
                                            const isChecked = selectedAnswers.includes(idx);
                                            
                                            // Base style: White rounded card matching screenshot
                                            let cardStyle = "bg-white text-slate-800 border-2 border-slate-100 hover:border-purple-300 shadow-sm";
                                            let checkboxStyle = "border-2 border-slate-300 bg-white";
                                            let textStyle = "text-slate-800 font-medium";
                                            let badgeTag = null;

                                            if (isChecked && !isSubmitted) {
                                                cardStyle = "bg-white text-slate-900 border-2 border-purple-600 shadow-md ring-2 ring-purple-500/20";
                                                checkboxStyle = "bg-purple-600 border-purple-600 text-white";
                                            }

                                            if (isSubmitted) {
                                                if (ans.correct) {
                                                    // Affirmation VRAIE
                                                    if (isChecked) {
                                                        cardStyle = "bg-emerald-50 text-emerald-950 border-2 border-emerald-500 shadow-sm font-semibold";
                                                        checkboxStyle = "bg-emerald-600 border-emerald-600 text-white";
                                                        textStyle = "text-emerald-950 font-semibold";
                                                        badgeTag = <span className="text-xs bg-emerald-600 text-white px-2.5 py-0.5 rounded-full font-bold shadow-sm">✓ Vrai (Bien coché)</span>;
                                                    } else {
                                                        cardStyle = "bg-amber-50/90 text-amber-950 border-2 border-amber-400 shadow-sm";
                                                        checkboxStyle = "border-2 border-amber-500 bg-amber-100 text-amber-700";
                                                        textStyle = "text-amber-950 font-semibold";
                                                        badgeTag = <span className="text-xs bg-amber-500 text-white px-2.5 py-0.5 rounded-full font-bold shadow-sm">⚠ Vrai (Oublié)</span>;
                                                    }
                                                } else {
                                                    // Affirmation FAUSSE -> Barrée !
                                                    if (isChecked) {
                                                        cardStyle = "bg-red-50 text-red-950 border-2 border-red-400 shadow-sm";
                                                        checkboxStyle = "bg-red-600 border-red-600 text-white";
                                                        textStyle = "line-through decoration-red-500 decoration-2 text-red-800 font-medium opacity-80";
                                                        badgeTag = <span className="text-xs bg-red-600 text-white px-2.5 py-0.5 rounded-full font-bold shadow-sm">✕ Faux (Coché à tort)</span>;
                                                    } else {
                                                        cardStyle = "bg-slate-100/80 text-slate-500 border border-slate-200 opacity-70";
                                                        checkboxStyle = "border border-slate-300 bg-slate-200 text-slate-400";
                                                        textStyle = "line-through decoration-slate-400 decoration-2 text-slate-400 font-normal";
                                                        badgeTag = <span className="text-xs bg-slate-200 text-slate-600 px-2 py-0.5 rounded-md font-semibold">Faux (Correctement évité)</span>;
                                                    }
                                                }
                                            }

                                            return (
                                                <button
                                                    key={ans.id || idx}
                                                    onClick={() => toggleAnswerChoice(idx)}
                                                    disabled={isSubmitted}
                                                    className={`p-4 rounded-2xl border-2 text-left transition-all flex items-center justify-between gap-4 cursor-pointer ${cardStyle}`}
                                                >
                                                    <div className="flex items-center gap-4 flex-1">
                                                        <div className={`w-6 h-6 rounded-lg flex items-center justify-center shrink-0 transition-colors ${checkboxStyle}`}>
                                                            {isChecked || (isSubmitted && ans.correct) ? (
                                                                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3}>
                                                                    <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                                                                </svg>
                                                            ) : null}
                                                        </div>
                                                        <span className={`text-sm md:text-base leading-relaxed ${textStyle}`}>
                                                            {ans.text}
                                                        </span>
                                                    </div>
                                                    {badgeTag && <div className="shrink-0">{badgeTag}</div>}
                                                </button>
                                            );
                                        })}
                                    </div>"""

if old_ui_block in html:
    html = html.replace(old_ui_block, new_ui_block)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html to match Lovable UI design and strikethrough correction!")
