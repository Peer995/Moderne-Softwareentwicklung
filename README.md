# Moderne Softwareentwicklung
Ein dediziertes Repository für die Abgaben des Moduls "Moderne Softwareentwicklung"

Es gibt in diesem Repository zwei Branches: der eine (main) enthält den Clean Code sowie die Checkliste, die für die Einsendeaufgabe 4 benötigt wird. Der Branch "not clean" enthält die alten Dateien, die nicht als Clean Code entwickelt worden sind. 

Dieses Repository dient sowohl der Einsendeaufgabe 4 (CCD) sowie der Nr. 5 (GitHub), da die Anforderungen dies möglich machen.

Schauen Sie sich gerne um.

## Worum handelt es sich bei dem Code? (EA_4)

Den Code habe ich gerade entwickelt für ein Weihnachtsrätsel, das ich meiner Freundin im Adventskalender präsentieren will - mit jedem Tag gibt es mehr Hinweise. Der Code gehört zu einem Alexa-Skill, den sie dann starten kann und sich mit Passwörtern aus dem Kalender Hinweise für die Rätsel geben lassen kann. Manchmal sind die Hinweise nötig für die Lösung, manchmal nur ein Zusatz oder Anstoß, wenn sie nicht weiterkommt.

Der Code an sich ist nicht ausführbar, da dafür das SSML (Speech Synthesis Markup Language) und das Sprachmodell von Alexa benötigt werden, die nicht Teil des Codes sind. Das Modell wird an anderer Stelle in der Entwicklung trainiert.

Der Skill ist allerdings voll funktionsfähig und wurde bereits vom Amazon-Team zertifiziert (zwecks Datenschutz, Funktion etc.). Er ist also bereits "ready-to-launch" ;)

## Warum ist dies Clean-Code? (EA_4)

Bei diesem Code handelt es sich um Clean Code, da er eine nicht zu hohe vertikale Ausbreitung besitzt, auch ohne Kommentare durch die SSML ganz gut verständlich ist und die Methoden / Klassen immer einen bestimmten Zweck erfüllen. Auch die anderen Richtlinien wurden eingehalten. So wurde der Code aus dem anderen Branch deutlich aufgewertet und vollständig mit zusätzlichen Kommentaren versehen, die auch dritten Entwickelnden einen leichten Einstieg bieten sowie Hinweise, worauf zu achten ist, wenn etwas verändert wird.

Wichtig finde ich persönlich auch, das Fehlerabfang-Mechanismen eigene Methoden haben, da diese oft recht unübersichtlich sind, wenn sie in die Methoden eingebaut werden. Bei der Methode im utils.py konnte dies nicht eingehalten werden, da diese Methode so von Amazon vorgegeben war. Hier ist der Fehlerblock allerdings auch nicht so groß, sodass es optisch nicht stört und die Methode nicht überladen ist. Hier wäre es sogar fast verwirrender, wenn extra eine zweite Methode für diese eine Fehlermeldung erstellt worden wäre.

Auch bei den Variablen wurden eindeutige Namen verwendet, die auch den im Sprachmodell hinterlegten Intents entsprechen mit "Handler" an den Namen gehängt - dies ist bei Alexa-Programmen so üblich. Abkürzungen werden nicht verwendet, die würden die Namensgebung durcheinanderbringen.

Bei der Formatierung wurde darauf geachtet, dass immer zwei Zeilen frei sind zwischen den Klassen, eine Zeile zwischen Methoden und drei Zeilen zum Ende, wenn der SkillBuilder programmiert wird, da dieser keinen Zusammenhang mit den übrigen Klassen hat und ein optischer Übergang darauf aufmerksam macht.

Die Fehlermeldungen haben zwei Stufen, wie auch in den Klassenbeschreibungen erläutert wird: die Fallback-Klasse, wenn etwas nicht richtig verstanden wurde, und die Exception-Klasse, die als Auffangnetz für andere Fehler dient, nach denen der Skill zum Beispiel geschlossen werden muss.

## Anforderungen für EA_5

Dieses Repository dient ebenfalls der Einsendeaufgabe 5. Die Dateien und Branches wurden einerseits über die Weboberfläche, andererseits über die Konsole von PyCharm erstellt, bearbeitet, gelöscht, abgefragt, verglichen und gemergt. Außerdem wurde eine Pull Request von Peer995:Peer995-neu-Pasta auf edlich:master erstellt mit einem Rezept für leckere Pasta Verde (Link: https://github.com/edlich/education/pull/312).
