from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials 

from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED 

import db
from models import User, Task 

import hashlib

app = FastAPI(
    title = 'FastAPI Tutorial TODO',
    descripstion = 'ToDo app with FastAPI and starlette',
    version = '0.1'
)

#Template Settings(Jinja2)
#Templeと神社、ぜってぇ違うだろ
templates = Jinja2Templates(directory='templates')
jinja_env = templates.env  # Jinja2.Environment : filterやglobalの設定用

def index(request: Request):
    return templates.TemplateResponse('index.html',{'request': request})

def admin(request: Request):
    # ユーザとタスクを取得
    # とりあえず今はadminユーザのみ取得
    user = db.session.query(User).filter(User.username == 'admin').first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all()
    db.session.close()

    return templates.TemplateResponse('admin.html',
                                      {'request': request,
                                       'user': user,
                                       'task': task})