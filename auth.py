import hashlib
import db
from models import User
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi import HTTPException


def auth(credentials):
    """
    Basic認証を行う関数
    sqlite3のuserとpasswordを照合する
    """
    # Basic認証で受け取った情報
    username = credentials.username
    password = hashlib.md5(credentials.password.encode()).hexdigest()
    # データベースからユーザ名が一致するデータを取得
    user = db.session.query(User).filter(User.username == username).first()
    db.session.close()

    # 該当ユーザがいない場合
    if user is None or user.password != password:
        error = 'ユーザ名かパスワードが間違っています．'
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail=error,
            headers={"WWW-Authenticate": "Basic"},
        )
    return username