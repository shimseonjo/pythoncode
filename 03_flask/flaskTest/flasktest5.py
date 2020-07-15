from flask import Flask, request

app = Flask(__name__)

@app.route('/postData', methods=['POST'])
def postData():
    if request.method == 'POST':
        uname = request.form['username']
        pw = request.form['password']
        return 'Username :  %s, pw :  %s' % (uname, pw) 

if __name__ == "__main__" :
    #app.debug = True
    app.run(host='0.0.0.0', port=8889)
