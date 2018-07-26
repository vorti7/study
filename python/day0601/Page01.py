from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello flask"
@app.route("/member/")
def member():
    return "member"
@app.route("/method/", methods = )
def re_method():


@app.route("/datasend/<title>/<page>/<count>")
def datasend(title,page,count):
    return "dfdf" + title + page + count

app.run(port = 81, host = '0.0.0.0')
