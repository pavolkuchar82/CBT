# using this library we can create asynchronous calls in python
import asyncio

# using this library we can create asynchtonous http calls
from aiohttp import ClientSession

base_url = "http://httpbin.org/"

# using async keyword i defined this count method. Betwwen each count between 1-4 is going 
# to call this asyncio.sleep method with the keyword await. 
# This is a critical function to create asynch method. While this method is countong and awaits for sleep 
# method the python can the other function.


# this function is similar to get_delay method, 
# but instead of using request library I am using aiohttp library

async def count():
    for i in [1,2,3,4]:
        print(i)
        await asyncio.sleep(1)

async def get_delay(seconds):
    endpoint = f'/delay/{seconds}'
    
    print(f'Getting with {seconds} delay..')
    
    # using async with to create instance of my client session object
    async with ClientSession() as session:
        # using async with here to actually execute the get on my get clinet session object
        # to get the response back. The response = respomse.read again with await.
        # here when I waiting to server response I can do other things
        async with session.get(base_url+endpoint) as response:
            response = await response.read()
            print(response)


async def main():
    # using await with asyncio.gather method amd passing these 2 functions 
    # so these functions run asynchronously/simultaniosly)

    await asyncio.gather(get_delay(5), count())

asyncio.run(main())
print('okay, all finished getting')
