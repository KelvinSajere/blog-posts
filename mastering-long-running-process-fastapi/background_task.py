
import time
from fastapi import BackgroundTasks, FastAPI


app = FastAPI()


def process_item(item_id: int):
    # Simulate a long-running process
    time.sleep(5)
    print(f"Processed item {item_id}")
    
@app.post("/process/{item_id}")
async def process_item_background(item_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_item, item_id)
    return {"message": "Processing started in the background"}