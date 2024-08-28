from flask import Flask
import pymongo
import db


# create the app 
app = Flask(__name__)

database = db.db

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test')
def test():
    return 'test test'

@app.route('/testdb')
def test_db():
    user = {'name':'user_name','password':'password'}
    database.users.insert_one(user)
    return "db insertion success"

# run app
if __name__ == '__main__':
    
    app.run(debug=True)