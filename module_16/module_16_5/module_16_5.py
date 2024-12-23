from fastapi import FastAPI, Path ,HTTPException, Request
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import  Jinja2Templates
app = FastAPI()
Jinja2Templates = Jinja2Templates(directory="templates")

users =[]
class User(BaseModel):
     id: int = None
     username: str
     age:int

@app.get("/")
async def get_message(request: Request) -> HTMLResponse:
        return Jinja2Templates.TemplateResponse("users.html", {"request": request, "users": users})
@app.get(path="/user/{user_id}")
async  def get_message(request: Request, user_id:int ) ->HTMLResponse:
    return Jinja2Templates.TemplateResponse("users.html", {"request": request, "user": users[user_id]})


@app.post('/user/{username}/{age}')
async  def append_user(username,age) ->List:
     users.append(User(id=len(users) + 1, username=username, age=age))
     return users
@app.put('/user/{user_id}/{username}/{age}')
async def update_user( user_id:int,username:str,age:int) ->List:
               try:
                    valid_user = users[user_id -1]
                    users[user_id - 1] = User(id=user_id, username=username, age=age)
                    return valid_user
               except IndexError:
                    raise HTTPException(status_code=404, detail="User was not found")
@app.delete("/user/{user_id}")
def delete_user(user_id:int) ->List:
    try:
        valid_user = users[user_id - 1]
        users.pop(user_id - 1)
        return valid_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")