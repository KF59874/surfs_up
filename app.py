from flask import Flask
app = Flask(__name__)

#Create a route
@app.route('/')
#Create a function
def hello_world():
    return 'Hello world this is a test'