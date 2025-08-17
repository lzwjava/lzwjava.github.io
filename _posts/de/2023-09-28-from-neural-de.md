---
audio: false
generated: false
image: false
lang: de
layout: post
title: Vom neuronalen Netzwerk zu GPT
translated: true
---

### YouTube-Videos

Andrej Karpathy – Lasst uns GPT von Grund auf bauen: im Code, Schritt für Schritt erklärt.

Umar Jamil – Attention is all you need (Transformer) – Modell-Erklärung (inkl. Mathematik), Inferenz und Training

StatQuest mit Josh Starmer – Transformer-Neuronale Netze, die Grundlage von ChatGPT, klar erklärt!!!

Pascal Poupart – CS480/680 Vorlesung 19: Attention und Transformer-Netzwerke

The A.I. Hacker – Michael Phi – Illustrierte Anleitung zu Transformer-Neuronalen Netzen: Eine Schritt-für-Schritt-Erklärung

---

### Wie ich lerne

Nachdem ich die Hälfte des Buches *„Neural Networks and Deep Learning“* gelesen hatte, begann ich, das Beispiel des neuronalen Netzes zur Erkennung handgeschriebener Ziffern nachzubauen. Ich erstellte ein Repository auf GitHub: [https://github.com/lzwjava/neural-networks-and-zhiwei-learning](https://github.com/lzwjava/neural-networks-and-zhiwei-learning).

Das ist der wirklich schwierige Teil. Wenn man etwas von Grund auf selbst schreiben kann, ohne Code zu kopieren, hat man es wirklich verstanden.

Mein nachgebauter Code fehlt noch die Implementierung von `update_mini_batch` und Backpropagation. Allerdings habe ich durch das genaue Beobachten der Variablen in den Phasen des Ladens der Daten, des Forward-Pass und der Auswertung ein viel besseres Verständnis für Vektoren, Dimensionalität, Matrizen und die Form der Objekte entwickelt.

Dann begann ich, die Implementierung von GPT und Transformern zu lernen. Durch Wort-Einbettung (*Word Embedding*) und positionelle Kodierung wird der Text in Zahlen umgewandelt. Im Grunde gibt es dann keinen Unterschied mehr zu einem einfachen neuronalen Netz zur Erkennung handgeschriebener Ziffern.

Andrej Karpathys Vorlesung *„Let’s build GPT“* ist sehr gut. Er erklärt die Dinge verständlich.

Der erste Grund ist, dass er wirklich bei Null anfängt. Zuerst sieht man, wie Text generiert wird – zunächst unscharf und zufällig. Der zweite Grund ist, dass Andrej Dinge sehr anschaulich erklären kann. Er hat mehrere Monate am Projekt *nanoGPT* gearbeitet.

Mir kam gerade eine neue Idee, um die Qualität einer Vorlesung zu bewerten: **Kann der Autor diesen Code wirklich selbst schreiben?** Warum verstehe ich bestimmte Dinge nicht und welche Themen hat der Autor möglicherweise übersehen? Neben den eleganten Diagrammen und Animationen: **Wo liegen ihre Schwächen und Mängel?**

Zurück zum Thema *Machine Learning* selbst. Wie Andrej erwähnt: *Dropout*, *Residual Connections*, *Self-Attention*, *Multi-Head Attention*, *Masked Attention*.

Durch das Anschauen der oben genannten Videos begann ich, ein bisschen mehr zu verstehen.

Durch positionelle Kodierung mit Sinus- und Kosinusfunktionen erhalten wir bestimmte Gewichte. Durch *Word Embedding* wandeln wir Wörter in Zahlen um.

$$
    PE_{(pos,2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right) \\
    PE_{(pos,2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)
$$

> *„The pizza came out of the oven and it tasted good.“*

Wie erkennt der Algorithmus in diesem Satz, ob sich *„it“* auf *„pizza“* oder *„oven“* bezieht? Wie berechnen wir die Ähnlichkeiten für jedes Wort im Satz?

Wir brauchen eine Menge an Gewichten. Wenn wir ein Transformer-Netzwerk für Übersetzungsaufgaben verwenden, soll es bei der Eingabe eines Satzes den entsprechenden Satz in einer anderen Sprache ausgeben können.

Zum **Skalarprodukt** hier: Ein Grund, warum wir es verwenden, ist, dass es jeden Wert im Vektor berücksichtigt. Was wäre, wenn wir das **quadrierte Skalarprodukt** nehmen? Zuerst quadrieren wir die Zahlen und bilden dann das Skalarprodukt. Oder was wäre mit einem *„umgekehrten“* Skalarprodukt?

Bei der **Maskierung** setzen wir die Hälfte der Matrix auf negative Unendlich. Dann verwenden wir *Softmax*, um die Werte zwischen 0 und 1 zu skalieren. Was wäre, wenn wir stattdessen die **linke untere Hälfte** auf negative Unendlich setzen würden?

---

### Plan

Weiterhin Code und Papers lesen sowie Videos anschauen. Einfach Spaß haben und meiner Neugier folgen.

[https://github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

[https://github.com/jadore801120/attention-is-all-you-need-pytorch](https://github.com/jadore801120/attention-is-all-you-need-pytorch)