import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT


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
users=[]
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
@app.post("/posts", tags=["posts"])
def create_post(post:PostSchema):
    post.id = len(posts)+1
    posts.append(post.dict())
    return {
        "info":"Post Added!",
        "data":posts
    }
    
# Create new user - UserSignUp
@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema=Body(default=None)):
    users.append(user)
    return signJWT(user.email)
    
 # Fucntion to check wheather user already exists or not
def check_user(data:UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

# User login route
@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema=Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:   
        return{
            "error":"Invalid Login details!"
        }
