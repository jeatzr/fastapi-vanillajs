from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# defining router under the prefix /user
router = APIRouter(prefix="/user", tags=["Users"])

users_list = [
    {"id": 1, "username": "pepito", "email": "pepito@gmail.com", "disabled": False},
    {"id": 2, "username": "andres", "email": "andresito@gmail.com", "disabled": True},
    {"id": 3, "username": "ladygaga", "email": "lady@gmail.com", "disabled": False},
]


class User(BaseModel):
    id: int
    username: str
    email: str
    disabled: bool


users_fake_db = [
    User(id=1, username="pepito", email="pepito@iesazarquiel.es", disabled=False),
    User(id=2, username="andres", email="andres@iesazarquiel.es", disabled=True),
    User(id=3, username="ladygaga", email="ladygaga@iesazarquiel.es", disabled=False),
]


@router.get("/json")
async def users():
    return users_list


@router.get("/", response_model=list[User])
async def users():
    return users_fake_db


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
async def insertUser(user: User):
    if type(search_user(user.id)) == User:
        # if any(user.id == user_aux.id for user_aux in users_fake_db):
        # return {"error": "Usuario ya existe con ese id"}
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="There is a user already with this ID",
        )
    users_fake_db.append(user)
    return user


@router.delete("/{id}")
async def deleteUser(id: int):
    # for index, user in enumerate(users_fake_db):
    # if user.id == id:
    # del users_fake_db[index]
    # users_fake_db.remove(user)
    found_user = search_user(id)
    if type(found_user) == User:
        users_fake_db.remove(found_user)
        return {"detail": "Usuario eliminado"}
    # return found_user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Not found user by ID to erase"
    )


@router.put("/")
async def modify(user: User):
    found_user = search_user(user.id)
    if type(found_user) == User:
        found_user.username = user.username
        found_user.email = user.email
        found_user.disabled = user.disabled
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Not found user by ID to modify",
    )


@router.get("/{id}", response_model=User)
async def userbyid(id: int):
    found_user = search_user(id)
    if type(found_user) == User:
        return found_user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="User by ID not found"
    )


def search_user(id: int):
    users_filtered = filter(lambda user: user.id == id, users_fake_db)
    try:
        return list(users_filtered)[0]
    except:
        return None

    # for user in users_fake_db:
    #    if user.id == id:
    #        return user
