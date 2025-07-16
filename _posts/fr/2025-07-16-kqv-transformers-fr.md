---
audio: false
generated: false
lang: fr
layout: post
title: Comment j'ai appris le mécanisme KQV dans les transformeurs
translated: true
---

Après avoir lu [Mécanisme K, Q, V dans les Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en), j'ai compris comment fonctionnent K, Q et V.

Q signifie Query, K signifie Key, et V signifie Value. Pour une phrase, la Query est une matrice qui stocke la valeur d'un token dont elle a besoin pour interroger les autres tokens. La Key représente la description des tokens, et la Value représente la matrice de sens réelle des tokens.

Ils ont des formes spécifiques, donc il faut connaître leurs dimensions et détails.

J'ai compris cela vers début juin 2025. J'en ai entendu parler pour la première fois vers la fin de 2023. À cette époque, j'ai lu des articles comme [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), mais je n'ai pas compris grand-chose.

Après environ deux ans, j'ai trouvé cela plus facile à comprendre maintenant. Pendant ces deux années, je me suis concentré sur le travail backend et la préparation de mes examens de licence, et je n'ai pas beaucoup lu ou appris sur le machine learning. Cependant, j'ai réfléchi à ces concepts de temps en temps lorsque je conduisais ou faisais autre chose.

Cela me rappelle l'effet du temps. Nous pouvons apprendre beaucoup de choses du premier coup, même si nous ne comprenons pas grand-chose. Mais cela déclenche un point de départ pour notre réflexion.

Avec le temps, j'ai constaté que pour la connaissance et la découverte, il est difficile de penser ou de comprendre les choses dès la première fois. Mais plus tard, cela semble plus facile à apprendre et à connaître.

Une raison est que, à l'ère de l'IA, il est plus facile d'apprendre car vous pouvez approfondir n'importe quel détail ou aspect pour résoudre vos doutes. Il y a aussi plus de vidéos sur l'IA disponibles. Plus important encore, vous voyez que tant de personnes apprennent et construisent des projets sur cette base, comme [llama.cpp](https://github.com/ggml-org/llama.cpp).

L'histoire de Georgi Gerganov est inspirante. En tant que nouvel apprenant en machine learning à partir de 2021, il a eu un impact puissant dans la communauté de l'IA.

Ce genre de chose se reproduira encore et encore. Donc, pour l'apprentissage par renforcement et les dernières connaissances en IA, même si je ne peux pas encore leur consacrer beaucoup de temps, je pense que je peux trouver du temps pour apprendre rapidement et essayer de réfléchir beaucoup à ce sujet. Le cerveau fera son travail.