# This backoff script wraps up my API call inside the loop, that will if I get the response
# other then 200, continue to try and call within increasing wait time in between each call.

import requests 
from time import sleep


base_url = "https://api.discogs.com/"

backoffs = {"factor" : 1.3,
            # multiplying my waiting time by 1.3 between each call
            "wait" : 1,
            # initial time is 1 second
            "max_tries": 5
            # max number if retires to not loop through infinitely
            }

def get_releases(release_id):
    endpoint = f'/releases/{release_id}'

    print(f'Getting release #{release_id}')
    response=requests.get(base_url+endpoint)
    response_code=response.status_code

    return response_code

# the above return of function (response_code) is implemented here wrapped inside while loop. 
# Instead of calling my code 30 times over, first I check if my response is not set to -1 which indicate success and can move on to the next calling my loop of 30.
# next inside the while loop i check my tries counter and see if it hint maximum tries yet. if I have, then(else) print the "Reached max retry count ", set the response_code to -1. Then my while loop exits and I move to next call in my range
# If I don't hit max numbers of tries then I call the API and check my response code. If it is 429 
# (I could write many if to test many diffrent responses codes and have diffrent code that happen to be excecuted under diffrent circumstances) 
# if it is 429 I sleep for the alloted wait time (initially is 1 sec) and increase my tries counter. 
# if I have sucessful 200 response (elif) I exit out of the code and move to the for loop that I running it 30 diffrent times
for i in range(0,30):
    tries = 0
    response_code = 0
    while response_code != -1:
        if tries <= backoffs["max_tries"]:
            response_code = get_releases(28571377)
            if response_code == 429:
               print(f'429- too many requests. Waiting "{backoffs["wait"]}"seconds.')
               sleep(backoffs["wait"])

               backoffs["wait"] *= backoffs["factor"]
               # It multiplies right operand with the left operand and assign the result to left operand. (c *= a is equivalent to c = c * a)
               tries += 1
               # += provides a convenient way to add a value to an existing variable and assign the new value back to the same variable
            elif response_code == 200:
               tries = 0
               response_code = -1
        else:
            print(f"reached max retry count {tries}")
            response_code = -1



