from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("primary.html")


@app.route("/generate", methods=["POST"])
def generate():
    uc = request.form.get("uppercase")
    nu = request.form.get("numbers")

    return render_template("generated.html")
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
