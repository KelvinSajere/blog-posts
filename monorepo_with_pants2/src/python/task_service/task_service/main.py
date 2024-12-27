from fastapi import FastAPI
import uvicorn
from task_service.database import Base, engine
from task_service.router import router

app = FastAPI()

# Include the router
app.include_router(router)


# Create all tables
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
