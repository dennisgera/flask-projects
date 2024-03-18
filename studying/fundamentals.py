from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'

@app.route('/reporter')
def reporter():
    return """<h2>Reporter Page</h2>
    <p>Reporter is a person who reports news.</p>
    <a href='/'>Return to home page</a>
    """

@app.route('/article/<article_name>')
def article(article_name):
    return f'<h2>Article Page</h2><p>Article: {article_name}</p>'


@app.router('/orders/<user_name>/<int:order_id>')
def orders(user_name: str, order_id: int):
    return f'<h2>Orders Page</h2><p>Orders of {user_name} with id {order_id}</p>'