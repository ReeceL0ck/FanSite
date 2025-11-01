from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

from fastapi.templating import Jinja2Templates

# app = FastAPI(dependencies=[Depends(get_query_token)]) # Use this if we want all routes to have the dependency
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="mainplay.html", context={"id": id}
    )
