from flask import Flask,flash, request, redirect, url_for
from flask import request
from lib.api.blueprint_module import blueprint
app = Flask(__name__)
app.register_blueprint(blueprint)

@app.route("/test", methods=['POST'])
def test():
    # user = request.args.get('test')
    # print("test=",user)
    return  "test"