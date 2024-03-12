from multiprocessing.managers import SyncManager
from typing import Optional, Dict, Any, Union

class MyManager(SyncManager):
    ...

class Meta:
    def __init__(self, *, port: int) -> None:
        self.manager = MyManager(("127.0.0.1", port), authkey=b"password")
        self.manager.connect()
        MyManager.register("syncdict")

        self.syncdict = self.manager.syncdict()

    def update(self, kwargs: Dict[Any, Any]) -> None:
        self.syncdict.update(kwargs)

    def reset(self, key: str):
        self.syncdict.update([(key, 0)])

    def increase_one(self, key: str) -> None:
        self.syncdict.update([(key, self.syncdict.get(key) + 1)])

    def report(self, item: Union[str, int]) -> int:
        return self.syncdict.get(item)

c = [
    {
        "Name": "Hugo",
        "Ort": "Bachtal"
    },
    14,
    "Oberfläche"
]

if __name__ == "__main__" :
    try:
        meta = Meta(port=5000)
        data = meta.report('magic')
        if data is None :
            print("It's not magic.")
            meta.reset('magic')
        else :
            print(f"Magic is: {data}")
            meta.increase_one('magic')
        global_c = meta.report('complex')
        if global_c is None :
            meta.update([('complex', c)])
        else :
            print(f"Global c {global_c[1]}")
    except Exception as e:
        print(f"Exception {e}")