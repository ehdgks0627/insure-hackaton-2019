from flask import Flask
from typeform import TypeForm

app = Flask(__name__)
typeform = TypeForm()


@app.route('/', methods=['GET'])
def index():
    pass


typeform.get_response()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088)
