from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials 

from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED 

import db
from models import User, Task 

import hashlib

from auth import auth
import datetime

app = FastAPI(
    title = 'FastAPI Tutorial TODO',
    descripstion = 'ToDo app with FastAPI and starlette',
    version = '0.1'
)

security = HTTPBasic()

#Template Settings(Jinja2)
#Templeと神社、ぜってぇ違うだろ
templates = Jinja2Templates(directory='templates')
jinja_env = templates.env  # Jinja2.Environment : filterやglobalの設定用

def index(request: Request):
    return templates.TemplateResponse('index.html',{'request': request})

def admin(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    # Basic認証で受け取った情報
    username = auth(credentials)

    # データベースからユーザ名が一致するデータを取得
    user = db.session.query(User).filter(User.username == username).first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all() if user is not None else []
    db.session.close()

    # 今日の日付と来週の日付
    today = datetime.datetime.now()

    return templates.TemplateResponse('admin.html',{'request': request, 'user': user})

def get(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    # auth
    username = auth(credentials)

    # userdata
    user = db.session.query(User).filter(User.username == username).first()
    db.session.close()

    # JSONフォーマット
    jsondata = {
        'username': user.username,
        'content': 'test'
    }

    return jsondata