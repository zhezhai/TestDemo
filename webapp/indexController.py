from flask import Blueprint, request, make_response, jsonify, render_template
from sqlalchemy import text
from application import db
import json
from common.models.user import User

index_page = Blueprint("index_page", __name__)
@index_page.route("/")
def index_page_index():
    return "index page"

@index_page.route('/my')
def hello():
    return 'hello'

@index_page.route('/get')
def get():
    # var_a = request.args.get('b', 'i love imooc')
    req = request.values
    var_a = req['a'] if "a" in req else "I love imooc"
    return 'request:%s params:%s var_a:%s' % (request.method, request.args, var_a)

@index_page.route('post', methods=["POST"])
def post():
    # var_a = request.form['a'] if "a" in request.form else ''
    req = request.values
    var_a = req['a'] if "a" in req else "I love imooc"
    return 'request:%s params:%s var_a:%s' % (request.method, request.form, var_a)

@index_page.route("/upload", methods=["POST"])
def upload():
    f = request.files['file'] if 'file' in request.files else None
    return 'request:%s params:%s file:%s' % (request.method, request.files, f)

@index_page.route("/text")
def text_a():
    return "text/html"

@index_page.route("text_same")
def text_same():
    response = make_response("text/html", 200)
    return response

@index_page.route("/json")
def json():
    data = {"a": "b"}
    response = make_response(jsonify(data))
    return response

@index_page.route("/template")
def template():
    name = "imooc"
    result = User.query.all()
    context = {'name': name, 'user': {"nickname": "zhaizhe", "qq": "309423428", "homepage": "123.com", },
               'num_list': [1, 2, 3, 4, 5], 'result': result}

    # sql = text("select * from `user`")
    # result = db.engine.execute(sql)

    return render_template("index.html", **context)

@index_page.route("/extend_template")
def extend_template():
    return render_template("extend_template.html")


@index_page.route("/extend_template_other")
def extend_template_other():
    return render_template("extend_template_other.html")
