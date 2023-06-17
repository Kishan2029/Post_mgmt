import uvicorn
from fastapi import FastAPI
from app.model import PostSchema

posts = [
    {
        "id": 1,
        "title": "Penguins",
        "text": "Penguins are a group of aquatic flightless birds."
    },
    {
        "id": 2,
        "title": "Tigers ",
        "text": "Tigers are the largest living cat species and a memeber of the genus panthera."
    },
    {
        "id": 3,
        "title": "Koalas ",
        "text": "Koala is arboreal herbivorous maruspial native to Australia."
    },
]

app = FastAPI()


# Get - for testing
@app.get("/", tags=["test"])
def greet():
    return {"data":"Hello World"}

# Get Posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}

# Get Post from id
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id:int):
    for post in posts:
        if post["id"] == id:
            return{
                "data":post
            }
    error = "Post with id-{} does not exist".format(id)
    return {
            "error":error
        }
    
# Create a Post from id