import asyncio
from aiocoap import *

async def main():
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri='coap://localhost:56830/temperature')
    response = await protocol.request(request).response
    print('Result: %s\n%r'%(response.code, response.payload.decode()))

if __name__ == "__main__":
    asyncio.run(main())

