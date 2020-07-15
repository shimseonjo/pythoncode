from flask import Flask,session,escape

app = Flask(__name__)

app.secret_key = "ABCDEFG"

@app.route("/")
def index():
    if "username" in session:
        return "Logged in as %s " % escape(session["username"])
    else:
        return "You are not logged in"


@app.route("/session")
def login():
    session["username"] = "DongDongE"
    return "Good~!"


@app.route("/out")
def session_out():
    session.pop("username", None)
    # session.clear()
    return "Session out"


if __name__ == "__main__" :
#app.debug = True
    app.run(host='127.0.0.1', port=8889)