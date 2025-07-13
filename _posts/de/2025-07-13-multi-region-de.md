---
audio: false
generated: false
lang: de
layout: post
title: Gedanken zur mehrregionalen Softwareentwicklung
translated: true
---

Für internationale Unternehmen gibt es oft Projekte, die den Menschen mehrerer Regionen dienen, wie Singapur, Hongkong, UK, USA und China.

Ich habe an einigen Projekten gearbeitet, die Nutzern mehrerer Regionen dienen. Es ist nicht einfach, dies bei Backend-Projekten richtig zu machen.

Für die Standard Chartered Bank gibt es Apps wie SC Mobile India und SC Mobile Hongkong. Bei McDonald's gibt es Versionen wie McDonald's China und McDonald's USA. Bei Starbucks gibt es Starbucks USA und Starbucks China. Im Wesentlichen bieten sie verschiedenen Ländern ihre eigenen Apps an. Diese Apps nutzen wahrscheinlich unterschiedliche Backend-Server und haben einige abweichende Funktionen, behalten aber dieselbe Designsprache bei.

Es ist wahrscheinlich falsch, dies zu tun. In den ersten Jahren scheint es einfach oder machbar. Aber nach einem Jahrzehnt werden sie wissen, dass es sehr schmerzhaft ist. Die Wartungskosten oder Synchronisierungskosten, die Testkosten – es gibt tonnenweise doppelte Anstrengungen.

Allerdings ist es bei Facebook, Google oder Apple Pay irgendwie einfach. Jemand könnte sagen, dass sie keine Finanz-Apps sind; sie haben einige Compliance-Regeln, die eingehalten werden müssen. Das ist nicht wahr. Die Compliance bedeutet oft den Datenbankserver, die Datenbank oder einige Daten, die Regierungsbehörden überprüfen oder für Prüfungsunternehmen zur Prüfung benötigen.

Allerdings sind die anderen Anstrengungen dieselben. Die Software ist sehr flexibel. Wir sollten den Code im selben Repository haben, wir sollten die Datenquellenkonfiguration nutzen, um die Daten verschiedener Regionen zu hosten, und wir sollten denselben Code, dasselbe Design, denselben Workflow und dieselben Tests so weit wie möglich teilen.

Apple Pay ist ein gutes Beispiel dafür. Der App Store ist auch ein gutes Beispiel dafür. Sie bedienen jedes Land.

Es gibt wahrscheinlich einige Projekte in großen Tech-Unternehmen, die Kontinente zur Trennung nutzen, wie Asien und den Pazifik, Nordamerika. Auch dafür.

Das Erste, was man bei der Multi-Region-Entwicklung tun sollte, ist zu wissen, was anders ist, welche Compliance wir einhalten müssen und wie man doppelte Anstrengungen so weit wie möglich reduzieren kann.

Bei Text-to-Speech muss Google Cloud unterschiedliche Sprachen trainieren. Sie bieten unterschiedliche Modelle und Sprachen dafür an. Bei Sprachen sind die Unterschiede zwischen den Sprachen ihre Klänge, ihre Aussprache und ihr Schriftbild. Das Erste bedeutet, dass man bei der Nutzung von Google Cloud für Text-to-Speech unterschiedliche Modelle verwenden muss. Beim Schriftbild bedeutet das, dass man bei der PDF-Generierung vorsichtig mit der Schriftauswahl sein muss.

Bei Multi-Region-Projekten kann man in Spring Boot-Projekten Aliase und unterschiedliche Objektinitialisierungen dafür nutzen. Man kann Eigenschaften oder YAML-Konfigurationen intelligent nutzen. Man kann alle unterschiedlichen Logiken basierend auf der Region in bestimmte Module oder Klassen legen.

Und bei der Code-Hosting kann es zunächst einfach erscheinen, unterschiedliche Zweige für unterschiedliche Länder zu nutzen, aber nach einigen Jahren wird man wissen, wie schmerzhaft es ist. Man muss für andere Regionen git cherry-pick machen. Und man muss in einem anderen Zweig erneut testen. Jedes Mal, wenn man eine kleine Änderung vornimmt, muss man sie in die Zweige synchronisieren. Und mit der Zeit, wenn wir uns nicht bemühen, den Code oder die Logik so weit wie möglich zu minimieren, werden die Unterschiede im Code zwischen mehreren Regionen oder Ländern groß genug, um nicht mehr reparierbar zu sein.

Die gute Nachricht ist, dass jetzt KI uns helfen kann, den Code zu refaktorieren oder besser zu schreiben oder die Multi-Region-Code-Design-Probleme zu beheben. Egal wie groß der Fehler ist, wenn wir ihn beheben, ist es ein kleiner Fehler.