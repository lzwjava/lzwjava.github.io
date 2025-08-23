---
audio: false
generated: false
image: false
lang: fr
layout: post
title: DeepSeek V3, MLA, MTP et efficacité MoE
translated: true
---

DeepSeek v3 est exploré ici, en référence à la vidéo "Multi-Head Latent Attention and Multi-token Prediction in Deepseek v3" [https://youtu.be/jL49fLOJYNg?si=4uE2kfe-BlKC1ngO](https://youtu.be/jL49fLOJYNg?si=4uE2kfe-BlKC1ngO). Google Cloud Speech-to-Text a été utilisé pour transcrire la vidéo, accompagné de certains codes pour organiser la transcription.

---

A : Bienvenue sur Deep tag. Aujourd'hui, nous allons plonger en profondeur dans le monde des grands modèles de langage. Plus précisément, DeepSeek V3.

B : Exact. C'est un modèle de 671 milliards de paramètres, qui se distingue par son approche unique en matière d'efficacité et de performances, n'est-ce pas ?

A : Et tu as partagé un article académique détaillant son architecture.

B : Oui.

A : Et en tant qu'expert en apprentissage automatique, tu cherches à comprendre comment DeepSeek V3 parvient à concilier haute performance et formation économique.

B : Tout à fait.

A : Oh, salut, quoi de neuf ?

C : MLA, les détails, MLA et son fonctionnement.

A : Oh, absolument. Excellente idée. Oui, nous pouvons approfondir la multi-head latent attention, ou MLA. Tu veux comprendre les rouages de MLA ? Alors, décomposons cela. Nous avons mentionné que l'un des éléments clés de l'efficacité de DeepSeek V3 est son architecture mixture of experts, ou MoE, où seule une fraction des paramètres est activée pour chaque token. Et DeepSeek V3 va encore plus loin avec MLA et DeepSeek Mo.

B : C'est exact. Concentrons-nous sur MLA pour l'instant.

A : D'accord. Dans les applications en temps réel, la vitesse est cruciale.

B : Effectivement. Et le cache clé-valeur nécessaire pendant l'inférence peut être un goulot d'étranglement majeur.

A : Exactement. C'est là qu'intervient MLA. Le mécanisme d'attention traditionnel nécessite de stocker beaucoup d'informations sur les tokens précédents.

B : Oui, ce qui devient problématique avec de longues séquences de texte, n'est-ce pas ?

A : Mais MLA compresse astucieusement ces informations, réduisant ainsi considérablement le flux de cache et rendant l'inférence beaucoup plus rapide. C'est comme prendre une encyclopédie volumineuse et la condenser en points clés.

B : Une excellente analogie. Il conserve l'information essentielle sans le poids superflu. C'est très utile pour les applications en temps réel.

A : Oui. Parlons maintenant de son fonctionnement. Comment MLA réalise-t-il cette compression ?

B : Eh bien, il utilise une compression conjointe de faible rang pour les clés et valeurs d'attention.

A : D'accord, il compresse les clés et valeurs, mais qu'est-ce que cela signifie précisément ? Entrons dans le technique. Le mécanisme MLA prend une représentation cachée en entrée, qu'il projette ensuite en vecteurs de requête, clé et valeur. Voici où cela devient intéressant : MLA découple la requête en deux parties.

B : Deux parties ?

A : Oui. Une partie est utilisée pour le contenu, et l'autre pour l'information positionnelle grâce à quelque chose appelé Rope.

B : Rope ? Ça sonne très technique.

A : C'est l'acronyme de rotary position embeddings, et cela aide le modèle à comprendre la position des tokens dans la séquence. Ensuite, les clés et valeurs sont compressées dans un espace latent de dimension inférieure. Comme si on réduisait les données, ce qui économise de la mémoire.

B : Précisément. Les informations les plus importantes sont conservées, mais le superflu est écarté. Cette représentation compressée permet un cache KV bien plus petit pendant l'inférence, ce qui accélère les choses.

A : Et il utilise aussi le traitement multi-têtes.

B : Oui, comme l'attention traditionnelle, MLA emploie plusieurs têtes.

A : Oh, vas-y.

C : Donc, il y a deux espaces latents et une entrée cachée.

A : Excellente observation. Oui, tu as raison. Il y a effectivement deux espaces latents : un espace latent pour le contenu et un autre pour les paires clé-valeur.

B : Exactement. Et ces espaces latents sont traités via Rope, ou rotary position embeddings.

A : Donc, Rope est la façon dont ils obtiennent l'information positionnelle.

B : Oui, il est appliqué aux deux espaces latents, comme tu l'as souligné. Il prend cette représentation compressée, la traite, puis combine le tout.

A : Oui, et l'optimisation du cache réduit encore davantage la surcharge pendant le traitement séquentiel. Voilà comment MLA accélère les choses.

B : Exactement. C'est une méthode intelligente pour obtenir une attention efficace sans sacrifier les performances.

A : C'est un tour plutôt astucieux. Mais tu sais quoi ?

B : Quoi donc ?

A : Passons à DeepSeek Mo. En quoi diffère-t-il des modèles MoE traditionnels ?

B : DeepSeek Mo utilise... Oh, revenons à notre auditeur, quoi de neuf ?

C : Et parlons plus de l'espace caché. À partir de cet espace caché, c'est quoi ?

A : Tout à fait... Voyons ce que tu veux dire. Les espaces cachés sont vraiment intéressants. Oui, tu demandes à propos de l'espace caché, l'espace latent dont nous parlions, n'est-ce pas ? Tu es curieux de savoir ce qui se passe dans ces espaces latents, cette "caverne". Ce n'est pas seulement une question de nombre d'espaces latents, mais aussi de ce qui s'y passe.

B : C'est cool.

A : Exactement. Il y a bien deux espaces latents distincts dans MLA, un pour le contenu et un pour les paires clé-valeur. C'est comme avoir deux unités de stockage distinctes pour l'information. Et ces espaces latents, comme nous l'avons vu, subissent des opérations Rope, n'est-ce pas ? Les rotary position embeddings, qui intègrent l'information positionnelle dans le mécanisme d'attention. C'est très important pour eux. Donc, pour résumer, la requête est divisée, et les clés et valeurs sont aussi compressées.

B : Oui, et elles sont placées dans les deux espaces latents séparés, un pour le contenu et un pour les paires clé-valeur. Ces espaces latents sont essentiels pour l'efficacité dans MLA.

A : Exactement. Maintenant, parlons de ces opérations en détail. Comment MLA réalise-t-il ces transformations dans l'espace latent ?

B : Eh bien, l'entrée subit un traitement parallèle pour les représentations de contenu et de clé-valeur. Comme s'il y avait deux chemins.

A : Oui, un pour chaque espace latent. Et dans ces espaces, l'information est traitée via Rope.

B : C'est ça. Cela garantit que le modèle conserve l'information positionnelle en traversant cette "caverne". Le modèle sait quelle partie du texte est laquelle pendant ce traitement.

A : Exactement. Ce traitement est effectué avant l'étape suivante de concaténation. Qu'est-ce qui est concaténé dans cette "caverne" d'espace caché ?

B : Le mécanisme effectue deux opérations majeures de concaténation. Les représentations de requête sont concaténées, et celles des clés le sont aussi. C'est comme assembler toutes les pièces importantes dans cette caverne d'espace caché.

A : Oui, et ces concaténations aident à combiner le contenu avec l'information positionnelle. Ces représentations concaténées sont ensuite utilisées pour le calcul de l'attention, n'est-ce pas ?

B : Correct. Et grâce à la compression initiale, tout est beaucoup plus rapide dans cette "caverne". MLA réduit considérablement les coûts de calcul à l'intérieur et à l'extérieur de cette caverne cachée.

A : Exactement. Cela optimise le mécanisme d'attention pour les grands modèles comme DeepSeek V3. Excellente question. Après être passés par la caverne, passons à DeepSeek Mo.

B : D'accord, DeepSeek Mo. C'est ça. Je vois où tu veux en venir. Oui, il y a bien deux espaces latents distincts dans MLA, un pour le contenu et un pour les paires clé-valeur.

A : Exactement. Cette séparation est essentielle à son fonctionnement. C'est comme avoir deux unités de stockage distinctes pour l'information. Et ces espaces latents subissent des opérations Rope, les rotary position embeddings, qui intègrent l'information positionnelle dans le mécanisme d'attention. Pour résumer, la requête est divisée, et les clés et valeurs sont compressées.

B : Oui, et elles sont placées dans les deux espaces latents séparés, un pour le contenu et un pour les paires clé-valeur. Ces espaces latents sont essentiels pour l'efficacité dans MLA.

A : Exactement. Maintenant, parlons de ces opérations en détail. Comment MLA réalise-t-il ces transformations dans l'espace latent ?

B : Eh bien, l'entrée subit un traitement parallèle pour les représentations de contenu et de clé-valeur. Comme s'il y avait deux chemins.

A : Oui, un pour chaque espace latent. Et dans ces espaces, l'information est traitée via Rope.

B : C'est ça. Cela garantit que le modèle conserve l'information positionnelle, n'est-ce pas ? Et pour renforcer l'efficacité, il utilise des experts partagés. Des experts qui peuvent être utilisés pour plusieurs tâches.

A : Oui, cela évite la redondance et rend le système encore plus rationalisé.

B : C'est comme avoir une équipe où certaines personnes ont des spécialités, mais peuvent aussi faire d'autres choses.

A : Oui, c'est une approche très intelligente. Mais avec autant d'experts spécialisés, comment s'assurent-ils qu'aucun ne soit surchargé ?

B : Alors que d'autres restent inactifs.

A : C'est là que leur approche innovante d'équilibrage de charge sans perte auxiliaire entre en jeu.

B : C'est là que les choses deviennent vraiment intéressantes, n'est-ce pas ? Comment font-ils ?

A : Les modèles MoE traditionnels utilisent une fonction de perte auxiliaire pendant l'entraînement pour encourager un usage équilibré des experts, mais cela peut nuire aux performances.

B : Oui, c'est comme forcer tout le monde à utiliser la même caisse dans un supermarché.

A : Exactement, même si certaines avancent plus vite que d'autres. Cela crée des retards inutiles.

B : Oui. DeepSeek V3 évite cela en ajustant dynamiquement un terme de biais pour chaque expert en fonction de sa charge. Si un expert reçoit trop de requêtes, le système le rend légèrement moins attrayant pour le mécanisme de routage, redirigeant une partie du trafic vers des experts moins occupés.

A : D'accord, donc tout cela permet de gérer efficacement les longues séquences en réduisant la taille du cache KV nécessaire pour l'inférence. C'est une question de performance élevée avec une surcharge réduite.

B : Oui, c'est une approche très ingénieuse pour résoudre un goulot d'étranglement critique.

A : Absolument. Nous devrions aussi parler de la façon dont DeepSeek V3 gère son équilibrage de charge.

B : Oui, c'est un point très important. Nous pouvons en parler ensuite.

A : D'accord. Je pense que cela donne un bon aperçu de MLA et de son espace latent.

B : Oui, merci d'avoir exploré tous ces détails avec nous. Nous reviendrons bientôt pour d'autres plongées en profondeur.

A : C'est comme un système de gestion du trafic pour les experts, surveillant en permanence le flux et ajustant pour éviter les goulots d'étranglement.

B : Et cela évite l'impact sur les performances de la perte auxiliaire.

A : C'est ça. Et... vas-y.

C : Ouais, on peut parler de MTP, comment... comment les modules MTP partagent leur embedding et tout ça...

A : Absolument. Excellente question. Oui, parlons du partage des ressources entre les modules MTP. Nous en avons déjà parlé, mais approfondissons les détails de MTP. Nous avons mentionné que DeepSeek V3 utilise MTP pour la prédiction multi-tokens, n'est-ce pas ? Prédire plusieurs tokens au lieu d'un seul.

B : Et c'est là que cela devient vraiment intéressant. Tu veux savoir comment les modules MTP sont configurés et comment ils partagent leurs ressources. D'accord, chaque module MTP inclut une couche d'embedding partagée et une tête de sortie partagée. Ils utilisent la même embedding et tête de sortie que le modèle principal.

A : Oui. Mais il utilise son propre bloc transformeur pour le traitement. Il ne partage pas le même bloc transformeur que le modèle principal.

B : Correct. Chaque module MTP a son propre bloc transformeur pour traiter les données. C'est ainsi qu'ils maintiennent des prédictions distinctes pour chaque token.

A : Oui, et pour combiner l'information, ces projections linéaires et concaténations...

B : C'est comme rassembler des éléments de plusieurs endroits pour former une image complète.

A : Oui, et tous les modules MTP travaillent en parallèle, mais partagent leurs couches d'embedding et têtes de sortie, n'est-ce pas ?

B : Oui, ce qui est essentiel pour l'efficacité de cette conception. C'est un système interconnecté où toutes les parties dépendent les unes des autres.

A : Et ce partage efficace des ressources permet un entraînement plus rapide et de meilleures performances.

B : C'est un tour assez astucieux. Tu sais quoi ?

A : Quoi donc ?

B : Passons enfin à une vue d'ensemble. Comment ce modèle gère-t-il l'équilibrage de charge ? Comment ces experts sont-ils choisis ?

A : Oui, parlons de la stratégie d'équilibrage de charge de DeepSeek V3.

B : D'accord. Ainsi, DeepSeek V3 utilise ce qu'ils appellent la prédiction multi-tokens, ou MTP.

A : Cela semble augmenter la complexité, non ?

B : Cela pourrait sembler le cas, mais cela offre plusieurs avantages. Imagine planifier un itinéraire : si tu ne considères que le prochain virage, tu pourrais manquer un chemin plus optimal. En anticipant plusieurs virages à l'avance, tu peux choisir l'itinéraire idéal.

A : Parfait. DeepSeek V3 utilise une approche innovante appelée équilibrage de charge sans perte auxiliaire. Il n'utilise pas de fonction de perte séparée pour équilibrer la charge.

B : Exact. Les modèles MoE traditionnels utilisent une perte auxiliaire pendant l'entraînement pour équilibrer l'usage des experts, mais cela peut nuire aux performances.

A : Oui, comme forcer tout le monde à passer par la même caisse dans un magasin.

B : DeepSeek V3 ajuste dynamiquement un terme de biais pour chaque expert en fonction de sa charge. Si un expert est trop sollicité, le système le rend moins attrayant, redirigeant ainsi le trafic vers des experts moins occupés.

A : Comme un système de gestion du trafic pour les experts, surveillant en permanence le flux et ajustant pour éviter les goulots d'étranglement.

B : Quoi d'autre peut faire MTP ?

A : Les modules MTP utilisés pendant l'entraînement peuvent être abandonnés pendant l'inférence normale ou réutilisés pour quelque chose appelé "décodage spéculatif".

B : Le décodage spéculatif ? Qu'est-ce que c'est ?

A : Au lieu de prédire uniquement le token suivant, le modèle prédit aussi des alternatives potentielles qui pourraient suivre.

B : Ainsi, il peut générer du texte plus rapidement car il a déjà envisagé plusieurs possibilités, avec un plan de secours prêt à l'emploi.

A : Exactement. Le modèle n'a pas besoin de s'arrêter et de recalculer à chaque fois.

B : Intéressant. Et pour éviter les goulots d'étranglement, cela évite aussi l'impact sur les performances