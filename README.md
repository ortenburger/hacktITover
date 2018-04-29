# Team: Deep Thought'); DROP TABLE *; --
This repository is used for the Hack{it}Over 2018 hackathon in Hanover. 

Prerequisites: 
* Beer
* Coffee

Used APIs: 
* GitHub
* SAP
* PRECIRE

Frameworks used: 
* SAP
* NodeJS
* Unity
* Android SDK
* Ionic

Languages used:
* Python
* JavaScript
* R
* TypeScript
* C/++



VISHONI is a Tool to improve team performance. According to The forming–storming–norming–performing model of group development by Bruce Tuckman (https://en.wikipedia.org/wiki/Tuckman%27s_stages_of_group_development) we develop a tool to get into the 'storming'-stage of team development with remotely working teams. To achieve this we put the teams into virtual escape rooms, where they will need to communicate and solve puzzles together. By creating this game environment we are able to overcome cultural differences and drastically increase the teams performance on the long run. We use the communication between the team members to get insights on their optimal team roles via PRECIRE and machine learning (Tensorflow in the SAP-Cloud) to help improve the agile assembly of new teams. To ensure data integrity and security and to prevent any kind of manipulation we are using the blockchain technology. The High score and sessions are stored via the SAP-Services.


Teambuilding ist ein immer wiederkehrendes Thema in unserer Arbeitswelt. Nach dem Modell von Tuckman muss ein Team bei jeder Änderung immer wieder die 4 Phasen durchlaufen.

![tuckmans](https://user-images.githubusercontent.com/38807108/39403475-83a7103a-4b7d-11e8-87ea-d34792944121.png)

In der Forming-Phase lernen sich die Teammitglieder kennen, die Ziele und Aufgaben werden definiert, alle sind noch recht vorsichtig miteinander. 
Storming ist die Phase, in der die Teammitglieder beginnen sich offen miteinander austauschen. Es können Konflikte bezüglich der Rollenverteilung entstehen. Die Leistung ist zwar gering aber die Phase ist notwendig um das gegenseitige Vertrauen aufzubauen und zu der nächster Phase überzuleiten. 
Im Norming hat sich das Team beruhigt und gefunden, die Beziehungen sind harmonischer, die Rollen verteilt. 
Ab der Performing-Phase agiert das Team als Kollektiv, es wird füreinander gearbeitet, man unterstützt sich gegenseitig. Die Produktivität und Leistungsorientierung des Teams sind jetzt auf einem hohen Niveau.
 
Jedoch kommen vor allem remote Teams selten über die Forming-Phase hinaus. Sie arbeiten zwar miteinander, tauschen sich aber kaum aus. Somit gelangen die Teams nie in die Norming-Phase, von der Performing-Phase ganz zu schweigen. 

Teamarbeit soll nicht dem Zufall überlassen werden. Aus diesem Grund hat die Teambildung/-entwicklung unter anderem das Ziel, ein positives Arbeitsklima zu schaffen und eine vertrauensvolle Zusammenarbeit zu gewährleisten. 

Unsere App hilft insbesondere remote arbeitenden Teams sich kennenzulernen, sie erreichen gemeinsam Ziele, die sie alleine niemals hätten erreichen können. In dem geschützten Aufgaben-Rahmen werden die Benutzer zu einer aktiven und offenen Kommunikation angeleitet und lernen konstruktive Kritik und Erwartungen an die Rolle der anderen zu formulieren. So können Forming und Storming schneller überwunden werden. Zudem erleben die Gruppenmitglieder gemeinsam Erfolge und Niederlagen. Dies führt zu einer engeren Verbindung auf der emotionalen Ebene und der Teamgeist wird gefördert, was sich wiederum positiv auf die Arbeit auswirkt.
Um zusätzliche Motivation zu erzeugen nutzen wir den SAP Gamification Service. Die Teams erreichen Punkte, welche unternehmensweit in der Hall of Fame angezeigt werden. Die Top Teams bekommen Belohnungen. Die Teams die am schlechtesten abschneiden, werden von Coaches unterstützt. Eventuell passen sie gar nicht zusammen und sollten lieber mit anderen zusammenarbeiten. 

Unterstützend zu den Daten aus der Game Performance können die Gespräche während den Challenges mit Hilfe von PRECIRE analysiert und so psychologische Rückschlüsse auf kommunikative und persönliche Kompetenzen der einzelnen Teammitglieder möglich werden. Dadurch können den Teams auf sie spezifisch abgestimmte Challenges gestellt werden.

Um Manipulationen gar nicht erst zu ermöglichen setzen wir auf der Blockchain, welche auf der SAP-Cloud implementiert wurde. So können wir die Nutzer eindeutig und anonymisiert (für die psychologische Auswertung interessant) identifizieren. Jede Session mit ihren Ergebnissen wird als Payload in der Chain gespeichert.

Die Technologie, welche wir hier entwickelt haben, lässt sich auch auf viele andere Felder anwenden, wie beispielsweise die Betreuung von Alten Menschen, welchen so die Möglichkeit geboten wird mit ihren Enkeln einfach und unkompliziert zu spielen oder auch PTSD-Patienten nahezu jederzeit eine Session mit ihrem Therapeuten wahrzunehmen. Eine weitere interessante Anwendungsmöglichkeit ist die Suizidhilfe, wir können mit ausreichend Trainingsdaten rechtzeitig intervenieren und erstmal über inbenta einen maschinellen Psychologen an die Hand geben, bis ein realer Zeit hat sich dem gefährdeten anzunehmen.
