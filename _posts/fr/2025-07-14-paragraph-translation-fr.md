---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Optimisation des coûts de traduction avec le Markdown par paragraphe
translated: true
---

Mon blog Jekyll utilise Markdown pour rédiger des paragraphes. Après avoir écrit en anglais, j'utilise des outils d'IA comme DeepSeek ou Mistral pour traduire dans huit autres langues. Bien qu'ils soient déjà peu coûteux, il y a encore place à l'amélioration.

Parfois, je modifie simplement un mot ou un paragraphe, et ensuite tout le texte d'un article est traduit dans les huit autres langues. Dans ce cas, l'utilisation des tokens est élevée. Si je ne traduis qu'un seul paragraphe à nouveau, l'utilisation des tokens sera plus faible, surtout pour les longs articles.

Cependant, je veux toujours utiliser Markdown pour enregistrer mes idées. Utiliser une base de données pour maintenir et mettre à jour les articles n'est pas pratique. Utiliser YAML ou JSON pourrait être trop encombrant également.

Le point clé est d'identifier les différences entre le texte avant et après la modification. Si nous utilisons une approche basée sur les paragraphes, cela signifie utiliser le caractère de nouvelle ligne "\n" pour diviser le texte.

Je dois savoir quels paragraphes ont changé et lesquels n'ont pas changé après la modification. Nous devons connaître les correspondances un à un des paragraphes entre le texte avant et après la modification.

Nous utilisons une approche basée sur les paragraphes car nous voulons mettre à jour les traductions faites par les modèles d'IA. Si nous utilisons des phrases, cela pourrait ne pas être aussi précis.

Pour Markdown, il pourrait être plus important d'utiliser une analyse Markdown pour synchroniser les traductions en fonction des éléments Markdown.

Mais si aucun bloc de code ou syntaxe Markdown spéciale n'est présent, nous pouvons utiliser une approche basée sur les paragraphes.

Pour une approche simple basée sur les paragraphes, nous avons deux tableaux de paragraphes et nous devons savoir comment ils correspondent.

Lors de la comparaison de n'importe quel paragraphe dans ces deux tableaux, il y a deux résultats possibles : ils sont identiques ou différents. S'ils sont différents, il y a plusieurs cas : les deux sont nouvellement ajoutés, celui de gauche est nouvellement ajouté, ou celui de droite est nouvellement ajouté.

Je veux simplement économiser des coûts, donc je veux réduire l'utilisation des tokens. Je n'ai besoin de rien d'autre. Je veux simplement traduire chaque paragraphe, mettre en cache le résultat, et la prochaine fois, pour chaque paragraphe, je chercherai d'abord le résultat de la traduction. S'il n'existe pas, alors je devrai le traduire à nouveau.

Pour Markdown, c'est un peu plus compliqué. Je ne veux pas traduire les blocs de code. Donc, nous pouvons d'abord utiliser une bibliothèque d'analyse Markdown pour traiter les blocs de code et le texte normal différemment.