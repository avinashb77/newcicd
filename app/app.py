from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'In the Game of election you are getting my vote of love without a campaign My Thangooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
