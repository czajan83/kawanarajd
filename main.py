import uvicorn
from fastapi import FastAPI
from code.routes import root, raws

app = FastAPI()
app.include_router(root.router, prefix="/api")
app.include_router(raws.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)