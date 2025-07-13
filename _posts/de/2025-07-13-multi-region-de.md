---
audio: false
generated: false
lang: de
layout: post
title: Mehrregionale Softwareentwicklung
translated: true
---

Für internationale Unternehmen gibt es oft Projekte, die den Menschen mehrerer Regionen dienen, wie Singapur, Hongkong, Großbritannien, USA und China.

Ich habe an einigen Projekten gearbeitet, die Nutzern mehrerer Regionen dienen. Es ist nicht einfach, dies bei Backend-Projekten richtig zu machen.

Für die Standard Chartered Bank gibt es Apps wie SC Mobile India und SC Mobile Hongkong. Bei McDonald's gibt es Versionen wie McDonald's China und McDonald's USA. Bei Starbucks gibt es Starbucks USA und Starbucks China. Im Wesentlichen bieten sie jedem Land seine eigene App. Oft unterscheiden sich die Anmeldeverfahren für Nutzer in China und internationale Nutzer. Neben der Nutzung von Mobiltelefonen haben chinesische Nutzer oft die Möglichkeit, sich mit WeChat anzumelden, während internationale Nutzer sich mit Facebook, Google oder Apple anmelden können. Diese Apps nutzen wahrscheinlich unterschiedliche Backend-Server und haben einige unterschiedliche Funktionen, behalten aber dieselbe Designsprache bei.

Es ist wahrscheinlich falsch, dies zu tun. In den ersten Jahren scheint es einfach oder machbar. Aber nach einem Jahrzehnt werden sie wissen, dass es sehr schmerzhaft ist. Die Wartungskosten oder Synchronisierungskosten, die Testkosten – es gibt tonnenweise doppelte Anstrengungen.

Allerdings ist es für Facebook, Google oder Apple Pay irgendwie einfach. Jemand könnte sagen, sie seien keine Finanz-Apps; sie hätten einige Compliance-Regeln, die befolgt werden müssen. Das ist nicht wahr. Die Compliance bedeutet oft den Datenbankserver, die Datenbank oder einige Daten, die Regierungsbehörden prüfen oder für Prüfungsunternehmen zur Prüfung benötigen.

Allerdings sind die anderen Anstrengungen dieselben. Die Software ist sehr flexibel. Wir sollten den Code im selben Repository haben, wir sollten die Datenquellenkonfiguration nutzen, um die Daten verschiedener Regionen zu hosten, und wir sollten denselben Code, dasselbe Design, denselben Workflow und dieselben Tests so weit wie möglich teilen.

Apple Pay ist ein gutes Beispiel dafür. Der App Store ist auch ein gutes Beispiel dafür. Sie bedienen jedes Land.

Es gibt wahrscheinlich einige Projekte in großen Technologieunternehmen, die Kontinente zur Trennung nutzen, wie Asien und den Pazifik, Nordamerika. Auch dafür.

Das Erste, was man bei der Entwicklung mehrerer Regionen tun muss, ist zu wissen, was anders ist, welche Compliance wir befolgen müssen und wie man doppelte Anstrengungen so weit wie möglich reduzieren kann.

Für Text-to-Speech benötigt Google Cloud unterschiedliche Sprachen. Sie bieten unterschiedliche Modelle und unterschiedliche Sprachen dafür. Bei Sprachen sind die Unterschiede zwischen den Sprachen ihre Klänge und ihr Schriftbild. Letzteres bedeutet, dass wir bei der PDF-Generierung auf die Schriftauswahl achten müssen.

Bei Projekten mit mehreren Regionen können wir in Spring Boot-Projekten Aliase und unterschiedliche Objektinitialisierungen verwenden. Wir können Eigenschaften oder YAML-Konfigurationen intelligent nutzen. Wir können alle unterschiedlichen Logiken basierend auf der Region in bestimmte Module oder Klassen legen.

Und für die Code-Hosting, scheinen unterschiedliche Zweige für unterschiedliche Länder zunächst einfach, aber nach einigen Jahren werden Sie wissen, wie schmerzhaft es ist. Sie müssen für andere Regionen git cherry-pick machen. Und Sie müssen in einem anderen Zweig erneut testen. Jedes Mal, wenn Sie eine kleine Änderung vornehmen, müssen Sie sie in die Zweige synchronisieren. Und mit der Zeit, wenn wir uns nicht bemühen, den Code oder die Logik so weit wie möglich zu minimieren, werden die Unterschiede im Code zwischen mehreren Regionen oder Ländern groß genug, um nicht mehr reparierbar zu sein.

Die gute Nachricht ist, dass jetzt KI uns helfen kann, den Code zu refaktorieren oder besser zu schreiben oder die Mehrregionen-Code-Designprobleme zu beheben. Egal wie groß der Fehler ist, wenn wir ihn beheben, ist es ein kleiner Fehler.

Nicht nur für die Codierung, Bereitstellung und Wartung der Veröffentlichung, sondern auch für die Erweiterbarkeit. Überlegen Sie, wie Sie ein neues Land oder eine neue Region hinzufügen. Wie viel Aufwand wird das erfordern? Wenn es minimal ist oder nur einige Konfigurationen erfordert, dann ist unser Design großartig. Wenn es einige Monate dauert, ist das auch akzeptabel. Wenn es mehrere Jahre dauert, werden wir es dann immer noch durchführen?

In Yin Wangs Essay, [On Linux，Windows und Mac](https://www.yinwang.org/blog-cn/2013/03/07/linux-windows-mac), erwähnte er, dass ein Adobe-Designer ihm sagte, sie hätten zwei Jahre damit verbracht, von Windows zu macOS zu migrieren.

Wird die Unterstützung einer neuen Region zwei Jahre Anpassung erfordern? Bei einigen Projekten könnte es so sein. Dies ist eine kritische Designüberlegung.

Die Welt wird immer stärker vernetzt. Egal, welches Land oder welche Region wir zunächst anvisieren, wir müssen auch andere Regionen berücksichtigen. Es ist besser, es von Anfang an richtig zu machen. Für etablierte internationale Unternehmen ist es ratsam, Softwareprodukte für mindestens zwei Länder oder Regionen von Anfang an zu entwickeln. Behalten Sie diesen Mehrregionen-Mindset von Anfang an bei. Wenn wir mehr Engineering-Ressourcen haben, können wir mehr Länder oder Regionen unterstützen.