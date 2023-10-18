import sys
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()  

class GrowiAPIError(Exception):
    def __init__(self, description):
        super().__init__()
        self.description = description
    
    def __repr__(self):
        return str(self.description)

    def __str__(self):
        return str(self.description)

def get_page_list(base_url: str, api_token: str, page_path: str) -> dict:
    """
    get page information
    """
    req_url = '{}{}'.format(base_url, '/_api/pages.list')
    params={'access_token': f'{api_token}', 'path': page_path}
    res = requests.get(req_url, params=params)

    if res.status_code == 200:
        return json.loads(res.text)['pages']
    else:
        raise GrowiAPIError(res.text)
    
def get_page_by_id(base_url: str, api_token: str, page_id: str) -> dict:
    """
    get page information
    """
    req_url = '{}{}'.format(base_url, '/_api/v3/page')
    params={'access_token': f'{api_token}', 'pageId': page_id}
    res = requests.get(req_url, params=params)

    if res.status_code == 200:
        return json.loads(res.text)['page']
    else:   
        raise GrowiAPIError(res.text)
    
def create_md_file(page_info: dict) -> None:
    """
    create folder and md file
    """
    growi_path = 'output/' + page_info['_id']
    
    if not os.getenv("FILE_NAME_ID_OPTION", False):
        growi_path = 'output' + page_info['path'].replace('"', '')
        os.makedirs("/".join(growi_path.split("/")[:-1]), exist_ok=True)

    if not page_info['revision']['body'] == '':      
        with open(growi_path + '.md', "w", encoding="utf-8") as f:
            f.write(page_info['revision']['body'])
        
    
if __name__ == '__main__':
    base_url = os.getenv("GROWI_BASE_URL")
    api_token = os.getenv("GROWI_API_TOKEN")
    path = sys.argv[1]

    pages = get_page_list(base_url, api_token, path)

    for page in pages:
        page_info = get_page_by_id(base_url, api_token, page['_id'])
        create_md_file(page_info)
        
    print("OK")