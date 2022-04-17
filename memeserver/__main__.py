from starlette.applications import Starlette
from starlette.routing import Route
import uvicorn
from starlette.responses import FileResponse



async def luonleo(scope):
    return FileResponse('memes/luonleo.jpeg')

async def wikipedia(scope):
    return FileResponse('memes/wikipedia.png')


routes = [
    Route("/luonleo", luonleo, methods=["GET", "POST", "PUT"]),
    Route("/wikipedia", wikipedia, methods=['GET', "POST", "PUT"])]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run("__main__:app")
