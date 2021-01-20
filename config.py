from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'bituser.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'bituser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Q!w2e3r4'
app.config['MYSQL_DATABASE_DB'] = 'bituser$default'

mysql = MySQL()
mysql.init_app(app)
