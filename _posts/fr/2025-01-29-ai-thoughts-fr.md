---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Workflows IA, Éditeurs de Code et Perturbation des Plateformes
translated: true
---

### Table des matières

1. [Réflexions sur l'IA](#ai-thoughts)
   - L'IA manque de véritable intelligence ou profondeur
   - L'apprentissage automatique est du calcul appliqué avancé
   - Les LLM peinent avec les formats de fichiers structurés
   - L'open source élimine le secret technologique
   - Les outils textuels seront disruptés en premier par l'IA

2. [Nouvelles plateformes alimentées par des workflows IA](#new-platforms-powered-by-ai-workflows)
   - Les workflows IA automatisent la génération de contenu multilingue
   - Les utilisateurs soumettent des requêtes pour la conversion de format
   - Les plateformes permettent l'affinage et la synthèse du contenu
   - Workflows IA personnalisables via des paramètres de mots-clés
   - L'IA gère la transformation du contenu de bout en bout

3. [La prochaine direction des éditeurs de code IA](#the-next-direction-of-ai-code-editors)
   - L'intégration cloud est essentielle pour les workflows CI/CD
   - Les tests A/B améliorent le contenu généré par l'IA
   - Le RLHF s'étend aux retours de déploiement en situation réelle
   - Les retours humains améliorent les sorties imparfaites de l'IA
   - L'optimisation des prompts surpasse la correction des sorties

## Réflexions sur l'IA

*Dernière mise à jour en août 2025*

- Satya Nadella a mentionné le paradoxe de Jevons. Cela vaut la peine d'être étudié.

- Yin Wang : Il n'y a pas d'"intelligence" dans l'intelligence artificielle, pas de "neural" dans les réseaux de neurones, pas d'"apprentissage" dans l'apprentissage automatique, et pas de "profondeur" dans l'apprentissage profond. Ce qui fonctionne vraiment dans ce domaine s'appelle le "calcul". Je préfère donc appeler ce domaine "calcul différentiable", et le processus de construction de modèles "programmation différentiable".

- Yin Wang : L'apprentissage automatique est une théorie vraiment utile, voire belle, car ce n'est rien d'autre que du calcul revisité ! C'est la vieille et grande théorie de Newton et Leibniz, sous une forme plus simple, élégante et puissante. L'apprentissage automatique utilise essentiellement le calcul pour dériver et ajuster certaines fonctions, et l'apprentissage profond ajuste des fonctions plus complexes.

- Actuellement, les modèles de langage ne peuvent pas filtrer par langage de fichier comme YAML ou Python. Pourtant, une partie significative de l'information dans le monde réel est organisée ainsi. Nous pourrions entraîner des modèles de langage sur des fichiers.

- Pour l'entraînement des modèles de langage, nous pourrions développer un système de correspondance exacte. Peut-être combiner l'algorithme de recherche KMP (Knuth-Morris-Pratt) avec l'architecture des transformers pour améliorer les capacités de recherche.

- Il n'y a pas de secrets technologiques. L'open source révèlera tous les secrets jalousement gardés.

- L'IA affectera de nombreux outils, même indirectement. Certains disent qu'ils n'auront plus besoin de Figma pour dessiner des prototypes et iront directement au codage. Postman connaîtra un sort similaire ; les gens utiliseront directement Python ou d'autres scripts pour appeler ou tester des API.

- Une raison pour laquelle nous n'utilisons pas Postman ou Figma à l'ère de l'IA est que leurs fonctionnalités ne peuvent pas être générées via du texte. Ils n'ont pas non plus de raccourci comme commande + K pour déclencher le remplacement de composants.

- Les interfaces utilisateur deviennent un obstacle à l'ère de l'IA. Pourquoi mettre à jour Postman pour le testing assisté par IA alors qu'on peut directement utiliser la bibliothèque `requests` de Python ou d'autres langages, qui seront aussi alimentés par l'IA ?

- Pourquoi mettre à jour Figma pour la création d'UI assistée par IA alors que la génération d'UI via du code, boostée par l'IA, offre une approche plus directe et puissante ?

- Les LLM changeront d'abord les applications textuelles : Google, les moteurs de recherche, les éditeurs de texte, Quizlet, Zendesk, DeepL, Medium, WordPress, Trello, Asana, Gmail, GitHub, Goodreads, Duolingo et Feedly.

- À l'inverse, les LLM ne révolutionneront pas des technologies comme Git, Linux, ffmpeg, les téléphones, le matériel, les navigateurs, les systèmes d'exploitation ou les appels voix/vidéo. Ces technologies sont centrées sur le code, qui n'est pas facilement générable par l'IA, contrairement aux outils de test d'API comme Postman.

- Les technologies avec beaucoup de code sont difficiles à révolutionner par l'IA, comme OpenOffice, MySQL, Mozilla Firefox, Chromium, VLC, Qt, LLVM/Clang et GNOME. Si l'IA pouvait aider à les créer, elles ne seraient pas remplacées. L'IA a besoin de plus de puissance pour générer autant de code.

- Les LLM apportent du changement de deux façons : en modifiant le contenu d'une plateforme (traduction dans TikTok) ou en remplaçant carrément des logiciels (Postman, Google Search).

- Les outils audio IA changent aussi les choses : en générant des livres audio pour Audible ou en remplaçant des applis comme Sing songs, car l'IA peut désormais faire ce que les humains faisaient.

- Mesurer l'impact de l'IA : évaluer la quantité de contenu ou de code pouvant être généré/amélioré par l'IA, partiellement ou totalement. L'IA peut aussi aider à inventer de nouveaux logiciels.

- Trois types de produits : produits d'IA générative, produits utilisant leurs API, et autres produits.

- Une idée : utiliser l'IA pour agréger des infos en temps réel depuis Reddit, GitHub Trending, Twitter, Quora et Zhihu. Les utilisateurs personnalisent leur flux via des prompts.

- Cinq types de données importants : texte, image, audio, vidéo et code.

- Autres types de données : numériques, géospatiales, biométriques, capteurs, transactions, métadonnées, séries temporelles, structurées/non structurées, santé, environnement, logs, réseau et comportement.

- Google reste meilleur pour l'indexation de sites, surtout pour télécharger des logiciels ou documents spécifiques. Un LLM n'a pas forcément les liens les plus récents.

- Google fonctionne comme une recherche par domaine ; pour aller sur un dépôt Maven et vérifier une version, c'est utile.

- Google reste utile pour la recherche d'images, tandis que les LLM excellent en génération de texte. Mais les gens préfèrent les vraies images pour vérifier des détails matériels ou des formes.

- Les chatbots IA sont populaires car le texte est plus dur à traiter que les images. Les images générées par IA ont un potentiel inexploité : demander des angles différents, zoomer sur des visages ou des circuits. Mais comme les gens travaillent plus avec du texte, les outils d'image IA ont une marge de progression.

- L'IA excelle pour expliquer des concepts. Les utilisateurs peuvent poser des questions sur n'importe quel détail. C'est probablement son utilité principale.

- J'ai utilisé l'IA pour comprendre les LLM. Le moment où elle m'a expliqué K, Q et V était génial.

- Depuis les LLM, je préfère Ubuntu car les apps colorées de macOS m'intéressent moins. Je préfère tout faire via le terminal et le texte.

- On peut évaluer l'IA sur sa capacité à mettre à jour un fichier `pom.xml` ou `requirements.txt`, vérifier les bibliothèques. C'est un travail complexe.

- À l'ère de l'IA, les langages performants et robustes gagnent en importance. La syntaxe compte moins, car les LLM génèrent le code.

- Les gens lisent tout via les chatbots IA car c'est facile, on peut poser des questions, le format est cohérent et la qualité est souvent excellente.

- Mais l'info ne se limite pas au texte. Avec les chatbots, on perd le site original, sa mise en page, ses images et son design.

- Les sites très interactifs (jeux web, Google Docs, Sheets, Zoom, Slack) seront peu affectés par l'IA. Ils sont centrés sur le code, pas juste le texte.

- Faire des fautes de frappe ou créer des prompts précis demande des efforts. Une banque ou un réseau social uniquement basé sur un chatbot IA ne fonctionne pas. Les boutons et la navigation traditionnelle restent plus pratiques.

- [Comment je vis bien à l'ère de l'IA et de la blockchain](./ai-blockchain-fr)

---

## Nouvelles plateformes alimentées par des workflows IA

*08.01.2025*

- Les workflows sont des systèmes où les LLM et outils sont orchestrés via des chemins de code prédéfinis.[^1]

- Imaginez une nouvelle plateforme (comme TikTok, Quora, X, Instagram, WhatsApp, etc.) entièrement alimentée par la traduction IA.

- Chaque publication ou réponse est sauvegardée dans une langue, puis traduite automatiquement en 20 langues, selon la préférence des utilisateurs.

- Outre la traduction, d'autres fonctionnalités IA (synthèse, génération audio/vidéo) jouent un rôle clé. L'utilisateur soumet un prompt, et la plateforme fait le reste.

- Les utilisateurs peuvent uploader du texte, images, audio ou vidéo, et la plateforme convertit automatiquement le contenu dans d'autres formats. Ils choisissent comment le recevoir.

- Les plateformes peuvent générer des synthèses, avec différents types disponibles en plusieurs langues.

- L'IA peut aider à générer, affiner, améliorer, corriger, synthétiser, étendre ou convertir tout contenu sur la plateforme.

- Les utilisateurs personnalisent la plateforme avec des mots-clés comme "anglais" ou "drôle" pour ajuster le style des workflows IA. Une fois configuré, l'IA adapte le contenu.

[^1]: Construire des agents efficaces, [Anthropic](https://www.anthropic.com/research/building-effective-agents)

---

## La prochaine direction des éditeurs de code IA

*08.01.2025*

Récemment, j'ai travaillé sur un pipeline `xelatex` pour GitHub Actions.

J'ai eu un problème avec le package `fontawesome5` dans le flux GitHub. La solution de 4o-mini (installer TeX Live 2021 et utiliser `tlmgr`) n'a pas fonctionné. Cependant, 4o a suggéré une meilleure approche : passer à TeX Live 2023. Bien que cela n'ait pas tout résolu, la situation s'est améliorée.

J'ai utilisé ChatGPT pour comprendre le problème. Pour plus de détails, voir [Ce que ChatGPT O1 peut faire que 4o-mini ne peut pas](./o1-fr).

Je n'ai pas utilisé des éditeurs comme Cursor ou Windsurf, car ils ne captent que les sorties locales, ce qui limite leur utilité dans les environnements cloud.

Dans les workflows comme GitHub Actions ou Jenkins, les éditeurs de code doivent mieux s'intégrer au cloud et aux processus CI/CD.

Cette intégration s'applique aussi aux outils de création de contenu (texte, images, audio, vidéo). Ils devraient être couplés à des systèmes de tests A/B. L'IA génère, et les tests A/B fournissent des retours, comme dans le Reinforcement Learning from Human Feedback (RLHF), mais étendu aux environnements réels.

Les tests peuvent être instantanés ou longs, automatisés ou assistés par des humains. Si automatisés (comme des tests A/B), l'IA s'améliore en fonction des résultats. Avec une assistance humaine, les retours sont plus subjectifs ("pas assez drôle", "améliorer un détail"), mais permettent d'affiner les résultats.

En théorie, toutes les règles humaines peuvent être écrites comme des prompts (utilisateur ou système). Il vaut mieux améliorer les prompts que corriger les sorties à chaque fois.