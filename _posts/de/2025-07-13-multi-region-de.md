---
audio: false
generated: false
lang: de
layout: post
title: Gedanken zur mehrregionalen Softwareentwicklung
translated: true
---

Für internationale Unternehmen gibt es oft Projekte, die den Menschen mehrerer Regionen dienen, wie Singapur, Hongkong, UK, USA und China.

Ich habe an einigen Projekten gearbeitet, die Nutzern mehrerer Regionen dienen. Es ist nicht einfach, dies in Backend-Projekten richtig zu machen.

Für die Standard Chartered Bank gibt es die SC Mobile India-App, die SC Mobile Hong Kong-App usw. Sie geben den Ländern im Grunde ihre eigenen Apps. Sie verwenden wahrscheinlich unterschiedliche Apps, unterschiedliche Backend-Server und einige Funktionen sind unterschiedlich, aber mit derselben Designsprache.

Es ist wahrscheinlich falsch, dies zu tun. In den ersten Jahren scheint es einfach oder machbar. Aber nach einem Jahrzehnt werden sie wissen, dass es sehr schmerzhaft ist. Die Wartungskosten oder Synchronisierungskosten, die Testkosten – es gibt Tonnen an doppelten Anstrengungen.

Allerdings ist es bei Facebook, Google oder Apple Pay irgendwie einfach. Jemand könnte sagen, sie seien keine Finanz-Apps; sie hätten einige Compliance-Regeln, die eingehalten werden müssen. Das ist nicht wahr. Die Compliance bedeutet oft den Datenbankserver oder die Datenbank oder einige Daten, die Regierungsbehörden prüfen oder für Prüfungsunternehmen Audits durchführen wollen.

Allerdings sind die anderen Anstrengungen dieselben. Die Software ist sehr flexibel. Wir sollten den Code im selben Repository haben, wir sollten die Datenquellenkonfiguration nutzen, um die Daten verschiedener Regionen zu hosten, und wir sollten denselben Code, dasselbe Design, denselben Workflow und dieselben Tests so weit wie möglich teilen.

Apple Pay ist ein gutes Beispiel dafür. Der App Store ist auch ein gutes Beispiel dafür. Sie bedienen jedes Land.

Es gibt wahrscheinlich einige Projekte in großen Tech-Unternehmen, die Kontinente zur Trennung nutzen, wie Asien und den Pazifik, Nordamerika. Auch dafür.

Das Erste, was man bei der Multi-Region-Entwicklung tun muss, ist zu wissen, was unterschiedlich ist, welche Compliance man einhalten muss und wie man doppelte Anstrengungen so weit wie möglich reduzieren kann.

Bei Text-to-Speech muss Google Cloud unterschiedliche Sprachen trainieren. Sie bieten unterschiedliche Modelle und unterschiedliche Sprachen dafür an. Bei Sprachen sind die Unterschiede zwischen den Sprachen ihre Klänge, ihre Aussprache und ihr Schriftbild. Das Erste bedeutet, dass man bei der Nutzung von Google Cloud für Text-to-Speech unterschiedliche Modelle verwenden muss. Beim Schriftbild bedeutet das, dass man bei der PDF-Generierung vorsichtig mit der Schriftauswahl sein muss.

Bei Multi-Region-Projekten kann man in Spring Boot-Projekten Aliase und unterschiedliche Objektinitialisierungen verwenden. Man kann Eigenschaften oder YAML-Konfigurationen intelligent nutzen. Man kann alle unterschiedlichen Logiken basierend auf der Region in bestimmte Module oder Klassen legen.

Und bei der Code-Hosting, scheinen unterschiedliche Branches für unterschiedliche Länder zunächst einfach, aber nach einigen Jahren weiß man, wie schmerzhaft es ist. Man muss für andere Regionen git cherry-pick machen. Und man muss in einem anderen Branch erneut testen. Jedes Mal, wenn man eine kleine Änderung vornimmt, muss man sie in die Branches synchronisieren. Und mit der Zeit, wenn wir uns nicht bemühen, den Code oder die Logikunterschiede zu minimieren, werden die Unterschiede im Code zwischen mehreren Regionen oder Ländern groß genug, um nicht mehr reparierbar zu sein.

Die gute Nachricht ist, dass jetzt KI uns helfen kann, Code zu refaktorieren oder besser zu schreiben oder die Multi-Region-Code-Design-Probleme zu beheben. Egal wie groß der Fehler ist, wenn wir ihn beheben, ist es ein kleiner Fehler.