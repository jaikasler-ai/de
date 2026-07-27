import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add timer state and useEffect in App component
old_state = "const [remainingHearts, setRemainingHearts] = useState(3);"
new_state = """const [remainingHearts, setRemainingHearts] = useState(3);
            const [quizTimerSeconds, setQuizTimerSeconds] = useState(0);

            // Chronometer timer effect
            React.useEffect(() => {
                let interval = null;
                if (activeQuizMode && !quizFinished) {
                    interval = setInterval(() => {
                        setQuizTimerSeconds(prev => prev + 1);
                    }, 1000);
                } else {
                    clearInterval(interval);
                }
                return () => clearInterval(interval);
            }, [activeQuizMode, quizFinished]);

            const formatQuizTime = (totalSec) => {
                const mins = Math.floor(totalSec / 60);
                const secs = totalSec % 60;
                const hrs = Math.floor(mins / 60);
                const remMins = mins % 60;
                if (hrs > 0) {
                    return `${hrs.toString().padStart(2, '0')}:${remMins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
                }
                return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
            };"""

html = html.replace(old_state, new_state)

# 2. Reset quizTimerSeconds to 0 in quiz launch functions
html = html.replace("setQuizFinished(false);", "setQuizFinished(false);\n                setQuizTimerSeconds(0);")

# 3. Add timer display to header
old_header_right = """                            <div className="flex items-center gap-4">
                                <span className="text-sm font-bold text-orange-400">Score : {quizScore}</span>
                                {activeQuizMode === 'crashtest' && (
                                    <div className="bg-red-950 border border-red-800 px-3 py-1 rounded-full text-red-400 text-xs font-bold">
                                        {Array.from({length: Math.max(0, remainingHearts)}).map(() => '❤️').join(' ')}
                                    </div>
                                )}
                            </div>"""

new_header_right = """                            <div className="flex items-center gap-4">
                                <div className="bg-slate-800 border border-slate-700 px-3.5 py-1.5 rounded-full text-slate-200 text-xs font-mono font-bold flex items-center gap-1.5 shadow-inner">
                                    <span className="text-orange-400 animate-pulse">⏱️</span>
                                    <span>{formatQuizTime(quizTimerSeconds)}</span>
                                </div>
                                <span className="text-sm font-bold text-orange-400">Score : {quizScore}</span>
                                {activeQuizMode === 'crashtest' && (
                                    <div className="bg-red-950 border border-red-800 px-3 py-1 rounded-full text-red-400 text-xs font-bold">
                                        {Array.from({length: Math.max(0, remainingHearts)}).map(() => '❤️').join(' ')}
                                    </div>
                                )}
                            </div>"""

html = html.replace(old_header_right, new_header_right)

# 4. Add time spent in summary screen
old_summary_header = """                                    <div className="text-center space-y-2">
                                        <div className="w-16 h-16 bg-red-600 rounded-3xl mx-auto flex items-center justify-center text-white text-2xl">🏆</div>
                                        <h2 className="text-2xl font-bold text-white">Session Terminée !</h2>
                                        <div className="text-orange-400 font-bold text-xl">Score : {quizScore} / {quizQuestions.length}</div>
                                    </div>"""

new_summary_header = """                                    <div className="text-center space-y-2">
                                        <div className="w-16 h-16 bg-gradient-to-tr from-red-600 to-orange-500 rounded-3xl mx-auto flex items-center justify-center text-white text-2xl shadow-lg">🏆</div>
                                        <h2 className="text-2xl font-bold text-white">Session Terminée !</h2>
                                        <div className="flex justify-center items-center gap-4 py-2">
                                            <div className="bg-slate-800 border border-slate-700 px-4 py-2 rounded-2xl text-orange-400 font-bold text-lg">
                                                Score : {quizScore} / {quizQuestions.length}
                                            </div>
                                            <div className="bg-slate-800 border border-slate-700 px-4 py-2 rounded-2xl text-slate-300 font-mono font-bold text-lg flex items-center gap-2">
                                                <span>⏱️</span>
                                                <span>{formatQuizTime(quizTimerSeconds)}</span>
                                            </div>
                                        </div>
                                    </div>"""

html = html.replace(old_summary_header, new_summary_header)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully added Chronometer timer to Quiz & Crash Test in index.html!")
