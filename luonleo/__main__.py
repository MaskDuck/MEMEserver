from starlette.applications import Starlette
from starlette.routing import Route
import uvicorn
from starlette.responses import FileResponse



async def handler(scope):
    return FileResponse('luonleo/luonleo.jpeg')


routes = [Route("/", handler, methods=["GET", "POST", "PUT"])]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run("__main__:app")
