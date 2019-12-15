from flask import Flask, render_template

# create an instance of a flask app
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/<username>/<int:post_id>')
def username(username=None,post_id=None):
    return render_template('index.html', name=username,post_id = post_id)