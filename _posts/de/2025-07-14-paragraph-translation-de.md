---
audio: false
generated: false
image: false
lang: de
layout: post
title: Kostenoptimierung bei Übersetzungen mit Absatz-basiertem Markdown
translated: true
---

Mein Jekyll-Blog verwendet Markdown, um Absätze zu schreiben. Nach dem Schreiben auf Englisch verwende ich KI-Tools wie DeepSeek oder Mistral, um in acht weitere Sprachen zu übersetzen. Obwohl sie bereits günstig sind, gibt es noch Verbesserungspotenzial.

Manchmal bearbeite ich nur ein Wort oder einen Absatz, und dann wird der gesamte Text eines Beitrags in die anderen acht Sprachen übersetzt. In diesem Fall ist der Token-Verbrauch hoch. Wenn ich nur den bearbeiteten Absatz erneut übersetze, ist der Token-Verbrauch geringer, besonders bei langen Beiträgen.

Ich möchte jedoch weiterhin Markdown verwenden, um meine Ideen festzuhalten. Die Pflege und Aktualisierung von Beiträgen in einer Datenbank ist nicht praktisch. YAML oder JSON könnten ebenfalls zu umständlich sein.

Der Schlüssel liegt darin, die Unterschiede zwischen dem Text vor und nach der Bearbeitung zu identifizieren. Wenn wir einen absatzbasierten Ansatz verwenden, bedeutet das, den Text mit dem Zeilenumbruch-Character "\n" zu teilen.

Ich muss wissen, welche Absätze sich nach der Bearbeitung geändert haben und welche nicht. Wir müssen eine eins-zu-eins-Absatzzuordnung zwischen dem Text vor und nach der Bearbeitung herstellen.

Wir verwenden einen absatzbasierten Ansatz, weil wir die von KI-Modellen erstellten Übersetzungen aktualisieren möchten. Wenn wir Sätze verwenden, könnte das möglicherweise nicht so genau sein.

Für Markdown könnte es wichtiger sein, eine Markdown-Analyse zu verwenden, um Übersetzungen basierend auf Markdown-Elementen zu synchronisieren.

Aber wenn es keine Code-Blöcke oder spezielle Markdown-Syntax gibt, können wir einen absatzbasierten Ansatz verwenden.

Für einen einfachen absatzbasierten Ansatz haben wir zwei Arrays von Absätzen und müssen wissen, wie sie übereinstimmen.

Beim Vergleichen eines beliebigen Absatzes in diesen beiden Arrays gibt es zwei mögliche Ergebnisse: Sie sind entweder gleich oder unterschiedlich. Wenn sie unterschiedlich sind, gibt es mehrere Fälle: Beide sind neu hinzugefügt, der linke ist neu hinzugefügt oder der rechte ist neu hinzugefügt.

Ich möchte einfach Kosten sparen, daher strebe ich eine Reduzierung des Token-Verbrauchs an. Ich brauche nichts anderes. Ich muss jeden Absatz übersetzen, das Ergebnis zwischenspeichern und beim nächsten Mal für jeden Absatz zuerst nach dem Übersetzungsergebnis suchen. Wenn es nicht existiert, muss ich ihn erneut übersetzen.

Für Markdown ist es etwas komplizierter. Ich möchte keine Code-Blöcke übersetzen. Daher können wir eine Markdown-Analysebibliothek verwenden, um Code-Blöcke und normalen Text unterschiedlich zu behandeln.

In ein paar Wochen werde ich dies mit Python und Grok umsetzen, weil es ein tatsächliches Problem ist. Ich muss es angehen.