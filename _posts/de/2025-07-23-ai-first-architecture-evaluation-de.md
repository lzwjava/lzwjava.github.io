---
audio: false
generated: true
lang: de
layout: post
title: KI-basierte Architektur für moderne Entwicklung
translated: true
---

Dieser Beitrag wurde mit Hilfe von Grok verfasst, aber die Ideen sind original.

---

### Bewertung Ihrer Punkte

Ich werde Ihre Punkte einzeln analysieren, sie gegen aktuelle Trends im Software Engineering, die Integration von AI/LLM (z. B. Tools wie GitHub Copilot, Cursor oder benutzerdefinierte LLM-Agenten) und praktische Implikationen bewerten. Sie greifen eine kritische Erkenntnis auf: Da AI zunehmend in Entwicklungsworkflows integriert wird, müssen Architekturen neben menschzentrierten Designs auch AI-Freundlichkeit priorisieren. Allerdings sind nicht alle Ideen universell anwendbar – der Kontext ist entscheidend, und ein Ausgleich zwischen Einfachheit und Skalierbarkeit ist essenziell. Ich werde Übereinstimmungen, Widersprüche und wichtige Nuancen darlegen.

#### 1. Traditionelle Bankarchitekturen haben Vorzüge, aber für neue Projekte sollte AI/LLM-Optimierung priorisiert werden: Fokus auf Context Engineering, klare Trennung und AI-first-Design
Theoretisch haben Sie Recht. Traditionelle Architekturen, wie sie in der Bankenbranche (angenommen wird hier eine Referenz auf monolithische oder geschichtete Unternehmenssysteme) verbreitet sind, überzeugen durch Zuverlässigkeit, Sicherheit und menschliche Wartbarkeit. Doch mit AI/LLM-Agenten, die Codegenerierung, Debugging und Refactoring vorantreiben, gewinnt ein „AI-first“-Mindset zunehmend an Relevanz. Dazu gehört das Design unter Berücksichtigung von LLM-Einschränkungen wie begrenzten Kontextfenstern (z. B. 128k Tokens in GPT-4o), indem Code modularisiert wird, um kritische Details innerhalb dieser Grenzen zu halten.

- **Stärken**: Klare Trennung von Verantwortlichkeiten (z. B. getrennte Datenflüsse, Prompts oder API-Grenzen) ermöglicht es der KI, effektiver zu arbeiten. Beispielsweise profitieren KI-Tools wie LangChain oder benutzerdefinierte Agenten von klar definierten, isolierten Kontexten statt verschachtelter Logik.
- **Nuancen**: Menschzentriertes Design bleibt entscheidend – KI benötigt weiterhin menschliche Überwachung in komplexen Domänen wie der Finanzwelt, wo regulatorische Compliance und Sicherheit von zentraler Bedeutung sind. Ein hybrides Modell könnte optimal sein: KI-optimiert für repetitive Aufgaben, menschlich optimiert für kritische Logik.
- **Gesamtbewertung**: Große Übereinstimmung; dieser Trend zeigt sich in AI-getriebenen Mikroservices und serverlosen Architekturen.

#### 2. Spring bietet robuste Abstraktionen, stellt aber Herausforderungen für die AI/LLM-Verständlichkeit dar
Hier haben Sie Recht. Spring (und ähnliche Java-Frameworks wie Micronaut) ist ideal für Unternehmensumgebungen mit Funktionen wie Dependency Injection, AOP und geschichteten Abstraktionen (z. B. Controller -> Services -> Repositories). Während es für menschlich verwaltete große Teams hervorragend geeignet ist, können diese Abstraktionen LLMs aufgrund von Indirektion und Boilerplate-Code überfordern.

- **Stärken**: LLMs haben oft Schwierigkeiten mit tiefen Aufrufstapeln oder impliziten Verhaltensweisen (z. B. @Autowired-Annotationen), was zu Halluzinationen oder unvollständigen Analysen führt. Forschungen zur KI-Codegenerierung zeigen höhere Fehlerraten in übermäßig abstrahierten Codebasen.
- **Nuancen**: Nicht alle Abstraktionen sind schädlich – Schnittstellen verbessern beispielsweise die Testbarkeit und unterstützen die KI indirekt bei Aufgaben wie Mock-Generierung. Übermäßige Verschachtelung erhöht jedoch den Kontext und erschwert die Logikverfolgung für LLMs.
- **Gesamtbewertung**: Starke Übereinstimmung; es gibt eine Verschiebung hin zu leichteren Frameworks (z. B. Quarkus) oder minimalen Framework-Ansätzen, um die KI-Kompatibilität zu verbessern.

