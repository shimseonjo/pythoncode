from flask import Flask,url_for

app = Flask(__name__)

@app.route('/login/')
def index():
    pass

if  __name__ == '__main__':
    with app.test_request_context():
        print(url_for('index',username='hong'))