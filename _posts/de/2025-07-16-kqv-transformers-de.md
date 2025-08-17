---
audio: false
generated: false
image: false
lang: de
layout: post
title: KQV, Transformer und GPT
translated: true
---

## Wie ich den KQV-Mechanismus in Transformern gelernt habe

*2025.07.16*

Nach dem Lesen von [K, Q, V Mechanism in Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en) habe ich irgendwie verstanden, wie K, Q und V funktionieren.

Q steht für Query, K für Key und V für Value. Bei einem Satz ist die Query eine Matrix, die den Wert eines Tokens speichert, über das es andere Token befragen muss. Der Key steht für die Beschreibung der Token, und der Value steht für die eigentliche Bedeutungsmatrix der Token.

Sie haben spezifische Formen, daher muss man ihre Dimensionen und Details kennen.

Ich habe das etwa Anfang Juni 2025 verstanden. Zum ersten Mal bin ich Ende 2023 darauf gestoßen. Damals habe ich Artikel wie [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) gelesen, aber nicht viel verstanden.

Nach etwa zwei Jahren fällt mir das Verständnis jetzt leichter. In diesen zwei Jahren habe ich mich auf Backend-Arbeit und die Vorbereitung auf meine Abschlussprüfungen konzentriert und nicht viel über maschinelles Lernen gelesen oder gelernt. Allerdings habe ich gelegentlich über diese Konzepte nachgedacht, zum Beispiel beim Autofahren oder bei anderen Tätigkeiten.

Das erinnert mich an die Wirkung von Zeit. Wir lernen vielleicht viele Dinge auf den ersten Blick, auch wenn wir sie nicht vollständig begreifen. Aber irgendwie löst es einen Startpunkt für unser Denken aus.

Mit der Zeit habe ich festgestellt, dass es bei Wissen und Entdeckungen schwer ist, Dinge beim ersten Mal zu verstehen oder zu durchdenken. Später scheint es jedoch einfacher zu sein, sie zu lernen und zu begreifen.

