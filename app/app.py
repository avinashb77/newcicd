from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Is your body A MAP--? Becasue am getting lost in every Curve'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
