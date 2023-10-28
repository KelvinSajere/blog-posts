from fastapi import FastAPI
import uvicorn

from python.shared_model.user import UserResponse



app = FastAPI()

# Sample user data
users_data = [
    {"id": 1, "username": "user1", "email": "user1@example.com"},
    {"id": 2, "username": "user2", "email": "user2@example.com"},
]


@app.get("/get_all_users", response_model=list[UserResponse])
async def get_all_users():
    # Return all users
    return users_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

