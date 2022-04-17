from starlette.applications import Starlette
from starlette.routing import Route
import uvicorn
from starlette.responses import FileResponse



async def luonleo(scope):
    return FileResponse('memeserver/memes/luonleo.jpeg')

async def wikipedia(scope):
    return FileResponse('memeserver/memes/wikipedia.png')

async def no_bitches(scope):
    return FileResponse('memeserver/memes/no-bitches.jpeg')

async def tias(scope):
    return FileResponse('memeserver/memes/tias.mp4')


routes = [
    Route("/luonleo", luonleo, methods=["GET", "POST", "PUT"]),
    Route("/wikipedia", wikipedia, methods=['GET', "POST", "PUT"]),
    Route("/no-bitches", no_bitches, methods=['GET', "POST", "PUT"]),
    Route('/tias', tias, methods=['GET', "POST", "PUT"])
]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run("__main__:app")
