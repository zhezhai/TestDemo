from indexController import index_page
from application import app

app.register_blueprint(index_page, url_prefix="/imooc")