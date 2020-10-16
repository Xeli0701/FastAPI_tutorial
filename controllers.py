from fastapi import FastAPI
from starlette.templating import Jinja2Templates  # HTMLTemplate
from starlette.requests import Request


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