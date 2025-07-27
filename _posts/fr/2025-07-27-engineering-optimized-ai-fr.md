---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Optimiser l'ingénierie logicielle pour l'IA
translated: true
---

Dans ce blog, j'ai utilisé des centaines de scripts pour aider à la traduction, au playground, à la maintenance des frontmatters et aux bots Telegram. Je pense que cette approche de développement pourrait représenter l'avenir de l'ingénierie logicielle optimisée pour l'IA.

Je ne me fie pas beaucoup aux fonctionnalités des modules Python, ni ne souhaite structurer le code comme un grand projet Java Spring.

J'ai travaillé comme consultant pour plusieurs projets bancaires ces dernières années. J'ai observé une architecture bancaire impressionnante, des microservices, une conception multi-pays efficace pour éliminer les doublons autant que possible, un cadre fondamental robuste construit sur Spring, et une gouvernance solide avec une configuration centralisée.

Bien que leur architecture bancaire soit impressionnante, si nous devions commencer aujourd'hui, je considérerais optimiser pour LLM/IA. Cela impliquerait une meilleure ingénierie de contexte, une meilleure séparation des contextes, et la priorisation de la pensée IA-first plutôt que de la conception centrée sur l'humain. Bien que Spring offre plusieurs niveaux et une bonne abstraction, il peut être difficile pour LLM/IA de naviguer.

Je pense que nous devrions viser des structures plus plates, similaires à une organisation plate. Cela signifie utiliser seulement deux niveaux : le premier niveau appelle le second niveau. Dans une fonction, il est préférable d'appeler directement 50 autres fonctions plutôt que d'avoir 50 niveaux ou piles imbriqués. L'IA/LLM a du mal à juger ou à inférer des structures complexes et imbriquées, mais elles excellent dans la gestion de petites fonctions de 100 à 200 lignes de code. Python est bien adapté pour appeler et importer depuis d'autres fichiers.

Une raison pour laquelle le code Python est plus facile que Java est que sa gestion des dépendances est simple. Il suffit d'utiliser `pip install` pour ajouter une dépendance. Avec Maven, il faut écrire la dépendance dans un fichier POM XML, puis utiliser `mvn compile` pour que Maven télécharge les dépendances.

Une autre raison de la simplicité de Python est que son code peut être exécuté directement sans difficulté.

Bien que, à partir de Java 11, la commande `java` puisse exécuter directement des programmes de code source à fichier unique sans avoir besoin de les compiler séparément avec `javac`, souvent, pour les projets Java, ils sont grands, donc il faut les exécuter avec `mvn spring-boot:run` ainsi que certaines configurations de propriétés.

Une troisième raison est que la conception des modules Python est simple ; vous pouvez utiliser `from` et `import` pour importer facilement du code depuis d'autres fichiers.

Pour l'instant, de nombreux chatbots IA peuvent exécuter directement du code Python dans la fenêtre du chatbot, comme Grok.

Lors de la comparaison de 100 fichiers Java, chacun contenant environ 1000 lignes de code, avec quelques scripts Python simples, ce n'est pas une comparaison équitable. Pour ce type de projet, je préférerais avoir 1000 fichiers Python, chacun contenant environ 100 lignes de code.

Il est acceptable de sélectionner des lignes de code ou une fonction pour les modifier. Cependant, il faut savoir où sélectionner. Pourquoi ne pas laisser cette tâche être gérée par l'IA pour nous faciliter la vie ? Ainsi, nous n'avons qu'à utiliser "sélectionner tout" pour sélectionner tout le code et dire à l'IA/LLM comment le modifier.

Pour Python, il est plus facile d'utiliser `if __name__ == "__main__":` pour exécuter et tester des fonctions dans un fichier. Il est également plus facile pour d'autres fichiers Python d'appeler les fonctions à l'intérieur de ce fichier sans avoir besoin d'exécuter le test.

C'est de l'ingénierie de contexte optimisée pour l'IA. Pourrions-nous l'aborder autrement ? L'IA/LLM est auto-régressive. Cependant, lorsque nous utilisons Copilot ou Claude Code, nous ne savons pas comment l'Agent Logiciel IA nous aide. Ils devraient y penser à notre place.

Pourrions-nous, du côté utilisateur, organiser le code spécifiquement pour réduire l'utilisation des tokens ? Pour ce point, l'approche consistant à avoir 1000 fichiers Python avec chacun 100 lignes de code est bonne à cet effet. Parce que vous pouvez vérifier les fonctions et les fichiers de code facilement avant de laisser d'autres codes Python les appeler.

Mais un problème est que si vous voulez modifier plusieurs fichiers de code ensemble, ce n'est pas facile à faire. Pour une méthode simple, vous pouvez copier le code dans les chatbots IA et leur demander comment modifier le code dans ces fichiers.

Possiblement, nous n'avons pas besoin d'utiliser le nombre de lignes pour séparer les fonctions ou la logique. Mais nous devrions le faire pour séparer la logique en petites fonctions. Nous pouvons le faire en les séparant naturellement par type de logique, afin qu'elles paraissent plus courtes.

Pourquoi voulons-nous une ingénierie logicielle optimisée pour l'IA ? Parce que l'IA est puissante, nous devrions optimiser tout pour l'IA et ensuite laisser l'IA aider l'ingénierie logicielle autant que possible.

Cela est possible non seulement pour le code, mais aussi pour tout texte. Supposons que nous soyons des éditeurs très pointilleux ; nous ne voulons pas qu'IA modifie nos grands textes d'un seul coup. Nous voulons vérifier paragraphe par paragraphe. Pour le code, nous pouvons tolérer de petites erreurs ou bugs. Pour le texte, nous pouvons les tolérer car la plupart des lecteurs ne sont pas si pointilleux.

Mais le code est différent en ce sens que parfois, même une petite erreur peut entraîner le dysfonctionnement complet d'un grand projet.

Pour les fichiers XML ou YAML, nous n'avons probablement pas besoin de les séparer autant car ils sont déjà très structurés.

Et pour les fichiers HTML, nous devrions faire une certaine séparation. Au lieu d'écrire des centaines de fichiers JavaScript avec des centaines de fichiers HTML, ce qui rend facile de dépasser 1000 lignes de code, nous devrions utiliser `import` pour JavaScript pour gérer cela. Pour le code JavaScript, nous pouvons utiliser les méthodes ci-dessus pour séparer.

Nous voulons structurer le code de manière à ce que l'IA puisse facilement ajouter, modifier, supprimer et exécuter du code. C'est le début. Imaginez un jour où tout le code peut être généré ou corrigé facilement par l'IA. Le monde sera très numérisé.

Imaginez-moi écrivant 100 grands projets logiciels et fournissant des API pour les connecter aux autres. Cela inclut mon agenda quotidien ; je suis, moi-même, comme une entreprise technologique de 1000 employés de nos jours. Ils sont personnalisés pour mes besoins, pour gagner de l'argent ou dépenser de l'argent pour mon bénéfice. C'est vraiment incroyable.