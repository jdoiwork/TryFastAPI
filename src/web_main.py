# pyright: strict

from fastapi  import FastAPI
from services import DbService
from models   import Name
from routes   import home, users
import ioc


def setup(c: ioc.Container):
    c[Name] = "world"

    db = DbService()
    db.name = "mysql"
    c[DbService] = db

app = FastAPI()

resolve = ioc.register(setup)

app.include_router(users.create(resolve), prefix='/users')
app.include_router(home.create(resolve))



@app.get("/")
def index(name: Name = resolve(Name)):
    return {
        "hello": name
    }
