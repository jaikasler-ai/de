import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Ancrage delays, labels and functions
old_ancrage_setup = """            // Délais en jours
            const STANDARD_DELAYS = [1, 7, 14, 28]; // J1, J7, J14, J28
            const REINFORCED_DELAYS = [1, 3, 6, 12, 24]; // J1, J3, J6, J12, J24 (si >= 3 échecs)

            const getAncrageStepLabel = (item) => {
                if (!item) return 'J1';
                const sequence = item.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                const days = sequence[item.stepIndex] || sequence[sequence.length - 1];
                return `J${days}${item.isReinforced ? ' (Renforcé)' : ''}`;
            };

            const getAncrageNextStepLabel = (item) => {
                if (!item) return 'J1';
                const sequence = item.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                const nextIdx = item.stepIndex + 1;
                if (nextIdx >= sequence.length) return 'Validation finale & Libération 🏆';
                return `J${sequence[nextIdx]} (dans ${sequence[nextIdx]} jours)`;
            };"""

new_ancrage_setup = """            // Algorithme Anki : Paliers & Intervalles stricts (en jours)
            // J0 = Faute/Aujourd'hui (0j), J1 = Demain (1j), J7 = 7j, J14 = 14j, J28 = 28j
            const STANDARD_INTERVALS = [0, 1, 7, 14, 28];
            const STANDARD_LABELS = ['J0 (Aujourd\'hui)', 'J1 (Demain)', 'J7 (dans 7j)', 'J14 (dans 14j)', 'J28 (dans 28j)'];

            const REINFORCED_INTERVALS = [0, 1, 3, 6, 12, 24];
            const REINFORCED_LABELS = ['J0 (Aujourd\'hui)', 'J1 (Demain)', 'J3 (dans 3j)', 'J6 (dans 6j)', 'J12 (dans 12j)', 'J24 (dans 24j)'];

            const getAncrageStepLabel = (item) => {
                if (!item) return 'J0 (Aujourd\'hui)';
                const labels = item.isReinforced ? REINFORCED_LABELS : STANDARD_LABELS;
                const lbl = labels[item.stepIndex] || labels[labels.length - 1];
                return `${lbl}${item.isReinforced ? ' (Renforcé)' : ''}`;
            };

            const getAncrageNextStepLabel = (item) => {
                if (!item) return 'J1 (dans 1 jour)';
                const intervals = item.isReinforced ? REINFORCED_INTERVALS : STANDARD_INTERVALS;
                const labels = item.isReinforced ? REINFORCED_LABELS : STANDARD_LABELS;
                const nextIdx = item.stepIndex + 1;
                if (nextIdx >= intervals.length) return 'Validation finale & Ancré 🏆';
                const nextDays = intervals[nextIdx];
                const nextLabel = labels[nextIdx];
                return `${nextLabel}`;
            };"""

html = html.replace(old_ancrage_setup, new_ancrage_setup)

# 2. Update handleMultiAnswerSubmit calculation for intervals
old_submit_calc = """                    if (activeQuizMode === 'ancrage') {
                        const targetEntryId = currentQ._ancrageEntryId;
                        setAncrageData(prev => {
                            let entryKey = targetEntryId;
                            if (!entryKey) {
                                const found = Object.values(prev).find(e => e.questionId === questionId && e.status === 'active');
                                if (found) entryKey = found.entryId;
                            }
                            if (!entryKey || !prev[entryKey]) return prev;

                            const existing = prev[entryKey];
                            const sequence = existing.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                            const nextStep = existing.stepIndex + 1;

                            if (nextStep >= sequence.length) {
                                return {
                                    ...prev,
                                    [entryKey]: {
                                        ...existing,
                                        stepIndex: nextStep,
                                        status: 'mastered',
                                        lastReviewTimestamp: todayMs
                                    }
                                };
                            } else {
                                const nextDelayDays = sequence[nextStep];
                                return {
                                    ...prev,
                                    [entryKey]: {
                                        ...existing,
                                        stepIndex: nextStep,
                                        nextReviewTimestamp: todayMs + (nextDelayDays * oneDayMs),
                                        lastReviewTimestamp: todayMs,
                                        status: 'active'
                                    }
                                };
                            }
                        });
                    }"""

new_submit_calc = """                    if (activeQuizMode === 'ancrage') {
                        const targetEntryId = currentQ._ancrageEntryId;
                        setAncrageData(prev => {
                            let entryKey = targetEntryId;
                            if (!entryKey) {
                                const found = Object.values(prev).find(e => e.questionId === questionId && e.status === 'active');
                                if (found) entryKey = found.entryId;
                            }
                            if (!entryKey || !prev[entryKey]) return prev;

                            const existing = prev[entryKey];
                            const intervals = existing.isReinforced ? REINFORCED_INTERVALS : STANDARD_INTERVALS;
                            const nextStep = existing.stepIndex + 1;

                            if (nextStep >= intervals.length) {
                                // Validation Ultime : Ancré et libéré !
                                return {
                                    ...prev,
                                    [entryKey]: {
                                        ...existing,
                                        stepIndex: nextStep,
                                        status: 'mastered',
                                        lastReviewTimestamp: todayMs
                                    }
                                };
                            } else {
                                const nextDelayDays = intervals[nextStep];
                                // Programmation Anki exacte dans nextDelayDays jours !
                                return {
                                    ...prev,
                                    [entryKey]: {
                                        ...existing,
                                        stepIndex: nextStep,
                                        nextReviewTimestamp: todayMs + (nextDelayDays * oneDayMs),
                                        lastReviewTimestamp: todayMs,
                                        status: 'active'
                                    }
                                };
                            }
                        });
                    }"""

