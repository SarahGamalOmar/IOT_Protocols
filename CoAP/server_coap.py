import asyncio
from aiocoap import resource, Context, Message
from aiocoap.numbers.codes import Code

class TemperatureResource(resource.Resource):
    async def render_get(self, request):
        payload = "Temperature: 25 C"
        return Message(payload=payload.encode('utf8'))

async def main():
    root = resource.Site()
    root.add_resource(['temperature'], TemperatureResource())

    await Context.create_server_context(root, bind=('localhost',56830))
    print("CoAP server running on port 56830")
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())

