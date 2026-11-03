# Mémoire de reprise — med-prep-app

## Projet
- Dépôt : `https://github.com/jaikasler-ai/de.git`
- Branche : `main`
- Application principale : `index.html` (React/Babel autonome, banque dans `INITIAL_QUESTIONS`).
- Archive d’origine : `/home/zty/Téléchargements/filemail.com - l,k,.zip`.

## Données importantes
- UE SHS : `subjectId: s12`.
- UE CCB : `subjectId: s_ccb`.
- Les QCM SHS sont répartis dans 14 fiches.
- Les séries utilisent `openUEConfig()` puis `launchConfiguredQuiz()`.
- Biostatistiques utilise aussi `isDp`, `dpId`/`dpTitle` et `dpStep` pour les Dossiers Progressifs.

## Correctif appliqué
Le lancement d’une série pouvait planter pour un import ancien utilisant `options` au lieu de `answers`, à cause de `[...]q.answers`. `index.html` contient maintenant `prepareQuestionForQuiz()`, qui accepte les deux formats et garantit `id`, `text`, `correct`, `explanation` et un tableau `answers`. Les chemins de lancement utilisent cette normalisation avant de mélanger les réponses.

## Vérifications à effectuer
1. Lancer une série globale SHS.
2. Lancer une série depuis chacune des 14 fiches SHS.
3. Tester CCB et Biostat (QCM simples + DP).
4. Vérifier la console : aucune erreur `q.answers is not iterable`.
5. Valider la syntaxe de `INITIAL_QUESTIONS`.
6. Contrôler `git diff`, pousser `main`, puis synchroniser `gh-pages` pour GitHub Pages.

## Règles
- Ne pas supprimer de QCM ou d’image sans demande explicite.
- Conserver les clés de correction et explications.
- Tout nouvel import doit être classé dans la fiche UE correspondante et dans un chapitre CCB séparé si demandé.
- Vérifier le rendu et le déploiement, pas seulement le commit local.
