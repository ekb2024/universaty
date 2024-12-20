from fastapi import FastAPI, Path ,HTTPException
from pydantic import BaseModel
from typing import List
app = FastAPI()

users =[]
class User(BaseModel):
     id: int = None
     username: str
     age:int
@app.get("/users")
async  def get_message( ) ->List:
     return users
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

