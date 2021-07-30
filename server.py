import asyncio
import websockets

async def echo(websocket, path):
    print('echo.')
    async for message in websocket:
        print(message, 'receive from client')
        greeting = f"Hello {message}!"
        await websocket.send(greeting)
        print(f"> {greeting}")

if __name__ == "__main__":
    start_server = websockets.serve(echo, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

    # asyncio.run ?