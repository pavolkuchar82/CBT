import requests

base_url = "https://api.discogs.com/"

def get_releases(release_id):

    endpoint = f'/releases/{release_id}'

    print(f'Getting release n: {release_id}')

    response = requests.get(base_url+endpoint)
    print(response)

get_releases('285a71377')