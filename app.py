from flask import Flask, render_template, send_from_directory
from typeform import TypeForm
from insure_list import insure_list

app = Flask(__name__, static_url_path='/static/', static_folder='templates/static')
typeform = TypeForm()


@app.route('/', methods=['GET'])
def index():
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
    context = {
        'age': 20,
        'gender': '남성',
        'score': {
            'brain': 40,
            'breast': 30,
            'colorectal': 20,
            'genital': 10,
            'heart': 86,
            'liver': 30,
            'lung': 20,
            'stomach': 69,
            'thyroid': 85,
            'urinary': 20
        },
        'avr_score': {
            'brain': 40,
            'breast': 30,
            'colorectal': 20,
            'genital': 10,
            'heart': 86,
            'liver': 30,
            'lung': 20,
            'stomach': 69,
            'thyroid': 85,
            'urinary': 20
        },
        'recommand': [],
        'TRANSLATE': TRANSLATE
    }
    return render_template('index.html', **context)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088)
