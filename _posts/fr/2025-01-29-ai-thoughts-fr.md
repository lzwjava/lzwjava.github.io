---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Flux de Travail IA, Éditeurs de Code et Perturbation des Plateformes
translated: true
---

### Table des matières

1. [Réflexions sur l'IA](#ai-thoughts)
   - L'IA manque d'intelligence ou de profondeur réelle
   - Le machine learning est du calcul appliqué avancé
   - Les modèles de langage peinent avec les formats de fichiers structurés
   - L'open source élimine le secret technologique
   - Les outils basés sur le texte sont les premiers touchés par l'IA

2. [Nouvelles plateformes alimentées par des workflows IA](#new-platforms-powered-by-ai-workflows)
   - Les workflows IA automatisent la génération de contenu multilingue
   - Les utilisateurs soumettent des requêtes pour la conversion de format
   - Les plateformes permettent l'affinage et la synthèse de contenu
   - Workflows IA personnalisables via des paramètres par mots-clés
   - L'IA gère la transformation de contenu de bout en bout

3. [L'avenir des éditeurs de code alimentés par l'IA](#the-next-direction-of-ai-code-editors)
   - L'intégration cloud est cruciale pour les workflows CI/CD
   - Les tests A/B améliorent le contenu généré par l'IA
   - Le RLHF s'étend aux retours de déploiement en situation réelle
   - Les retours humains affinent les sorties imparfaites de l'IA
   - L'optimisation des requêtes surpasse la correction des résultats


## Réflexions sur l'IA

*Dernière mise à jour en août 2025*

- Satya Nadella a évoqué le paradoxe de Jevons. Cela vaut la peine de s'y intéresser.

- Yin Wang : Il n'y a pas "d'intelligence" dans l'intelligence artificielle, pas de "neural" dans les réseaux neuronaux, pas "d'apprentissage" dans le machine learning, et pas de "profondeur" dans le deep learning. Ce qui fonctionne vraiment dans ce domaine s'appelle le "calcul". Je préfère donc appeler ce domaine "calcul différentiable", et le processus de construction de modèles "programmation différentiable".

- Yin Wang : Le machine learning est une théorie vraiment utile, voire belle, car ce n'est que du calcul remanié ! C'est la grande et ancienne théorie de Newton et Leibniz, sous une forme plus simple, élégante et puissante. Le machine learning consiste essentiellement à utiliser le calcul pour dériver et ajuster certaines fonctions, et le deep learning à ajuster des fonctions plus complexes.

- Actuellement, les grands modèles de langage (LLM) ne peuvent pas filtrer par format de fichier comme YAML ou Python. Pourtant, une grande partie de l'information dans le monde réel est organisée ainsi. On pourrait donc entraîner des LLM avec des fichiers.

- Pour l'entraînement des LLM, on pourrait développer un système de correspondance exacte. Peut-être combiner l'algorithme de recherche KMP (Knuth-Morris-Pratt) avec l'architecture des transformers pour améliorer les capacités de recherche.

- Il n'y a pas de secrets technologiques. L'open source révèlera tous les secrets jalousement gardés.

- L'IA affectera de nombreux outils, même indirectement. On dit qu'on n'aura plus besoin de Figma pour dessiner des prototypes, on ira directement au code. Je pense que Postman suivra le même chemin ; les gens utiliseront directement Python ou d'autres scripts pour appeler ou tester des API.

- Une raison pour laquelle nous n'utiliserons pas Postman ou Figma à l'ère de l'IA est que leurs fonctionnalités ne peuvent pas être générées par du texte. Ils n'ont pas non plus de raccourci comme commande + K pour déclencher le remplacement de composants.

- Les interfaces utilisateur deviennent un obstacle à l'ère de l'IA. Pourquoi améliorer Postman pour qu'il soit compatible avec l'IA pour tester des applications quand on peut utiliser directement la bibliothèque requests de Python ou d'autres langages pour tester le code, puisque ces derniers seront alimentés par l'IA ?

- Pourquoi améliorer Figma pour qu'il soit compatible avec l'IA pour la création d'interfaces quand la génération d'interfaces par code, boostée par l'IA, offre une approche plus directe et potentiellement plus puissante ?

- Les LLM changeront d'abord les applications liées au texte, comme Google, les moteurs de recherche, les éditeurs de texte et outils d'écriture, Quizlet, Zendesk, DeepL, Medium, WordPress, Trello, Asana, Gmail, GitHub, Goodreads, Duolingo et Feedly.

- À l'inverse, les LLM ne révolutionneront probablement pas des technologies comme Git, Linux, ffmpeg, les téléphones portables, le matériel, les navigateurs, les systèmes d'exploitation ou les appels vocaux et vidéo. Ces technologies sont centrées sur le code, et leur code n'est pas facilement générable par l'IA, contrairement aux outils de test d'API comme Postman.

- Les technologies comportant beaucoup de code sont difficiles à révolutionner par l'IA, comme OpenOffice, MySQL, Mozilla Firefox, Chromium, VLC Media Player, Qt Framework, LLVM/Clang et GNOME. Si l'IA pouvait aider à créer ces technologies, elles ne seraient pas remplacées. L'IA devrait aider à créer de meilleures technologies, et pour cela, elle aura besoin de plus de puissance de calcul pour générer une quantité équivalente de code.

- Il y a deux façons dont les LLM peuvent apporter du changement : premièrement, en modifiant le contenu ou les données d'une plateforme ou d'un logiciel, comme la traduction de contenu dans des applications comme TikTok ; deuxièmement, en remplaçant directement certains logiciels ou plateformes, comme Postman ou Google Search, y compris Google Translate.

- Il y a deux façons dont les outils audio basés sur l'IA peuvent apporter du changement : premièrement, en modifiant le contenu ou les données d'une plateforme ou d'un logiciel, comme la génération de livres audio pour Audible ; deuxièmement, en remplaçant directement certains logiciels ou plateformes, par exemple, une application de chant, car l'IA peut maintenant faire ce que les humains font, rendant plus facile le chant comme hobby.

- Il existe plusieurs façons de mesurer l'impact de l'IA sur les logiciels ou plateformes actuels. Une façon est de mesurer quelle quantité de données ou de contenu peut être générée ou améliorée par l'IA, partiellement ou totalement. Une autre est de mesurer quelle quantité de code peut être écrite ou améliorée par l'IA, partiellement ou totalement. Ainsi, on utilise ce que génère l'IA pour améliorer les plateformes existantes. De plus, l'IA peut aider à inventer de nouveaux logiciels et plateformes.

- Il existe trois types de produits : les produits d'IA générative, les produits utilisant les API de produits d'IA générative, et les autres produits.

- Une idée de produit est d'utiliser l'IA pour accumuler des informations en temps réel, des actualités ou des mises à jour provenant de plateformes sociales comme Reddit, GitHub Trending, Twitter Trending, Quora Trending et Zhihu Trending. Les utilisateurs pourraient utiliser des requêtes pour personnaliser leur fil d'actualité ou même ajouter des comptes sociaux spécifiques.

- Il existe cinq types de données importants : texte, image, audio, vidéo et code.

- D'autres types de données importants incluent les données numériques, géospatiales, biométriques, de capteurs, transactionnelles, métadonnées, temporelles, structurées, non structurées, semi-structurées, de santé, environnementales, de journaux, réseau et comportementales.

- Google reste meilleur pour l'indexation de sites web, surtout si vous voulez télécharger un logiciel ou un document depuis un site spécifique. Cela fonctionne comme une recherche de domaine. Vous ne l'utilisez pas pour trouver des informations, mais pour naviguer vers d'autres sites afin d'effectuer des tâches. Un LLM peut ne pas avoir les liens de téléchargement les plus récents.

- Google fonctionne comme une recherche de domaine ; si vous voulez accéder à un site de dépôt Maven pour vérifier la dernière version, vous pouvez l'utiliser.

- Google reste utile pour la recherche d'images, tandis que les LLM excellent dans la génération de texte. Pourtant, les gens préfèrent souvent les images réelles pour vérifier les détails matériels, les dimensions, les formes d'objets ou l'apparence d'une personne.

- Les chatbots IA sont populaires car le texte est plus difficile à traiter que les images. Les gens préfèrent les images réelles à celles générées par l'IA, car les images sont plus faciles à comprendre d'un coup d'œil. Cependant, la génération d'images par IA a un potentiel inexploité : les utilisateurs pourraient demander à l'IA de montrer différents angles, zoomer sur des visages ou grossir les détails d'une carte électronique. Comme les gens travaillent principalement avec du texte plutôt qu'avec des images, il y a une marge de progression significative pour les outils d'image IA.

- L'IA excelle dans l'explication de concepts et la facilitation de la compréhension. De plus, les utilisateurs peuvent poser des questions sur n'importe quel détail spécifique. C'est probablement l'utilité la plus importante des outils IA.

- J'ai utilisé l'IA pour apprendre les grands modèles de langage. Le moment où elle m'a aidé à comprendre K, Q et V a été merveilleux.

- La raison pour laquelle je préfère utiliser Ubuntu depuis la sortie des LLM est que les applications riches et colorées de macOS me plaisent moins. Je préfère écrire mes programmes et tout faire via le terminal et le texte.

- L'IA peut être évaluée par sa capacité à mettre à jour un fichier pom.xml ou requirements.txt vers la dernière version, à mettre à jour des bibliothèques et à effectuer des vérifications. Ce processus peut demander beaucoup de travail et peut parfois être complexe.

- À l'ère de l'IA, les langages de programmation offrant de meilleures performances et une meilleure robustesse sont plus importants et seront plus populaires, tandis que la syntaxe l'est moins. Cela parce que les LLM aideront à générer du code, ce qui le rendra moins contraignant tant que le programme s'exécute bien.

- Les gens ont tendance à tout lire depuis les chatbots IA car c'est facile à apprendre, ils peuvent poser des questions sur n'importe quel aspect, le format est cohérent et la qualité est souvent parmi les meilleures trouvées sur Internet.

- Mais l'information ne se limite pas au texte, vous pouvez lire la plupart des informations textuelles depuis les chatbots IA, mais vous perdez le site d'origine, sa mise en page et sa forme, ses images explicatives et son design.

- Les sites web avec beaucoup d'interaction ont peu de chances d'être significativement changés par l'IA, comme les jeux web, Google Docs, Google Sheets et les outils de collaboration comme Zoom ou Slack. Ils sont centrés sur le code et pas seulement sur le texte.

- Il est facile de faire des fautes de frappe ou cela demande des efforts pour formuler des requêtes pour les chatbots IA. C'est pourquoi une banque numérique entièrement pilotée par l'IA, une application de trading numérique ou un réseau social IA avec une simple boîte de chat ne fonctionnent souvent pas. Les boutons traditionnels, la navigation par pages et les mises en page dans les applications mobiles sont plus pratiques.

- [Comment je vis bien à l'ère de l'IA et de la blockchain](./ai-blockchain-en)


---

## Nouvelles plateformes alimentées par des workflows IA

*08.01.2025*

- Les workflows sont des systèmes où les grands modèles de langage (LLM) et les outils sont orchestrés via des chemins de code prédéfinis.[^1]

- Imaginez une nouvelle plateforme, comme TikTok ou Quora, X, Threads, Instagram, WhatsApp, Facebook, LinkedIn, Reddit ou YouTube, entièrement alimentée par la traduction IA.

- Chaque publication ou réponse créée par les utilisateurs peut être enregistrée dans une seule langue. La plateforme traduira automatiquement le contenu dans 20 langues, permettant aux utilisateurs de le voir dans leur langue préférée.

- Au-delà de la traduction, d'autres fonctionnalités alimentées par l'IA, comme la synthèse, la génération audio et vidéo, joueront un rôle clé. En gros, l'utilisateur soumet un contexte de requête, et la plateforme s'occupe du reste.

- Les utilisateurs peuvent télécharger du texte, des images, de l'audio ou des vidéos, et la plateforme convertira automatiquement le contenu dans d'autres formats. Les utilisateurs peuvent choisir comment ils souhaitent recevoir ce contenu (par exemple, sous forme de texte, d'images, d'audio ou de vidéo).

- Les plateformes peuvent générer automatiquement des synthèses, avec différents types de résumés disponibles en plusieurs langues.

- Dans n'importe quel texte, image, audio ou vidéo sur la plateforme, l'IA peut aider à générer, affiner, améliorer, corriger, synthétiser, développer, convertir vers d'autres formats ou imaginer de nouvelles formes du contenu.

- Les utilisateurs peuvent personnaliser la plateforme avec des mots-clés comme "anglais" ou "drôle" pour ajuster le style des workflows IA sur des plateformes comme TikTok. Une fois configuré, l'IA adaptera le contenu en conséquence.


---

[^1]: Construire des agents efficaces, [Anthropic](https://www.anthropic.com/research/building-effective-agents)

---

## L'avenir des éditeurs de code alimentés par l'IA

*08.01.2025*

Récemment, je travaillais sur l'ajout d'une pipeline `xelatex` à GitHub Actions.

J'ai rencontré un problème avec le package `fontawesome5` dans le flux GitHub. La solution proposée par 4o-mini (installer TeX Live 2021 et utiliser `tlmgr install fontawesome5`) n'a pas fonctionné pour moi. Cependant, 4o a suggéré une meilleure approche : passer à TeX Live 2023 et toujours utiliser `tlmgr` pour installer `fontawesome5`. Bien que cela n'ait pas complètement résolu le problème, le passage à TeX Live 2023 a considérablement amélioré la situation.

J'ai utilisé ChatGPT pour m'aider à comprendre le problème. Pour plus de détails, consultez [Ce que ChatGPT O1 peut faire que 4o-mini ne peut pas](./o1-en).

À ce stade, je n'ai pas utilisé d'éditeurs comme Cursor ou Windsurf, bien que je les aie testés dans un autre projet. Le problème avec ces éditeurs de code est qu'ils ne captent que les sorties de test locales, ce qui limite leur fonctionnalité dans les environnements cloud.

Dans les workflows comme GitHub Actions, les jobs Jenkins ou tout flux de déploiement ou de test de code, les éditeurs de code doivent mieux s'intégrer. Ils devraient offrir une interaction transparente avec le cloud et les processus CI/CD.

Cette intégration s'applique aussi aux autres outils de création de contenu, qu'il s'agisse de texte, d'images, d'audio ou de vidéo. Ces outils devraient être intégrés à des systèmes de tests A/B. Les outils IA pourraient générer du contenu, et les outils de tests A/B fourniraient des retours. Cette dynamique est similaire à l'apprentissage par renforcement avec retours humains (RLHF), où les modèles IA s'améliorent avec le temps grâce aux retours du monde réel.

Cette idée d'étendre le RLHF au-delà des simples sorties de modèles, vers des environnements de test et de déploiement réels, semble être une direction prometteuse pour l'amélioration des éditeurs de code et des outils de création de contenu pilotés par l'IA.

Le test peut être instantané ou long, automatisé ou assisté par des humains. Si les tests sont automatisés, comme les tests A/B pour un outil IA, cela implique toujours des retours humains, mais le processus est automatisé. Par exemple, on peut demander à l'ordinateur de vérifier les résultats tous les jours ou toutes les heures en fonction des résultats des tests A/B pour améliorer le processus de création. De même, pour les jobs Jenkins ou GitHub Actions, on peut demander à l'ordinateur de vérifier après l'exécution des tâches.

Si une assistance humaine est impliquée, le retour ne peut pas être entièrement compris par la machine et est souvent un peu vague. Par exemple, lorsque les outils IA créent du contenu comme des images ou des vidéos, les humains peuvent signaler que le contenu n'est pas assez drôle ou qu'un détail spécifique devrait être amélioré. Les machines ont encore du chemin à faire pour tout rendre parfait, et ce qui est "parfait" est souvent subjectif, dépendant des goûts individuels. Ce sont les retours humains qui permettent de s'améliorer.

En théorie, toutes les règles définies par l'homme peuvent être écrites sous forme de requêtes. Il y a des requêtes utilisateur et des requêtes système. Nous devrions nous concentrer sur l'amélioration des requêtes plutôt que de corriger les résultats à chaque fois.