from flask import Flask, render_template  
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='kim')

@app.route("/plist/")
def plist() :
    list = {"motor","servor","door","pir","sound"}
    return render_template("pList.html", plist = list)

@app.route("/ulist/")
def ulist() :
    list = {"led1":"ON","led2":"OFF","led3":"ON","temp":32,"moter":90}
    return render_template("list.html", ulist = list)

@app.route("/css")
def css():
    return render_template('style.html')

if  __name__ == "__main__":
    app.run(host='0.0.0.0', port=8890, debug=True)


