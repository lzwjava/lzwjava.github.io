---
audio: false
generated: false
lang: fr
layout: post
title: Avantages de l'accumulation de journaux
translated: true
---

Lorsque j'ai travaillé comme contractuel pour une banque singapourienne, nous utilisions une plateforme d'applications multi-cloud pour servir les microservices. À cette époque, j'ai commencé à accumuler des journaux lorsque je travaillais dans l'entreprise.

Plusieurs années se sont écoulées, et je pense toujours que c'est l'une des meilleures façons de m'aider à travailler ou à faire de l'ingénierie logicielle. Avec le temps, dans mon répertoire de journaux, il y a des centaines de fichiers de journaux.

Je n'ai pas de sous-répertoires spécifiques ou de noms de fichiers de journaux formels pour ceux-ci. Parfois, j'utilise simplement le nom de la tâche JIRA comme préfixe du nom du fichier de journal ou cette fonctionnalité. Ensuite, j'ajoute un numéro au suffixe. C'est comme mutual-fund-1.log, mutual-fund-2.log, etc. Cela signifie que dans le microservice des fonds communs de placement, j'ai ce journal lors de l'exécution de ce microservice.

Parfois, lorsque je travaille sur des projets servant plusieurs régions, j'ajoute ce pays en suffixe, comme mutual-fund-cn-1.log, mutual-fund-sg-1.log. Les noms de fichiers des journaux sont quelque peu informels. Parce qu'à cette époque, j'avais besoin de me concentrer sur les piles d'erreurs ou les appels de fonctions environnantes.

Les journaux des programmes comptent. Tout le monde le sait. Cependant, je veux souligner l'importance d'accumuler les journaux plutôt que de simplement les regarder dans la console et de les laisser partir. Vous connaîtrez plus de commodité lorsque le projet est en cours. Vous avez plus de temps pour trouver les anciens journaux. Vous pourriez avoir besoin de savoir si un appel similaire de procédure stockée de base de données s'est produit auparavant. Vous pourriez avoir besoin de savoir si la même erreur s'est produite auparavant. Vous pourriez avoir besoin de vous rappeler comment résoudre ce problème la dernière fois.

Il y a des tonnes de détails dans un grand projet ou des dizaines de microservices. Et les erreurs, les exceptions ou les problèmes se produisent encore et encore. Le journal est comme le document d'exécution d'un programme. Et ils sont générés par le programme automatiquement sans saisie humaine. Et pour les développeurs, ces journaux sont lisibles. Donc, lorsque vous commencez une nouvelle tâche ou corrigez un nouveau bug, vous avez des centaines de journaux à portée de main pour résoudre ce nouveau bug. Vous n'êtes pas seul.

Pourquoi les accumulons-nous ? Parce que les choses ou les connaissances sont facilement oubliées.

Il y a eu un progrès de la civilisation humaine lorsque le papier a été inventé. Et lorsque les ordinateurs ont été inventés, il y a eu un autre niveau de civilisation humaine. Prendre des notes sur papier est comme accumuler des journaux dans les ordinateurs.

Pas seulement pour les humains, mais pour les chatbots IA, les outils LLM, ces journaux deviennent de plus en plus importants. GreptimeDB, une base de données pour la collecte et l'analyse unifiées des données d'observabilité (métriques, journaux et traces) établie en 2022, n'est pas une coïncidence.

Pourquoi ne l'ai-je pas fait avant ? Après avoir travaillé comme contractuel pour de grandes banques, j'ai dû faire plus de collaboration et travailler sur des projets plus importants. Avant cela, la plupart du temps dans la startup ou ma période de startup, je travaillais en solo. Lorsque je travaillais chez LeanCloud avant, j'ai travaillé sur l'application IM LeanChat pendant environ la moitié du temps.

Et lorsque je suis entré dans le monde plus formel de l'entreprise, le développement des projets était différent de mon projet personnel ou de mon projet de startup. Ils ont des environnements de test SIT, UAT. Et l'environnement de production est souvent ouvert à certaines petites équipes. Obtenir les journaux de leur part et résoudre les problèmes devient long et quelque peu fastidieux. Et l'exécution d'un projet prend du temps, et le pipeline Jenkins a souvent besoin de la moitié d'une heure pour s'exécuter.

Donc, je ne peux pas exécuter ou tester le programme comme une mouche. Je ne peux pas faire un déploiement en tapant simplement une commande sur mon ordinateur personnel et en téléchargeant le code sur le serveur pour l'exécution.

Cela m'a donc amené à accumuler des journaux pour avoir plus de contexte pour gérer les tâches. Nous devrions résoudre les problèmes du premier coup. Nous devrions vérifier notre correction en quelques fois seulement. Nous ne pouvons pas facilement obtenir les journaux du programme qui s'exécute dans un cloud ou le serveur de l'entreprise, donc nous ferions mieux de les copier et de les sauvegarder sur l'ordinateur portable local, pour l'analyse.

Et maintenant, pour mes projets personnels, j'accumule également les journaux. Cela devient une habitude. Après avoir travaillé dans de grandes entreprises pendant quelques années, j'ai quelque peu plus de patience ou de stratégie pour rendre mes projets plus grands et plus longs. Donc, je sais que j'ai besoin de ces journaux avec le temps.

Certaines personnes pourraient dire que vous n'avez besoin que d'un code élégant et d'un projet fonctionnel. Vous n'avez pas besoin d'accumuler les journaux ou les traces d'erreurs. C'est bon. Lorsque nous avons un bug ou une nouvelle fonctionnalité, nous pouvons exécuter le programme pour obtenir les journaux actuels. Nous n'avons pas besoin des journaux du processus de développement. Ils sont comme les enregistrements détaillés des expériences scientifiques. À première vue, cela semble bien. Mais à long terme, si un jour vous voulez travailler dessus à nouveau, ou vous voulez le partager, ou le laisser à d'autres, cela peut ne pas être bon.

Je pense qu'il pourrait y avoir de bonnes opportunités ici. Dans les entreprises, pourquoi n'encourageons-nous pas chaque développeur à partager leurs journaux accumulés ? Dans les projets open source, nous devrions en avoir aussi. Nous ne trouvons pas les journaux des autres attrayants parce que nous ne les connaissons pas. Nous perdons le contexte lors de la sauvegarde de ces journaux. Et à l'intérieur, il semble y avoir des tonnes de messages sans rapport ou triviaux.

Mais l'effort d'accumuler des journaux est trivial. C'est juste copier-coller chaque fois que nous voyons des journaux, surtout ceux des journaux d'erreurs. Et si nous le faisions de manière automatisée ? C'est une bonne idée d'enregistrer les journaux dans un répertoire chaque fois que nous exécutons un projet, comme ceux des projets Spring Boot.

Le monde devient de plus en plus numérique, donc accumuler les journaux des programmes numériques est comme accumuler des livres dans le monde physique.