html = html.replace(old_submit_calc, new_submit_calc)

# 3. Update tab filters in startAncrageSession for j0, j1, j7, j14, j28
old_session_filters = """                } else if (filter === 'j1') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 0);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J1."); return; }
                } else if (filter === 'j7') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 1);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J7."); return; }
                } else if (filter === 'j14') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 2);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J14."); return; }
                } else if (filter === 'j28') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 3);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J28."); return; }
                }"""

new_session_filters = """                } else if (filter === 'j0') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 0);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J0 (Aujourd'hui)."); return; }
                } else if (filter === 'j1') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 1);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J1 (Demain)."); return; }
                } else if (filter === 'j7') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 2);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J7 (7 jours)."); return; }
                } else if (filter === 'j14') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 3);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J14 (14 jours)."); return; }
                } else if (filter === 'j28') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && !item.isReinforced && item.stepIndex === 4);
                    if (targetEntries.length === 0) { alert("Aucun QCM actuellement à l'étape J28 (28 jours)."); return; }
                }"""

html = html.replace(old_session_filters, new_session_filters)

# 4. Update Tab Bar UI Labels in Ancrage view
old_tabs_ui = """                                                {[
                                                    { id: 'due', label: `⚡ Du Jour (${ancrageDueCount})` },
                                                    { id: 'all', label: `Tout (${ancrageActiveCount})` },
                                                    { id: 'j1', label: `J1 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===0).length})` },
                                                    { id: 'j7', label: `J7 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===1).length})` },
                                                    { id: 'j14', label: `J14 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===2).length})` },
                                                    { id: 'j28', label: `J28 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===3).length})` },
                                                    { id: 'reinforced', label: `🚨 Renforcé (${ancrageReinforcedCount})` },
                                                    { id: 'mastered', label: `🏆 Ancrés (${ancrageMasteredCount})` }
                                                ].map(tab => ("""

new_tabs_ui = """                                                {[
                                                    { id: 'due', label: `⚡ Du Jour (${ancrageDueCount})` },
                                                    { id: 'all', label: `Tout (${ancrageActiveCount})` },
                                                    { id: 'j0', label: `J0 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===0).length})` },
                                                    { id: 'j1', label: `J1 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===1).length})` },
                                                    { id: 'j7', label: `J7 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===2).length})` },
                                                    { id: 'j14', label: `J14 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===3).length})` },
                                                    { id: 'j28', label: `J28 (${ancrageList.filter(i => i.status==='active' && !i.isReinforced && i.stepIndex===4).length})` },
                                                    { id: 'reinforced', label: `🚨 Renforcé (${ancrageReinforcedCount})` },
                                                    { id: 'mastered', label: `🏆 Ancrés (${ancrageMasteredCount})` }
                                                ].map(tab => ("""

html = html.replace(old_tabs_ui, new_tabs_ui)

# 5. Update Tab filter logic in list mapping
old_list_filter_fn = """                                                    if (ancrageTabFilter === 'due') return item.status === 'active' && item.nextReviewTimestamp <= nowMs;
                                                    if (ancrageTabFilter === 'j1') return item.status === 'active' && !item.isReinforced && item.stepIndex === 0;
                                                    if (ancrageTabFilter === 'j7') return item.status === 'active' && !item.isReinforced && item.stepIndex === 1;
                                                    if (ancrageTabFilter === 'j14') return item.status === 'active' && !item.isReinforced && item.stepIndex === 2;
                                                    if (ancrageTabFilter === 'j28') return item.status === 'active' && !item.isReinforced && item.stepIndex === 3;"""

new_list_filter_fn = """                                                    if (ancrageTabFilter === 'due') return item.status === 'active' && item.nextReviewTimestamp <= nowMs;
                                                    if (ancrageTabFilter === 'j0') return item.status === 'active' && !item.isReinforced && item.stepIndex === 0;
                                                    if (ancrageTabFilter === 'j1') return item.status === 'active' && !item.isReinforced && item.stepIndex === 1;
                                                    if (ancrageTabFilter === 'j7') return item.status === 'active' && !item.isReinforced && item.stepIndex === 2;
                                                    if (ancrageTabFilter === 'j14') return item.status === 'active' && !item.isReinforced && item.stepIndex === 3;
                                                    if (ancrageTabFilter === 'j28') return item.status === 'active' && !item.isReinforced && item.stepIndex === 4;"""

html = html.replace(old_list_filter_fn, new_list_filter_fn)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully implemented exact Anki Spaced Repetition Intervals & Step progression!")
