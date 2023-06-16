from flask import Flask, render_template, request
from flask_mysqldb import mysql

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'foo'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def home():
	if request.method == 'GET':
		return '/login'

	if request.method == 'POST':
		return "SUUUU"

@app.route('/login')
def login():
	return "cheh"
