from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(defult=None)
    content: str = Field(defult=None)

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "some title about animals",
                "content": "some content about animals"
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(defult=None)
    password: str = Field(defult=None)

    class Config:
        the_schema={
            "user_demo":{
                "fullname":"Kevin Dev",
                "email":"kevin@gmail.com",
                "password":"kevin@123"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(defult=None)
    password: str = Field(defult=None)

    class Config:
        the_schema={
            "user_demo":{
                "email":"kevin@gmail.com",
                "password":"kevin@123"
            }
        }
