from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# python -m uvicorn Module_16_2:app
@app.get("/")
async def welcome() -> dict:
    return {"message":"Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}



@app.get("/user/{user_id}")
async def get_id(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]) -> dict:
    return {"message": f"Вы вошли как пользователь {user_id}"}



@app.get("/user/{username}/{age}")
async def users_id(username: Annotated[str,Path(min_length=5, max_length=20, description= "Enter your username", example="UrbanUser")],
                   age: int = Path(ge=18, le=120, description="Enter age", example=24)) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

