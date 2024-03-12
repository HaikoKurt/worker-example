from multiprocessing.managers import SyncManager
from time import sleep

class GlobalManager(SyncManager):
    ...

globals = {}

def get_globals():
    return globals

if __name__ == "__main__":
    GlobalManager.register("globals", get_globals)
    manager = GlobalManager(("127.0.0.1", 5000), authkey=b"hewtit-fitqis-8cybXe")
    manager.start()
    theGlobals = manager.globals()
    theGlobals.update([('magic', 0)])

    try :
        while True :
            sleep(1)
    except KeyboardInterrupt :
        pass

    manager.shutdown()