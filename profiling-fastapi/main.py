from time import sleep
from fastapi import FastAPI

from pyinstrument import Profiler
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

class PyInstrumentMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        profiler = Profiler(interval=0.001, async_mode="enabled")
        profiler.start()
        response = await call_next(request)
        profiler.stop()
        profiler.write_html("profile.html")
        return response 

app = FastAPI()

app.add_middleware(PyInstrumentMiddleWare)

@app.get("/process")
async def get_long_process():
    # similulate a long running task
    sleep(20)
    return {"result":"result"}


