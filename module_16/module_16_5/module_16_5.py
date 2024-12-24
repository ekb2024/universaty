from fastapi import FastAPI, Path ,HTTPException, Request
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import  Jinja2Templates
from typing import Annotated

app = FastAPI()
Jinja2Templates = Jinja2Templates(directory="templates")

users =[]


class User(BaseModel):
    id: int = Field(ge=1, le=100, description="Enter User ID")
    username: str = Field(min_length=5, max_length=20, description="Название продукта должно быть от 5 до 20 символов")
    age: int = Field(ge=18, le=100, description="возраст должен быть от 18 до 100")


@app.get("/")
async def get_message(request: Request) -> HTMLResponse:
        return Jinja2Templates.TemplateResponse("users.html", {"request": request, "users": users})
@app.get(path="/user/{user_id}")
async  def get_message(request: Request, user_id:int ) ->HTMLResponse:
    return Jinja2Templates.TemplateResponse("users.html", {"request": request, "user": users[user_id]})


@app.post('/user/{username}/{age}')
async  def append_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) ->User:
     new_user = User(id = (max((id_user.id for id_user in users), default=0) + 1), username=username, age=age)
     users.append(new_user)
     return new_user
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id:Annotated[int, Path(ge=1, le=100, description='Enter age', example='1')], username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')])->User:
                   valid = False
                   for u in range(len(users)):
                        if users[u].id == user_id:
                           users[u] = User(id=user_id, username=username, age=age)
                           valid = users[u]
                           return valid
                   if valid == False:
                           raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
def delete_user(user_id:Annotated[int, Path(ge=1, le=100, description='Enter age', example='1')]) ->User:
       valid = False
       for u in range(len(users)):
            if users[u].id == user_id:
                  valid = users.pop(u)
                  return valid
       if  valid == False:
              raise HTTPException(status_code=404, detail="User was not found")

