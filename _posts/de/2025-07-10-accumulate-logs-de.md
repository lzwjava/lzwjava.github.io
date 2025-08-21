---
audio: false
generated: false
image: false
lang: de
layout: post
title: Vorteile des Protokollisierens
translated: true
---

## Vorteile des Ansammelns von Logs

Als ich früher als Auftragnehmer für eine Bank arbeitete, verwendeten wir eine Multi-Cloud-Anwendungsplattform, um die Microservices bereitzustellen. Damals begann ich, Logs anzusammeln, während ich im Unternehmen arbeitete.

Mehrere Jahre sind vergangen, und ich denke immer noch, dass dies eine der besten Möglichkeiten ist, mir bei der Arbeit oder beim Software Engineering zu helfen. Im Laufe der Zeit befinden sich Hunderte von Log-Dateien in meinem Log-Verzeichnis.

Ich habe keine spezifischen Unterverzeichnisse oder formelle Log-Dateinamen dafür. Manchmal verwende ich einfach den JIRA-Aufgabenamen oder das Feature als Präfix für meinen Log-Dateinamen. Und dann füge ich eine Zahl an den Suffix an. Es ist wie mutual-fund-1.log, mutual-fund-2.log usw. Das bedeutet, dass ich im Mutual Fund Microservice dieses Log habe, wenn ich diesen Microservice ausführe.

Manchmal, wenn ich an Projekten arbeite, die mehrere Regionen bedienen, füge ich das Land als Suffix hinzu, wie mutual-fund-cn-1.log, mutual-fund-sg-1.log. Die Dateinamen der Logs sind irgendwie zwanglos. Denn damals musste ich mich auf Fehlerstacks oder die umgebende Funktionsaufrufe konzentrieren.

Die Logs der Programme sind wichtig. Jeder weiß das. Ich möchte jedoch die Bedeutung des Ansammelns von Logs überbetonen, anstatt sie nur in der Konsole zu beobachten und dann zu verwerfen. Sie werden mehr Komfort erfahren, wenn das Projekt läuft. Sie haben mehr Zeit, die vorherigen Logs zu finden. Es kann sein, dass Sie wissen müssen, ob ähnliche Datenbank-Stored-Procedure-Aufrufe zuvor stattgefunden haben. Es kann sein, dass Sie wissen müssen, ob derselbe Fehler zuvor aufgetreten ist. Es kann sein, dass Sie sich erinnern müssen, wie dieses Problem das letzte Mal behoben wurde.

In einem großen Projekt oder dutzenden Microservices gibt es tonnenweise Details. Und die Fehler, Ausnahmen oder Probleme treten immer wieder auf. Das Log ist wie das laufende Dokument eines Programms. Und sie werden vom Programm automatisch generiert, ohne dass ein Mensch tippen muss. Und für Entwickler sind diese Logs lesbar. Wenn Sie also eine neue Aufgabe beginnen oder einen neuen Fehler beheben, haben Sie Hunderte von Logs zur Hand, um diesen neuen Fehler zu beheben. Sie sind nicht allein.

Warum sammeln wir sie an? Weil Dinge oder Wissen leicht vergessen werden.

Es gab einen Fortschritt der menschlichen Zivilisation, als Papier erfunden wurde. Und als Computer erfunden wurden, gab es eine weitere Ebene der menschlichen Zivilisation. Notizen auf Papier zu machen ist wie das Ansammeln von Logs in Computern.

Nicht nur für Menschen, sondern auch für KI-Chatbots, LLM-Tools werden diese Logs immer wichtiger. Die GreptimeDB, eine Datenbank für die vereinheitlichte Sammlung und Analyse von Beobachtbarkeitsdaten (Metriken, Logs und Traces), die 2022 gegründet wurde, ist kein Zufall.

