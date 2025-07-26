---
audio: false
generated: false
image: true
lang: de
layout: post
title: Ein wählerischer Ingenieursblick auf KI-Programmierwerkzeuge
translated: true
---

Kürzlich habe ich Claude Code erfolgreich ausgeführt, daher möchte ich meine Tool-Auswahlreise teilen. Ich habe auch einige [AI-Tool-Tipps](ai-tips-en) unterwegs gesammelt.

Ich war relativ spät dabei, Claude Code zu übernehmen.

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet) wurde Ende Februar 2025 veröffentlicht.

Ich hatte erst kürzlich Erfolg, es auszuprobieren. Ein Grund dafür ist, dass es die Anthropic-API erfordert, die chinesische Visa-Karten nicht unterstützt.

Ein weiterer Grund ist, dass [Claude Code Router](https://github.com/musistudio/claude-code-router) verfügbar wurde, was meinen letzten Versuch erfolgreich machte.

Ich höre immer wieder Lob darüber. Ich habe den Gemini CLI im Juli 2025 ausprobiert, aber nach mehreren gescheiterten Versuchen, ihn zum Reparieren meines Codes zu bringen, aufgegeben.

Ich habe auch Aider, einen weiteren Software-Agenten, ausprobiert. Ich habe Cursor nach etwa sechs Monaten aufgegeben, weil viele seiner VSCode-basierten Plugins nicht funktionierten. Ich habe kurz mit Cline experimentiert, aber nicht übernommen.

Ich verwende das Copilot-Plugin in VSCode mit einem angepassten Modell, Grok 3 Beta über OpenRouter, was gut funktioniert.

Ich denke nicht, dass Claude Code meine Gewohnheiten ändern wird, aber da ich es erfolgreich ausführen kann und die Geduld habe, es noch ein paar Mal auszuprobieren, werde ich sehen, wie ich mich in den kommenden Wochen fühle.

Ich bin ein wählerischer Benutzer mit 10 Jahren Software-Engineering-Erfahrung. Ich hoffe, dass Tools im tatsächlichen Einsatz großartig sind. Ich kaufe keine Marke ein – ich kümmere mich nur um den täglichen Nutzen.

Nach der Verwendung von Claude Code zur Korrektur der Grammatik dieses Beitrags habe ich festgestellt, dass es in bestimmten Szenarien gut funktioniert. Obwohl ich KI für die Grammatikhilfe schätze (ich habe sogar ein Python-Skript geschrieben, um LLM-APIs für diesen Zweck aufzurufen), habe ich ein frustrierendes Muster bemerkt – selbst wenn ich minimale Korrekturen anfordere, tauchen die Tools mit zahlreichen Grammatikvorschlägen zur Überprüfung auf. Dieser manuelle Überprüfungsprozess macht den Zweck der Automatisierung zunichte. Als Kompromiss lasse ich die KI jetzt ganze Aufsätze bearbeiten, obwohl dieser Ansatz meine Lernmöglichkeiten einschränkt, da ich die spezifischen Korrekturen nicht sehe, die vorgenommen werden.

Was mich am meisten beeindruckt hat, ist, wie Claude Code Änderungen anzeigt – es zeigt Vorher-Nachher-Vergleiche ähnlich wie git diffs, was das Überprüfen der Bearbeitungen viel einfacher macht.

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Quelle: Selbst-Screenshot*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Quelle: Selbst-Screenshot*{: .caption }