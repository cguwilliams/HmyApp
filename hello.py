from flask import Flask
import numpy
import matplotlib

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! Hello Github'

x = linspace(0, 10)
y = sin(x)
plot(x, y)
    
