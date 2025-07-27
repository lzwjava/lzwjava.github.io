---
audio: false
generated: false
image: false
lang: de
layout: post
title: Software-Engineering für KI optimieren
translated: true
---

In diesem Blog habe ich Hunderte von Skripten genutzt, um bei Übersetzungen, Spielwiesen, Frontmatter-Wartung und Telegram-Bots zu helfen. Ich glaube, dieser Entwicklungsansatz könnte die Zukunft der Softwareentwicklung darstellen, die für KI optimiert ist.

Ich verlasse mich nicht stark auf die Funktionalität von Python-Modulen, und ich möchte den Code nicht wie ein großes Java-Spring-Projekt strukturieren.

Ich habe meinem vorherigen Teamleiter gesagt, dass ihre Bankarchitektur zwar beeindruckend ist, aber wenn wir heute anfangen würden, würde ich eine Optimierung für LLM/KI in Betracht ziehen. Dies würde eine bessere Kontexttechnik, eine verbesserte Trennung der Kontexte und die Priorisierung von KI-erstem Denken gegenüber menschenzentriertem Design beinhalten. Während Spring mehrere Ebenen und eine gute Abstraktion bietet, kann es für LLM/KI schwierig sein, diese zu navigieren.

Ich glaube, wir sollten flachere Strukturen anstreben, ähnlich wie eine flache Organisation. Das bedeutet, nur zwei Ebenen zu verwenden: die erste Ebene ruft die zweite Ebene auf. In einer Funktion ist es besser, direkt 50 andere Funktionen aufzurufen, anstatt 50 verschachtelte Ebenen oder Stapel zu haben. KI/LLM haben Schwierigkeiten, übermäßig komplexe, verschachtelte Strukturen zu beurteilen oder abzuleiten, aber sie sind gut darin, kleinere Funktionen mit 100 bis 200 Codezeilen zu handhaben. Python eignet sich gut zum Aufrufen und Importieren aus anderen Dateien.

Ein Grund, warum Python-Code einfacher ist als Java, ist, dass die Abhängigkeitsverwaltung einfach ist. Man muss nur `pip install` verwenden, um eine Abhängigkeit hinzuzufügen. Bei Maven muss man die Abhängigkeit in einer POM-XML-Datei schreiben und dann `mvn compile` verwenden, damit Maven die Abhängigkeiten herunterlädt.

Ein weiterer Grund für die Einfachheit von Python ist, dass der Code direkt ohne Probleme ausgeführt werden kann.

Obwohl ab Java 11 der `java`-Befehl einzelne Quellcode-Dateien direkt ausführen kann, ohne dass sie separat mit `javac` kompiliert werden müssen, sind Java-Projekte oft groß, sodass man sie mit `mvn spring-boot:run` zusammen mit einigen Eigenschaftskonfigurationen ausführen muss.

Ein dritter Grund ist, dass das Modul-Design von Python einfach ist; man kann `from` und `import` verwenden, um Code einfach aus anderen Dateien zu importieren.

Derzeit können viele KI-Chatbots Python-Code direkt im Chatbot-Fenster ausführen, wie z. B. Grok.

Beim Vergleich von 100 Java-Dateien, jeweils mit etwa 1000 Codezeilen, mit einigen einfachen Python-Skripten ist das kein fairer Vergleich. Für dieses Projekt würde ich lieber 1000 Python-Dateien haben, jeweils mit etwa 100 Codezeilen.

Es ist akzeptabel, Codezeilen oder eine Funktion zum Bearbeiten auszuwählen. Aber man muss wissen, wo man auswählen soll. Warum nicht diese Aufgabe der KI überlassen, um unser Leben einfacher zu machen? Also müssen wir nur "Alles auswählen" verwenden, um den gesamten Code auszuwählen, und der KI/LLM sagen, wie sie ihn bearbeiten soll.

Für Python ist es einfacher, `if __name__ == "__main__":` zu verwenden, um Funktionen in einer Datei auszuführen und zu testen. Es ist auch einfacher für andere Python-Dateien, die Funktionen in dieser Datei aufzurufen, ohne die Tests ausführen zu müssen.

Das ist Kontexttechnik, die für KI optimiert ist. Könnten wir das auf andere Weise angehen? KI/LLM ist autoregressiv. Aber wenn wir Copilot oder Claude Code verwenden, wissen wir nicht, wie die KI-Software-Agenten uns helfen. Sie sollten darüber nachdenken, anstatt dass wir es tun.

Könnten wir auf der Benutzerseite den Code speziell anordnen, um die Token-Nutzung zu reduzieren? Für diesen Punkt ist der Ansatz mit 1000 Python-Dateien, jeweils mit 100 Codezeilen, gut für diesen Zweck. Denn man kann Funktionen und Code-Dateien leicht überprüfen, bevor andere Python-Code sie aufrufen.

Aber ein Problem ist, dass es nicht einfach ist, mehrere Code-Dateien gleichzeitig zu ändern. Für eine einfache Methode kann man den Code zu KI-Chatbots kopieren und sie können einem sagen, wie man den Code in diesen Dateien bearbeitet.

Möglicherweise müssen wir die Anzahl der Zeilen nicht verwenden, um Funktionen oder Logik zu trennen. Aber wir sollten es tun, um die Logik in kleine Funktionen zu trennen. Wir können dies tun, indem wir sie natürlich nach Art der Logik trennen, sodass sie kürzer erscheinen.

Warum wollen wir Software-Engineering, das für KI optimiert ist? Weil KI mächtig ist, sollten wir alles für KI optimieren und dann die KI so weit wie möglich bei der Software-Engineering unterstützen lassen.

Das ist nicht nur für Code möglich, sondern auch für jeden Text. Angenommen, wir sind sehr wählerische Redakteure; wir wollen nicht, dass KI unsere großen Texte auf einmal bearbeitet. Wir wollen Absatz für Absatz prüfen. Für Code können wir kleinere Fehler oder Bugs tolerieren. Für Text können wir sie tolerieren, weil die meisten Leser nicht so wählerisch sind.

Aber Code ist anders, denn manchmal kann schon ein kleiner Fehler zum vollständigen Ausfall eines großen Projekts führen.

Für XML- oder YAML-Dateien müssen wir sie wahrscheinlich nicht so stark trennen, weil sie bereits stark strukturiert sind.

Und für HTML-Dateien sollten wir eine Trennung vornehmen. Statt Hunderte von JavaScript-Dateien zusammen mit Hunderte von HTML-Dateien zu schreiben, wodurch es einfach ist, über 1000 Codezeilen zu überschreiten, sollten wir `import` für JavaScript verwenden, um dies zu verwalten. Für JavaScript-Code können wir die oben genannten Methoden zur Trennung verwenden.

Wir wollen den Code so strukturieren, dass KI uns leicht helfen kann, Code hinzuzufügen, zu bearbeiten, zu löschen und auszuführen. Das ist der Anfang. Stellen Sie sich einen Tag vor, an dem alle Codes von KI leicht generiert oder repariert werden können. Die Welt wird hochgradig digitalisiert sein.

Stellen Sie sich vor, ich schreibe 100 große Softwareprojekte und biete APIs zum Verbinden mit anderen an. Dazu gehört mein täglicher Kalender; ich bin selbst wie ein Tech-Unternehmen mit 1000 Mitarbeitern heutzutage. Sie sind für meine Bedürfnisse angepasst, um Geld zu verdienen oder Geld für meine Vorteile auszugeben. Das ist wirklich erstaunlich.