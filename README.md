# Quart mit mehreren Workern und Globalem State

Nutzt man `Flask` oder `Quart` mit WSGI- (`Gunicorn`) oder ASGI-Servern (`Hypercorn`) und konfiguriert mehr als einen Worker, kann man keinen serverbasierten State halten, da jeder Worker seinen eigenen State besitzt und es so zu Inkonsistenzen kommt. Eine Lösung ist, den State in einer Datenbanktabelle abzulegen. Manchmal ist das jedoch unpraktisch, weil man z.B. gar keinen __persistenten__ State benötigt oder keine Datenbank einsetzt. 

Lösung ist ein Serverbasierter State, der von allen Workern genutzt werden kann. Dafür kann der `SyncManager` aus dem `multiprocessing.managers` Paket verwendet werden.

Hier ist ein entsprechendes Beispiel, das in einem Docker-Container gestartet werden kann. Statt eines Integer-Wertes können auch komplexere Datenstrukturen in dem globalen `dict` gespeichert werden. Das Beispiel realisiert zu Anschauungszwecken auch eine Version ohne den Serverbasierten State (`use_global = False`).

Über Anregungen, Diskussionen und Verbesserungsmöglichkeiten freue ich mich!

# Quart with multiple workers and global state 

If you use `Flask` or `Quart` with WSGI (`Gunicorn`) or ASGI servers (`Hypercorn`) and configure more than one worker, you cannot maintain a server-based state, because every worker has its own state and this leads to inconsistencies. One solution is to store the state in a database table. However, sometimes this is impractical because, for example, you don't need a __persistent__ state or you don't use a database.

The solution is a server-based state that can be used by all workers. The `SyncManager` from the `multiprocessing.managers` package can be used for this. Here is a corresponding example that can be launched in a Docker container. Instead of an integer value, more complex data structures can also be stored in the global `dict`. For illustrative purposes, the example also implements a version without the server-based state (`use_global = False`).

I welcome suggestions, discussions and opportunities for improvement!
