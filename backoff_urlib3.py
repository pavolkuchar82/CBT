#leveraging urlib3 library  with script. All that retry is built in int the libraty itself.

import requests
import logging

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

base_url = "https://api.discogs.com/"

# seting the logging to the DEBUG to see all the output
logging.basicConfig(level=logging.DEBUG)


def get_releases(release_id):
    endpoint = f'/releases/{release_id}'
    
    # 3 lines of additional code
    session=requests.Session()
    retries=Retry(total=5, backoff_factor=1, status_forcelist=[429,500,502,503,504])
    # retries object include all the details about rety i want including status force list
    # which is a array (rather then having a big if statement inside the code) of different statuses 
    # that i want to trigger the retry and the library is going to handle this for me.
    session.mount(base_url, HTTPAdapter(max_retries=retries))
    # here calling mount commnad on base url with HTTP adapter that uses that retries object.
    # The reason I do that is that this way everything that is done with my session object,  
    # if it matches the base url will use my retries.


    print(f'Getting release #{release_id}')

    #I call it as before and I will use library to handle for me
    response=session.get(base_url+endpoint)
    response_code=response.status_code
    return response_code

