import uvicorn
from fastapi import FastAPI
from code.routes import root

app = FastAPI()
app.include_router(root.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)