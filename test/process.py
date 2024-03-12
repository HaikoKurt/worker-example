from multiprocessing.managers import SyncManager
from time import sleep

class MyManager(SyncManager):
    pass

syncdict = {}

def get_dict():
    return syncdict

if __name__ == "__main__":
    MyManager.register("syncdict", get_dict)
    manager = MyManager(("127.0.0.1", 5000), authkey=b"password")
    manager.start()
    local_syncdict = manager.syncdict()

    try :
        while True :
            sleep(1)
            print(f"The magic: {local_syncdict}")
            c = local_syncdict.get('complex')
            if c is not None :
                c[1] += 1
                local_syncdict.update([('complex', c)])
                print(f"complex: {c}")
    except KeyboardInterrupt :
        pass

    manager.shutdown()