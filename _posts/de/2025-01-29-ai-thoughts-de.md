---
audio: false
generated: false
image: false
lang: de
layout: post
title: KI-Workflows, Code-Editoren und Plattformdisruption
translated: true
---

### Inhaltsverzeichnis

1. [Gedanken zu KI](#ai-thoughts)  
   - KI fehlt echte Intelligenz oder Tiefe  
   - Maschinelles Lernen ist fortgeschrittene angewandte Analysis  
   - LLMs haben Schwierigkeiten mit strukturierten Dateiformaten  
   - Open Source beseitigt technologische Geheimhaltung  
   - Textbasierte Tools werden zuerst von KI disruptiert  

2. [Neue Plattformen mit KI-gestützten Workflows](#new-platforms-powered-by-ai-workflows)  
   - KI-Workflows automatisieren mehrsprachige Inhaltsgenerierung  
   - Nutzer reichen Prompts für Formatkonvertierung ein  
   - Plattformen ermöglichen Inhaltsverfeinerung und Zusammenfassung  
   - Anpassbare KI-Workflows durch Schlüsselworteinstellungen  
   - KI übernimmt Inhaltsumwandlung von Anfang bis Ende  

3. [Die nächste Richtung von KI-Code-Editoren](#the-next-direction-of-ai-code-editors)  
   - Cloud-Integration entscheidend für CI/CD-Workflows  
   - A/B-Tests verbessern KI-generierte Inhalte  
   - RLHF erweitert auf Feedback aus realen Einsätzen  
   - Menschliches Feedback verfeinert unvollkommene KI-Ergebnisse  
   - Prompt-Optimierung übertrifft Ausgabekorrektur  

## Gedanken zu KI  

*Zuletzt aktualisiert im August 2025*  

- Satya Nadella erwähnte das Jevons-Paradox. Es lohnt sich, darüber zu lernen.  

- Yin Wang: Es gibt keine „Intelligenz“ in künstlicher Intelligenz, kein „Neural“ in neuronalen Netzwerken, kein „Lernen“ im maschinellen Lernen und keine „Tiefe“ im Deep Learning. Was in diesem Bereich wirklich funktioniert, heißt „Analysis“. Daher bevorzuge ich die Bezeichnung „differentzierbare Berechnung“, und der Prozess der Modellentwicklung wird „differentzierbare Programmierung“ genannt.  

- Yin Wang: Maschinelles Lernen ist eine wirklich nützliche, sogar elegante Theorie, weil es im Grunde Analysis in neuem Gewand ist! Es ist die alte und großartige Theorie von Newton und Leibniz in einer einfacheren, eleganteren und leistungsfähigeren Form. Maschinelles Lernen ist im Wesentlichen die Anwendung von Analysis, um Funktionen abzuleiten und anzupassen, und Deep Learning ist die Anpassung komplexerer Funktionen.  

- Derzeit können große Sprachmodelle nicht nach Dateisprachen wie YAML oder Python filtern. Ein bedeutender Teil der Informationen in der realen Welt ist jedoch so organisiert. Das bedeutet, wir könnten große Sprachmodelle mit Dateien trainieren.  

- Für das Training großer Sprachmodelle könnten wir ein System entwickeln, das exakte Übereinstimmungen findet. Vielleicht können wir den KMP (Knuth-Morris-Pratt)-Suchalgorithmus mit der Transformer-Architektur kombinieren, um die Suchfähigkeiten zu verbessern.  

- Es gibt keine technologischen Geheimnisse. Open Source wird alle streng gehüteten Geheimnisse aufdecken.  

- KI wird viele Tools beeinflussen, auch indirekte. Man sagt, man brauche Figma nicht mehr, um Prototypen zu zeichnen, sondern gehe direkt zum Code. Ich denke, Postman wird ähnlich sein; Leute werden direkt Python oder andere Skripte verwenden, um APIs aufzurufen oder zu testen.  

- Ein Grund, warum wir Postman oder Figma im KI-Zeitalter nicht verwenden, ist, dass ihre Funktionen nicht über Text generiert werden können. Außerdem fehlt ihnen eine Befehlstaste + K, um Komponentenersetzung auszulösen.  

- Benutzeroberflächen werden im KI-Zeitalter zu einer Barriere. Warum Postman für KI-gestütztes Testen von Anwendungen aufrüsten, wenn wir direkt Pythons requests-Bibliothek oder andere Programmiersprachen verwenden können, die von KI unterstützt werden?  

- Warum Figma für KI-gestütztes UI-Design aufrüsten, wenn codebasierte UI-Generierung durch KI einen direkteren und potenziell leistungsfähigeren Ansatz bietet?  

- LLMs werden zuerst textbezogene Anwendungen verändern, wie Google, Suchmaschinen, Texteditoren, Schreib-Tools, Quizlet, Zendesk, DeepL, Medium, WordPress, Trello, Asana, Gmail, GitHub, Goodreads, Duolingo und Feedly.  

- Im Gegensatz dazu werden LLMs Technologien wie Git, Linux, ffmpeg, Handys, Hardware, Browser, Betriebssysteme oder Sprach- und Videoanrufe wahrscheinlich nicht revolutionieren. Diese Technologien sind codezentriert, und ihr Code wird nicht so leicht von KI generiert, anders als API-Testtools wie Postman.  

- Technologien mit mehr Code sind schwer durch KI zu revolutionieren, wie OpenOffice, MySQL, Mozilla Firefox, Chromium, VLC Media Player, Qt Framework, LLVM/Clang und GNOME. Wenn KI helfen könnte, diese Technologien zu verbessern, würden sie nicht ersetzt werden. KI sollte helfen, bessere Technologien zu entwickeln, und dafür wird sie mehr Rechenleistung benötigen, um denselben Umfang an Code zu generieren.  

- Es gibt zwei Möglichkeiten, wie LLMs Wandel bringen können: Erstens durch die Veränderung von Inhalten oder Daten innerhalb einer Plattform oder Software, wie z. B. Übersetzungen in Apps wie TikTok; zweitens durch den direkten Ersatz bestimmter Software oder Plattformen, wie Postman oder Google Suche, einschließlich Google Translate.  

- KI-Audio-Tools können auf zwei Arten Wandel bringen: Erstens durch die Veränderung von Inhalten oder Daten innerhalb einer Plattform oder Software, wie z. B. die Generierung von Hörbüchern für Audible; zweitens durch den direkten Ersatz bestimmter Software oder Plattformen, z. B. Sing-Songs-Apps, da KI jetzt dieselben Aufgaben wie Menschen erledigen kann, was es einfacher macht, Singen als Hobby zu betreiben.  

- Es gibt mehrere Möglichkeiten, den Einfluss von KI auf aktuelle Software oder Plattformen zu messen. Eine Möglichkeit ist zu messen, wie viel Daten oder Inhalte von KI ganz oder teilweise generiert oder verbessert werden können. Eine andere Möglichkeit ist zu messen, wie viel Code von KI ganz oder teilweise geschrieben oder verbessert werden kann. Das bedeutet, wir nutzen, was KI generiert, um bestehende Plattformen zu verbessern. Zusätzlich kann KI helfen, neue Software und Plattformen zu erfinden.  

- Es gibt drei Arten von Produkten: Generative-KI-Produkte, Produkte, die APIs generativer KI-Produkte nutzen, und andere Produkte.  

- Eine Produktidee ist, KI zu nutzen, um Echtzeitinformationen, Nachrichten oder Updates von sozialen Plattformen wie Reddit, GitHub Trending, Twitter Trending, Quora Trending und Zhihu Trending zu sammeln. Nutzer können mit Prompts ihren Feed anpassen oder sogar spezifische Social-Media-Accounts hinzufügen.  

- Es gibt fünf wichtige Datentypen: Text, Bild, Audio, Video und Code.  

- Weitere wichtige Datentypen sind numerische, georäumliche, biometrische, Sensor-, Transaktions-, Metadaten, Zeitreihen, strukturierte, unstrukturierte, halbstrukturierte, Gesundheits-, Umwelt-, Log-, Netzwerk- und Verhaltensdaten.  

- Google ist immer noch besser für die Website-Indizierung, besonders wenn man Software oder ein Dokument von einer bestimmten Seite herunterladen möchte. Es funktioniert wie eine Domain-Suche. Man nutzt es nicht, um Informationen zu finden, sondern um zu anderen Seiten zu navigieren, um Aufgaben zu erledigen. Ein LLM hat möglicherweise nicht die neuesten Download-Links.  

- Google funktioniert wie eine Domain-Suche; wenn man zu einer Maven-Repository-Seite gehen möchte, um die neueste Version zu überprüfen, kann man es nutzen.  

- Google bleibt nützlich für die Bildersuche, während LLMs bei der Textgenerierung glänzen. Dennoch bevorzugen Leute oft echte Bilder, um Hardwaredetails, Abmessungen, Objektformen oder das Aussehen einer Person zu überprüfen.  

- KI-Chatbots sind beliebt, weil Text schwerer zu verarbeiten ist als Bilder. Leute bevorzugen echte Bilder gegenüber KI-generierten, da Bilder auf einen Blick verständlich sind. Dennoch hat KI-Bildgenerierung ungenutztes Potenzial – Nutzer könnten die KI bitten, verschiedene Blickwinkel zu zeigen, Gesichter zu vergrößern oder Leiterplattendetails zu vergrößern. Da Menschen hauptsächlich mit Text arbeiten, gibt es viel Raum für Wachstum bei KI-Bildtools.  

- KI ist ausgezeichnet darin, Konzepte zu erklären und Verständnis zu fördern. Darüber hinaus können Nutzer Fragen zu spezifischen Details stellen. Dies ist wahrscheinlich der größte Nutzen von KI-Tools.  

- Ich habe KI genutzt, um über große Sprachmodelle zu lernen. Der Moment, in dem sie mir half, K, Q und V zu verstehen, war wunderbar.  

- Der Grund, warum ich seit der Veröffentlichung von LLM lieber Ubuntu nutze, ist, dass die bunten und vielfältigen Apps von macOS mich weniger ansprechen. Ich bevorzuge es, meine Programme zu schreiben und alles über Terminal und Text zu erledigen.  

- KI kann danach bewertet werden, wie gut sie eine pom.xml- oder requirements.txt-Datei auf die neueste Version aktualisieren, Bibliotheken aktualisieren und Prüfungen durchführen kann. Dieser Prozess kann viel Arbeit erfordern und manchmal komplex sein.  

- Im KI-Zeitalter sind Programmiersprachen mit besserer Leistung und Robustheit wichtiger und werden beliebter sein, während die Syntax weniger wichtig ist, da LLMs helfen, Code zu generieren, solange das Programm gut läuft.  

- Leute neigen dazu, alles von KI-Chatbots zu lesen, weil es leicht zu lernen ist, sie Fragen zu jedem Aspekt stellen können, das Format konsistent ist und die Qualität oft zu den besten im Internet gehört.  

- Aber Informationen sind nicht nur Text. Man kann die meisten Textinformationen von KI-Chatbots lesen, verliert jedoch die ursprüngliche Website, ihr Layout, ihre Erklärbilder und ihr Design.  

- Websites mit viel Interaktion werden wahrscheinlich nicht stark von KI verändert, wie Webspiele, Google Docs, Google Tabellen und Kollaborationstools wie Zoom oder Slack. Sie sind codezentriert und nicht nur auf Text fokussiert.  

- Es ist leicht, Tippfehler zu machen oder erfordert Aufwand, Prompts für KI-Chatbots zu formulieren. Deshalb funktioniert eine vollständig KI-gesteuerte Digitalbank, eine Handels-App oder KI-Social-Media mit einem einfachen Chatfenster oft nicht. Traditionelle Klickbuttons, Seitenavigation und Layouts in mobilen Apps sind bequemer.  

- [Wie ich gut in der KI- und Blockchain-Ära lebe](./ai-blockchain-en)  

---

## Neue Plattformen mit KI-gestützten Workflows  

*08.01.2025*  

- Workflows sind Systeme, in denen große Sprachmodelle (LLMs) und Tools über vordefinierte Codepfade orchestriert werden.[^1]  

- Stellen Sie sich eine neue Plattform vor, wie TikTok, Quora, X, Threads, Instagram, WhatsApp, Facebook, LinkedIn, Reddit oder YouTube, vollständig mit KI-Übersetzung betrieben.  

- Jeder Beitrag oder jede Antwort, die von Nutzern erstellt wird, kann in einer einzigen Sprache gespeichert werden. Die Plattform übersetzt Inhalte automatisch in 20 Sprachen, sodass Nutzer sie in ihrer bevorzugten Sprache ansehen können.  

- Neben der Übersetzung spielen andere KI-gestützte Funktionen wie Zusammenfassung, Audio- und Videogenerierung eine Schlüsselrolle. Im Wesentlichen reichen Nutzer den Prompt-Kontext ein, und die Plattform übernimmt den Rest.  

- Nutzer können Text, Bilder, Audio oder Videos hochladen, und die Plattform wandelt die Inhalte automatisch in andere Formate um. Nutzer können entscheiden, wie sie die Inhalte erhalten möchten (z. B. als Text, Bild, Audio oder Video).  

- Plattformen können automatisch Zusammenfassungen generieren, wobei verschiedene Arten der Zusammenfassung in mehreren Sprachen verfügbar sind.  

- In jedem Text, Bild, Audio oder Video auf der Plattform kann KI helfen, Inhalte zu generieren, zu verfeinern, zu verbessern, zu reparieren, zusammenzufassen, zu erweitern, in andere Formate umzuwandeln oder neue Formen des Inhalts zu imaginieren.  

- Nutzer können die Plattform mit Schlüsselwörtern wie „Englisch“ oder „lustig“ anpassen, um den Stil der KI-Workflows in Plattformen wie TikTok anzupassen. Einmal eingestellt, passt die KI die Inhalte entsprechend an.  

---  

[^1]: Effektive Agenten entwickeln, [Anthropic](https://www.anthropic.com/research/building-effective-agents)  

---

## Die nächste Richtung von KI-Code-Editoren  

*08.01.2025*  

Kürzlich habe ich daran gearbeitet, eine `xelatex`-Pipeline zu GitHub Actions hinzuzufügen.  

Ich stieß auf ein Problem mit dem `fontawesome5`-Paket im GitHub-Flow. Die von 4o-mini vorgeschlagene Lösung (Installation von TeX Live 2021 und Verwendung von `tlmgr install fontawesome5`) funktionierte bei mir nicht. Allerdings schlug 4o einen besseren Ansatz vor: ein Upgrade auf TeX Live 2023 und weiterhin die Verwendung von `tlmgr` zur Installation von `fontawesome5`. Während dies das Problem nicht vollständig löste, verbesserte die Umstellung auf TeX Live 2023 die Situation erheblich.  

Ich habe ChatGPT genutzt, um das Problem zu lösen. Für weitere Details siehe [Was ChatGPT O1 kann, was 4o-mini nicht kann](./o1-en).  

Zu diesem Zeitpunkt nutzte ich keine Editoren wie Cursor oder Windsurf, obwohl ich sie in einem anderen Projekt ausprobiert habe. Das Problem mit diesen Code-Editoren ist, dass sie nur lokale Testausgaben erfassen, was ihre Funktionalität in Cloud-Umgebungen einschränkt.  

In Workflows wie GitHub Actions, Jenkins-Jobs oder jedem Code-Deployment- oder Test-Flow müssen Code-Editoren besser integriert sein. Sie sollten nahtlose Interaktion mit der Cloud und CI/CD-Prozessen ermöglichen.  

Diese Integration gilt auch für andere Inhaltserstellungstools – ob für Text, Bilder, Audio oder Video. Diese Tools sollten mit A/B-Test-Systemen integriert sein. KI-Tools könnten Inhalte generieren, und A/B-Test-Tools könnten Feedback geben. Diese Dynamik ähnelt Reinforcement Learning from Human Feedback (RLHF), bei dem KI-Modelle basierend auf Feedback aus der Praxis kontinuierlich verbessert werden.  

Dieses Konzept, RLHF über reine Modellausgaben hinaus auf reale Test- und Einsatzumgebungen auszudehnen, scheint eine vielversprechende Richtung für die Verbesserung von Code-Editoren und KI-gestützten Inhaltserstellungstools zu sein.  

Tests können sofort oder langfristig sein und automatisiert oder mit menschlicher Unterstützung erfolgen. Wenn die Tests automatisiert sind, wie z. B. A/B-Tests für ein KI-Tool, beinhaltet dies dennoch menschliches Feedback, aber der Prozess ist automatisiert. Beispielsweise kann der Computer jeden Tag oder jede Stunde basierend auf A/B-Test-Ergebnissen überprüfen, um den Erstellungsprozess zu verbessern. Ebenso können für Jenkins- oder GitHub-Actions-Jobs Prüfungen durch den Computer erfolgen, nachdem die Aufgaben abgeschlossen sind.  

Wenn menschliche Unterstützung beteiligt ist, kann das Feedback von der Maschine nicht vollständig verstanden werden und ist oft vage. Wenn KI-Tools beispielsweise Bilder oder Videos erstellen, könnten Menschen anmerken, dass der Inhalt nicht lustig genug ist oder dass ein bestimmtes Detail verbessert werden sollte. Maschinen haben noch einen langen Weg vor sich, um alles perfekt zu machen, und was „perfekt“ ist, ist oft subjektiv und hängt vom individuellen Geschmack ab. Menschliches Feedback hilft, Dinge zu verbessern.  

Theoretisch können alle von Menschen definierten Regeln als Prompts geschrieben werden. Es gibt Nutzer-Prompts und System-Prompts. Wir sollten uns darauf konzentrieren, die Prompts zu verbessern, anstatt jedes Mal die Ausgabe zu korrigieren.