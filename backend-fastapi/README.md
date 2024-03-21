- create virtual environment
`python -m venv .venv`

- activate venv en MAC OS:
`source .venv/bin/activate`
- Activate venv - Windows PowerShell:
`.\.venv\Scripts\Activate.ps1`
- Activate venv - Windows cmd 
`.\.venv\Scripts\activate.bat`

- Install requirements:
`pip install -r requirements.txt`

- Start uvicorn server
`uvicorn main:app --reload`

- Swagger documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redocly documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)