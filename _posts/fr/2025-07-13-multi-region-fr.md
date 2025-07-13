---
audio: false
generated: false
lang: fr
layout: post
title: Réflexions sur le développement logiciel multi-régions
translated: true
---

Pour les entreprises internationales, il existe souvent des projets qui servent les populations de plusieurs régions, comme Singapour, Hong Kong, le Royaume-Uni, les États-Unis et la Chine.

J'ai travaillé sur certains projets qui desservent les utilisateurs de plusieurs régions. Faire les choses correctement dans les projets backend n'est pas facile.

Pour la Standard Chartered Bank, il y a l'application SC Mobile India, l'application SC Mobile Hong Kong, etc. Ils donnent essentiellement à chaque pays sa propre application. Ils utilisent probablement des applications différentes, des serveurs backend différents, et certaines fonctionnalités sont différentes mais avec le même langage de conception.

Il est probablement incorrect de faire cela. Les premières années, cela semble simple ou réalisable. Mais après une décennie, ils sauront que c'est très douloureux. Le coût de maintenance ou de synchronisation, le coût des tests—il y a des tonnes d'efforts en double.

Cependant, pour Facebook, Google ou Apple Pay, c'est assez simple. Certaines personnes pourraient dire qu'ils ne sont pas des applications financières ; ils ont certaines règles de conformité à respecter. Ce n'est pas vrai. La conformité signifie souvent le serveur de base de données, ou la base de données, ou certaines données que les départements gouvernementaux veulent vérifier ou pour que les sociétés d'audit effectuent des audits.

Cependant, les autres efforts sont les mêmes. Le logiciel est très flexible. Nous devrions laisser le code être dans le même dépôt, nous devrions utiliser la configuration de la source de données pour héberger les données de différentes régions, et nous devrions partager autant que possible le même code, la même conception, le même flux de travail et les mêmes tests.

Apple Pay est un bon exemple de cela. L'App Store est également un bon exemple de cela. Ils desservent chaque pays aussi.

Il y a probablement des projets dans les grandes entreprises technologiques qui utilisent les continents pour séparer, comme l'Asie et la région Pacifique, l'Amérique du Nord. Pour ceux-ci aussi.

La première chose à faire lors du développement multi-régions est de savoir ce qui est différent, quelles sont les conformités que nous devons suivre, et comment réduire au maximum les efforts en double.

Pour la synthèse vocale, Google Cloud doit entraîner différentes langues. Ils fournissent différents modèles et différentes langues pour cela. Pour les langues, les différences entre les langues sont leurs sons, leur prononciation et leur apparence des caractères. Le premier signifie que lorsque nous utilisons Google Cloud pour la synthèse vocale, nous devons utiliser différents modèles. Pour leur apparence des caractères, cela signifie que lors de la génération de PDF, nous devons être prudents dans le choix de la police.

Pour les projets multi-régions, dans les projets Spring Boot, nous pouvons utiliser ses alias et différentes initialisations d'objets pour cela. Nous pouvons utiliser intelligemment les propriétés ou la configuration YAML. Nous pouvons mettre toute la logique différente basée sur la région dans certains modules ou classes spécifiques.

Et pour l'hébergement de code, différentes branches pour différents pays semblent faciles au début, mais après quelques années, vous saurez à quel point c'est douloureux. Vous devez faire un git cherry-pick pour les autres régions. Et vous devez tester à nouveau dans une autre branche. Chaque fois que vous faites un petit changement, vous devez le synchroniser avec les branches. Et avec le temps, si nous ne faisons pas d'efforts pour minimiser les différences de code ou de logique, les différences de code entre plusieurs régions ou pays deviennent suffisamment grandes pour être impossibles à corriger.

La bonne nouvelle, c'est qu'aujourd'hui, l'IA peut nous aider à refactoriser ou à écrire un meilleur code, ou à corriger les problèmes de conception de code multi-régions. Peu importe la taille de l'erreur, lorsque nous la corrigeons, c'est une petite erreur.