import requests

base_url = "http://httpbin.org/"

# defining function that takes number of seconds
def get_delay(seconds):

    # building an endpoint with that number of seconds included
    endpoint = f'/delay/{seconds}'

    print(f'Getting with {seconds} delay...')

    # calling that url here:

    response = requests.get(base_url+endpoint)
    data = response.json()
    # when it returns it prints out the data
    print(data)

get_delay(5)

print('Okay! all finished getting.')
