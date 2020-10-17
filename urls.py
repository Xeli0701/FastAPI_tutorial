from controllers import app, index

# FastAPIのルーティング用関数
app.add_api_route('/', index)