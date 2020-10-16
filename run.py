from urls import app
import uvicorn
 
if __name__ == '__main__':
    # コンソールで [$ uvicorn run:app --reload]でも可
    #port変更
    uvicorn.run(app=app, port=8888)
    #uvicorn.run(app=app)