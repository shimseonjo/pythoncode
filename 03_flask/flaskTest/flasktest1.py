from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello world'

if  __name__ == '__main__':  
    app.run()
#  app.run(debug=True, host='0.0.0.0’ )  원격 컴퓨터에서 접속 가능한 설정 시작
#  app.debug=True
#  app.run(host='0.0.0.0‘, port = 80)
