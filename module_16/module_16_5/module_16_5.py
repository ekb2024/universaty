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
     users.append(User(id = (max((id_user.id for id_user in users), default=0) + 1), username=username, age=age))
     return users
@app.put('/user/{user_id}/{username}/{age}')
async def update_user( user_id:int,username:str,age:int) ->List:
               try:
                    for u in range(len(users)):
                        if users[u].id == user_id:
                           users[u] = User(id=user_id, username=username, age=age)
                           valid = users[u]
                           break
                    return valid
               except IndexError:
                    raise HTTPException(status_code=404, detail="User was not found")
@app.delete("/user/{user_id}")
def delete_user(user_id:int) ->List:
    try:
        valid_user = users[user_id ]
        for u in range(len(users)):
            if users[u].id == user_id:
                valid = users[u]
                users.pop(u)
                break

        return valid
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
