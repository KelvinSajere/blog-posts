import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from task_api.database import Base, engine
from task_api.router import router

app = FastAPI()


# Include the router
app.include_router(router)

# Create all tables
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host=host, port=port)
