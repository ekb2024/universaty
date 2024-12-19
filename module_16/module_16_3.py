from fastapi import FastAPI,Path
from typing import Annotated
users = {'1': 'Имя: Example, возраст: 18'}
app = FastAPI()
@app.get("/users")
async  def get_message( ) ->dict:
     return users

@app.post('/user/{username}/{age}')
async  def append_user(username :Annotated[str,Path(min_length=3,max_length=20,description='Enter username' ,example='UrbanUser')]
                       ,age:Annotated[int,Path(ge=18, le=120,description='Enter age' ,example='23')])->str:
     index = str(int(max(users, key=int)) + 1)
     users[index] = f'Имя: {username} ,возраст: {age}'
     return f"User {index}  is registered "

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int=Path(ge=1, le=int(max(users, key=int)), description='Enter id' ,example='2' ),
                        username: str=Path(min_length=3,max_length=20, description='Enter Username' ,example='Urban' ),
                        age: int=Path(ge=18, le=120,description='Enter age' ,example='24')) ->str:
     users[str(user_id)] =  f'Имя: {username} ,возраст: {age}'
     return f'The user {str(user_id)} is updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: int=Path(ge=1, le=int(max(users, key=int)))) ->str:
     users.pop(str(user_id))
     return f"User {str(user_id)} has been deleted"