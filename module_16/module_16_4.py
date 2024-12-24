from fastapi import FastAPI, Path ,HTTPException
from pydantic import BaseModel , Field
from typing import List
from typing import Annotated

app = FastAPI()

#python -m uvicorn module_16_4:app

users =[]
class User(BaseModel):
     id: int = None
     username: str
     age:int

@app.get("/users")
async  def get_message( ) ->List:
     return users
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

