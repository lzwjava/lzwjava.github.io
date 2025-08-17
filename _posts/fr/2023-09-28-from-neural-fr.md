---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Du réseau de neurones à GPT
translated: true
---

### Vidéos YouTube

Andrej Karpathy - Construisons GPT : à partir de zéro, en code, expliqué en détail.

Umar Jamil - L'attention est tout ce dont vous avez besoin (Transformer) - Explication du modèle (y compris les mathématiques), inférence et entraînement

StatQuest avec Josh Starmer - Réseaux de neurones Transformers, la base de ChatGPT, clairement expliqué !!!

Pascal Poupart - CS480/680 Cours 19 : Attention et réseaux Transformers

The A.I. Hacker - Michael Phi - Guide illustré des réseaux de neurones Transformers : une explication étape par étape

### Comment j'apprends

Après avoir lu la moitié du livre *"Neural Networks and Deep Learning"*, j'ai commencé à reproduire l'exemple de réseau de neurones pour la reconnaissance de chiffres manuscrits. J'ai créé un dépôt sur GitHub, [https://github.com/lzwjava/neural-networks-and-zhiwei-learning](https://github.com/lzwjava/neural-networks-and-zhiwei-learning).

C'est là la partie vraiment difficile. Si quelqu'un peut l'écrire à partir de zéro sans copier de code, alors il comprend très bien.

Mon code reproduit manque encore l'implémentation de `update_mini_batch` et de la rétropropagation. Cependant, en observant attentivement les variables lors des phases de chargement des données, de propagation avant et d'évaluation, j'ai beaucoup mieux compris les vecteurs, la dimensionnalité, les matrices et la forme des objets.

Et j'ai commencé à apprendre l'implémentation de GPT et des Transformers. Grâce à l'encodage des mots et à l'encodage positionnel, le texte se transforme en nombres. Ensuite, en essence, cela ne diffère pas du simple réseau de neurones pour reconnaître des chiffres manuscrits.

La conférence d'Andrej Karpathy *"Let's build GPT"* est très bonne. Il explique très bien les choses.

La première raison est qu'il part vraiment de zéro. On voit d'abord comment générer du texte. C'est un peu flou et aléatoire. La deuxième raison est qu'Andrej peut expliquer les choses de manière très intuitive. Andrej a travaillé sur le projet nanoGPT pendant plusieurs mois.

J'ai eu une nouvelle idée pour évaluer la qualité d'une conférence : l'auteur peut-il vraiment écrire ces codes ? Pourquoi je ne comprends pas et quels sujets l'auteur a-t-il omis ? Au-delà de ces diagrammes et animations élégants, quels sont leurs défauts et leurs lacunes ?

Revenons au sujet de l'apprentissage automatique lui-même. Comme le mentionne Andrej, le *dropout*, les connexions résiduelles, l'*auto-attention*, l'*attention multi-têtes*, l'*attention masquée*.

En regardant davantage les vidéos ci-dessus, j'ai commencé à comprendre un peu.

Grâce à l'encodage positionnel avec les fonctions sinus et cosinus, nous obtenons certains poids. Grâce à l'encodage des mots, nous transformons les mots en nombres.

$$
    PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{model}})
$$

> La pizza est sortie du four et elle avait bon goût.

Dans cette phrase, comment l'algorithme sait-il si cela fait référence à la pizza ou au four ? Comment calculons-nous les similarités pour chaque mot de la phrase ?

Nous voulons un ensemble de poids. Si nous utilisons le réseau Transformer pour faire de la traduction, chaque fois que nous entrons une phrase, il peut sortir la phrase correspondante dans une autre langue.

À propos du produit scalaire ici. Une raison pour laquelle nous utilisons le produit scalaire est qu'il prend en compte chaque nombre du vecteur. Et si nous utilisions le produit scalaire au carré ? Nous calculerions d'abord le carré des nombres, puis nous ferions le produit scalaire. Et si nous faisions un produit scalaire inversé ?

À propos du masque ici, nous changeons les nombres de la moitié de la matrice en moins l'infini. Ensuite, nous utilisons la fonction *softmax* pour faire en sorte que les valeurs soient comprises entre 0 et 1. Et si nous changions les nombres en bas à gauche en moins l'infini ?

### Plan

Continuer à lire du code, des articles et regarder des vidéos. Juste m'amuser et suivre ma curiosité.

[https://github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

[https://github.com/jadore801120/attention-is-all-you-need-pytorch](https://github.com/jadore801120/attention-is-all-you-need-pytorch)