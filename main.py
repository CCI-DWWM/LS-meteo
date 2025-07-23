# c'est le controller

from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

import model


# from dotenv import load_dotenv
# import os
# load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# DB_HOST=os.getenv('DB_HOST')
# print(f"{DB_HOST}")

@app.get("/")
async def redirect_typer():
    return RedirectResponse("/items/test")


@app.get("/items/{id}")
def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}

    # request = request, name = "item.html", context = {"id": id, "maList": ["555", "hhh", "iii"]}
    )


@app.get("/items2/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/formulaire")
def read_formulaire(request: Request, codePostal: str):
    """
    Cette fonction permet de récupérer le code postal saisis par l'utilisateur
    :param request:
    :param codePostal:
    :return: code postal
    """
    myresult = model.get_city(codePostal)
    return templates.TemplateResponse(
        request=request, name="item.html", context={"codePostal": codePostal, "myresult": myresult})