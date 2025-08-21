---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Avantages de l'accumulation de journaux
translated: true
---

## Avantages de l'accumulation de journaux

Lorsque je travaillais en tant qu'entrepreneur pour une banque, nous utilisions une plateforme d'applications multi-cloud pour servir les microservices. À cette époque, j'ai commencé à accumuler des journaux en travaillant dans l'entreprise.

Plusieurs années ont passé, et je pense toujours que c'est l'une des meilleures façons de m'aider à travailler ou à faire de l'ingénierie logicielle. Au fil du temps, dans mon répertoire de journaux, il y a des centaines de fichiers journaux.

Je n'ai pas de sous-répertoires spécifiques ni de noms de fichiers journaux formels pour ceux-ci. Parfois, j'utilise simplement le nom de cette tâche JIRA comme préfixe de nom de fichier de journal ou comme fonctionnalité. Et puis j'ajoute un numéro au suffixe. C'est comme fonds-mutuel-1.log, fonds-mutuel-2.log, etc. Cela signifie que dans le microservice de fonds mutuels, j'ai ce journal lorsque j'exécute ce microservice.

Parfois, lorsque je travaille sur des projets qui servent plusieurs régions, j'ajoute ce pays comme suffixe, comme fonds-mutuel-cn-1.log, fonds-mutuel-sg-1.log. Les noms de fichiers des journaux sont en quelque sorte informels. Parce qu'à ce moment-là, je devais me concentrer sur les piles d'erreurs ou les appels de fonctions environnants.

Les journaux des programmes sont importants. Tout le monde le sait. Cependant, je veux insister sur l'importance d'accumuler les journaux au lieu de simplement les regarder dans la console et de les laisser disparaître. Vous connaîtrez plus de commodité au fur et à mesure que le projet avance. Vous avez plus de temps pour trouver les journaux précédents. Vous pourriez avoir besoin de savoir si un appel de procédure stockée de base de données similaire s'est produit auparavant. Vous pourriez avoir besoin de savoir si la même erreur s'est produite auparavant. Vous pourriez avoir besoin de vous rappeler comment résoudre ce problème la dernière fois.

Il y a des tonnes de détails dans un grand projet ou des dizaines de microservices. Et les erreurs, les exceptions ou les problèmes se produisent encore et encore. Le journal est comme le document de fonctionnement d'un programme. Et ils sont générés automatiquement par le programme sans saisie humaine. Et pour les développeurs, ces journaux sont lisibles. Donc, lorsque vous commencez une nouvelle tâche ou corrigez un nouveau bug, vous avez des centaines de journaux à votre disposition pour corriger ce nouveau bug. Vous n'êtes pas seul.

Pourquoi les accumulons-nous ? Parce que les choses ou les connaissances s'oublient facilement.

Il y a eu un progrès de la civilisation humaine lorsque le papier a été inventé. Et lorsque les ordinateurs ont été inventés, il y a eu un autre niveau de civilisation humaine. Garder des notes sur papier est comme accumuler des journaux dans les ordinateurs.

Non seulement pour les humains, mais pour les chatbots IA, les outils LLM, ces journaux deviennent de plus en plus importants. Le GreptimeDB, une base de données pour la collecte et l'analyse unifiées de données d'observabilité (métriques, journaux et traces) établie en 2022 n'est pas une coïncidence.

Pourquoi ne l'ai-je pas fait avant ? Après avoir travaillé comme entrepreneur pour de grandes banques, j'ai dû faire plus de collaboration et travailler sur des projets plus importants. Avant cela, la plupart du temps dans la startup ou ma période de startup, je travaillais en solo. Lorsque je travaillais chez LeanCloud auparavant, j'ai travaillé sur l'application de messagerie instantanée LeanChat pendant environ la moitié du temps.

Et quand je suis entré dans le monde de l'entreprise plus formel, le développement des projets était différent de mon projet personnel ou de mon projet de startup. Ils ont des environnements de test SIT, UAT. Et l'environnement de production n'est souvent ouvert qu'à de petites équipes spécifiques. Obtenir les journaux de ceux-ci et résoudre les problèmes devient long et quelque peu fastidieux. Et l'exécution d'un projet prend du temps, et le pipeline Jenkins a souvent besoin d'une demi-heure pour s'exécuter.

Je ne peux donc pas exécuter ou tester le programme comme une mouche. Je ne peux pas effectuer un déploiement en tapant simplement une commande sur mon ordinateur personnel et en téléchargeant du code sur le serveur pour l'exécution.

Donc, cela m'a en quelque sorte amené à accumuler des journaux pour avoir plus de contexte pour gérer les tâches. Nous ferions mieux de résoudre les problèmes du premier coup. Nous ferions mieux de vérifier notre correction en quelques fois seulement. Nous ne pouvons pas facilement obtenir les journaux du programme qui s'exécute dans un cloud ou sur le serveur de l'entreprise, nous ferions donc mieux de les copier et de les enregistrer sur l'ordinateur portable local, pour effectuer l'analyse.

Et maintenant, pour mes projets personnels, j'accumulerai aussi les journaux. C'est devenu une habitude. Après avoir travaillé dans de grandes entreprises pendant quelques années, j'ai en quelque sorte plus de patience ou de stratégie pour rendre mes projets plus grands et plus longs. Donc je sais que j'aurai besoin de ces journaux au fil du temps.

Quelqu'un pourrait dire qu'il suffit d'avoir un code élégant et un projet fonctionnel. Vous n'avez pas besoin d'accumuler les journaux ou les traces de pile d'erreurs. C'est bon. Quand nous avons un bug ou une nouvelle fonctionnalité, nous pouvons exécuter le programme pour obtenir les journaux actuels. Nous n'avons pas besoin des journaux du processus de développement. Ils sont comme les enregistrements détaillés des expériences scientifiques. À première vue, cela semble bien. Mais à long terme, si un jour vous voulez y retravailler, ou si vous voulez le partager, ou laisser d'autres le reprendre, cela pourrait ne pas être bon.

Je pense qu'il pourrait y avoir de bonnes opportunités ici. Dans les entreprises, pourquoi n'encourageons-nous pas chaque développeur à partager ses journaux accumulés ? Dans les projets open source, nous devrions avoir cela aussi. Nous ne trouvons pas les journaux des autres attrayants parce que nous ne les connaissons pas. Nous perdons le contexte lorsque nous enregistrons ces journaux. Et à l'intérieur, il semble y avoir des tonnes de messages non pertinents ou insignifiants.

Mais l'effort pour accumuler des journaux est trivial. Il suffit de copier-coller chaque fois que nous voyons des journaux, en particulier les journaux d'erreur. Et si nous le faisions de manière automatisée ? C'est une bonne idée d'enregistrer les journaux dans un répertoire chaque fois que nous exécutons un projet, comme ces projets Spring Boot.

Le monde devient de plus en plus numérique, donc accumuler des journaux de programmes numériques, c'est comme accumuler des livres dans un monde physique.