Ein Grund dafür ist, dass es im Zeitalter der KI einfacher ist zu lernen, weil man sich in jedes Detail oder jeden Aspekt vertiefen kann, um seine Zweifel zu klären. Es gibt auch mehr verwandte KI-Videos. Noch wichtiger ist, dass man sieht, wie viele Menschen auf dieser Grundlage lernen und Projekte aufbauen, wie z. B. [llama.cpp](https://github.com/ggml-org/llama.cpp).

Die Geschichte von Georgi Gerganov ist inspirierend. Als neuer Lernender im Bereich maschinelles Lernen, der etwa 2021 begann, hat er einen starken Einfluss in der KI-Community hinterlassen.

Solche Dinge werden sich immer wieder wiederholen. Daher denke ich, dass ich für verstärkendes Lernen und das neueste KI-Wissen, auch wenn ich ihnen noch nicht viel Zeit widmen kann, trotzdem etwas Zeit finden kann, um schnell zu lernen und viel darüber nachzudenken. Das Gehirn wird seine Arbeit tun.

---

## Vom neuronalen Netzwerk zu GPT

*2023.09.28*

### YouTube-Videos

Andrej Karpathy - Let's build GPT: from scratch, in code, spelled out.

Umar Jamil - Attention is all you need (Transformer) - Modell-Erklärung (inkl. Mathematik), Inferenz und Training

StatQuest mit Josh Starmer - Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!

Pascal Poupart - CS480/680 Lecture 19: Attention and Transformer Networks

The A.I. Hacker - Michael Phi - Illustrated Guide to Transformers Neural Network: A step-by-step explanation

### Wie ich lerne

Nachdem ich die Hälfte des Buches "Neural Networks and Deep Learning" gelesen hatte, begann ich, das Beispiel eines neuronalen Netzes zur Erkennung handgeschriebener Ziffern nachzubauen. Ich erstellte ein Repository auf GitHub: https://github.com/lzwjava/neural-networks-and-zhiwei-learning.

Das ist der wirklich schwierige Teil. Wenn man etwas von Grund auf schreiben kann, ohne Code zu kopieren, versteht man es sehr gut.

Mein nachgebauter Code enthält noch nicht die Implementierung von update_mini_batch und Backpropagation. Durch das genaue Beobachten der Variablen in den Phasen des Ladens von Daten, des Feed-Forwarding und der Auswertung habe ich jedoch ein viel besseres Verständnis für Vektoren, Dimensionalität, Matrizen und die Formen der Objekte entwickelt.

Und ich begann, die Implementierung von GPT und Transformern zu lernen. Durch Wort-Einbettung (Word Embedding) und positionelle Kodierung (Positional Encoding) wird der Text in Zahlen umgewandelt. Im Grunde genommen gibt es dann keinen Unterschied mehr zu einem einfachen neuronalen Netzwerk, das handgeschriebene Ziffern erkennt.

Andrej Karpathys Vorlesung "Let's build GPT" ist sehr gut. Er erklärt die Dinge gut.

Der erste Grund ist, dass es wirklich von Grund auf ist. Zuerst sieht man, wie Text generiert wird. Es ist irgendwie unscharf und zufällig. Der zweite Grund ist, dass Andrej Dinge sehr anschaulich erklären kann. Andrej hat mehrere Monate am Projekt nanoGPT gearbeitet.

Mir ist eine neue Idee gekommen, um die Qualität einer Vorlesung zu beurteilen: Kann der Autor diesen Code wirklich schreiben? Warum verstehe ich etwas nicht und welches Thema hat der Autor ausgelassen? Neben diesen eleganten Diagrammen und Animationen, welche Mängel und Defekte haben sie?

Zurück zum eigentlichen Thema des maschinellen Lernens. Wie Andrej erwähnt, sind Dropout, Residual Connections, Self-Attention, Multi-Head Attention und Masked Attention wichtig.

Durch das Ansehen der oben genannten Videos begann ich, ein bisschen zu verstehen.

Durch positionelle Kodierung mit Sinus- und Kosinusfunktionen erhalten wir einige Gewichte. Durch Wort-Einbettung wandeln wir Wörter in Zahlen um.

$$
    PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = cos(pos/10000^{2i/d_{model}})
$$

> Die Pizza kam aus dem Ofen und sie schmeckte gut.

In diesem Satz: Wie weiß der Algorithmus, ob er sich auf Pizza oder Ofen bezieht? Wie berechnen wir die Ähnlichkeiten für jedes Wort im Satz?

Wir möchten eine Reihe von Gewichten haben. Wenn wir das Transformer-Netzwerk für die Aufgabe der Übersetzung verwenden, gibt es jedes Mal, wenn wir einen Satz eingeben, den entsprechenden Satz in einer anderen Sprache aus.

Zum Skalarprodukt hier: Ein Grund, warum wir das Skalarprodukt verwenden, ist, dass es jede Zahl im Vektor berücksichtigt. Was wäre, wenn wir das quadrierte Skalarprodukt verwenden würden? Wir würden zuerst das Quadrat der Zahlen berechnen und dann das Skalarprodukt bilden. Was wäre, wenn wir ein umgekehrtes Skalarprodukt durchführen würden?

Zur Maskierung: Wir ändern die Zahlen der Hälfte der Matrix in negative Unendlichkeit. Dann verwenden wir Softmax, um die Werte auf den Bereich von 0 bis 1 zu bringen. Was wäre, wenn wir die Zahlen in der linken unteren Hälfte in negative Unendlichkeit ändern würden?

### Plan

Weiterhin Code und Papers lesen und Videos anschauen. Einfach Spaß haben und meiner Neugier folgen.

https://github.com/karpathy/nanoGPT

https://github.com/jadore801120/attention-is-all-you-need-pytorch