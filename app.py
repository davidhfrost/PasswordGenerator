from flask import Flask, render_template, request, url_for, redirect
from secrets import choice, randbelow

app = Flask(__name__)
uppercaseList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route("/")
def home():
    return render_template("primary.html")


def validPassword(password):
    numberOfNumbers = 0
    numberOfUppercase = 0
    numberOfLowercase = 0
    #for i in range(len(password)):
    #    if password[i] in
    return numberOfNumbers > 0 and numberOfUppercase > 0 and numberOfLowercase > 0
    pass


@app.route("/generate", methods=["POST"])
def generate():
    charList = []
    uc = request.form.get("uppercase")
    lc = request.form.get("lowercase")
    nu = request.form.get("numbers")
    if lc is not None:
        charList.extend(uppercaseList)
    if nu is not None:
        charList.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    if uc is not None:
        charList.extend(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    password = ""
    while (validPassword(password)):

    for i in range(10):
        password = password + choice(charList)

    return render_template("generated.html", password=password)
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
