from flask import Flask, request
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/user/<username>/<int:age>')
def show_user_profile_age(username, age):
    return 'Username %s, 나이 %d' % (username, age) 

if __name__ == "__main__" :
    # app.debug = True
    app.run(host='0.0.0.0', port = 80)
