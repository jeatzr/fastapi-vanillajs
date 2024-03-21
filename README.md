## Users-API created in FastAPI and simple HTML form wich VanillaJS and Bootstrap to post a new user

- This is a very simple example of a CRUD API to manage users in a fake DB (not database, not persistence, just in memory). It has been programmed in python with [FastAP](https://fastapi.tiangolo.com/) framework. In order to allow CORS from your prefered client, make sure that you add the origin in CORS configuration in `main.py` inside `backend-fastapi`

````python
# CORS configuration
origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8000",  # Add allowed origins here
    "http://127.0.0.1:5500",
]
````

- You will need to install python in your computer to run the API server. Follow the instructions inside the directory `backend-fastapi` to create the virtual environment `.venv`, install dependencies inside `.venv` and run the `uvicorn` server. 

- You can test the API with Postman, Thunder Client, curl or whatever thing. 

- You can see also a very easy example of how post a new user from a simple HTML + Bootstrap + VanillaJS using a fetch method with the POST method. You can find inside `frontend-vanillajs` directory. You can just run with Live Server -> index.html.



