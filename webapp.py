import time
from flask import Flask, render_template, request, redirect, session, make_response
from auto_attendance import submit_attendance

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/login", methods=["GET", "POST"])
def login():
    time.sleep(10)
    if request.method == "POST":
        tp = request.form["tp"]
        pwd = request.form["pwd"]
        remember = request.form.get("remember")

        session["tp"] = tp
        session["pwd"] = pwd

        resp = make_response(redirect("/"))
        if remember:
            resp.set_cookie("tp", tp, max_age=30*24*60*60)
            resp.set_cookie("pwd", pwd, max_age=30*24*60*60)
        return resp

    tp_cookie = request.cookies.get("tp")
    pwd_cookie = request.cookies.get("pwd")

    if tp_cookie and pwd_cookie:
        session["tp"] = tp_cookie
        session["pwd"] = pwd_cookie
        return redirect("/")

    return render_template("login.html")


@app.route("/")
def index():
    if "tp" not in session or "pwd" not in session:
        return redirect("/login")
    return render_template("web_app.html")

@app.route("/submit", methods=["POST"])
def submit():
    if "tp" not in session or "pwd" not in session:
        return redirect("/login")
    code = request.form["code"]
    tp = session["tp"]
    pwd = session["pwd"]
    try:
        submit_attendance(code, tp, pwd)
        return f"<h2>✅ Submitted Successfully Code: {code}</h2>"
    except Exception as e:
        return f"<h2>❌ Error: {e}</h2>"

@app.route("/logout")
def logout():
    session.clear()
    resp = make_response(redirect("/login"))

    resp.set_cookie("tp", "", max_age=0)
    resp.set_cookie("pwd", "", max_age=0)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
