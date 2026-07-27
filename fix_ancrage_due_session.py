import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update addAncrageEntry to make initial failure due today (nowMs) so it appears in today's review session
old_add_entry = """            // Fonction pour ajouter une instance / doublon de QCM en ancrage
            const addAncrageEntry = (questionId) => {
                const todayMs = Date.now();
                const newEntryId = 'ancrage-' + todayMs + '-' + Math.random().toString(36).substr(2, 6);
                
                // Compter les doublons existants pour cette question
                const existingCount = Object.values(ancrageData).filter(item => item.questionId === questionId).length;

                setAncrageData(prev => ({
                    ...prev,
                    [newEntryId]: {
                        entryId: newEntryId,
                        questionId: questionId,
                        instanceNumber: existingCount + 1,
                        stepIndex: 0,
                        failureCount: 0,
                        isReinforced: false,
                        nextReviewTimestamp: todayMs + (1 * 24 * 3600 * 1000),
                        lastReviewTimestamp: todayMs,
                        status: 'active',
                        addedDate: new Date().toISOString()
                    }
                }));
            };"""

new_add_entry = """            // Fonction pour ajouter une instance / doublon de QCM en ancrage
            const addAncrageEntry = (questionId) => {
                const todayMs = Date.now();
                const newEntryId = 'ancrage-' + todayMs + '-' + Math.random().toString(36).substr(2, 6);
                
                // Compter les doublons existants pour cette question
                const existingCount = Object.values(ancrageData).filter(item => item.questionId === questionId).length;

                setAncrageData(prev => ({
                    ...prev,
                    [newEntryId]: {
                        entryId: newEntryId,
                        questionId: questionId,
                        instanceNumber: existingCount + 1,
                        stepIndex: 0,
                        failureCount: 0,
                        isReinforced: false,
                        nextReviewTimestamp: todayMs, // À réviser immédiatement aujourd'hui !
                        lastReviewTimestamp: todayMs,
                        status: 'active',
                        addedDate: new Date().toISOString()
                    }
                }));
            };"""

html = html.replace(old_add_entry, new_add_entry)

# 2. Fix startAncrageSession to STRICTLY respect due dates without fallback to future QCMs
old_start_session = """            const startAncrageSession = (filter = 'due') => {
                let targetEntries = [];
                if (filter === 'due') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && item.nextReviewTimestamp <= nowMs);
                    if (targetEntries.length === 0) {
                        targetEntries = ancrageList.filter(item => item.status === 'active');
                    }
                } else if (filter === 'reinforced') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && item.isReinforced);
                } else {
                    targetEntries = ancrageList.filter(item => item.status === 'active');
                }

                if (targetEntries.length === 0) {
                    alert("Aucun QCM dans votre boîte d'ancrage mémoriel pour le moment !");
                    return;
                }"""

new_start_session = """            const startAncrageSession = (filter = 'due') => {
                let targetEntries = [];
                if (filter === 'due') {
                    // STRICTEMENT les QCM dont l'échéance est aujourd'hui ou dépassée
                    targetEntries = ancrageList.filter(item => item.status === 'active' && item.nextReviewTimestamp <= nowMs);
                    if (targetEntries.length === 0) {
                        alert("🎉 Aucun QCM à réviser aujourd'hui ! Vos prochaines révisions espacées (J1, J7, J14, J28) sont programmées pour les jours à venir.\\n\\nSi vous souhaitez quand même réviser par avance, utilisez le bouton '🎯 Réviser Tout'.");
                        return;
                    }
                } else if (filter === 'reinforced') {
                    targetEntries = ancrageList.filter(item => item.status === 'active' && item.isReinforced);
                    if (targetEntries.length === 0) {
                        alert("Aucun QCM en mode renforcé pour le moment.");
                        return;
                    }
                } else {
                    targetEntries = ancrageList.filter(item => item.status === 'active');
                    if (targetEntries.length === 0) {
                        alert("Votre boîte d'ancrage mémoriel est vide pour le moment.");
                        return;
                    }
                }"""

html = html.replace(old_start_session, new_start_session)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully fixed startAncrageSession to strictly filter due QCMs!")
