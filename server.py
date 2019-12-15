from flask import Flask, render_template

# create an instance of a flask app
app = Flask(__name__)


@app.route("/index.html")
def my_home():
    return render_template('index.html')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/works.html")
def works():
    return render_template('works.html')



@app.route("/work.html")
def work():
    return render_template('work.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/components.html")
def components():
    return render_template('components.html')




@app.route('/<username>/<int:post_id>')
def username(username=None,post_id=None):
    return render_template('index.html', name=username,post_id = post_id)