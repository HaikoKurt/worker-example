# Quart mit mehreren Workern und Globalem State

Nutzt man `Flask` oder `Quart` mit WSGI- (`Gunicorn`) oder ASGI-Servern (`Hypercorn`) und konfiguriert mehr als einen Worker, kann man keinen serverbasierten State halten, da jeder Worker seinen eigenen State besitzt und es so zu Inkonsistenzen kommt. Eine Lösung ist, den State in einer Datenbanktabelle abzulegen. Manchmal ist das jedoch unpraktisch, weil man z.B. gar keinen __persistenten__ State benötigt oder keine Datenbank einsetzt. 

Lösung ist ein Serverbasierter State, der von allen Workern genutzt werden kann. Dafür kann der `SyncManager` aus dem `multiprocessing.managers` Paket verwendet werden.

Hier ist ein entsprechendes Beispiel, das in einem Docker-Container gestartet werden kann. Statt eines Integer-Wertes können auch komplexere Datenstrukturen in dem globalen `dict` gespeichert werden. Das Beispiel realisiert zu Anschauungszwecken auch eine Version ohne den Serverbasierten State (`use_global = False`).

Über Anregungen; Diskussionen und Verbesserungsmöglichkeiten freue ich mich!