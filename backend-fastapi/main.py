from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users

app = FastAPI()

# including the imported  /user router in the main app
app.include_router(users.router)


# CORS configuration
origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8000",  # Add allowed origins here
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "DELETE",
    ],  # Add allowed methods here
    allow_headers=["*"],  # Allow headers here
)


@app.get("/")
async def root():
    return {"message": "Hello world!!"}


@app.get("/url")
async def url():
    return {"url": "http://ies-azarquiel.es"}


@app.get("/sum")
async def suma(a: int = 0, b: int = 0):
    return {"sum": a + b}


@app.get("/name/{name}")
async def greet(name: str):
    return {"greet": "Hello " + str(name) + "!!!"}
