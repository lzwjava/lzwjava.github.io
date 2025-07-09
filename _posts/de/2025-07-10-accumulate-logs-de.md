---
audio: false
generated: false
lang: de
layout: post
title: Vorteile der Logsammlung
translated: true
---

Als ich als Vertragsarbeiter für eine singapurische Bank arbeitete, nutzten wir Pivotal Cloud Foundry, um Microservices bereitzustellen. Damals begann ich, Logs zu sammeln, während ich im Unternehmen arbeitete.

Mehrere Jahre sind vergangen, und ich denke immer noch, dass es eine der besten Methoden ist, um mir bei der Arbeit oder bei der Softwareentwicklung zu helfen. Mit der Zeit gibt es in meinem Log-Verzeichnis Hunderte von Log-Dateien.

Ich habe keine spezifischen Unterverzeichnisse oder formale Log-Dateinamen für diese. Manchmal verwende ich einfach den JIRA-Aufgabenamen als Präfix für den Log-Dateinamen oder das Feature. Dann füge ich eine Nummer als Suffix hinzu. Es ist wie mutual-fund-1.log, mutual-fund-2.log usw. Das bedeutet, dass ich in dem Microservice für Investmentfonds diese Logs habe, wenn ich diesen Microservice ausführe.

Manchmal, wenn ich an Projekten arbeite, die mehrere Regionen bedienen, füge ich das Land als Suffix hinzu, wie mutual-fund-cn-1.log, mutual-fund-sg-1.log.

Die Dateinamen der Logs sind irgendwie locker. Denn damals musste ich mich auf Fehlerstapel oder die umgebenden Funktionsaufrufe konzentrieren.

Die Logs der Programme sind wichtig. Das weiß jeder. Aber ich möchte die Bedeutung des Sammelns von Logs betonen, anstatt sie nur in der Konsole zu betrachten und sie dann zu vergessen.

Man merkt erst, wie praktisch es ist, wenn das Projekt läuft. Man hat mehr Zeit, um die vorherigen Logs zu finden. Man muss wissen, ob ähnliche Datenbank-Stored-Procedure-Aufrufe zuvor stattgefunden haben. Man muss wissen, ob der gleiche Fehler zuvor aufgetreten ist. Man muss sich erinnern, wie man das Problem beim letzten Mal behoben hat.

Es gibt unzählige Details in einem großen Projekt oder Dutzenden von Microservices. Und Fehler, Ausnahmen oder Probleme treten immer wieder auf.

Die Logs sind wie das laufende Dokument eines Programms. Und sie werden automatisch vom Programm generiert, ohne dass ein Mensch schreiben muss. Und für Entwickler sind diese Logs lesbar.

Wenn man also eine neue Aufgabe beginnt oder einen neuen Fehler behebt, hat man Hunderte von Logs zur Hand, um diesen neuen Fehler zu beheben. Man ist nicht allein.

Warum sammeln wir sie? Weil Dinge oder Wissen leicht vergessen werden.

Es gab Fortschritte der menschlichen Zivilisation, als das Papier erfunden wurde. Und als die Computer erfunden wurden, gab es eine weitere Stufe der menschlichen Zivilisation. Notizen auf Papier zu machen, ist wie das Sammeln von Logs in Computern.

Nicht nur für Menschen, sondern auch für KI-Chatbots, LLM-Tools werden diese Logs immer wichtiger. Die GreptimeDB, eine Datenbank für die einheitliche Sammlung und Analyse von Observability-Daten (Metriken, Logs und Traces), die 2022 gegründet wurde, ist kein Zufall.

Warum habe ich das vorher nicht gemacht? Nachdem ich als Vertragsarbeiter für große Banken gearbeitet hatte, musste ich mehr zusammenarbeiten und an größeren Projekten arbeiten. Davor arbeitete ich meistens allein, sei es in einem Startup oder in meiner Startup-Phase. Als ich bei LeanCloud arbeitete, arbeitete ich etwa die Hälfte der Zeit an der IM-App LeanChat.

Und als ich in die formellere Unternehmenswelt eintrat, war die Entwicklung der Projekte anders als bei meinen persönlichen Projekten oder Startup-Projekten. Sie hatten SIT-, UAT-Testumgebungen. Und die Produktionsumgebung war oft nur für bestimmte kleine Teammitglieder zugänglich. Das Abrufen der Logs von ihnen und das Beheben von Problemen wurde langwierig und etwas mühsam. Und das Ausführen eines Projekts dauert Zeit, und die Jenkins-Pipeline benötigt oft eine halbe Stunde.

Ich kann also nicht wie eine Fliege das Programm ausführen oder testen. Ich kann nicht einfach durch das Eingeben eines Befehls auf meinem persönlichen Computer und das Hochladen von Code auf den Server eine Bereitstellung durchführen.

Das veranlasst mich, Logs zu sammeln, um mehr Kontext für Aufgaben zu haben. Wir sollten Probleme beim ersten Versuch beheben. Wir sollten unsere Behebung in nur wenigen Versuchen überprüfen. Wir können die Logs des Programms, das in einer Cloud oder auf dem Server des Unternehmens läuft, nicht leicht abrufen, also sollten wir sie kopieren und auf dem lokalen Laptop speichern, um eine Analyse durchzuführen.

Und jetzt sammle ich auch für meine persönlichen Projekte Logs. Es ist zur Gewohnheit geworden. Nach einigen Jahren in großen Unternehmen habe ich irgendwie mehr Geduld oder Strategie, um meine Projekte größer und länger zu machen. Also weiß ich, dass ich diese Logs mit der Zeit brauche.

Manche könnten sagen, dass man nur einen eleganten Code und ein funktionierendes Projekt braucht. Man muss keine Logs oder Fehlerstapel speichern. Das ist okay. Wenn wir einen Fehler oder ein neues Feature haben, können wir das Programm ausführen, um die aktuellen Logs zu erhalten. Wir brauchen keine Logs aus dem Entwicklungsprozess. Sie sind wie detaillierte Aufzeichnungen wissenschaftlicher Experimente. Auf den ersten Blick scheint es in Ordnung zu sein. Aber langfristig, wenn man eines Tages wieder daran arbeiten möchte oder es teilen oder anderen übergeben möchte, könnte es nicht gut sein.

Ich denke, es könnte hier gute Möglichkeiten geben. In Unternehmen, warum ermutigen wir nicht jeden Entwickler, seine gesammelten Logs zu teilen? In Open-Source-Projekten sollten wir das auch tun. Wir finden die Logs anderer nicht ansprechend, weil wir sie nicht kennen. Wir verlieren den Kontext, wenn wir diese Logs speichern. Und dort scheinen unzählige irrelevante oder banale Nachrichten zu sein.

Aber die Mühe, Logs zu sammeln, ist trivial. Es ist nur Kopieren und Einfügen, jedes Mal, wenn wir Logs sehen, besonders Fehler-Logs. Und wie wäre es, wenn wir das automatisiert machen? Es ist eine gute Idee, die Logs jedes Mal in einem Verzeichnis aufzuzeichnen, wenn wir ein Projekt ausführen, wie bei Spring Boot-Projekten.

Die Welt wird immer digitaler, also das Sammeln von Logs digitaler Programme ist wie das Sammeln von Büchern in der physischen Welt.