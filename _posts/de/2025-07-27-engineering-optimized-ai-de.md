---
audio: false
generated: false
image: false
lang: de
layout: post
title: Software-Engineering für KI optimieren
translated: true
---

In diesem Blog habe ich Hunderte von Skripten genutzt, um bei Übersetzungen, Spielwiesen, Frontmatter-Wartung und Telegram-Bots zu unterstützen. Ich glaube, dieser Entwicklungsansatz könnte die Zukunft der Softwareentwicklung darstellen, die für KI optimiert ist.

Ich stütze mich nicht stark auf die Funktionalität von Python-Modulen, und ich möchte den Code auch nicht wie ein großes Java-Spring-Projekt strukturieren.

Ich habe im Laufe meiner Karriere an vielen Softwareprojekten gearbeitet. Ich habe beeindruckende Bankarchitekturen, Microservices, effektive Mehrländer-Designs zur Minimierung von Duplikaten, robuste Grundgerüste auf Basis von Spring und starke Governance mit zentralisierter Konfiguration beobachtet.

Obwohl diese Bankarchitekturen beeindruckend sind, würde ich, wenn wir heute damit beginnen würden, eine Optimierung für LLMs und KI in Betracht ziehen. Dies würde eine bessere Kontexttechnik, eine verbesserte Trennung von Verantwortlichkeiten und die Priorisierung von KI-erster-Denken gegenüber menschenzentriertem Design beinhalten. Obwohl Spring mehrere Schichten und gute Abstraktion bietet, kann es für LLMs und KI schwierig sein, diese zu navigieren.

Ich glaube, wir sollten flachere Strukturen anstreben, ähnlich einer flachen Organisation. Das bedeutet, nur zwei Ebenen zu verwenden: die erste Ebene ruft die zweite Ebene auf. In einer Funktion ist es besser, direkt 50 andere Funktionen aufzurufen, anstatt 50 verschachtelte Ebenen oder Stapel zu haben. KI/LLMs haben Schwierigkeiten, übermäßig komplexe, verschachtelte Strukturen zu beurteilen oder abzuleiten, aber sie sind gut im Umgang mit kleineren Funktionen von 100 bis 200 Codezeilen. Python eignet sich gut zum Aufrufen und Importieren aus anderen Dateien.

Ein Grund, warum Python-Code einfacher ist als Java, ist, dass die Abhängigkeitsverwaltung einfach ist. Man muss nur `pip install` verwenden, um eine Abhängigkeit hinzuzufügen. Bei Maven muss man die Abhängigkeit in einer POM-XML-Datei schreiben und dann `mvn compile` verwenden, damit Maven die Abhängigkeiten herunterlädt.

Ein weiterer Grund für die Einfachheit von Python ist, dass der Code direkt ohne Umstände ausgeführt werden kann.

Obwohl ab Java 11 der `java`-Befehl einzelne Quellcode-Dateien ohne separate Kompilierung mit `javac` direkt ausführen kann, sind Java-Projekte oft groß, sodass man sie mit `mvn spring-boot:run` zusammen mit einigen Eigenschaftskonfigurationen ausführen muss.

Ein dritter Grund ist, dass das Modul-Design von Python einfach ist; man kann `from` und `import` verwenden, um Code einfach aus anderen Dateien zu importieren.

Derzeit können viele KI-Chatbots Python-Code direkt im Chatbot-Fenster ausführen, wie z. B. Grok.

Beim Vergleich von 100 Java-Dateien mit jeweils etwa 1000 Codezeilen mit einigen einfachen Python-Skripten ist das kein fairer Vergleich. Für dieses Projekt würde ich lieber 1000 Python-Dateien mit jeweils etwa 100 Codezeilen haben.

Es ist akzeptabel, Codezeilen oder eine Funktion zum Bearbeiten auszuwählen. Man muss jedoch wissen, wo man auswählen soll. Warum nicht diese Aufgabe von der KI erledigen lassen, um unser Leben einfacher zu machen? Wir müssen also nur "Alles auswählen" verwenden, um den gesamten Code auszuwählen, und der KI/LLM sagen, wie sie ihn bearbeiten soll.

