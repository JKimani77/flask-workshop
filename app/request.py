from app import main
import urllib.request,json
import requests
from .models import Recipe


# Getting api key
api_key = None
# Getting the movie base url
base_url = None
articles_url = None

def configure_request(app):
    global api_key, base_url, base_url
    api_key = app.config['SPOON_API_KEY']
    base_url = app.config["SPOON_API_BASE_URL"]

def searchfunc(id):
    results = []
    r = requests.get(base_url, auth=(api_key))

    print (r.status_code)
    print (r.headers['content-type'])
    '''
    get_spoon_url = base_url.fomat(id, api_key)

    with urllib.request.urlopen(get_spoon_url) as url:
        get_spoon_data = url.read()
        get_spoon_response = json.loads(get_spoon_data)
    
        spoon_results = None
        '''

    return r
