from quart import Quart, render_template, redirect, url_for
from multiprocessing.managers import SyncManager
from typing import Dict, Any, Union

app = Quart(__name__)

class GlobalManager(SyncManager):
    ...

class Global:
    def __init__(self) -> None:
        self.manager = GlobalManager(("127.0.0.1", 5000), authkey=b"hewtit-fitqis-8cybXe")
        self.manager.connect()
        GlobalManager.register("globals")

        self.globals = self.manager.globals()

    def update(self, kwargs: Dict[Any, Any]) -> None:
        self.globals.update(kwargs)

    def reset(self, key: str):
        self.globals.update([(key, 0)])

    def increase_one(self, key: str) -> None:
        self.globals.update([(key, self.globals.get(key) + 1)])

    def report(self, item: Union[str, int]) -> int:
        return self.globals.get(item)

global_magic = Global()

use_global = True

class Magic :
    def __init__(self) -> None:
        self.value = 0

    def incr(self) :
        self.value += 1

    def reset(self) :
        self.value = 0

magic = Magic()

@app.route("/")
async def hello():
    if use_global :
        magic_value = global_magic.report('magic')
    else :
        magic_value = magic.value
    return await render_template("index.html", value = magic_value)

@app.route("/reset")
async def reset():
    if use_global :
        global_magic.reset('magic')
    else :
        magic.reset()
    return redirect(url_for('hello'))

@app.route("/incr")
async def increment():
    if use_global :
        global_magic.increase_one('magic')
    else :
        magic.incr()
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run()