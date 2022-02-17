# pyright: strict

from fastapi                import FastAPI
from lagom                  import Container
from routes                 import users
from services.users_service import DummyUsersService, UsersService
from utils.dep_container    import DepContainer

def setup_container(c: Container):
    c[UsersService] = DummyUsersService

app = FastAPI()

@app.get("/")
def index():
    return {
        "hello": "world",
    }


app.include_router(users.router, prefix='/users')

# Inject with Lagom Container
# Open http://localhost:8000/users
c = Container()
app.dependency_overrides = DepContainer(c).to_dependency_overrides()
setup_container(c)
