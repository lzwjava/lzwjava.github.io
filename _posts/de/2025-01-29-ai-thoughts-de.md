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

1. [KI-Gedanken](#ki-gedanken)  
   - KI fehlt echte Intelligenz oder Tiefe  
   - Maschinelles Lernen ist fortgeschrittene angewandte Analysis  
   - LLMs haben Schwierigkeiten mit strukturierten Dateiformaten  
   Open Source beseitigt technologische Geheimhaltung  
   Textbasierte Tools werden zuerst von KI disruptiert  

2. [Neue Plattformen mit KI-Workflows](#neue-plattformen-mit-ki-workflows)  
   - KI-Workflows automatisieren mehrsprachige Inhaltserstellung  
   - Nutzer geben Prompts für Formatkonvertierung ein  
   - Plattformen ermöglichen Inhaltsverfeinerung und Zusammenfassung  
   - Anpassbare KI-Workflows durch Schlüsselworteinstellungen  
   - KI übernimmt Inhaltsumwandlung end-to-end  

3. [Die nächste Richtung von KI-Code-Editoren](#die-nächste-richtung-von-ki-code-editoren)  
   - Cloud-Integration entscheidend für CI/CD-Workflows  
   - A/B-Tests verbessern KI-generierte Inhalte  
   - RLHF erweitert auf Feedback aus realen Einsätzen  
   - Menschliches Feedback verfeinert unvollkommene KI-Outputs  
   - Prompt-Optimierung übertrifft Output-Korrektur  

## KI-Gedanken  

*Zuletzt aktualisiert im August 2025*  

- Satya Nadella erwähnte das Jevons-Paradox. Es lohnt sich, darüber zu lernen.  

- Yin Wang: Es gibt keine „Intelligenz“ in künstlicher Intelligenz, kein „Neural“ in neuronalen Netzen, kein „Lernen“ im maschinellen Lernen und keine „Tiefe“ im Deep Learning. Was in diesem Bereich wirklich funktioniert, heißt „Analysis“. Daher bevorzuge ich die Bezeichnung „differenzierbare Berechnung“, und der Prozess der Modellerstellung wird „differenzierbare Programmierung“ genannt.  

- Yin Wang: Maschinelles Lernen ist wirklich nützlich, man könnte sogar sagen, eine schöne Theorie, denn es ist im Grunde Analysis nach einem Makeover! Es ist die alte und großartige Theorie von Newton und Leibniz in einer einfacheren, eleganten und mächtigeren Form. Maschinelles Lernen ist im Wesentlichen die Anwendung von Analysis, um Funktionen abzuleiten und anzupassen, und Deep Learning ist die Anpassung komplexerer Funktionen.  

- Derzeit können große Sprachmodelle nicht nach Dateisprachen wie YAML oder Python filtern. Ein erheblicher Teil der Informationen in der realen Welt ist jedoch so organisiert. Das bedeutet, wir könnten große Sprachmodelle mit Dateien trainieren.  

- Für das Training großer Sprachmodelle könnten wir ein System entwickeln, das exakte Übereinstimmungen findet. Vielleicht können wir den KMP (Knuth-Morris-Pratt)-Suchalgorithmus mit der Transformer-Architektur kombinieren, um die Suchfähigkeiten zu verbessern.  

- Es gibt keine technologischen Geheimnisse. Open Source wird alle gut gehüteten Geheimnisse enthüllen.  

- KI wird viele Tools beeinflussen, auch indirekt. Man sagt, man braucht Figma nicht mehr, um Prototypen zu zeichnen, man geht direkt zum Code. Ich denke, Postman wird ähnlich sein; Leute werden direkt Python oder andere Skripte verwenden, um APIs aufzurufen oder zu testen.  

- Ein Grund, warum wir Postman oder Figma in der KI-Ära nicht verwenden, ist, dass ihre Funktionen nicht durch Text generiert werden können. Ihnen fehlt auch eine Befehlstaste + K, um Komponentenersetzung auszulösen.  

- Benutzeroberflächen werden in der KI-Ära zu einer Barriere. Warum Postman für KI-gestütztes Testen von Anwendungen upgraden, wenn wir direkt die requests-Bibliothek von Python oder andere Programmiersprachen verwenden können, um Code zu testen, da Letztere von KI unterstützt werden?  

- Warum Figma für KI-gestützte UI-Erstellung upgraden, wenn codebasierte UI-Generierung, verstärkt durch KI, einen direkteren und potenziell mächtigeren Ansatz bietet?  

- LLMs werden zuerst textbezogene Anwendungen verändern, wie Google, Suchmaschinen, Texteditoren und Schreibtools, Quizlet, Zendesk, DeepL, Medium, WordPress, Trello, Asana, Gmail, GitHub, Goodreads, Duolingo und Feedly.  

- Andererseits werden LLMs Technologien wie Git, Linux, ffmpeg, Handys, Hardware, Browser, Betriebssysteme oder Sprach- und Videoanrufe wahrscheinlich nicht revolutionieren. Diese Technologien sind codezentriert, und ihr Code wird nicht so leicht von KI generiert, im Gegensatz zu API-Testtools wie Postman.  

- Technologien mit mehr Code sind schwer durch KI zu revolutionieren, wie OpenOffice, MySQL, Mozilla Firefox, Chromium, VLC Media Player, Qt Framework, LLVM/Clang und GNOME. Wenn KI helfen könnte, diese Technologien zu verbessern, würden sie nicht ersetzt werden. KI sollte helfen, bessere Technologien zu schaffen, und dafür wird sie mehr Rechenleistung benötigen, um die gleiche Menge an Code zu generieren.  

- Es gibt zwei Wege, wie LLMs Veränderung bringen können: erstens durch die Veränderung von Inhalten oder Daten innerhalb einer Plattform oder Software, wie Content-Übersetzung in Apps wie TikTok; zweitens durch den direkten Ersatz bestimmter Software oder Plattformen, wie Postman oder Google Search, einschließlich Google Translate.  

- Es gibt zwei Wege, wie KI-Audio-Tools Veränderung bringen können: erstens durch die Veränderung von Inhalten oder Daten innerhalb einer Plattform oder Software, wie die Erzeugung von Hörbüchern für Audible; zweitens durch den direkten Ersatz bestimmter Software oder Plattformen, zum Beispiel die Sing-Songs-App, da KI jetzt die gleichen Aufgaben wie Menschen erledigen kann, was es einfacher macht, das Singen als Hobby zu betreiben.  

- Es gibt mehrere Möglichkeiten, den Einfluss von KI auf aktuelle Software oder Plattformen zu messen. Eine Möglichkeit ist, zu messen, wie viele Daten oder Inhalte von KI erzeugt oder verbessert werden können, teilweise oder vollständig. Eine andere Möglichkeit ist, zu messen, wie viel Code von KI geschrieben oder verbessert werden kann, teilweise oder vollständig. Das bedeutet, wir nutzen das, was KI erzeugt, um aktuelle Plattformen zu verbessern. Zusätzlich kann KI helfen, neue Software und Plattformen zu erfinden.  

- Es gibt drei Arten von Produkten: Generative-KI-Produkte, Produkte, die APIs von generativen KI-Produkten nutzen, und andere Produkte.  

- Eine Produktidee ist, KI zu nutzen, um Echtzeitinformationen, Nachrichten oder Updates von sozialen Plattformen wie Reddit, GitHub Trending, Twitter Trending, Quora Trending und Zhihu Trending zu sammeln. Nutzer können Prompts verwenden, um den Feed anzupassen oder sogar spezifische Social-Media-Accounts hinzuzufügen.  

- Es gibt fünf wichtige Arten von Daten: Text, Bild, Audio, Video und Code.  

- Andere wichtige Datentypen sind numerische, georäumliche, biometrische, Sensoren-, Transaktions-, Metadaten, Zeitreihen, strukturierte, unstrukturierte, halbstrukturierte, Gesundheits-, Umwelt-, Log-, Netzwerk- und Verhaltensdaten.  

- Google ist immer noch besser für die Website-Indizierung, besonders wenn man Software oder ein Dokument von einer bestimmten Site herunterladen möchte. Es funktioniert wie eine Domain-Suche. Man nutzt es nicht, um Informationen zu finden, sondern um zu anderen Sites zu navigieren, um Aufgaben zu erledigen. Ein LLM hat möglicherweise nicht die neuesten Download-Links.  

- Google funktioniert wie eine Domain-Suche; wenn man zu einer Maven-Repository-Site gehen möchte, um die neueste Version zu prüfen, kann man es nutzen.  

- Google bleibt nützlich für die Bildersuche, während LLMs in der Texterzeugung glänzen. Dennoch bevorzugen Menschen oft echte Bilder, um Hardwaredetails, Abmessungen, Objektformen oder das Aussehen einer Person zu überprüfen.  

- KI-Chatbots sind beliebt, weil Text schwerer zu verarbeiten ist als Bilder. Menschen bevorzugen echte Bilder gegenüber KI-generierten, da Bilder auf einen Blick leichter zu verstehen sind. Allerdings hat die KI-Bildgenerierung ungenutztes Potenzial – Nutzer könnten die KI bitten, verschiedene Winkel zu zeigen, Gesichter zu zoomen oder Leiterplattendetails zu vergrößern. Da Menschen hauptsächlich mit Text arbeiten, gibt es großes Wachstumspotenzial für KI-Bildtools.  

- KI ist hervorragend darin, Konzepte zu erklären und Verständnis zu fördern. Außerdem können Nutzer Fragen zu bestimmten Details stellen. Dies ist wahrscheinlich der größte Nutzen von KI-Tools.  

- Ich habe KI genutzt, um über große Sprachmodelle zu lernen. Der Moment, in dem sie mir half, K, Q und V zu verstehen, war wunderbar.  

- Der Grund, warum ich seit der Veröffentlichung von LLM lieber Ubuntu verwende, ist, dass die bunten und vielfältigen Apps in macOS mich weniger ansprechen. Ich bevorzuge es, meine Programme zu schreiben und alles über Terminal und Text zu erledigen.  

- KI kann danach bewertet werden, wie gut sie eine pom.xml oder requirements.txt-Datei auf die neueste Version aktualisieren, Bibliotheken updaten und Prüfungen durchführen kann. Dieser Prozess kann erhebliche Arbeit umfassen und manchmal komplex sein.  

- In der KI-Ära sind Programmiersprachen mit besserer Leistung und Robustheit wichtiger und werden beliebter sein, während die Syntax weniger wichtig ist. Denn LLM hilft beim Code-Generieren, was weniger Aufwand bedeutet, solange das Programm gut ausgeführt wird.  

- Menschen neigen dazu, alles von KI-Chatbots zu lesen, weil es leicht zu lernen ist, sie Fragen zu jedem Aspekt stellen können, das Format konsistent ist und die Qualität oft zu den besten im Internet gehört.  

- Aber Informationen sind nicht nur Text, man kann die meisten Textinformationen von KI-Chatbots lesen, verliert jedoch die ursprüngliche Website, ihr Layout und Design, ihre Erklärungsbilder und das Website-Design.  

- Websites mit viel Interaktion werden wahrscheinlich nicht stark von KI verändert, wie Webspiele, Google Docs, Google Sheets und Kollaborationstools wie Zoom oder Slack. Sie sind codezentriert und nicht nur auf Text fokussiert.  

- Es ist leicht, Tippfehler zu machen oder erfordert Aufwand, Prompts für KI-Chatbots zu formulieren. Deshalb funktioniert eine vollständig KI-gesteuerte digitale Bank, eine digitale Trading-App oder KI-Social-Media mit einem einfachen Chatfenster oft nicht. Traditionelle Klickbuttons, Seitenavigation und Layouts in mobilen Apps sind bequemer.  

- [Wie ich gut in der KI- und Blockchain-Ära lebe](./ai-blockchain-de)  

---  

## Neue Plattformen mit KI-Workflows  

*2025.01.08*  

- Workflows sind Systeme, in denen große Sprachmodelle (LLMs) und Tools durch vordefinierte Codepfade orchestriert werden.[^1]  

- Stell dir eine neue Plattform vor, wie TikTok oder Quora, X, Threads, Instagram, WhatsApp, Facebook, LinkedIn, Reddit oder YouTube, vollständig mit KI-Übersetzung betrieben.  

- Jeder Post oder jede Antwort, die von Nutzern erstellt wird, kann in einer einzigen Sprache gespeichert werden. Die Plattform übersetzt den Inhalt automatisch in 20 Sprachen, sodass Nutzer ihn in ihrer bevorzugten Sprache sehen können.  

- Neben Übersetzung werden andere KI-gestützte Funktionen wie Zusammenfassung, Audio- und Videogenerierung eine zentrale Rolle spielen. Im Wesentlichen reicht der Nutzer den Prompt-Kontext ein, und die Plattform erledigt den Rest.  

- Nutzer können Texte, Bilder, Audio oder Videos hochladen, und die Plattform wandelt den Inhalt automatisch in andere Formate um. Nutzer können entscheiden, wie sie den Inhalt erhalten möchten (z. B. als Text, Bild, Audio oder Video).  

- Plattformen können automatisch Zusammenfassungen generieren, wobei verschiedene Arten der Zusammenfassung in mehreren Sprachen verfügbar sind.  

- In jedem Text, Bild, Audio oder Video auf der Plattform kann KI helfen, Inhalte zu generieren, zu verfeinern, zu verbessern, zu beheben, zusammenzufassen, zu erweitern, in andere Formate zu konvertieren oder sich neue Formen des Inhalts vorzustellen.  

- Nutzer können die Plattform mit Schlüsselwörtern wie „Englisch“ oder „lustig“ anpassen, um den Stil der KI-Workflows in Plattformen wie TikTok anzupassen. Einmal eingestellt, passt die KI die Inhalte entsprechend an.  

---  

[^1]: Building Effective Agents, [Anthropic](https://www.anthropic.com/research/building-effective-agents)  

---  

## Die nächste Richtung von KI-Code-Editoren  

*2025.01.08*  

Kürzlich arbeitete ich daran, eine `xelatex`-Pipeline zu GitHub Actions hinzuzufügen.  

Ich stieß auf ein Problem mit dem `fontawesome5`-Paket im GitHub-Workflow. Die von 4o-mini angebotene Lösung (Installation von TeX Live 2021 und Verwendung von `tlmgr install fontawesome5`) funktionierte bei mir nicht. Allerdings schlug 4o einen besseren Ansatz vor: ein Upgrade auf TeX Live 2023 und weiterhin die Verwendung von `tlmgr` zur Installation von `fontawesome5`. Obwohl dies das Problem nicht vollständig löste, verbesserte die Umstellung auf TeX Live 2023 die Situation erheblich.  

Ich nutzte ChatGPT, um das Problem zu lösen. Für weitere Details siehe [Was ChatGPT O1 kann, was 4o-mini nicht kann](./o1-de).  

Zu diesem Zeitpunkt nutzte ich keine Editoren wie Cursor oder Windsurf, obwohl ich sie in einem anderen Projekt ausprobierte. Das Problem mit diesen Code-Editoren ist, dass sie nur lokale Testausgaben erfassen, was ihre Funktionalität in Cloud-Umgebungen einschränkt.  

In Workflows wie GitHub Actions, Jenkins-Jobs oder jedem Code-Deployment- oder Test-Workflow müssen Code-Editoren besser integriert sein. Sie sollten nahtlose Interaktion mit der Cloud und CI/CD-Prozessen bieten.  

Diese Integration gilt auch für andere Inhaltserstellungstools – sei es für Text, Bilder, Audio oder Video. Diese Tools sollten in A/B-Testsysteme integriert sein. KI-Tools könnten Inhalte generieren, und A/B-Test-Tools kön Feedback geben. Diese Dynamik ähnelt dem Reinforcement Learning from Human Feedback (RLHF), bei dem KI-Modelle sich basierend auf Feedback aus der realen Welt verbessern.  

Dieses Konzept, RLHF über Modelloutputs hinaus auf reale Test- und Einsatzumgebungen auszuweiten, scheint eine vielversprechende Richtung für die Verbesserung von Code-Editoren und KI-gestützten Inhaltserstellungstools zu sein.  

Der Test kann sofort oder langfristig sein und automatisiert oder mit menschlicher Unterstützung erfolgen. Wenn die Tests automatisiert sind, wie z. B. A/B-Tests für ein KI-Tool, beinhaltet der Prozess immer noch menschliches Feedback, aber er ist automatisiert. Zum Beispiel können wir den Computer täglich oder stündlich basierend auf A/B-Test-Ergebnissen prüfen lassen, um den Erstellungsprozess zu verbessern. Ebenso können wir für Jenkins- oder GitHub-Actions-Jobs den Computer nach Abschluss ihrer Aufgaben prüfen lassen.  

Wenn menschliche Unterstützung involviert ist, kann das Feedback nicht vollständig von der Maschine verstanden werden und ist oft etwas vage. Zum Beispiel, wenn KI-Tools Inhalte wie Bilder oder Videos erstellen, könnten Menschen anmerken, dass der Inhalt nicht lustig genug ist oder ein bestimmtes Detail verbessert werden sollte. Maschinen haben noch einen langen Weg vor sich, um alles perfekt zu machen, und „perfekt“ ist oft subjektiv und hängt vom individuellen Geschmack ab. Menschliches Feedback hilft, Dinge besser zu machen.  

Theoretisch können alle von Menschen definierten Regeln als Prompts geschrieben werden. Es gibt Nutzer-Prompts und System-Prompts. Wir sollten uns darauf konzentrieren, die Prompts zu verbessern, anstatt die Ausgabe jedes Mal zu korrigieren.