#### 3. Flachere Strukturen bevorzugen, ähnlich wie flache Organisationen: Auf maximal 2 Ebenen beschränken, wobei die erste Ebene die zweite aufruft und tiefe Stapel mit 50 Ebenen vermieden werden
Dies ist eine überzeugende Idee für Einfachheit, wenn auch nicht universell ideal. Flachere Strukturen (z. B. ein Top-Level-Orchestrator, der mehrere kleine Funktionen aufruft) reduzieren die Verschachtelung und helfen LLMs, Fehler bei der Verarbeitung komplexer Aufrufstapel zu vermeiden. Dies ähnelt der einfachen Funktionsverkettung, die oft in Python-Skripten zu sehen ist.

- **Stärken**: Flachere Codes reduzieren die kognitive Belastung für die KI – LLMs arbeiten besser mit linearer oder paralleler Logik als mit tiefer Rekursion. Die Analogie zur „flachen Organisation“ trifft zu: Wie Startups ist flacher Code anpassungsfähiger für KI-Modifikationen.
- **Nuancen**: Der Aufruf zahlreicher Funktionen von einem einzigen Punkt aus kann zu „Spaghetti-Code“ führen, wenn keine disziplinierte Organisation (z. B. klare Benennung oder Modularisierung) besteht. In größeren Systemen verhindert eine minimale Hierarchie (3-4 Ebenen) das Chaos. Während KI-Agenten wie Devin flache Strukturen gut handhaben, können ohne ordnungsgemäße Orchestrierung Leistungsprobleme auftreten.
- **Gesamtbewertung**: Teilweise Übereinstimmung; Flachheit ist dort vorteilhaft, wo es möglich ist, aber die Skalierbarkeit muss getestet werden. Dies entspricht den Trends des funktionalen Programmierens in der KI-getriebenen Entwicklung.

#### 4. AI/LLMs haben Schwierigkeiten mit komplexen verschachtelten Strukturen, sind aber bei kleinen Funktionen (100-200 Zeilen) gut: Das Aufruf- und Import-System von Python unterstützt dies
Sie haben vollkommen Recht in Bezug auf die Fähigkeiten von LLMs. Aktuelle Modelle (z. B. Claude 3.5, GPT-4) sind bei fokussierten, begrenzten Aufgaben gut, scheitern aber an Komplexität – die Fehlerrate steigt ab etwa 500 Zeilen Kontext aufgrund von Tokenbegrenzungen und Aufmerksamkeitsspanne.

- **Stärken**: Kleine Funktionen (100-200 Zeilen) sind optimal für die KI: einfach zu prompten, zu generieren oder zu refaktorieren. Das Import-System von Python (z. B. `from module import func`) fördert die Modularität und macht es KI-freundlicher als die klassenorientierte Struktur von Java.
- **Nuancen**: Während LLMs Fortschritte machen (z. B. mit Chain-of-Thought-Prompting), bleibt verschachtelte Logik eine Herausforderung. Die Flexibilität von Python hilft, aber statische Typisierung (z. B. TypeScript) kann der KI ebenfalls helfen, indem sie explizite Hinweise liefert.
- **Gesamtbewertung**: Starke Übereinstimmung; dies erklärt, warum ML/AI-Ökosysteme (z. B. Hugging Face-Bibliotheken) oft den modularen Stil von Python übernehmen.

#### 5. Große Java-Dateien sollten in kleinere Dateien mit mehr Funktionen aufgeteilt werden, um das Testen/Verifizieren zu erleichtern; Java-Projekte sollten die Struktur von Python nachahmen
Dies ist eine praktische Richtung. Große, monolithische Java-Klassen (z. B. 1000+ Zeilen) sind sowohl für Menschen als auch für KI schwierig, während das Aufteilen in kleinere Dateien/Funktionen die Granularität verbessert.

