# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, info='primary key')
    nickname = db.Column(db.String(30, 'utf8mb4_bin'), info='nickname')
    login_name = db.Column(db.String(20, 'utf8mb4_bin'), unique=True, info='login name')
    login_pwd = db.Column(db.String(32, 'utf8mb4_bin'), info='login password')
    login_salt = db.Column(db.String(32, 'utf8mb4_bin'), info='encryption')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='0:False 1:True')
    updated_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='last updated time')
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='insert time')
