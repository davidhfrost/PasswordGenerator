from flask import Flask, render_template, request, url_for, redirect
from secrets import choice, randbelow

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("primary.html")


@app.route("/generate", methods=["POST"])
def generate():
    charList = []
    uc = request.form.get("uppercase")
    lc = request.form.get("lowercase")
    nu = request.form.get("numbers")
    if lc is not None:
        charList.extend(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    if nu is not None:
        charList.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    password = ""
    #for i in range(10):
        #password = password + charList[randbelow(36)]
    return render_template("generated.html", passw=charList)
    """pref = request.args.get("uppercase")
    print(pref)
    if (request.method == 'POST'):
        test = request.form['uppercase']
        print("Hello world")
        return "Hi"
    # your code
    # return a response
    """


# def generate():

if __name__ == '__main__':
    app.run()
