from flask import Flask as fl
from markupsafe import escape

app = fl(__name__)
print(app)
print(__name__)

@app.route("/")
def index():
    return 'Index Page'

@app.route("/<name>")
def hello(name):    
    return f"Hello, {escape(name)}!"

@app.route("/hello")
def helloworld():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):    
    # show the user profile for that user    
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):    
    # show the post with the given id, the id is an integer    
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):    
    # show the subpath after /path/    
    return f'Subpath {escape(subpath)}'


if __name__ == '__main__':
    app.run()