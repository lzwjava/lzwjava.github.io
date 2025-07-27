---
audio: false
generated: false
image: true
lang: fr
layout: post
title: Un ingénieur exigeant sur les outils de codage IA
translated: true
---

Récemment, j'ai réussi à exécuter Claude Code, alors je veux partager mon parcours de sélection d'outils. J'ai également collecté quelques [Astuces d'Outils IA](ai-tips-en.md) en cours de route.

J'ai été assez en retard à adopter Claude Code.

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet) a été lancé vers la fin de février 2025.

Je n'ai pas réussi à l'essayer jusqu'à récemment. Une raison est qu'il nécessite l'API Anthropic, qui ne prend pas en charge les cartes Visa chinoises.

Une autre raison est que [Claude Code Router](https://github.com/musistudio/claude-code-router) est devenu disponible, ce qui a rendu ma récente tentative réussie.

J'entends souvent des éloges à son sujet. J'ai essayé le CLI Gemini en juillet 2025 mais j'ai abandonné après plusieurs tentatives infructueuses pour le faire corriger mon code.

J'ai également essayé Aider, un autre agent logiciel. J'ai arrêté d'utiliser Cursor après environ six mois car de nombreux plugins basés sur VSCode ne fonctionnaient pas. De plus, je ne veux pas donner trop de crédit à Cursor car il est construit sur VSCode. Comme le plugin Copilot dans VSCode s'est récemment amélioré et ne se situe pas loin derrière, je préfère l'utiliser plus souvent.

Cependant, VSCode est construit sur Electron, une technologie open source. Il est difficile d'attribuer le mérite à la bonne équipe ou à la bonne personne. Étant donné que de nombreuses grandes entreprises et startups profitent des projets open source, je dois me concentrer sur mon budget et sur ce qui me convient le mieux. Je ne devrais pas trop m'inquiéter de donner du crédit. Je préfère utiliser des outils abordables et efficaces.

J'ai brièvement expérimenté Cline mais ne l'ai pas adopté.

J'utilise le plugin Copilot dans VSCode avec un modèle personnalisé, Grok 3 beta via OpenRouter, ce qui fonctionne bien.

Je ne pense pas que Claude Code changera mes habitudes, mais puisque je peux l'exécuter avec succès et que j'ai la patience de l'essayer quelques fois de plus, je verrai comment je me sentirai dans les semaines à venir.

Je suis un utilisateur exigeant avec 10 ans d'expérience en ingénierie logicielle. J'espère que les outils seront excellents en utilisation réelle. Je ne me fie pas à la marque—je me soucie seulement de l'utilité quotidienne.

Après avoir utilisé Claude Code pour corriger la grammaire de ce post, j'ai constaté qu'il fonctionne bien dans certains scénarios. Bien que j'apprécie l'aide de l'IA pour la grammaire (j'ai même écrit un script Python pour appeler les API LLM à cette fin), j'ai remarqué un schéma frustrant - même lorsque je demande des corrections minimales, les outils continuent de proposer de nombreuses suggestions de grammaire à examiner. Ce processus de vérification manuelle contredit le but de l'automatisation. En compromis, je laisse maintenant l'IA gérer des essais entiers, bien que cette approche limite mes opportunités d'apprentissage puisque je ne vois pas les corrections spécifiques qui sont faites.

Ce qui m'a le plus impressionné, c'est la façon dont Claude Code affiche les modifications - en montrant des comparaisons avant/après similaires aux diffs git, ce qui rend la révision des modifications beaucoup plus facile.

Après une journée, j'ai utilisé Claude pour corriger du code également. Cependant, je continue d'utiliser le plugin Copilot avec le modèle Grok 3 beta, car il est simple et facile pour moi.

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Source : Capture d'écran personnelle*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Source : Capture d'écran personnelle*{: .caption }

{: .centered }
![](assets/images/claude/vscode-fix.jpg){: .responsive }
*Source : Capture d'écran personnelle*{: .caption }