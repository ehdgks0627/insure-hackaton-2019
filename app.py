# -*- coding: UTF-8 -*-

from flask import Flask, render_template, send_from_directory
from typeform import TypeForm
from insure_list import insure_list
import random

app = Flask(__name__, static_url_path='/static/', static_folder='templates/static')
typeform = TypeForm()

TRANSLATE = {
    'brain': '뇌혈관질환',
    'breast': '유방암',
    'colorectal': '대장암',
    'genital': '생식기암',
    'heart': '심장질환',
    'liver': '간암',
    'lung': '폐암',
    'stomach': '위암',
    'thyroid': '갑상선암',
    'urinary': '비뇨기과암'
}


@app.route('/', methods=['GET'])
def index():
    recommend = insure_list[:]
    random.shuffle(recommend)
    answer = typeform.get_response()[0]
    data = typeform.answer_to_obj(answer)
    context = {
        'age': '25 ~ 29',
        'score': {
            'brain': 15,
            'breast': 6,
            'colorectal': 20,
            'genital': 10,
            'heart': 36,
            'liver': 55,
            'lung': 4,
            'stomach': 10,
            'thyroid': 30,
            'urinary': 20
        },
        'avr_score': {
            'brain': 11,
            'breast': 2,
            'colorectal': 23,
            'genital': 10,
            'heart': 15,
            'liver': 45,
            'lung': 30,
            'stomach': 30,
            'thyroid': 20,
            'urinary': 50
        },
        'recommend': recommend[:5],
        'data': data,
        'TRANSLATE': TRANSLATE
    }
    return render_template('index.html', **context)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088)
