---
audio: false
generated: false
image: true
lang: fr
layout: post
title: Un ingénieur exigeant sur les outils de codage en IA
translated: true
---

Récemment, j'ai réussi à exécuter Claude Code, alors je veux partager mon parcours de sélection d'outils. J'ai également collecté quelques [conseils sur les outils IA](ai-tips-en) en cours de route.

J'ai été assez en retard à adopter Claude Code.

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet) a été lancé vers la fin de février 2025.

Je n'ai pas réussi à l'essayer avant récemment. Une des raisons est qu'il nécessite l'API d'Anthropic, qui ne prend pas en charge les cartes Visa chinoises.

Une autre raison est que [Claude Code Router](https://github.com/musistudio/claude-code-router) est devenu disponible, ce qui a rendu ma récente tentative réussie.

J'entends souvent des éloges à son sujet. J'ai essayé le CLI Gemini en juillet 2025 mais j'ai abandonné après plusieurs tentatives infructueuses pour le faire corriger mon code.

J'ai également essayé Aider, un autre agent logiciel. J'ai arrêté d'utiliser Cursor après environ six mois car de nombreux plugins basés sur VSCode ne fonctionnaient pas correctement. J'ai brièvement expérimenté Cline mais ne l'ai pas adopté.

J'utilise le plugin Copilot dans VSCode avec un modèle personnalisé, Grok 3 beta via OpenRouter, ce qui fonctionne bien.

Je ne pense pas que Claude Code changera mes habitudes, mais puisque je peux l'exécuter avec succès et que j'ai la patience d'essayer quelques fois de plus, je verrai comment je me sentirai dans les semaines à venir.

Je suis un utilisateur exigeant avec 10 ans d'expérience en ingénierie logicielle. J'espère que les outils sont excellents dans la pratique. Je ne me fie pas à la marque – je me soucie seulement de l'utilité quotidienne.

Après avoir utilisé Claude Code pour corriger la grammaire de ce post, j'ai constaté qu'il fonctionne bien dans certains scénarios. Bien que j'apprécie l'IA pour l'aide grammaticale (j'ai même écrit un script Python pour appeler les API LLM à cette fin), j'ai remarqué un schéma frustrant - même lorsque je demande des corrections minimales, les outils continuent de proposer de nombreuses suggestions grammaticales à examiner. Ce processus de vérification manuelle contredit le but de l'automatisation. En compromis, je laisse maintenant l'IA s'occuper de l'ensemble des essais, bien que cette approche limite mes opportunités d'apprentissage puisque je ne vois pas les corrections spécifiques apportées.

Ce qui m'a le plus impressionné, c'est la façon dont Claude Code affiche les modifications - en montrant des comparaisons avant/après similaires aux diffs git, ce qui rend la révision des modifications beaucoup plus facile.

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Source : Capture d'écran personnelle*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Source : Capture d'écran personnelle*{: .caption }