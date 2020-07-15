from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index1.html")


@app.route("/setcookie", methods=["GET", "POST"])
def setcookie():
    if request.method == "POST":
        user = request.form["name"]
        res = make_response("Create Cookie!!")
        res.set_cookie("userID", user)
        return res


@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    return name

if __name__ == "__main__" :
#app.debug = True
    app.run(host='127.0.0.1', port=8889)