- **Stärken**: Kleinere Einheiten vereinfachen das Unit-Testing (z. B. mit JUnit) und die Verifizierung (die KI kann sich auf eine Funktion konzentrieren), was dem Ansatz „ein Modul pro Funktion“ von Python ähnelt. Build-Tools wie Maven/Gradle unterstützen dies nahtlos.
- **Nuancen**: Das Paketsystem von Java unterstützt dies bereits, aber ein kultureller Wandel von OOP-Monolithen ist notwendig. Nicht alle Java-Projekte sollten Python nachahmen – leistungskritische Anwendungen könnten von einer gewissen Konsolidierung profitieren.
- **Gesamtbewertung**: Übereinstimmung; modernes Java (z. B. mit Records und versiegelten Klassen in Java 21+) bewegt sich in diese Richtung.

#### 6. Prozedurale Programmierung könnte in der Ära von AI/LLM die objektorientierte Programmierung übertreffen
Dies ist eine mutige, aber kontextuell gültige Perspektive. Prozedurale (oder funktionale) Ansätze, die sich auf einfache Abläufe und reine Funktionen konzentrieren, entsprechen den Stärken von LLMs – die Generierung linearer Codes ist einfacher als das Handhaben von OOP-State, Vererbung und Polymorphismus.

- **Stärken**: OOP-Abstraktionen wie tiefe Vererbung verwirren LLMs oft, was zu Fehlern im generierten Code führt. Prozeduraler Code ist vorhersehbarer und entspricht der Mustererkennungsnatur der KI. Sprachen wie Rust (mit prozeduralen Traits) und Go (mit Fokus auf Einfachheit) spiegeln diesen Trend wider.
- **Nuancen**: OOP ist nicht obsolet – es ist effektiv für die Modellierung komplexer Domänen (z. B. Finanzobjekte). Ein hybrider Ansatz (prozeduraler Kern mit OOP-Ummantelungen) könnte ideal sein. Mit angepassten Prompts können LLMs OOP bewältigen, wenn auch prozeduraler Code die Reibung verringert.
- **Gesamtbewertung**: Teilweise Übereinstimmung; prozedurale/funktionale Stile gewinnen in AI-Workflows an Bedeutung, aber OOP behält seinen Wert für die langfristige Wartbarkeit großer Systeme.

#### 7. IDEs wie VSCode oder IntelliJ IDEA sollten Shortcuts für KI-gestützte Funktion/Methoden-Bearbeitung anbieten
Sie haben Recht, dass dies die Workflows beschleunigen würde. Während aktuelle IDEs teilweise Unterstützung bieten (z. B. „Go to Definition“ in VSCode oder Inline-Vorschläge von Copilot), werden dedizierte KI-Bearbeitungs-Shortcuts immer häufiger.

- **Stärken**: Das Auswählen einer Funktion/ Methode und das Prompten der KI (z. B. „refaktoriere dies“) würde die Effizienz steigern. Tools wie Cursor (basierend auf VSCode) ermöglichen bereits bereichsspezifische KI-Änderungen.
- **Nuancen**: IntelliJ IDEA bietet „Extract Method“ und KI-Assistenten (über JetBrains AI), während VSCode-Erweiterungen wie GitHub Copilot Chat auswahlbasierte Abfragen unterstützen. Dennoch wäre ein nativ integrierter „KI-bearbeite diese Funktion“-Shortcut eine wertvolle Ergänzung – wahrscheinlich in zukünftigen Updates.
- **Gesamtbewertung**: Übereinstimmung; dies entspricht dem wachsenden Trend zu KI-optimierter Tooling.

### Zusammenfassung
Ihre Erkenntnisse sind größtenteils korrekt: Die Übernahme von AI-optimierten Architekturen (flach, modular, kleine Einheiten) adressiert echte LLM-Einschränkungen und kann die Entwicklung beschleunigen. Allerdings können Extreme wie vollständig prozedurale oder übermäßig flache Designs die langfristige Wartbarkeit beeinträchtigen – ein Ausgleich ist entscheidend. In Bereichen wie der Finanzwelt können Sicherheit und Compliance bestimmte Abstraktionen erfordern. Ihre Perspektive entspricht den aufkommenden Best Practices im KI-gestützten Coding, bei denen Einfachheit sowohl Menschen als auch Maschinen zugutekommt.

Falls Sie spezifische Code-Beispiele haben oder eine AI-first-Neugestaltung erkunden möchten, fragen Sie gerne nach!