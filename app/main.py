from fastapi import FastAPI, HTTPException


app = FastAPI()


# In-memory sample data
recipes = [
    {
        "id": 1,
        "title": "Spaghetti Carbonara",
        "description": "Classic Roman pasta with eggs, cheese, pancetta, and pepper.",
    },
    {
        "id": 2,
        "title": "Chicken Tikka Masala",
        "description": "Marinated chicken in a spiced tomato cream sauce.",
    },
    {
        "id": 3,
        "title": "Avocado Toast",
        "description": "Toasted sourdough with smashed avocado, lemon, and chili flakes.",
    },
]


@app.get("/recipes")
async def list_recipes():
    return recipes


@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int):
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)


@app.get("/ping", response_class=PlainTextResponse)
async def ping() -> str:
	return "pong"

