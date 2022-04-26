from flask import Flask as fl, url_for
from flask import request
from markupsafe import escape
from flask import render_template

app = fl(__name__)

# print(app.test_request_context())
# # with app.test_request_context() :
# #     print(url_for('static', filename='style.css'))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':        
        return do_the_login()    
    else:        
        return show_the_login_form()

def do_the_login():
    return "process login"
def show_the_login_form():
    return "login form"

if __name__ == '__main__':
    app.run()