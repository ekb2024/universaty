from fastapi import FastAPI
from routers import user
from routers import task

app = FastAPI()
@app.get('/')
async def get_message() -> dict:
    return  {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)

#python -m uvicorn main:app