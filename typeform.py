import requests
from pprint import pprint


class TypeForm:
    API_BASE = 'https://api.typeform.com'
    TOKEN = 'HR4fzmTsuJAV2jUradaxSRqwkZR7HGvJpjdDwSJV33Zy'
    FORM_ID = 'aPPXH7'

    def __init__(self):
        self.session = requests.session()
        self.session.headers['Authorization'] = 'Bearer ' + self.TOKEN
        self.get_form_info()

    def get_form_info(self):
        url = self.API_BASE + '/forms/{form_id}'.format(form_id=self.FORM_ID)
        r = self.session.get(url).json()
        pprint(r)

    def get_response(self):
        url = self.API_BASE + '/forms/{form_id}/responses'.format(form_id=self.FORM_ID)
        params = {
            'page_size': 1000,
            'completed': ''
        }
        r = self.session.get(url, params=params).json()
        # pprint(r)
