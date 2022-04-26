
# -- import package
from flask import Flask as fl

# TODO: Hello World

app = fl(__name__)
print(app)
print(__name__)
@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run()