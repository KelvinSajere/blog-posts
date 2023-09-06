import random

from fastapi import FastAPI
from propan import RabbitBroker


broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
app = FastAPI()

@broker.handle(queue="fastapi")
async def base_handler(body):
    print(f"This is the queue result :: {body}")

@app.on_event("shutdown")
async def shutdown():
    await broker.close()


@app.on_event("startup")
async def on_start_up():
     # Starts the broker 
     await broker.start()

@app.post("/external-queue")
async def rabbitmq_queue():
    print("Queueing a job Using Rabbit MQ")
    await broker.publish(
                      queue='fastapi',
                      message=str(random.randint(1, 100))
    )
    
    return {"result": "success"}
