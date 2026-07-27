import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace obsolete REINFORCED_DELAYS and key={item.questionId} in the map function
old_map_item = """                                                }).map((item) => {
                                                    const q = questions.find(qItem => qItem.id === item.questionId);
                                                    if (!q) return null;
                                                    const targetSub = subjects.find(s => s.id === q.subjectId);
                                                    const isDue = item.status === 'active' && item.nextReviewTimestamp <= nowMs;
                                                    const sequence = item.isReinforced ? REINFORCED_DELAYS : STANDARD_DELAYS;
                                                    const daysLeft = Math.max(0, Math.ceil((item.nextReviewTimestamp - nowMs) / (24 * 3600 * 1000)));

                                                    return (
                                                        <div key={item.questionId} className={`p-6 rounded-3xl border-2 transition-all space-y-4 ${"""

new_map_item = """                                                }).map((item) => {
                                                    const q = questions.find(qItem => qItem.id === item.questionId);
                                                    if (!q) return null;
                                                    const targetSub = subjects.find(s => s.id === q.subjectId);
                                                    const isDue = item.status === 'active' && item.nextReviewTimestamp <= nowMs;
                                                    const sequence = item.isReinforced ? REINFORCED_INTERVALS : STANDARD_INTERVALS;
                                                    const daysLeft = Math.max(0, Math.ceil((item.nextReviewTimestamp - nowMs) / (24 * 3600 * 1000)));

                                                    return (
                                                        <div key={item.entryId || item.questionId} className={`p-6 rounded-3xl border-2 transition-all space-y-4 ${"""

html = html.replace(old_map_item, new_map_item)

# Also fix any remaining REINFORCED_DELAYS or STANDARD_DELAYS references
html = html.replace('REINFORCED_DELAYS', 'REINFORCED_INTERVALS')
html = html.replace('STANDARD_DELAYS', 'STANDARD_INTERVALS')
html = html.replace("l'algorithme", "l’algorithme")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully fixed Ancrage page load crash!")
