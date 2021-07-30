import asyncio
import websockets

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Jimmy")
        print(f"(client) send to server: Jimmy")
        name = await websocket.recv()
        print(f"(client) recv from server {name}")

if __name__ == "__main__":
    uri = "ws://localhost:8765"
    asyncio.get_event_loop().run_until_complete(hello(uri))