Für Python ist es einfacher, `if __name__ == "__main__":` zu verwenden, um Funktionen in einer Datei auszuführen und zu testen. Es ist auch einfacher für andere Python-Dateien, die Funktionen in dieser Datei aufzurufen, ohne die Tests ausführen zu müssen.

Das ist Kontexttechnik, die für KI optimiert ist. Könnten wir das auf andere Weise angehen? KI/LLM ist autoregressiv. Wenn wir jedoch Copilot oder Claude Code verwenden, wissen wir nicht, wie die KI-Software-Agenten uns helfen. Sie sollten stattdessen für uns nachdenken.

Könnten wir auf der Benutzerseite den Code speziell anordnen, um den Token-Verbrauch zu reduzieren? Für diesen Punkt ist der Ansatz mit 1000 Python-Dateien mit jeweils 100 Codezeilen gut für diesen Zweck geeignet. Denn man kann Funktionen und Code-Dateien leicht überprüfen, bevor andere Python-Code sie aufrufen.

Aber ein Problem ist, dass es nicht einfach ist, mehrere Code-Dateien gleichzeitig zu ändern. Für eine einfache Methode können Sie den Code in KI-Chatbots kopieren und sie Ihnen sagen lassen, wie Sie den Code in diesen Dateien bearbeiten sollen.

Möglicherweise müssen wir die Anzahl der Codezeilen nicht verwenden, um Funktionen oder Logik zu trennen. Aber wir sollten dies tun, um die Logik in kleine Funktionen zu trennen. Wir können dies tun, indem wir sie natürlich nach Art der Logik trennen, sodass sie kürzer erscheinen.

Warum wollen wir Software-Engineering, das für KI optimiert ist? Weil KI mächtig ist, sollten wir alles für KI optimieren und dann die KI so weit wie möglich bei der Software-Engineering unterstützen.

Das ist nicht nur für Code möglich, sondern auch für jeden Text. Angenommen, wir sind sehr wählerische Redakteure; wir wollen nicht, dass KI unsere großen Texte auf einmal bearbeitet. Wir wollen Absatz für Absatz prüfen. Bei Code können wir kleinere Fehler oder Bugs tolerieren. Bei Text können wir sie tolerieren, weil die meisten Leser nicht so wählerisch sind.

Aber Code ist anders, denn manchmal kann bereits ein kleiner Fehler zum vollständigen Ausfall eines großen Projekts führen.

Für XML- oder YAML-Dateien müssen wir sie wahrscheinlich nicht so stark trennen, weil sie bereits hoch strukturiert sind.

Und für HTML-Dateien sollten wir eine Trennung vornehmen. Statt Hunderte von JavaScript-Dateien zusammen mit Hunderte von HTML-Dateien zu schreiben, was es einfach macht, 1000 Codezeilen zu überschreiten, sollten wir `import` für JavaScript verwenden, um dies zu verwalten. Für JavaScript-Code können wir die oben genannten Methoden zur Trennung verwenden.

Wir wollen den Code so strukturieren, dass die KI uns leicht beim Hinzufügen, Bearbeiten, Löschen und Ausführen von Code helfen kann. Das ist der Anfang. Stellen Sie sich einen Tag vor, an dem der gesamte Code leicht von der KI generiert oder repariert werden kann. Die Welt wird hochgradig digitalisiert sein.

Stellen Sie sich vor, ich schreibe 100 große Softwareprojekte und biete APIs zum Verbinden mit anderen an. Dazu gehört auch mein täglicher Kalender; ich bin selbst wie ein Tech-Unternehmen mit 1000 Mitarbeitern. Sie sind auf meine Bedürfnisse zugeschnitten, um Geld zu verdienen oder Geld für meinen Nutzen auszugeben. Das ist wirklich erstaunlich.