Warum habe ich das vorher nicht gemacht? Nachdem ich als Auftragnehmer für große Banken gearbeitet hatte, musste ich mehr zusammenarbeiten und an größeren Projekten arbeiten. Davor, die meiste Zeit in der Startup- oder meiner Startup-Phase, arbeitete ich alleine. Als ich vorher bei LeanCloud arbeitete, arbeitete ich etwa die Hälfte der Zeit an der IM-App LeanChat.

Und als ich in die formellere Unternehmenswelt kam, unterschied sich die Entwicklung der Projekte von meinem persönlichen Projekt oder Startup-Projekt. Sie haben SIT-, UAT-Testumgebungen. Und die Produktionsumgebung ist oft nur für bestimmte kleine Teamkollegen zugänglich. Das Abrufen der Logs von ihnen und das Beheben von Problemen wird langwierig und etwas mühsam. Und ein Projekt zu betreiben dauert seine Zeit, und die Jenkins-Pipeline benötigt oft eine halbe Stunde zum Ausführen.

Ich kann das Programm also nicht wie eine Fliege ausführen oder testen. Ich kann kein Deployment durchführen, indem ich einfach einen Befehl auf meinem PC eingebe und Code zum Ausführen auf den Server hochlade.

Daher veranlasst es mich irgendwie, Logs anzusammeln, um mehr Kontext für die Bearbeitung von Aufgaben zu haben. Wir sollten Probleme beim ersten Anlauf besser beheben. Wir sollten unsere Korrektur in wenigen Versuchen besser überprüfen. Wir können nicht einfach Logs des Programms abrufen, das in einer Cloud oder auf dem Server des Unternehmens läuft, daher ist es besser, sie zu kopieren und auf dem lokalen Laptop zu speichern, um Analysen durchzuführen.

Und jetzt, für meine persönlichen Projekte, werde ich die Logs auch ansammeln. Es wird eine Gewohnheit. Nachdem ich einige Jahre in großen Unternehmen gearbeitet habe, habe ich irgendwie mehr Geduld oder Strategie, um meine Projekte größer und länger zu machen. Also weiß ich, dass ich diese Logs im Laufe der Zeit brauche.

Jemand mag sagen, dass man nur eleganten Code und ein funktionierendes Projekt braucht. Man braucht keine Logs oder Fehlermeldungen anzusammeln. Das ist in Ordnung. Wenn wir einen Fehler oder eine neue Funktion haben, können wir das Programm ausführen, um die aktuellen Logs zu erhalten. Wir brauchen die Logs aus dem Entwicklungsprozess nicht. Sie sind wie die detaillierten Aufzeichnungen wissenschaftlicher Experimente. Auf den ersten Blick scheint es in Ordnung zu sein. Aber auf lange Sicht, wenn Sie eines Tages wieder daran arbeiten möchten, oder es teilen möchten, oder es anderen überlassen möchten, ist es vielleicht nicht gut.

Ich denke, hier könnten sich gute Möglichkeiten ergeben. Warum ermutigen wir in Unternehmen nicht jeden Entwickler, seine gesammelten Logs zu teilen? Auch in Open-Source-Projekten sollten wir das haben. Wir finden die Logs anderer nicht ansprechend, weil wir sie nicht kennen. Wir verlieren den Kontext beim Speichern dieser Logs. Und darin scheinen sich Tonnen von nicht verwandten oder trivialen Nachrichten zu befinden.

Aber der Aufwand, Logs anzusammeln, ist trivial. Es ist nur Kopieren und Einfügen jedes Mal, wenn wir Logs sehen, besonders diese Fehler-Logs. Und wie wäre es, das auf automatisierte Weise zu tun? Es ist eine gute Idee, die Logs jedes Mal in einem Verzeichnis aufzuzeichnen, wenn wir ein Projekt ausführen, wie diese Spring Boot-Projekte.

Die Welt wird immer digitaler, daher ist das Ansammeln von Logs digitaler Programme genau wie das Ansammeln von Büchern in einer physischen Welt.