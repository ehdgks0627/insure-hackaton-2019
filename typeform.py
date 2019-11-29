import requests
from pprint import pprint


class TypeForm:
    API_BASE = 'https://api.typeform.com'
    TOKEN = 'HR4fzmTsuJAV2jUradaxSRqwkZR7HGvJpjdDwSJV33Zy'
    FORM_ID = 'aPPXH7'

    def __init__(self):
        self.session = requests.session()
        self.session.headers['Authorization'] = 'Bearer ' + self.TOKEN

    def answer_to_obj(self, answer):
        data = {
            'gender': self.get_property(answer, 'gNNduCiC9l7Z'),
            'birth': self.get_property(answer, 'FplRy5D2epbO').split('T')[0],
            'exercise': self.get_property(answer, 'gcDJw19MMaY7'),
            'exercise_time': self.get_property(answer, 'fAo9on3XxwvA'),
            'height': self.get_property(answer, 'dv2WvFC37cXp'),
            'weight': self.get_property(answer, 'y15cQTU4HUHu'),
            'family': self.get_property(answer, 'EallzMDFxIHV')
        }
        return data

    def get_form_info(self):
        url = self.API_BASE + '/forms/{form_id}'.format(form_id=self.FORM_ID)
        r = self.session.get(url).json()
        return r

    def get_response(self):
        url = self.API_BASE + '/forms/{form_id}/responses'.format(form_id=self.FORM_ID)
        params = {
            'page_size': 1000,
            'completed': ''
        }
        r = self.session.get(url, params=params).json()
    irint(data)
        return list(filter(lambda x: x['answers'], r['items']))

    def get_property(self, answer, name):
        a = list(filter(lambda x: x['field']['id'] == name, answer['answers']))
        if len(a) == 0:
            return None
        a = a[0]
        if a['type'] == 'choice':
            return a['choice']['label']
        elif a['type'] == 'date':
            return a['date']
        elif a['type'] == 'text':
            return a['text']
        elif a['type'] == 'number':
            return a['number']
        return ''
