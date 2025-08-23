---
audio: false
generated: false
image: false
lang: de
layout: post
title: KI-Workflows, Code-Editoren und Plattform-Disruption
translated: true
---

### Inhaltsverzeichnis

1. [KI-Gedanken](#ki-gedanken)
   - KI fehlt echte Intelligenz oder Tiefe
   - Maschinelles Lernen ist fortgeschrittene angewandte Analysis
   - LLMs haben Schwierigkeiten mit strukturierten Dateiformaten
   - Open Source beseitigt technologische Geheimnisse
   - Textbasierte Tools werden zuerst von KI disruptiv verändert

2. [Neue Plattformen, die von KI-Workflows angetrieben werden](#neue-plattformen-die-von-ki-workflows-angetrieben-werden)
   - KI-Workflows automatisieren die Erstellung mehrsprachiger Inhalte
   - Benutzer reichen Prompts für Formatkonvertierungen ein
   - Plattformen ermöglichen die Verfeinerung und Zusammenfassung von Inhalten
   - Anpassbare KI-Workflows durch Schlüsselwort-Einstellungen
   - KI übernimmt die Inhaltsumwandlung von Anfang bis Ende

3. [Die nächste Richtung von KI-Code-Editoren](#die-nächste-richtung-von-ki-code-editoren)
   - Cloud-Integration ist entscheidend für CI/CD-Workflows
   - A/B-Tests verbessern KI-generierte Inhalte
   - RLHF erweitert Feedback aus realen Einsatzszenarien
   - Menschliches Feedback verfeinert unvollkommene KI-Ergebnisse
   - Prompt-Optimierung ist besser als Ausgabekorrektur


## KI-Gedanken

*Zuletzt aktualisiert im August 2025*

- Satya Nadella erwähnte das Jevons-Paradox. Es lohnt sich, dies zu lernen.

- Yin Wang: Es gibt keine „Intelligenz“ in künstlicher Intelligenz, kein „Neural“ in neuronalen Netzen, kein „Lernen“ in maschinellem Lernen und keine „Tiefe“ im Deep Learning. Was in diesem Bereich wirklich funktioniert, heißt „Analysis“. Daher bevorzuge ich die Bezeichnung „differenzierbare Berechnung“ für dieses Feld, und der Prozess des Modellbaus wird „differenzierbare Programmierung“ genannt.

- Yin Wang: Maschinelles Lernen ist wirklich nützlich, man könnte sogar sagen, eine schöne Theorie, denn es ist im Grunde Analysis in neuem Gewand! Es ist die alte und großartige Theorie von Newton und Leibniz in einer einfacheren, eleganten und mächtigeren Form. Maschinelles Lernen ist im Wesentlichen die Anwendung von Analysis, um Funktionen abzuleiten und anzupassen, und Deep Learning ist die Anpassung komplexerer Funktionen.

- Derzeit können große Sprachmodelle nicht nach Dateisprachen wie YAML oder Python filtern. Doch ein erheblicher Teil der Informationen in der realen Welt ist so organisiert. Das bedeutet, dass wir große Sprachmodelle mit Dateien trainieren könnten.

- Für das Training großer Sprachmodelle könnten wir ein System entwickeln, das exakte Übereinstimmungen findet. Vielleicht können wir den KMP (Knuth-Morris-Pratt)-Suchalgorithmus mit der Transformer-Architektur kombinieren, um die Suchfähigkeiten zu verbessern.

- Es gibt keine technologischen Geheimnisse. Open Source wird alle gehüteten Geheimnisse offenlegen.

- KI wird viele Tools beeinflussen, auch indirekte. Die Leute sagen, sie brauchen Figma nicht mehr, um Prototypen zu zeichnen, sie werden direkt zum Code übergehen. Ich denke, Postman wird ähnlich sein; die Leute werden direkt Python oder andere Skripte verwenden, um APIs aufzurufen oder zu testen.

- Ein Grund, warum wir Postman oder Figma im KI-Zeitalter nicht verwenden, ist, dass ihre Funktionalitäten nicht durch Text generiert werden können. Ihnen fehlt auch eine Befehlstaste + K, um Komponentenersetzung auszulösen.

- Benutzeroberflächen werden im KI-Zeitalter zu einer Barriere. Warum Postman für das Testen von Anwendungen KI-fähig machen, wenn wir direkt die requests-Bibliothek von Python oder andere Programmiersprachen verwenden können, um Code zu testen, da letztere von KI unterstützt werden?

- Warum Figma KI-fähig machen, um Benutzeroberflächen zu erstellen, wenn die UI-Generierung durch Code, verstärkt durch KI, einen direkteren und potenziell mächtigeren Ansatz bietet?

- LLMs werden zuerst textbezogene Anwendungen verändern, wie Google, Suchmaschinen, Texteditoren und Schreibtools, Quizlet, Zendesk, DeepL, Medium, WordPress, Trello, Asana, Gmail, GitHub, Goodreads, Duolingo und Feedly.

- Andererseits werden LLMs wahrscheinlich keine Technologien wie Git, Linux, ffmpeg, Handys, Hardware, Browser, Betriebssysteme oder Sprach- und Videoanrufe revolutionieren. Diese Technologien sind codezentriert, und ihr Code wird nicht so einfach von KI generiert, anders als bei API-Testtools wie Postman.

- Technologien mit mehr Code sind schwer von KI zu revolutionieren, wie OpenOffice, MySQL, Mozilla Firefox, Chromium, VLC Media Player, Qt Framework, LLVM/Clang und GNOME. Wenn KI helfen könnte, diese Technologien zu verbessern, würden sie nicht ersetzt werden. KI sollte helfen, bessere Technologien zu schaffen, und dafür wird sie mehr Rechenleistung benötigen, um denselben Umfang an Code zu generieren.

- Es gibt zwei Möglichkeiten, wie LLMs Veränderung bringen können: erstens durch die Veränderung von Inhalten oder Daten innerhalb einer Plattform oder Software, wie z. B. Inhaltsübersetzung in Apps wie TikTok; zweitens durch den direkten Ersatz bestimmter Software oder Plattformen, wie Postman oder Google Search, einschließlich Google Translate.

- Es gibt zwei Möglichkeiten, wie KI-Audio-Tools Veränderung bringen können: erstens durch die Veränderung von Inhalten oder Daten innerhalb einer Plattform oder Software, wie die Erstellung von Hörbüchern für Audible; zweitens durch den direkten Ersatz bestimmter Software oder Plattformen, zum Beispiel Sing-Songs-Apps, da KI nun dieselben Aufgaben wie Menschen erfüllen kann, was es für Menschen einfacher macht, das Singen als Hobby zu betreiben.

- Es gibt mehrere Möglichkeiten zu messen, wie KI aktuelle Software oder Plattformen beeinflusst. Eine Möglichkeit ist zu messen, wie viele Daten oder Inhalte von KI generiert oder verbessert werden können, teilweise oder vollständig. Eine andere Möglichkeit ist zu messen, wie viel Code von KI geschrieben oder verbessert werden kann, teilweise oder vollständig. Das bedeutet, wir nutzen das, was KI generiert, um aktuelle Plattformen zu verbessern. Darüber hinaus kann KI helfen, neue Software und Plattformen zu erfinden.

- Es gibt drei Arten von Produkten: KI-Generierungsprodukte, Produkte, die APIs von KI-Generierungsprodukten nutzen, und andere Produkte.

- Eine Produktidee ist, KI zu nutzen, um Echtzeitinformationen, Nachrichten oder Updates von sozialen Plattformen wie Reddit, GitHub Trending, Twitter Trending, Quora Trending und Zhihu Trending zu sammeln. Benutzer können mit Prompts ihren Feed anpassen oder sogar bestimmte Social-Media-Konten hinzufügen.

- Es gibt fünf wichtige Arten von Daten: Text, Bild, Audio, Video und Code.

- Andere wichtige Datentypen sind numerische, geospatiale, biometrische, Sensordaten, Transaktionsdaten, Metadaten, Zeitreihen, strukturierte, unstrukturierte, teilweise strukturierte, Gesundheits-, Umwelt-, Protokoll-, Netzwerk- und Verhaltensdaten.

- Google ist immer noch besser für die Indexierung von Websites, besonders wenn man Software oder ein Dokument von einer bestimmten Seite herunterladen möchte. Es funktioniert wie eine Domain-Suche. Man nutzt es nicht, um Informationen zu finden, sondern um zu anderen Seiten zu navigieren, um Aufgaben zu erledigen. Ein LLM hat möglicherweise nicht die aktuellsten Download-Links.

- Google funktioniert wie eine Domain-Suche; wenn man auf eine Maven-Repository-Seite gehen möchte, um die neueste Version zu prüfen, kann man es nutzen.

- Google bleibt nützlich für die Bildersuche, während LLMs in der Texterstellung glänzen. Dennoch bevorzugen die Leute oft echte Bilder, um Hardware-Details, Abmessungen, Objektformen oder das Aussehen einer Person zu überprüfen.

- KI-Chatbots sind beliebt, weil Text schwerer zu verarbeiten ist als Bilder. Die Leute bevorzugen echte Bilder gegenüber KI-generierten, da Bilder auf einen Blick verständlich sind. Doch die KI-Bildgenerierung hat ungenutztes Potenzial – Benutzer könnten die KI bitten, verschiedene Perspektiven zu zeigen, Gesichter zu vergrößern oder Details auf Leiterplatten heranzuzoomen. Da die Leute hauptsächlich mit Text arbeiten als mit Bildern, gibt es viel Raum für Wachstum bei KI-Bildtools.

- KI ist gut darin, Konzepte zu erklären und das Verständnis zu erleichtern. Außerdem können Benutzer Fragen zu beliebigen Details stellen. Dies ist wahrscheinlich der größte Nutzen von KI-Tools.

- Ich habe KI genutzt, um etwas über große Sprachmodelle zu lernen. Der Moment, in dem sie mir half, K, Q und V zu verstehen, war wunderbar.

- Der Grund, warum ich seit der Veröffentlichung von LLM lieber Ubuntu verwende, ist, dass die bunten und vielfältigen Apps von macOS mir weniger gefallen. Ich bevorzuge es, meine Programme zu schreiben und alles über das Terminal und Text zu erledigen.

- KI kann danach bewertet werden, wie gut sie eine pom.xml- oder requirements.txt-Datei auf die neueste Version aktualisieren, Bibliotheken aktualisieren und Prüfungen durchführen kann. Dieser Prozess kann viel Arbeit erfordern und manchmal komplex sein.

- Im KI-Zeitalter sind Programmiersprachen, die eine bessere Leistung und Robustheit bieten, wichtiger und werden beliebter sein, während die Syntax weniger wichtig ist. Dies liegt daran, dass LLM hilft, Code zu generieren, was es weniger umständlich macht, solange das Programm gut ausgeführt wird.

- Die Leute neigen dazu, alles von KI-Chatbots zu lesen, weil es einfach zu lernen ist, sie Fragen zu jedem Aspekt stellen können, das Format konsistent ist und die Qualität oft zu den besten im Internet gehört.

- Aber Informationen sind nicht nur Text. Man kann die meisten Textinformationen von KI-Chatbots lesen, verliert jedoch die Originalwebsite und ihr Layout, ihre Erklärungsbilder und Webdesign.

- Websites mit viel Interaktion werden von KI wahrscheinlich nicht stark verändert, wie Webspiele, Google Docs, Google Sheets und Kollaborationstools wie Zoom oder Slack. Sie sind codezentriert und nicht nur auf Text fokussiert.

- Es ist einfach, Tippfehler zu machen oder es erfordert Aufwand, Prompts für KI-Chatbots zu formulieren. Deshalb funktionieren vollständig KI-gesteuerte digitale Banken, Handels-Apps oder soziale Medien mit einem einfachen Chatfenster oft nicht. Traditionelle Klickbuttons, Seitenavigation und Layouts in mobilen Apps sind bequemer.

- [Wie ich gut in der KI- und Blockchain-Ära lebe](./ai-blockchain-en)


---

## Neue Plattformen, die von KI-Workflows angetrieben werden

*08.01.2025*

- Workflows sind Systeme, in denen große Sprachmodelle (LLMs) und Tools über vordefinierte Codepfade orchestriert werden.[^1]

- Stellt euch eine neue Plattform vor, wie TikTok oder Quora, X, Threads, Instagram, WhatsApp, Facebook, LinkedIn, Reddit oder YouTube, vollständig von KI-Übersetzung angetrieben.

- Jeder Beitrag oder jede Antwort, die von Benutzern erstellt wird, kann in einer einzigen Sprache gespeichert werden. Die Plattform übersetzt die Inhalte automatisch in 20 Sprachen, sodass Benutzer sie in ihrer bevorzugten Sprache anzeigen können.

- Neben der Übersetzung werden andere KI-gestützte Funktionen wie Zusammenfassung, Audiogenerierung und Videogenerierung eine Schlüsselrolle spielen. Im Wesentlichen reichen Benutzer den Prompt-Kontext ein, und die Plattform übernimmt den Rest.

- Benutzer können Text, Bilder, Audio oder Videos hochladen, und die Plattform wandelt die Inhalte automatisch in andere Formate um. Benutzer können entscheiden, wie sie die Inhalte erhalten möchten (z. B. als Text, Bilder, Audio oder Video).

- Plattformen können automatisch Zusammenfassungen generieren, wobei verschiedene Arten der Zusammenfassung in mehreren Sprachen verfügbar sind.

- In jedem Text, Bild, Audio oder Video auf der Plattform kann KI helfen, Inhalte zu generieren, zu verfeinern, zu verbessern, zu reparieren, zusammenzufassen, zu erweitern, in andere Formate zu konvertieren oder sich neue Formen des Inhalts vorzustellen.

- Benutzer können die Plattform mit Schlüsselwörtern wie „Englisch“ oder „lustig“ anpassen, um den Stil der KI-Workflows in Plattformen wie TikTok anzupassen. Einmal eingestellt, passt die KI die Inhalte entsprechend an.


---

[^1]: Building Effective Agents, [Anthropic](https://www.anthropic.com/research/building-effective-agents)

---

## Die nächste Richtung von KI-Code-Editoren

*08.01.2025*

Kürzlich arbeitete ich daran, eine `xelatex`-Pipeline zu GitHub Actions hinzuzufügen.

Ich stieß auf ein Problem mit dem `fontawesome5`-Paket im GitHub-Flow. Die von 4o-mini vorgeschlagene Lösung (Installation von TeX Live 2021 und Verwendung von `tlmgr install fontawesome5`) funktionierte bei mir nicht. Allerdings schlug 4o einen besseren Ansatz vor: ein Upgrade auf TeX Live 2023 und dennoch die Verwendung von `tlmgr` zur Installation von `fontawesome5`. Obwohl dies das Problem nicht vollständig löste, verbesserte der Wechsel zu TeX Live 2023 die Situation erheblich.

Ich nutzte ChatGPT, um das Problem zu lösen. Für weitere Details siehe [Was ChatGPT O1 kann, was 4o-mini nicht kann](./o1-en).

An diesem Punkt nutzte ich keine Editoren wie Cursor oder Windsurf, obwohl ich sie in einem anderen Projekt ausprobierte. Das Problem mit diesen Code-Editoren ist, dass sie nur lokale Testausgaben erfassen, was ihre Funktionalität in Cloud-Umgebungen einschränkt.

In Workflows wie GitHub Actions, Jenkins-Jobs oder jedem Code-Deployment- oder Test-Flow müssen Code-Editoren besser integriert werden. Sie sollten eine nahtlose Interaktion mit der Cloud und CI/CD-Prozessen bieten.

Diese Integration gilt auch für andere Inhaltserstellungstools – ob für Text, Bilder, Audio oder Video. Diese Tools sollten mit A/B-Test-Systemen integriert werden. KI-Tools könnten Inhalte generieren, und A/B-Test-Tools könnten Feedback liefern. Diese Dynamik ähnelt dem Reinforcement Learning from Human Feedback (RLHF), bei dem KI-Modelle sich basierend auf Feedback aus der realen Welt mit der Zeit verbessern.

Dieses Konzept, RLHF über reine Modellausgaben hinaus auf reale Test- und Einsatzumgebungen auszuweiten, scheint eine vielversprechende Richtung für die Verbesserung von Code-Editoren und KI-gesteuerten Inhaltserstellungstools zu sein.

Der Test kann sofort oder langfristig sein und automatisiert oder mit menschlicher Unterstützung erfolgen. Wenn die Tests automatisiert sind, wie z. B. A/B-Tests für ein KI-Tool, beinhaltet der Prozess dennoch menschliches Feedback, ist aber automatisiert. Beispielsweise können wir den Computer täglich oder stündlich basierend auf A/B-Test-Ergebnissen prüfen lassen, um den Erstellungsprozess zu verbessern. Ähnlich können wir bei Jenkins- oder GitHub-Actions-Jobs den Computer nach Abschluss der Aufgaben prüfen lassen.

Wenn menschliche Unterstützung involviert ist, kann das Feedback von der Maschine nicht vollständig verstanden werden und ist oft etwas vage. Wenn KI-Tools zum Beispiel Bilder oder Videos erstellen, könnten Menschen anmerken, dass der Inhalt nicht lustig genug ist oder ein bestimmtes Detail verbessert werden sollte. Maschinen haben noch einen langen Weg vor sich, um alles perfekt zu machen, und ob etwas „perfekt“ ist, hängt oft vom individuellen Geschmack ab. Menschliches Feedback hilft, Dinge zu verbessern.

Theoretisch können alle menschengemachten Regeln als Prompts formuliert werden. Es gibt Benutzer-Prompts und System-Prompts. Wir sollten uns darauf konzentrieren, die Prompts zu verbessern, anstatt jedes Mal die Ausgabe zu korrigieren.