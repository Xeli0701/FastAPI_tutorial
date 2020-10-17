from controllers import *

# FastAPI Rooting
app.add_api_route('/', index)
app.add_api_route('/admin', admin)
app.add_api_route('/get', get)