---
audio: false
generated: true
lang: fr
layout: post
title: Programmation Réactive en Java
translated: true
---

Pour utiliser **reactor-core**, une bibliothèque Java pour construire des applications non bloquantes et asynchrones basées sur la spécification Reactive Streams, suivez ces étapes :

---

### 1. Ajouter reactor-core comme dépendance
Tout d'abord, incluez **reactor-core** dans votre projet. Selon votre outil de construction :

- **Maven** : Ajoutez ceci à votre `pom.xml` :
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle** : Ajoutez ceci à votre `build.gradle` :
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

Cela garantit que la bibliothèque est disponible dans votre projet. Vérifiez la dernière version sur [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core) si nécessaire.

---

### 2. Comprendre les composants principaux
Reactor-core fournit deux classes principales pour la programmation réactive :
- **`Flux`** : Représente un flux asynchrone qui peut émettre **0 à N éléments**.
- **`Mono`** : Représente un flux asynchrone qui émet **0 ou 1 élément**.

Ce sont les blocs de construction que vous utiliserez pour gérer les données de manière réactive.

---

### 3. Créer un Flux ou un Mono
Vous pouvez créer des instances de `Flux` ou `Mono` pour représenter vos flux de données.

- **Exemple avec Flux** (plusieurs éléments) :
  ```java
  Flux<Integer> numbers = Flux.just(1, 2, 3, 4, 5);
  ```

- **Exemple avec Mono** (un seul élément) :
  ```java
  Mono<String> greeting = Mono.just("Hello, World!");
  ```

La méthode `just` est un moyen simple de créer un flux à partir de valeurs statiques, mais Reactor propose de nombreuses autres méthodes de création (par exemple, à partir de tableaux, de plages ou de sources personnalisées).

---

### 4. S'abonner pour traiter les données
Pour consommer les éléments émis, vous devez **vous abonner** au `Flux` ou `Mono`. L'abonnement déclenche le flux pour commencer à émettre des données.

- **S'abonner à Flux** :
  ```java
  numbers.subscribe(System.out::println);  // Affiche : 1, 2, 3, 4, 5
  ```

- **S'abonner à Mono** :
  ```java
  greeting.subscribe(System.out::println); // Affiche : Hello, World!
  ```

La méthode `subscribe` peut également prendre des arguments supplémentaires, comme des gestionnaires d'erreurs ou des rappels de complétion, pour un contrôle accru.

---

### 5. Transformer les données avec des opérateurs
Reactor fournit un ensemble riche d'opérateurs pour manipuler les flux, tels que `map`, `filter`, et bien d'autres.

- **Exemple avec Flux et map** :
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // Affiche : 2, 4, 6, 8, 10
  ```

- **Exemple avec Mono et map** :
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // Affiche : HELLO, WORLD!
  ```

Ces opérateurs vous permettent de transformer, filtrer ou combiner les données de manière déclarative.

---

### 6. Gérer les erreurs et la contre-pression
Reactor-core prend en charge la gestion des erreurs et la gestion de la contre-pression :
- **Gestion des erreurs** : Utilisez `subscribe` avec un consommateur d'erreurs :
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // Affiche : Oops!
  ```
- **Contre-pression** : Contrôlez comment les abonnés gèrent les flux de données écrasants en utilisant des opérateurs comme `onBackpressureBuffer()` ou `onBackpressureDrop()`.

---

### 7. Explorer plus avant
Pour une utilisation plus avancée :
- Consultez la [documentation officielle de Reactor](https://projectreactor.io/docs/core/release/reference/) pour des exemples détaillés et des tutoriels.
- Consultez le [dépôt GitHub de reactor-core](https://github.com/reactor/reactor-core) pour des ressources supplémentaires.

---

### Résumé
Pour utiliser **reactor-core** :
1. Ajoutez-le comme dépendance dans votre projet.
2. Utilisez `Flux` pour plusieurs éléments ou `Mono` pour un seul élément.
3. Créez des flux avec des méthodes comme `just`.
4. Abonnez-vous pour traiter les données.
5. Appliquez des opérateurs pour transformer les flux selon vos besoins.

C'est un point de départ convivial pour la programmation réactive avec reactor-core. Expérimentez avec de petits exemples pour vous familiariser avec son paradigme réactif !