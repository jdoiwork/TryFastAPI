# pyright: strict

from fastapi           import FastAPI, Depends, Request
from fastapi.responses import RedirectResponse
from services          import DbService, Service
from models            import Name
from ioc               import container, di

from lagom             import Container

from routes            import home, users


def setup(c: Container):
    c[Name] = "world"

    def db_service():
        db = DbService()
        db.name = "mysql"
        return db
    c[DbService] = db_service
    

app = FastAPI()
c = container


def current_user(request: Request) -> str:
    return "jdoi"

@app.get("/")
def index(
    name: Name = di(Name),
    s:Service = di(Service),
    user: str = Depends(current_user)
):
    return {
        "hello": name,
        "db_name": s.db.name,
        'user': user,
    }

@app.get('/users')
def redirect_to_users():
    return RedirectResponse('/users/')

app.include_router(users.router, prefix='/users')
app.include_router(home.router)
setup(c)
