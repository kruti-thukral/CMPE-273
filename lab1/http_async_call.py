import asyncio
from aiohttp import ClientSession

# makes HTTP get request to the specified URL asynchronously
async def get_data(url, session): 
        async with session.get(url) as response:
            #print (response.headers)
            return response

# registers futures and waits for their completion 
async def execute(number_of_times):
    url = "https://webhook.site/08a946a7-c490-4e2a-9498-037c6eb4849d"
    requests = []

    async with ClientSession() as client_session:
        for i in range(number_of_times):
            request = asyncio.ensure_future(get_data(url, client_session))
            requests.append(request)

        responses = await asyncio.gather(*requests)
        for response in responses:
            if (response.status == 200):
                print_date(response.headers)

def print_date(header):
    print (header['Date'])

number_of_times = 3;
loop = asyncio.get_event_loop()
loop.run_until_complete(execute(number_of_times))