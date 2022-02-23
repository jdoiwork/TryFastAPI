# pyright: strict

from fastapi                import FastAPI
from lagom                  import Container
from routes                 import users, admin, token
from services.admin_service import AdminService, DummyAdminService
from services.token_service import DummyTokenService, TokenService
from services.users_service import DummyUsersService, UsersService
from utils.dep_container    import DepContainer

def setup_container(c: Container):
    c[UsersService] = DummyUsersService
    c[AdminService] = DummyAdminService
    c[TokenService] = DummyTokenService

app = FastAPI()

@app.get("/")
def index():
    return {
        "hello": "world",
    }


app.include_router(token.router)
app.include_router(users.router, prefix='/users')
app.include_router(admin.router, prefix='/admin')

# Inject with Lagom Container
# Open http://localhost:8000/users
c = Container()
app.dependency_overrides = DepContainer(c).to_dependency_overrides()
setup_container(c)
