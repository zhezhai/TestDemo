from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:1234@127.0.0.1/movie_cat"
db = SQLAlchemy(app)




