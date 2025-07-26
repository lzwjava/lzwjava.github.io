---
audio: false
generated: false
image: false
lang: de
layout: post
title: Vorteile des Log-Sammelns
translated: true
---

Als ich früher als Vertragsarbeiter für eine Bank gearbeitet habe, haben wir eine Multi-Cloud-Anwendungsplattform genutzt, um Microservices bereitzustellen. Damals begann ich, Logs zu sammeln, während ich im Unternehmen arbeitete.

Mehrere Jahre sind vergangen, und ich denke immer noch, dass es eine der besten Methoden ist, um mir bei der Arbeit oder der Softwareentwicklung zu helfen. Mit der Zeit habe ich in meinem Log-Verzeichnis Hunderte von Logdateien angesammelt.

Ich habe keine spezifischen Unterverzeichnisse oder formale Logdateinamen für diese. Manchmal verwende ich einfach den JIRA-Aufgabennamen als Präfix für den Logdateinamen oder das Feature. Dann füge ich eine Nummer als Suffix hinzu. Es sieht so aus wie mutual-fund-1.log, mutual-fund-2.log usw. Das bedeutet, dass ich in dem Microservice für Investmentfonds diese Logs habe, wenn ich diesen Microservice ausführe.

Manchmal, wenn ich an Projekten arbeite, die mehrere Regionen bedienen, füge ich das Land als Suffix hinzu, wie mutual-fund-cn-1.log, mutual-fund-sg-1.log. Die Dateinamen der Logs sind irgendwie locker. Denn zu dieser Zeit musste ich mich auf die Fehlerstapel oder die umgebenden Funktionsaufrufe konzentrieren.

Die Logs der Programme sind wichtig. Das weiß jeder. Aber ich möchte die Bedeutung des Sammelns von Logs betonen, anstatt sie einfach in der Konsole zu betrachten und sie dann zu vergessen. Sie werden mehr Komfort haben, wenn das Projekt läuft. Sie haben mehr Zeit, um die vorherigen Logs zu finden. Vielleicht müssen Sie wissen, ob ein ähnlicher Datenbank-Stored-Procedure-Aufruf zuvor stattgefunden hat. Vielleicht müssen Sie wissen, ob der gleiche Fehler zuvor aufgetreten ist. Vielleicht müssen Sie sich erinnern, wie Sie das Problem beim letzten Mal behoben haben.

In einem großen Projekt oder Dutzenden von Microservices gibt es unzählige Details. Und Fehler, Ausnahmen oder Probleme treten immer wieder auf. Die Logs sind wie das laufende Dokument eines Programms. Und sie werden automatisch vom Programm generiert, ohne dass ein Mensch etwas eingibt. Und für Entwickler sind diese Logs lesbar. Wenn Sie also eine neue Aufgabe starten oder einen neuen Fehler beheben, haben Sie Hunderte von Logs zur Hand, um diesen neuen Fehler zu beheben. Sie sind nicht allein.

Warum sammeln wir sie? Weil Dinge oder Wissen leicht vergessen werden.

Es gab einen Fortschritt der menschlichen Zivilisation, als das Papier erfunden wurde. Und als Computer erfunden wurden, gab es eine weitere Stufe der menschlichen Zivilisation. Notizen auf Papier zu machen, ist wie das Sammeln von Logs in Computern.

Nicht nur für Menschen, sondern auch für KI-Chatbots, LLM-Tools werden diese Logs immer wichtiger. Die GreptimeDB, eine Datenbank für die einheitliche Sammlung und Analyse von Observability-Daten (Metriken, Logs und Traces), die 2022 gegründet wurde, ist kein Zufall.

Warum habe ich das vorher nicht gemacht? Nachdem ich als Vertragsarbeiter für große Banken gearbeitet hatte, musste ich mehr zusammenarbeiten und an größeren Projekten arbeiten. Davor arbeitete ich meistens allein, sei es in Startups oder in meiner Startup-Phase. Als ich bei LeanCloud arbeitete, arbeitete ich etwa die Hälfte der Zeit an der IM-App LeanChat.

Und als ich in die formellere Unternehmenswelt eintrat, war die Entwicklung der Projekte anders als bei meinen persönlichen Projekten oder Startup-Projekten. Sie hatten SIT-, UAT-Testumgebungen. Und die Produktionsumgebung war oft nur bestimmten kleinen Teammitgliedern zugänglich. Das Abrufen der Logs von ihnen und das Beheben von Problemen wurde lang und etwas mühsam. Und die Durchführung eines Projekts dauert Zeit, und die Jenkins-Pipeline benötigt oft eine halbe Stunde, um zu laufen.

Daher kann ich das Programm nicht wie eine Fliege ausführen oder testen. Ich kann keine Bereitstellung einfach durch das Eingeben eines Befehls auf meinem persönlichen Computer und das Hochladen von Code auf den Server zum Ausführen durchführen.

Daher sammle ich Logs, um mehr Kontext für Aufgaben zu haben. Wir sollten Probleme beim ersten Versuch beheben. Wir sollten unsere Lösung in nur wenigen Versuchen überprüfen. Wir können die Logs des Programms, das in einer Cloud oder auf dem Server des Unternehmens läuft, nicht leicht abrufen, daher sollten wir sie kopieren und auf dem lokalen Laptop speichern, um eine Analyse durchzuführen.

Und jetzt sammle ich auch für meine persönlichen Projekte Logs. Es ist zur Gewohnheit geworden. Nach einigen Jahren in großen Unternehmen habe ich irgendwie mehr Geduld oder Strategie, um meine Projekte größer und länger zu machen. Daher weiß ich, dass ich diese Logs im Laufe der Zeit brauche.

Manche werden sagen, dass Sie nur einen eleganten Code und ein funktionierendes Projekt benötigen. Sie müssen keine Logs oder Fehlerstapel speichern. Das ist in Ordnung. Wenn wir einen Fehler oder ein neues Feature haben, können wir das Programm ausführen, um die aktuellen Logs zu erhalten. Wir brauchen keine Logs aus dem Entwicklungsprozess. Sie sind wie detaillierte Aufzeichnungen wissenschaftlicher Experimente. Auf den ersten Blick scheint es in Ordnung zu sein. Aber langfristig, wenn Sie eines Tages wieder daran arbeiten möchten oder es teilen oder es an andere übergeben möchten, könnte es nicht gut sein.

Ich denke, es gibt hier gute Möglichkeiten. In Unternehmen, warum ermutigen wir nicht jeden Entwickler, ihre gesammelten Logs zu teilen? In Open-Source-Projekten sollten wir das auch haben. Wir finden die Logs anderer nicht ansprechend, weil wir sie nicht kennen. Wir verlieren den Kontext, wenn wir diese Logs speichern. Und darin scheinen unzählige irrelevante oder banale Nachrichten zu sein.

Aber die Mühe, Logs zu sammeln, ist nur trivial. Es ist einfach nur Kopieren und Einfügen, jedes Mal, wenn wir einige Logs sehen, besonders die Fehler-Logs. Und wie wäre es, wenn wir das auf automatisierte Weise tun? Es ist eine gute Idee, die Logs jedes Mal in einem Verzeichnis aufzuzeichnen, wenn wir ein Projekt ausführen, wie bei Spring Boot-Projekten.

Die Welt wird immer digitaler, daher ist das Sammeln von Logs digitaler Programme wie das Sammeln von Büchern in der physischen Welt.