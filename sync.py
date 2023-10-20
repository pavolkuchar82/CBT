import requests

base_url = "http://httpbin.org/"

def get_delay(seconds):
    endpoint = f'/delay/{seconds}'

    print(f'Getting with {seconds} delay...')

    resp = requests.get(base_url+endpoint)
    data = resp.json()
    print(data)

get_delay(5)

print('Okay! all finished getting.')
