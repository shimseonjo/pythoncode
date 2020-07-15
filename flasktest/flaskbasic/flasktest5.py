from flask import Flask,url_for,redirect

app= Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'hello %s as guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect('/admin')
    else:
        return redirect('/guest/%s'%name)


if __name__ == '__main__':
    app.run()