import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.logging import setup_logging, get_logger
# routers
# from apis import auth, users, vocabulary, learning, progress, stats



# setup logging
setup_logging()
logger = get_logger("main")




app = FastAPI(
    title="Learn English App",
    description="A modern AI-powered English learning application",
    version="0.1.0",
    # life_span=lifespan, # for bot
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods= ["*"], #["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"], #["Content-Type", "Authorization"],
)

# app.include_router()

@app.get("/")
def read_root():
    return {"message": "Hello Hello, Are you sure ?"}

@app.get("/health")
def health_check():
    return {"message": "I am ok, thanks! 😊", "status": "OK"}

if __name__ == "__main__":
    import uvicorn
    logging.info("Server is running on port 8000")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug")