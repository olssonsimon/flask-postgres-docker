import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%s:%s@%s/%s' % (
	os.environ['POSTGRES_USER'],
	os.environ['POSTGRES_PASSWORD'],
	os.environ['POSTGRES_HOST'],
	os.environ['POSTGRES_DB']
)

DB = SQLAlchemy(app)

from models import *

@app.route("/", methods = ['GET'])
def hello():
	return "Hello world!"

@app.route("/create", methods = ['GET'])
def create_user():
	user = User("Simon Olsson")

	DB.session.add(user)
	DB.session.commit()

	return "Created Simon Olsson!"

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=5000)